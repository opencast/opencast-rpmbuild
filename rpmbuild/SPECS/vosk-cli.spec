%global pypi_name vosk-cli
%global pypi_version 0.3

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A command line interface for Vosk.

License:        Apache-2.0
URL:            https://github.com/elan-ev/vosk-cli
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(setuptools)
Requires:       python3dist(vosk)
Requires:       python3dist(webvtt-py)
Requires:       ffmpeg

%description
This project serves as an Vosk interface for Opencast. It allows to generate subtitles (WebVVT files) from video and audio sources via Vosk.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/vosk-cli
%{python3_sitelib}/voskcli
%{python3_sitelib}/vosk_cli-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 24 2023 Lars Kiesow <lkiesow@uos.de> - 0.3-1
- Initial package.
