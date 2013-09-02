%global __provides_exclude_from ^(%{python_sitearch})/.*\\.so$

Name:		python-czjson
Version:	1.0.8
Release:	1%{?dist}
Summary:	Fast JSON encoder/decoder for Python
License:	LGPLv2

URL:		https://pypi.python.org/pypi/czjson
Source0:	https://pypi.python.org/packages/source/c/czjson/czjson-%{version}.tar.gz

BuildRequires:	python2-devel

%description
This module implements a very fast JSON encoder/decoder for Python.

JSON stands for JavaScript Object Notation and is a text based lightweight
data exchange format which is easy for humans to read/write and for machines
to parse/generate. JSON is completely language independent and has multiple
implementations in most of the programming languages, making it ideal for
data exchange and storage.

The module is written in C and it is up to 250 times faster when compared to
the other python JSON implementations which are written directly in python.
This speed gain varies with the complexity of the data and the operation and
is the the range of 10-200 times for encoding.

This is a bug fix fork of python-cjson.

%prep
%setup -q -n czjson-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc LICENSE README
%{python_sitearch}/*

%changelog
* Mon Sep 02 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.0.8-1
- Initial version of package
