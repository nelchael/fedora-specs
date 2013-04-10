Name:		vim-colorscheme-inkpot
Version:	20130410
Release:	2%{?dist}
Summary:	Vim color scheme: inkpot

License:	Vim
URL:		https://github.com/ciaranm/inkpot
Source:		https://raw.github.com/ciaranm/inkpot/master/colors/inkpot.vim

BuildArch:	noarch
Conflicts:	vim-colorschemes

%description
Vim color scheme: inkpot.

%prep
cp -p %SOURCE0 .

%build

%install
install -m 755 -d %{buildroot}%{_datadir}/vim/vimfiles/colors
install -m 644 inkpot.vim %{buildroot}%{_datadir}/vim/vimfiles/colors

%files
%{_datadir}/vim/vimfiles/colors/

%changelog
* Wed Apr 10 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20130410-2
- Use file name for install call.

* Wed Apr 10 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20130410-1
- Version bump.

* Mon Dec 31 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20121122-1
- Split from vim-colorschemes package, small updates.

* Sat Oct 13 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20121013-1
- Initial version of package
