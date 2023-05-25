%global srcname webvtt-py

Name:           python-%{srcname}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Read, write and segment WebVTT caption files in Python

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/1b/83/115b001f8c79f9580834faf214062b1ff69f61c62ab1a5c3c1e5e347d4a3/webvtt_py-0.4.6-py3-none-any.whl
Source1:        https://github.com/glut23/webvtt-py/raw/%{version}/README.rst
Source2:        https://github.com/glut23/webvtt-py/raw/%{version}/LICENSE

%global _description %{expand:
webvtt-py is a Python module for reading/writing WebVTT caption files.
It also features caption segmentation useful when captioning HLS videos.
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  unzip

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
mv -v webvtt* %{buildroot}%{python3_sitelib}/

%clean
rm -rf %{buildroot}

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/webvtt*
