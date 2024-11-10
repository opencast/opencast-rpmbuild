%define _models large-v3 large-v3-q5_0 large-v3-turbo large-v3-turbo-q5_0

Name:           whisper.cpp
Version:        0.1
Release:        2%{?dist}
Summary:        Models fpr WhisperC++
Group:          Networking/Daemons
License:        ASL 2.0
Source0:        https://raw.githubusercontent.com/ggerganov/whisper.cpp/v1.7.1/models/download-ggml-model.sh
BuildRoot:      %{_tmppath}/%{name}

BuildArch: noarch

BuildRequires:  curl

%description
Models for whisper.cpp

%package large-v3
Summary: Model 'large-v3' for whisper.cpp
%description large-v3
Model 'large-v3' for whisper.cpp

%package large-v3-q5_0
Summary: Model 'large-v3-q5_0' for whisper.cpp
%description large-v3-q5_0
Model 'large-v3-q5_0' for whisper.cpp

%package large-v3-turbo
Summary: Model 'large-v3-turbo' for whisper.cpp
%description large-v3-turbo
Model 'large-v3-turbo' for whisper.cpp

%package large-v3-turbo-q5_0
Summary: Model 'large-v3-turbo-q5_0' for whisper.cpp
%description large-v3-turbo-q5_0
Model 'large-v3-turbo-q5_0' for whisper.cpp


%prep
%setup -c -n %{name} -T
install -m 0755 %{SOURCE0} .


%build
for model in %{_models}
do
  ./download-ggml-model.sh "${model}"
  df -h .
done
du -hs .
ls -lh

%install
for model in %{_models}
do
  install -p -D -m 0644 ggml-${model}.bin %{buildroot}%{_datadir}/whisper.cpp/models/ggml-${model}.bin
  # need to save space on github
  rm ggml-${model}.bin
  df -h .
done


%files large-v3
%{_datadir}/whisper.cpp/models/ggml-large-v3.bin

%files large-v3-q5_0
%{_datadir}/whisper.cpp/models/ggml-large-v3-q5_0.bin

%files large-v3-turbo
%{_datadir}/whisper.cpp/models/ggml-large-v3-turbo.bin

%files large-v3-turbo-q5_0
%{_datadir}/whisper.cpp/models/ggml-large-v3-turbo-q5_0.bin

%changelog
* Sun Oct 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1-1
- Added new model: large-v3
- Added new model: large-v3-q5_0
- Added new model: large-v3-turbo
- Added new model: large-v3-turbo-q5_0
