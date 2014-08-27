%global commit 25ae9963087a
Name:		hg-publishall
Version:	0
Release:	1.git20131118%{?dist}
Summary:	Mercurial extension allowing one to push simultaneously to many repositories
License:	MIT

URL:		https://bitbucket.org/pelletier/hg-publishall/src
Source0:	https://bitbucket.org/pelletier/%{name}/get/%{commit}.zip#/%{name}-%{version}-%{commit}.zip

BuildArch:	noarch

%description
Hg-publishall is a mercurial extension which allows you to push simultaneously
to multiple repositories, in a single command.

%prep
%setup -q -n pelletier-%{name}-%{commit}

%build
dos2unix -o publishall.py

%install
mkdir -p %{buildroot}%{python_sitelib}
cp publishall.py %{buildroot}%{python_sitelib}/

%files
%doc LICENSE README.markdown
%{python_sitelib}/*

%changelog
* Mon Nov 18 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 0-1.git20131118
- Initial version of package
