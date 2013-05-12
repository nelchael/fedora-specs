Name:		yuicompressor
Version:	2.4.7
Release:	1%{?dist}
Summary:	Tool that supports the compression of both JavaScript and CSS files
License:	BSD

URL:		http://yuilibrary.com/projects/yuicompressor/
Source0:	http://yui.zenfs.com/releases/yuicompressor/%{name}-%{version}.zip

BuildArch:		noarch
BuildRequires:	unzip
BuildRequires:	ant
Requires:		java

%description
YUI Compressor is an open source tool that supports the compression of both
JavaScript and CSS files. The JavaScript compression removes comments and
white-spaces as well as obfuscates local variables using the smallest possible
variable name. CSS compression is done using a regular-expression-based CSS
minifier.

%prep
%setup -q

%build
ant clean build.jar

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}

cp build/%{name}-%{version}.jar %{buildroot}%{_datadir}/%{name}/

# Create the launcher:
cat >> %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash

java -jar %{_datadir}/%{name}/%{name}-%{version}.jar \${@}
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

%files
%doc doc/CHANGELOG doc/README
%{_datadir}/%{name}/%{name}-%{version}.jar
%{_bindir}/%{name}

%changelog
* Sun Aug 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 2.4.7-1
- Initial version of package
