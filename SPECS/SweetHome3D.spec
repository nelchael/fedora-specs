Name:		SweetHome3D
Version:	4.2
Release:	1%{?dist}
Summary:	Free interior design application

License:	GPLv2
URL:		http://www.sweethome3d.com
Source0:	http://downloads.sourceforge.net/project/sweethome3d/%{name}-source/%{name}-%{version}-src/%{name}-%{version}-src.zip

BuildArch:	noarch
Requires:	java
BuildRequires:	ant
BuildRequires:	zip
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix

%description
Sweet Home 3D is a free interior design application that helps you draw the plan
of your house, arrange furniture on it and visit the results in 3D.

%prep
%setup -q -n %{name}-%{version}-src

%build
dos2unix --oldfile THIRDPARTY-LICENSE-SUNFLOW.TXT THIRDPARTY-LICENSE-JDOM.TXT README.TXT \
	THIRDPARTY-LICENSE-JDEPEND.TXT THIRDPARTY-LICENSE-JAVA.TXT

for n in APPLEJAVAEXTENSIONS CONTRIBUTIONS; do
	iconv --from-code=iso-8859-1 --to-code=utf-8 THIRDPARTY-LICENSE-${n}.TXT > iconv-tmp
	mv -f iconv-tmp THIRDPARTY-LICENSE-${n}.TXT
done

ant jarExecutable
zip -d install/%{name}-%{version}.jar 'macosx/*' 'windows/*' '*.TXT'
# TODO: Unbundle stuff from resulting jar file

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}

cp install/%{name}-%{version}.jar %{buildroot}%{_datadir}/%{name}/
cp deploy/%{name}Icon32x32.png %{buildroot}%{_datadir}/pixmaps/
cp deploy/%{name}Icon48x48.png %{buildroot}%{_datadir}/pixmaps/

# Create the launcher:
cat >> %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash

java -jar %{_datadir}/%{name}/%{name}-%{version}.jar \${@}
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# Create desktop file:
cat >> %{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
GenericName=%{name}
Exec=%{name}
Icon=%{name}Icon48x48.png
Terminal=false
Type=Application
Categories=Graphics;
EOF
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

%files
%doc *.TXT
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}-%{version}.jar
%{_datadir}/pixmaps/%{name}Icon*x*.png

%changelog
* Thu Nov 14 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 4.2-1
- Initial version of package
