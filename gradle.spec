Name:		gradle
Version:	2.3
Release:	1%{?dist}
Summary:	Open source build automation

License:	ASL 2.0
URL:		http://gradle.org/
Source0:	https://downloads.gradle.org/distributions/%{name}-%{version}-bin.zip

BuildArch:		noarch
BuildRequires:	unzip
Requires:		java
AutoReqProv:	no

%define __jar_repack 0

%description
Gradle is a project automation tool that builds upon the concepts of Apache Ant
and Apache Maven and introduces a Groovy-based domain-specific language (DSL)
instead of the more traditional XML form of declaring the project configuration.

%prep
%setup -q

%build
:

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/bin
mkdir -p %{buildroot}%{_datadir}/%{name}/lib

cp bin/gradle %{buildroot}%{_datadir}/%{name}/bin/
ln -s %{_datadir}/%{name}/bin/gradle %{buildroot}%{_bindir}/

cp -r lib/* %{buildroot}%{_datadir}/%{name}/lib/

%files
%doc changelog.txt getting-started.html LICENSE NOTICE
%{_bindir}/gradle
%{_datadir}/%{name}/bin/gradle
%{_datadir}/%{name}/lib/*.jar
%{_datadir}/%{name}/lib/plugins/*.jar

%changelog
* Fri Apr 03 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 2.3-1
- Initial version of package
