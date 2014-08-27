Name:		vim-python
Version:	3.3.6
Release:	1%{?dist}
Summary:	Enhanced version of the python syntax highlighting script
License:	Vim

URL:		http://www.vim.org/scripts/script.php?script_id=790
Source0:	http://www.vim.org/scripts/download_script.php?src_id=20632#/%{name}-%{version}.vim

BuildArch:	noarch

%description
Enhanced version of the original (from vim6.1) python.vim for Python programming
language.

%prep
cp -p %SOURCE0 python.vim

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/syntax
cp python.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax

%files
%{_datadir}/vim/vimfiles/syntax/*

%changelog
* Sat Feb 01 2014 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.3.6-1
- Version bump

* Sat Aug 24 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 3.3.4-1
- Initial version of package
