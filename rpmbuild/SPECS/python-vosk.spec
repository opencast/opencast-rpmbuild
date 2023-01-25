%global srcname vosk

Name:           python-%{srcname}
Version:        0.3.45
Release:        %{?dist}
Summary:        Offline speech recognition API

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/alphacep/vosk-api/releases/download/v%{version}/vosk-%{version}-py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.whl
Source1:        https://raw.githubusercontent.com/alphacep/vosk-api/v%{version}/README.md
Source2:        https://raw.githubusercontent.com/alphacep/vosk-api/v%{version}/COPYING

%global _description %{expand:
This is a Python module for Vosk.

Vosk is an offline open source speech recognition toolkit. It enables speech
recognition models for 17 languages and dialects - English, Indian English,
German, French, Spanish, Portuguese, Chinese, Russian, Turkish, Vietnamese,
Italian, Dutch, Catalan, Arabic, Greek, Farsi, Filipino.
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  unzip

Requires:       %{py3_dist cffi} >= 1
Requires:       %{py3_dist srt}
Requires:       %{py3_dist tqdm}

%description -n python3-%{srcname} %_description

%prep
unzip %{SOURCE0}
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
# nothing to do
# we cheat and download the prebuild package

%install
install -p -d -m 0755 %{buildroot}%{python3_sitelib}/
mv -v vosk* %{buildroot}%{python3_sitelib}/

%clean
rm -rf %{buildroot}

%files -n python3-%{srcname}
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}*


%changelog
* Thu Jan 12 2023 Lars Kiesow <lkiesow@uos.de> - 0.3.45-1
- Update to 0.3.45

