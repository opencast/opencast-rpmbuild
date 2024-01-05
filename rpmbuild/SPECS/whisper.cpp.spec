Name:           whisper.cpp
Version:        1.5.4
Release:        1%{?dist}
Summary:        Whisper automatic speech recognition
License:        MIT
Source0:        https://github.com/ggerganov/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  coreutils make gcc-c++ libstdc++-devel
Requires:       libstdc++ curl
URL:            https://github.com/ggerganov/whisper.cpp

%define debug_package %{nil}
%define source_date_epoch_from_changelog 0

%description
High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model.

%prep
%setup -q

%build
make -j
# patch model download script
sed -i 's#models_path=.*$#models_path=%{_datadir}/%{name}/models/#' models/download-ggml-model.sh

%install
install -p -d -m 0755 %{buildroot}%{_datadir}/%{name}/models/
install -p -d -m 0755 %{buildroot}%{_bindir}
install -p    -m 0755 main %{buildroot}%{_bindir}/%{name}
install -p    -m 0755 quantize %{buildroot}%{_bindir}/%{name}-quantize
install -p    -m 0755 server %{buildroot}%{_bindir}/%{name}-server
install -p -d -m 0755 %{buildroot}%{_sbindir}
install -p    -m 0744 models/download-ggml-model.sh %{buildroot}%{_sbindir}/%{name}-model-download


%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}/models/
%{_bindir}/%{name}
%{_bindir}/%{name}-quantize
%{_bindir}/%{name}-server
%{_sbindir}/%{name}-model-download

%changelog
* Fri Jan 05 2024 Lars Kiesow <lkiesow@uos.de> - 1.5.4-1
- Update to whisper.cpp 1.5.4

* Thu Jan 04 2024 Lars Kiesow <lkiesow@uos.de> - 1.5.3-1
- Update to whisper.cpp 1.5.3

* Fri Dec 15 2023 Lars Kiesow <lkiesow@uos.de> - 1.5.2-1
- Update to version 1.5.2

* Fri Dec 08 2023 Lars Kiesow <lkiesow@uos.de> - 1.5.1-1
- Initial build
