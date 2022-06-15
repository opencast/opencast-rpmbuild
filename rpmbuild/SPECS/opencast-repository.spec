Name:      opencast-repository
Summary:   Opencast RPM Repository
Version:   12
Release:   1%{?dist}
License:   CC-0
URL:       https://pkg.opencast.org
Source0:   https://raw.githubusercontent.com/lkiesow/opencast-rpmbuild/r/%{version}.x/rpmbuild/SOURCES/opencast.repo
Source1:   https://raw.githubusercontent.com/lkiesow/opencast-rpmbuild/r/%{version}.x/rpmbuild/SOURCES/opencast-testing.repo
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%if 0%{?el7}%{?el8}
Requires: epel-release
%endif

Provides:  opencast-repository-12  = %{version}
Obsoletes: opencast-repository-12 <= %{version}
Obsoletes: opencast-repository-11 <= %{version}
Obsoletes: opencast-repository-10 <= %{version}
Obsoletes: opencast-repository-9 <= %{version}


%description
RPM repository for Opencast 12 on CentOS Stream, Red hat Enterprise Linux and
equivalent distributions.


%prep


%build


%install
install -m 0644 -p -D %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/opencast.repo
install -m 0644 -p -D %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/opencast-testing.repo


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/*


%changelog
* Wed Jun 15 2022 Lars Kiesow <lkiesow@uos.de> - 12-1
- Opencast 12 repository

* Wed Dec 15 2021 Lars Kiesow <lkiesow@uos.de> - 11-1
- Opencast 11 repository

* Tue Jun 15 2021 Lars Kiesow <lkiesow@uos.de> - 10-1
- Opencast 10 repository

* Thu Jan 14 2021 Lars Kiesow <lkiesow@uos.de> - 9-1
- Rolling repository package

* Wed Dec 23 2020 Lars Kiesow <lkiesow@uos.de> - 0-1
- Opencast 9 repository

* Mon Feb 24 2020 Lars Kiesow <lkiesow@uos.de> - 0-1
- Make Opencast 8 specific

* Wed Jan 29 2020 Lars Kiesow <lkiesow@uos.de> - 0-1
- Initial build
