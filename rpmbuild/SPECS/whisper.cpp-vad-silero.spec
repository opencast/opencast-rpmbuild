Name:           whisper.cpp-vad-silero
Version:        5.1.2
Release:        1%{?dist}
Summary:        VAD Model fpr WhisperC++
Group:          Networking/Daemons
License:        ASL 2.0
Source0:        https://raw.githubusercontent.com/ggml-org/whisper.cpp/refs/tags/v1.7.6/models/download-vad-model.sh
BuildRoot:      %{_tmppath}/%{name}

BuildArch: noarch

BuildRequires:  curl

%description
Voice activation detection model for whisper.cpp

%prep
%setup -c -n %{name} -T
install -m 0755 %{SOURCE0} .


%build
./download-vad-model.sh silero-v%{version}

%install
install -p -D -m 0644 ggml-silero-v%{version}.bin %{buildroot}%{_datadir}/whisper.cpp/models/ggml-silero-v%{version}.bin

%files
%{_datadir}/whisper.cpp/models/ggml-silero-v%{version}.bin

%changelog
* Fri Aug 29 2025 Lars Kiesow <lkiesow@uos.de> - 5.1.2-1
- Initial build
