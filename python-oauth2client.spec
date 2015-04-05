Name:		python-oauth2client
Version:	1.4.7
Release:	2%{?dist}
Summary:	Python library for accessing resources protected by OAuth 2.0
License:	ASL 2.0

URL:		https://github.com/google/oauth2client
Source0:	https://github.com/google/oauth2client/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:		noarch
BuildRequires:	python-setuptools

%description
oauth2client makes it easy to interact with OAuth2-protected resources,
especially those related to Google APIs.

%prep
%setup -q -n oauth2client-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc CHANGELOG.md LICENSE README.md
%{python_sitelib}/*

%changelog
* Sun Apr 05 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.4.7-2
- Fix dependencies

* Sun Apr 05 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.4.7-1
- Initial version of package
