%global vosk_model small-es

Name:           vosk-cli-model-%{vosk_model}
Version:        0.42
Release:        1%{?dist}
Summary:        Language model %{vosk_model} for Vosk.

License:        Apache-2.0
URL:            alphacephei.com/vosk/models/

Source0:        https://alphacephei.com/vosk/models/vosk-model-%{vosk_model}-%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip


%description
This is the %{vosk_model} language model for Vosk.

Vosk is an offline open source speech recognition toolkit. It enables speech
recognition models for 17 languages and dialects - English, Indian English,
German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese,
Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino.


%prep
unzip %{SOURCE0}


%build
# nothing to do
# we download the language model and move it to the desired directory


%install
mkdir -p %{buildroot}%{_datadir}/vosk/models/
mv vosk-model-%{vosk_model}-%{version} %{buildroot}%{_datadir}/vosk/models/%{vosk_model}


%clean
rm -rf %{buildroot}


%files
%{_datadir}/vosk/models/%{vosk_model}


%changelog
* Tue Jan 24 2023 Lars Kiesow <lkiesow@uos.de> - 0.42-1
- Initial build
