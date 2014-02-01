%global commit 88f4a11739bbd28f27837b45b18076f3b0b947f4
Name:		vim-lightline
Version:	20140126
Release:	1%{?dist}
Summary:	A light and configurable statusline/tabline
License:	MIT

URL:		https://github.com/itchyny/lightline.vim
Source0:	https://github.com/itchyny/lightline.vim/archive/%{commit}.zip#/%{name}-%{version}-%{commit}.zip

BuildArch:	noarch

%description
A light and configurable statusline/tabline for Vim.

More information about fonts for special features of this plugin:
https://powerline.readthedocs.org/en/latest/installation/linux.html#font-installation

%prep
%setup -q -n lightline.vim-%{commit}

%build
:

%install
install -m 755 -d %{buildroot}%{_datadir}/vim/vimfiles/autoload
install -m 755 -d %{buildroot}%{_datadir}/vim/vimfiles/plugin
install -m 755 -d %{buildroot}%{_datadir}/vim/vimfiles/doc

cp -R autoload/lightline* %{buildroot}%{_datadir}/vim/vimfiles/autoload/
cp -R plugin/lightline.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin/
cp -R doc/lightline.txt %{buildroot}%{_datadir}/vim/vimfiles/doc

%files
%doc README.md
%{_datadir}/vim/vimfiles/autoload/lightline*
%{_datadir}/vim/vimfiles/plugin/lightline.vim
%{_datadir}/vim/vimfiles/doc/lightline.txt

%changelog
* Sat Feb 01 2014 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20140126-1
- Version bump

* Fri Sep 27 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20130927-1
- Initial version of package
