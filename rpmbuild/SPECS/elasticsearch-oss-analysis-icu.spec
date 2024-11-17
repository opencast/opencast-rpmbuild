%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

%global plugin_name analysis-icu

Name:          elasticsearch-oss-plugin-%{plugin_name}
Summary:       Elasticsearch ICU analysis plugin
Version:       7.10.2
Release:       1%{?dist}
License:       Apache-2

Source0:       https://artifacts.elastic.co/downloads/elasticsearch-plugins/%{plugin_name}/%{plugin_name}-%{version}.zip
URL:           https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html
BuildRoot:     %{_tmppath}/%{name}-root

BuildArch:     noarch

BuildRequires: unzip
Requires:      elasticsearch-oss = %{version}


%description
The ICU Analysis plugin integrates the Lucene ICU module into Elasticsearch, adding extended Unicode support using the
ICU libraries, including better analysis of Asian languages, Unicode normalization, Unicode-aware case folding,
collation support, and transliteration.


%prep
unzip -o %{SOURCE0}


%build


%install
rm -rf %{buildroot}

install -p -d -m 0755 %{buildroot}%{_datadir}/elasticsearch/plugins/%{plugin_name}
install -p -m 0644 *.jar *.properties %{buildroot}%{_datadir}/elasticsearch/plugins/%{plugin_name}/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc NOTICE.txt
%license LICENSE.txt
%{_datadir}/elasticsearch/plugins/%{plugin_name}


%changelog
* Sun Nov 17 2024 Lars Kiesow <lkiesow@uos.de> - 7.10.2-1
- Initial build
