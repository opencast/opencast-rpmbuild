# vim: et:ts=3:sw=3:sts=3

%global __os_install_post /usr/lib/rpm/brp-compress %{nil}
%define __requires_exclude_from ^.*\\.jar$
%define __provides_exclude_from ^.*\\.jar$

%define srcversion 9.7
%define uid   opencast
%define gid   opencast
%define nuid  7967
%define ngid  7967

%if "%{?ocdist}" == ""
%define ocdist allinone
%endif

%if "%{?tarversion}" == ""
%define tarversion %{version}
%endif

Name:          opencast-%{ocdist}
Version:       %{srcversion}
Release:       1%{?dist}
Summary:       Open Source Lecture Capture & Video Management Tool

Group:         Applications/Multimedia
License:       ECL 2.0
URL:           https://opencast.org
Source0:       opencast-dist-%{ocdist}-%{tarversion}.tar.gz
Source1:       jetty.xml
Source2:       opencast.logrotate
Source3:       org.apache.aries.transaction.cfg
Source4:       org.apache.karaf.shell.cfg

BuildRequires: tar
BuildRequires: gzip

Requires: ffmpeg >= 3
Requires: hunspell >= 1.2.8
Requires: java >= 1:1.8.0
Requires: sox >= 14
Requires: tesseract >= 3

# For the start/stop scripts:
Requires: bash
Requires: nc
Requires: sed

%if "%{?ocdist}" == "allinone"
Requires: activemq-dist >= 5.14
%if 0%{?el7}
Requires: elasticsearch-oss >= 7.9
Requires: elasticsearch-oss < 8
%else
Recommends: elasticsearch-oss >= 7.9
Recommends: elasticsearch-oss < 8
%endif
%endif
%if "%{?ocdist}" == "admin"
%if 0%{?el7}
Requires: elasticsearch-oss >= 7.9
Requires: elasticsearch-oss < 8
%else
Recommends: elasticsearch-oss >= 7.9
Recommends: elasticsearch-oss < 8
%endif
%endif

BuildRequires:     systemd
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

Provides:  opencast             = %{version}
Provides:  opencast9-%{ocdist}  = %{version}
Obsoletes: opencast9-%{ocdist} <= %{version}
Obsoletes: opencast8-%{ocdist} <= %{version}

BuildArch: noarch



%description
Opencast is a free, open-source platform to support the management of
educational audio and video content. Institutions will use Opencast to
produce lecture recordings, manage existing video, serve designated
distribution channels, and provide user interfaces to engage students with
educational videos.


%prep
%setup -q -c -a 0


%build
# Fix newline character at end of configuration files
find opencast-dist-%{ocdist}/etc -name '*.xml' \
   -o -name '*.cfg' -exec sed -i -e '$a\' '{}' \;
# ' fix vim hl
sed -i -e '$a\' opencast-dist-%{ocdist}/etc/shell.init.script
# ' fix vim hl


%install
rm -rf %{buildroot}

# Create directories
mkdir -m 755 -p %{buildroot}%{_datadir}
mkdir -m 755 -p %{buildroot}%{_sharedstatedir}
mkdir -m 755 -p %{buildroot}%{_sysconfdir}
mkdir -m 755 -p %{buildroot}/srv/opencast
mkdir -m 755 -p %{buildroot}%{_localstatedir}/log/opencast

# Move files into the package filesystem
mv opencast-dist-%{ocdist} \
   %{buildroot}%{_datadir}/opencast
mv %{buildroot}%{_datadir}/opencast/etc \
   %{buildroot}%{_sysconfdir}/opencast
mv %{buildroot}%{_datadir}/opencast/bin/setenv \
   %{buildroot}%{_sysconfdir}/opencast/setenv
mv %{buildroot}%{_datadir}/opencast/data \
   %{buildroot}%{_sharedstatedir}/opencast

# Create instances dir. This is still hardcoded in Karaf
mkdir %{buildroot}%{_sharedstatedir}/opencast/instances

# Create some links to circumvent Karaf bugs
ln -s %{_sysconfdir}/opencast \
   %{buildroot}%{_datadir}/opencast/etc
ln -s %{_sysconfdir}/opencast/setenv \
   %{buildroot}%{_datadir}/opencast/bin/setenv
ln -s %{_sharedstatedir}/opencast \
   %{buildroot}%{_datadir}/opencast/data
ln -s %{_sharedstatedir}/opencast/instances \
   %{buildroot}%{_datadir}/opencast/instances

# Add custom jetty.xml
# Otherwise Karaf will attempt to do that and fail to start
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/opencast/jetty.xml

# Install logrotate configuration
install -p -D -m 0644 %{SOURCE2} \
   %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install workaround dummy file in /etc
install -p -D -m 0644 %{SOURCE3} \
   %{buildroot}%{_sysconfdir}/opencast
install -p -D -m 0644 %{SOURCE4} \
   %{buildroot}%{_sysconfdir}/opencast

# Install Systemd unit file
install -p -D -m 0644 \
   %{buildroot}%{_datadir}/opencast/docs/scripts/service/opencast.service \
   %{buildroot}%{_unitdir}/opencast.service

# Patch up some directories

# Systemd unit file (path to binary)
sed -i 's#/opt/#/usr/share/#' %{buildroot}%{_unitdir}/opencast.service

# Binary file configuration
echo "export KARAF_DATA=%{_sharedstatedir}/opencast" >> \
   %{buildroot}%{_sysconfdir}/opencast/setenv
echo "export KARAF_ETC=%{_sysconfdir}/opencast" >> \
   %{buildroot}%{_sysconfdir}/opencast/setenv

# Patch log file locations
sed -i 's#fileName *= *${karaf.data}/log#fileName = %{_localstatedir}/log/opencast#' \
   %{buildroot}%{_sysconfdir}/opencast/org.ops4j.pax.logging.cfg

# Patch storage dir
sed -i 's#^\(org.opencastproject.storage.dir\)=.*$#\1=/srv/opencast#' \
   %{buildroot}%{_sysconfdir}/opencast/custom.properties



%clean
rm -rf ${buildroot}



%pre
# Create user and group if nonexistent
# Try using a common numeric uid/gid if possible
if [ ! $(getent group %{gid}) ]; then
   if [ ! $(getent group %{ngid}) ]; then
      groupadd -r -g %{ngid} %{gid} > /dev/null 2>&1 || :
   else
      groupadd -r %{gid} > /dev/null 2>&1 || :
   fi
fi
if [ ! $(getent passwd %{uid}) ]; then
   if [ ! $(getent passwd %{nuid}) ]; then
      useradd -M -r -u %{nuid} -d /srv/opencast -g %{gid} %{uid} > /dev/null 2>&1 || :
   else
      useradd -M -r -d /srv/opencast -g %{gid} %{uid} > /dev/null 2>&1 || :
   fi
fi


%post
%systemd_post opencast.service


%preun
%systemd_preun opencast.service


%postun
%systemd_postun_with_restart opencast.service


%files
%config(noreplace) %{_sysconfdir}/opencast/
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/opencast.service
%{_datadir}/opencast
%attr(755,%{uid},%{gid}) %{_datadir}/opencast/bin/*
%attr(755,%{uid},%{gid}) %dir /srv/opencast
%attr(755,%{uid},%{gid}) %dir %{_localstatedir}/log/opencast
%attr(755,%{uid},%{gid}) %{_sharedstatedir}/opencast


%changelog
* Thu Jul 15 2021 Lars Kiesow <lkiesow@uos.de> - 9.6-1
- Update to 9.7

* Tue Jun 15 2021 Lars Kiesow <lkiesow@uos.de> - 9.6-1
- Update to 9.6

* Mon May 17 2021 Lars Kiesow <lkiesow@uos.de> - 9.5-1
- Update to 9.5

* Mon Apr 19 2021 Lars Kiesow <lkiesow@uos.de> - 9.4-1
- Update to 9.4

* Mon Mar 15 2021 Lars Kiesow <lkiesow@uos.de> - 9.3-1
- Update to 9.3

* Mon Feb 15 2021 Lars Kiesow <lkiesow@uos.de> - 9.2-1
- Update to Opencast 9.2

* Mon Jan 11 2021 Lars Kiesow <lkiesow@uos.de> - 9.1-5
- Obsolete opencast8-...

* Mon Jan 11 2021 Lars Kiesow <lkiesow@uos.de> - 9.1-4
- Fix upgrade path from earlier 9.x builds

* Tue Jan 05 2021 Lars Kiesow <lkiesow@uos.de> - 9.1-3
- Switch from `opencast9` to `opencast` package name

* Fri Dec 25 2020 Lars Kiesow <lkiesow@uos.de> - 9.1-2
- Recommend elasticsearch

* Thu Dec 17 2020 Lars Kiesow <lkiesow@uos.de> - 9.1-1
- Update to Opencast 9.1

* Tue Dec 15 2020 Lars Kiesow <lkiesow@uos.de> - 9.0-1
- Update to Opencast 9.0

* Mon Dec 14 2020 Lars Kiesow <lkiesow@uos.de> - 8.9-1
- Update to Opencast 8.9
- Initial automated build

