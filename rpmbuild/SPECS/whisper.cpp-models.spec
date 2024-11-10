%define _models tiny base small medium large-v1 large-v2 large-v2-q5_0
#large-v3 large-v3-q5_0 large-v3-turbo large-v3-turbo-q5_0

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

%package tiny
Summary: Model 'tiny' for whisper.cpp
%description tiny
Model 'tiny' for whisper.cpp

%package base
Summary: Model 'base' for whisper.cpp
%description base
Model 'base' for whisper.cpp

%package small
Summary: Model 'small' for whisper.cpp
%description small
Model 'small' for whisper.cpp

%package medium
Summary: Model 'medium' for whisper.cpp
%description medium
Model 'medium' for whisper.cpp

%package large-v1
Summary: Model 'large-v1' for whisper.cpp
%description large-v1
Model 'large-v1' for whisper.cpp

%package large-v2
Summary: Model 'large-v2' for whisper.cpp
%description large-v2
Model 'large-v2' for whisper.cpp

%package large-v2-q5_0
Summary: Model 'large-v2-q5_0' for whisper.cpp
%description large-v2-q5_0
Model 'large-v2-q5_0' for whisper.cpp

#%package large-v3
#Summary: Model 'large-v3' for whisper.cpp
#%description large-v3
#Model 'large-v3' for whisper.cpp
#
#%package large-v3-q5_0
#Summary: Model 'large-v3-q5_0' for whisper.cpp
#%description large-v3-q5_0
#Model 'large-v3-q5_0' for whisper.cpp
#
#%package large-v3-turbo
#Summary: Model 'large-v3-turbo' for whisper.cpp
#%description large-v3-turbo
#Model 'large-v3-turbo' for whisper.cpp
#
#%package large-v3-turbo-q5_0
#Summary: Model 'large-v3-turbo-q5_0' for whisper.cpp
#%description large-v3-turbo-q5_0
#Model 'large-v3-turbo-q5_0' for whisper.cpp


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


%files tiny
%{_datadir}/whisper.cpp/models/ggml-tiny.bin

%files base
%{_datadir}/whisper.cpp/models/ggml-base.bin

%files small
%{_datadir}/whisper.cpp/models/ggml-small.bin

%files medium
%{_datadir}/whisper.cpp/models/ggml-medium.bin

%files large-v1
%{_datadir}/whisper.cpp/models/ggml-large-v1.bin

%files large-v2
%{_datadir}/whisper.cpp/models/ggml-large-v2.bin

%files large-v2-q5_0
%{_datadir}/whisper.cpp/models/ggml-large-v2-q5_0.bin

#%files large-v3
#%{_datadir}/whisper.cpp/models/ggml-large-v3.bin
#
#%files large-v3-q5_0
#%{_datadir}/whisper.cpp/models/ggml-large-v3-q5_0.bin
#
#%files large-v3-turbo
#%{_datadir}/whisper.cpp/models/ggml-large-v3-turbo.bin
#
#%files large-v3-turbo-q5_0
#%{_datadir}/whisper.cpp/models/ggml-large-v3-turbo-q5_0.bin

%changelog
* Sun Oct 27 2024 Lars Kiesow <lkiesow@uos.de> - 0.1-1
- Added new model: large-v1
- Added new model: large-v2
- Added new model: large-v2-q5_0
#- Added new model: large-v3
#- Added new model: large-v3-q5_0
#- Added new model: large-v3-turbo
#- Added new model: large-v3-turbo-q5_0

* Sat Dec 16 2023 Lars Kiesow <lkiesow@uos.de> - 0.1-1
- Initial Build

