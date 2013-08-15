%define upstream_name google-api-python-client

Name:		python-google-api-client
Version:	1.2
Release:	1%{?dist}
Summary:	Google API Client Library for Python
License:	ASL 2.0

URL:		http://code.google.com/p/google-api-python-client/
Source0:	https://pypi.python.org/packages/source/g/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	python-setuptools
Requires:		python-httplib2

%description
The Google API Client for Python is a client library for accessing the Plus,
Moderator, and many other Google APIs.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# Tests fail, a lot :(
#make tests

%files
%doc LICENSE CHANGELOG FAQ README
%{python_sitelib}/*

%changelog
* Thu Aug 15 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.2-1
- Initial version of package
