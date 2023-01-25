# Created by pyp2rpm-3.3.8
%global pypi_name srt
%global pypi_version 3.5.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A tiny library for parsing, modifying, and composing SRT files

License:        MIT
URL:            https://github.com/cdown/srt
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
|travis| |lgtm| |coveralls|.. |travi .. |lgt .. |coverall srt is a tiny but
featureful Python library for parsing, modifying, and composing SRT files_.
Take a look at the quickstart_ for a basic overview of

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
|travis| |lgtm| |coveralls|.. |travi .. |lgt .. |coverall srt is a tiny but
featureful Python library for parsing, modifying, and composing SRT files_.
Take a look at the quickstart_ for a basic overview of


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/srt
%{_bindir}/srt-deduplicate
%{_bindir}/srt-fixed-timeshift
%{_bindir}/srt-linear-timeshift
%{_bindir}/srt-lines-matching
%{_bindir}/srt-mux
%{_bindir}/srt-normalise
%{_bindir}/srt-play
%{_bindir}/srt-process
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/srt_tools/utils.py
%{python3_sitelib}/srt_tools
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info


%changelog
* Thu Jan 12 2023 Lars Kiesow <lkiesow@uos.de> - 3.5.2-1
- Initial package.
