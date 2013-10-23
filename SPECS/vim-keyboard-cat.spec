%global commit a3ff76ed0425654ac1e8f7775c4f0d9ec41b53ba
Name:		vim-keyboard-cat
Version:	20131023
Release:	1%{?dist}
Summary:	A vim plugin for pretending like you can type really fast
License:	Vim

URL:		https://github.com/natw/keyboard_cat.vim
Source0:	https://raw.github.com/natw/keyboard_cat.vim/%{commit}/plugin/keyboard_cat.vim#/%{name}-%{version}-%{commit}.vim

BuildArch:	noarch

%description
A vim plugin for pretending like you can type really fast.

Conceivably, when giving some kind of presentation, you might want to pretend
like you are typing something out. But typing and talking is hard, so with this
you can just mash on the keyboard and let the letters magically appear.

This might only really be useful for less serious presentations, like TiP BoF
talks

%prep
cp -p %SOURCE0 keyboard_cat.vim

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/plugin
cp keyboard_cat.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin

%files
%{_datadir}/vim/vimfiles/plugin/*

%changelog
* Wed Oct 23 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20131023-1
- Initial version of package
