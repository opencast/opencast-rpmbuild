%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

%global plugin_name analysis-icu

Name:          opensearch-plugin-%{plugin_name}
Summary:       OpenSearch ICU analysis plugin
Version:       1.3.17
Release:       2%{?dist}
License:       Apache-2.0

Source0:       https://artifacts.opensearch.org/releases/plugins/%{plugin_name}/%{version}/%{plugin_name}-%{version}.zip
URL:           https://github.com/opensearch-project/OpenSearch/tree/main/plugins
BuildRoot:     %{_tmppath}/%{name}-root

BuildArch:     noarch

BuildRequires: unzip
Requires:      opensearch = %{version}


%description
The ICU Analysis plugin integrates the Lucene ICU module into OpenSearch, adding extended Unicode support using the
ICU libraries, including better analysis of Asian languages, Unicode normalization, Unicode-aware case folding,
collation support, and transliteration.


%prep
unzip -o %{SOURCE0}


%build


%install
rm -rf %{buildroot}

install -p -d -m 0755 %{buildroot}%{_datadir}/opensearch/plugins/%{plugin_name}
install -p -m 0644 *.jar *.properties %{buildroot}%{_datadir}/opensearch/plugins/%{plugin_name}/

%clean
rm -rf %{buildroot}

%post
# after initial installation
if [ $1 -eq 1 ] ; then
  systemctl try-restart opensearch.service
fi

%postun
# after upgrade
if [ $1 -eq 1 ] ; then
  systemctl try-restart opensearch.service
fi


%files
%defattr(-,root,root,-)
%doc NOTICE.txt
%license LICENSE.txt
%{_datadir}/opensearch/plugins/%{plugin_name}


%changelog
* Sun Jan 19 2025 Lars Kiesow <lkiesow@uos.de> - 1.3.17-2
- Automatically restart OpenSearch if necessary

* Sun Nov 17 2024 Lars Kiesow <lkiesow@uos.de> - 1.3.17-1
- Initial build

