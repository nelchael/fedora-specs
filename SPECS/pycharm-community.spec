Name:		pycharm-community
Version:	3.0.1
Release:	3%{?dist}
Summary:	The intelligent Python IDE with unique code assistance and analysis
License:	ASL 2.0

URL:		http://www.jetbrains.com/pycharm/
Source0:	http://download-ln.jetbrains.com/python/%{name}-%{version}.tar.gz

Requires:	java
BuildArch:	noarch

%define __jar_repack 0
%global debug_package %{nil}
%define _binaries_in_noarch_packages_terminate_build 0

%description
The intelligent Python IDE with unique code assistance and analysis, for
productive Python development on all levels.

Free Community Edition for pure Python coding and learning.

 - Intelligent Editor, with code completion, on-the-fly error highlighting,
   auto-fixes, etc.
 - Automated code refactorings and rich navigation capabilities
 - Integrated debugger and unit testing support
 - Native VCS integrations
 - Customizable UI and key-bindings, with VIM emulation available

%prep
%setup -q

%build
sed -i -e 's,read I,#read I,g' bin/pycharm.sh
strip bin/fsnotifier*
strip plugins/terminal/lib/linux/*/libpty.so

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}

cp bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/
rm -f bin/pycharm.png

cp -R \
	bin \
	help \
	helpers \
	lib \
	plugins \
	%{buildroot}%{_libdir}/%{name}/
rm -fv %{buildroot}%{_libdir}/%{name}/help/*.pdf

# Create the launcher:
cat >> %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash

exec %{_libdir}/%{name}/bin/pycharm.sh \${@}
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# Create desktop file:
cat >> %{name}.desktop <<EOF
[Desktop Entry]
Name=PyCharm Community
GenericName=PyCharm Community
Exec=%{name}
Icon=pycharm.png
Terminal=false
Type=Application
Categories=Development;
EOF
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

%files
%defattr(-, root, root, -)
%doc license help/ReferenceCard.pdf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/pycharm.png
%{_libdir}/%{name}/bin
%{_libdir}/%{name}/help
%{_libdir}/%{name}/helpers
%{_libdir}/%{name}/lib
%{_libdir}/%{name}/plugins

%changelog
* Wed Nov 13 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.0.1-3
- Changed to noarch

* Sat Nov 09 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.0.1-2
- Changed to arch-dependant RPM, minor fixes

* Tue Nov 05 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.0.1-1
- Initial version of package
