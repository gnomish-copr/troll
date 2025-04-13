%global commit 53155a02e06ff66e6c15d470f39d782305c1502f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           troll
Version:        0.1
Release:        2%{?dist}
Summary:        Troll GJS library
License:        ISC
URL:            https://github.com/sonnyp/troll
Source0:        https://github.com/sonnyp/troll/archive/%{commit}.zip
BuildArch:      noarch

BuildRequires:  nodejs
BuildRequires:  npm

Requires:       gjs

%description
troll is an implementation of common JavaScript APIs for gjs and some helpers.

%prep
%autosetup -n %{name}-%{commit}

%build
npm install
# TODO: It should work without this if
# Check if rollup is installed in node_modules
if [ -f ./node_modules/.bin/rollup ]; then
  ./node_modules/.bin/rollup -c rollup.config.js
else
  echo "Rollup not found, installing globally..."
  npm install -g rollup
  rollup -c rollup.config.js
fi

%install
# Create directories
mkdir -p %{buildroot}%{_datadir}/gjs-1.0/troll/
mkdir -p %{buildroot}%{_datadir}/doc/%{name}

# install library files
cp -a src/ %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a gjspack/ %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a gsx-demo/ %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a test/ %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a tst/ %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a package.json %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a package-lock.json %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a rollup.config.js %{buildroot}%{_datadir}/gjs-1.0/troll/

mkdir -p %{buildroot}%{_datadir}/gjs-1.0/troll/dist

cp -a README.md %{buildroot}%{_datadir}/doc/%{name}/
cp -a LICENSE %{buildroot}%{_datadir}/doc/%{name}/
cp -a notes.md %{buildroot}%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc README.md
%{_datadir}/gjs-1.0/troll/
%{_datadir}/doc/%{name}/

%changelog
* Sun Apr 13 2025 Taiwbi <taiwbii@proton.me> - 0.1-2
- Moved to rpkg packaging format
- Install missed files and directories
* Mon Apr 07 2025 Taiwbi <taiwbii@proton.me> - 0.1-1
- Initial package
