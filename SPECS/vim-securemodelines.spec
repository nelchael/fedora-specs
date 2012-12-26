Name:		vim-securemodelines
Version:	20080424
Release:	2%{?dist}
Summary:	Secure, user-configurable modeline support

License:	Vim
URL:		http://www.vim.org/scripts/script.php?script_id=1876
# Download form $URL
Source0:	securemodelines.vim

BuildArch:	noarch

%description
Secure, user-configurable modeline support for Vim 7.

Vim's internal modeline support allows all sorts of annoying and potentially
insecure options to be set. This script implements a much more heavily
restricted modeline parser that permits only user-specified options to be set.

%prep
cp -p %SOURCE0 .

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/plugin
cp securemodelines.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin

%files
%{_datadir}/vim/vimfiles/plugin/*

%changelog
* Sat Oct 13 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20080424-2
- Fix prep section

* Wed Aug 29 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20080424-1
- Initial version of package
