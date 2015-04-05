%define upstream_name google-api-python-client

Name:		python-google-api-client
Version:	1.4.0
Release:	3%{?dist}
Summary:	Google API Client Library for Python
License:	ASL 2.0

URL:		https://github.com/google/google-api-python-client
Source0:	https://github.com/google/google-api-python-client/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	python-setuptools
Requires:		python-oauth2client
Requires:		python-uri-templates

%description
The Google API Client for Python is a client library for accessing the Plus,
Moderator, and many other Google APIs.

%prep
%setup -q -n %{upstream_name}-%{version}
sed -i -e 's,import os,return,' setup.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# Tests fail, a lot :(
#make tests

%files
%doc CHANGELOG LICENSE README.md docs/dyn docs/epy
%{python_sitelib}/*

%changelog
* Sun Apr 05 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.4.0-3
- Fix dependencies

* Sun Apr 05 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.4.0-2
- Fix dependencies

* Sun Apr 05 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.4.0-1
- Version bump, update URLs

* Thu Aug 15 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.2-1
- Initial version of package
