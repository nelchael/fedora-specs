Name:		yed
Version:	3.11.1
Release:	1%{?dist}
Summary:	Application to quickly and effectively generate diagrams
License:	yEd

URL:		http://www.yworks.com/en/products_yed_about.html
Source0:	http://www.yworks.com/products/yed/demo/yEd-%{version}.zip

BuildArch:		noarch
BuildRequires:	unzip
BuildRequires:	desktop-file-utils
Requires:		java

%define __jar_repack 0

%description
yEd is a powerful desktop application that can be used to quickly and
effectively generate high-quality diagrams. Create diagrams manually, or import
your external data for analysis.

%prep
%setup -q

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}

cp yed.jar %{buildroot}%{_datadir}/%{name}/
cp vectorgraphics.jar %{buildroot}%{_datadir}/%{name}/

cp icons/yicon32.png %{buildroot}%{_datadir}/pixmaps/
cp icons/yicon16.png %{buildroot}%{_datadir}/pixmaps/

# Create the launcher:
cat >> %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash

java -jar %{_datadir}/%{name}/yed.jar \${@}
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# Create desktop file:
cat >> yed.desktop <<EOF
[Desktop Entry]
Name=yEd
GenericName=yEd
Exec=yed
Icon=yicon32
Terminal=false
Type=Application
Categories=Graphics;
EOF
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	yed.desktop

%files
%doc license.html
%{_bindir}/%{name}
%{_datadir}/applications/yed.desktop
%{_datadir}/%{name}/*.jar
%{_datadir}/pixmaps/yicon??.png

%changelog
* Fri Oct 11 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.11.1-1
- Version bump.

* Wed Apr 10 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.10.2-1
- Version bump.

* Sat Jan 19 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.10.1-1
- Initial version of package
