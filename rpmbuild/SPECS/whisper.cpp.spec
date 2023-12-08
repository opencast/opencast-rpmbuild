Name:           whisper.cpp
Version:        1.5.1
Release:        1%{?dist}
Summary:        Library CPU Inference of Whisper in C/C++ with OpenCL CLBLAS option.
License:        MIT
Source0:        https://github.com/ggerganov/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  coreutils make gcc-c++ libstdc++-devel
Requires:       libstdc++ curl
URL:            https://github.com/ggerganov/whisper.cpp

%define debug_package %{nil}
%define source_date_epoch_from_changelog 0

%description
Inference library with optional OpenCL support for Meta's Whisper models using default options.
Models are not included in this package and must be downloaded separately.

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
install -p -d -m 0755 %{buildroot}%{_sbindir}
install -p    -m 0744 models/download-ggml-model.sh %{buildroot}%{_sbindir}/%{name}-model-download


%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}/models/
%{_bindir}/%{name}
%{_sbindir}/%{name}-model-download

%changelog
* Fri Dec 08 2023 Lars Kiesow <lkiesow@uos.de> - 1.5.1-1
- Initial build

