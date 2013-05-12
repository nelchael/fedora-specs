%global commit 10d6c6b52fcdd12f3ba457126f66fee4ccceec04
Name:		vim-securemodelines
Version:	20120929
Release:	1%{?dist}
Summary:	Secure, user-configurable modeline support

License:	Vim
URL:		https://github.com/ciaranm/securemodelines
Source0:	https://raw.github.com/ciaranm/securemodelines/%{commit}/plugin/securemodelines.vim#/%{name}-%{version}-%{commit}.vim

BuildArch:	noarch

%description
Secure, user-configurable modeline support for Vim 7.

Vim's internal modeline support allows all sorts of annoying and potentially
insecure options to be set. This script implements a much more heavily
restricted modeline parser that permits only user-specified options to be set.

%prep
cp -p %SOURCE0 securemodelines.vim

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/plugin
cp securemodelines.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin

%files
%{_datadir}/vim/vimfiles/plugin/*

%changelog
* Mon Dec 31 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20120929-1
- Version bump, fix URLs

* Sat Oct 13 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20080424-2
- Fix prep section

* Wed Aug 29 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20080424-1
- Initial version of package
