%define _models tiny base small medium 

Name:           whisper.cpp
Version:        0.1
Release:        1%{?dist}
Summary:        Models fpr WhisperC++
Group:          Networking/Daemons
License:        ASL 2.0
Source0:        https://raw.githubusercontent.com/ggerganov/whisper.cpp/v1.5.2/models/download-ggml-model.sh
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


%prep
%setup -c -n %{name} -T
install -m 0755 %{SOURCE0} .


%build
for model in %{_models}
do
  ./download-ggml-model.sh "${model}"
done

%install
for model in %{_models}
do
  install -p -D -m 0644 ggml-${model}.bin %{buildroot}%{_datadir}/whisper.cpp/models/ggml-${model}.bin
done


%files tiny
%{_datadir}/whisper.cpp/models/ggml-tiny.bin

%files base
%{_datadir}/whisper.cpp/models/ggml-base.bin

%files small
%{_datadir}/whisper.cpp/models/ggml-small.bin

%files medium
%{_datadir}/whisper.cpp/models/ggml-medium.bin

%changelog
* Sat Dec 16 2023 Lars Kiesow <lkiesow@uos.de> - 0.1-1
- Initial Build

