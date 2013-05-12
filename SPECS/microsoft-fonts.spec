Name:		microsoft-fonts
Version:	20120826
Release:	2%{?dist}
Summary:	Set of Microsoft fonts (web-core fonts and Vista fonts)
License:	proprietary

Source0:	microsoft-fonts-20120826.tar.xz

BuildArch:	noarch

%description
Set of Microsoft fonts:
 - web-core - http://www.microsoft.com/typography/fonts/web.aspx
 - new Windows Vista and Windows 7 fonts

%prep
%setup -q

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/fonts/microsoft-fonts/
cp *.ttf %{buildroot}%{_datadir}/fonts/microsoft-fonts/

%files
%{_datadir}/fonts/microsoft-fonts/*.ttf

%changelog
* Wed Dec 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20120826-2
- Remove unused clean section

* Sun Aug 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20120826-1
- Initial version of package
