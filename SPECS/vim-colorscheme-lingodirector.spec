Name:		vim-colorscheme-lingodirector
Version:	1.1
Release:	1%{?dist}
Summary:	Vim color scheme: lingodirector

License:	Vim
URL:		http://www.vim.org/scripts/script.php?script_id=4068
Source:		lingodirector.vim

BuildArch:	noarch
Conflicts:	vim-colorschemes

%description
Vim color scheme: lingodirector.

%prep
cp -p %SOURCE0 .

%build

%install
install -m 755 -d %{buildroot}%{_datadir}/vim/vimfiles/colors
install -m 644 *.vim %{buildroot}%{_datadir}/vim/vimfiles/colors

%files
%{_datadir}/vim/vimfiles/colors/

%changelog
* Mon Dec 31 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1.1-1
- Split from vim-colorschemes package, small updates.

* Sat Oct 13 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20121013-1
- Initial version of package
