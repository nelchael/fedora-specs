Name:		vim-colorschemes
Version:	20121013
Release:	1%{?dist}
Summary:	A selection of color schemes for Vim

License:	Vim
URL:		http://www.vim.org/
Source0:	gentooish.vim
Source1:	inkpot.vim
Source2:	lingodirector.vim

BuildArch:	noarch

%description
A selection of color schemes for Vim.

%prep
cp -p %SOURCE0 .
cp -p %SOURCE1 .
cp -p %SOURCE2 .

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/colors
cp \
	gentooish.vim \
	inkpot.vim \
	lingodirector.vim \
	%{buildroot}%{_datadir}/vim/vimfiles/colors

%files
%{_datadir}/vim/vimfiles/colors/*

%changelog
* Sat Oct 13 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20121013-1
- Initial version of package
