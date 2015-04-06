Name:		microsoft-fonts
Version:	20150406
Release:	1%{?dist}
Summary:	Set of Microsoft fonts
License:	proprietary

Source0:	arialbd.ttf
Source1:	arialbi.ttf
Source2:	ariali.ttf
Source3:	arial.ttf
Source4:	ariblk.ttf
Source5:	calibrib.ttf
Source6:	calibrii.ttf
Source7:	calibri.ttf
Source8:	calibriz.ttf
Source9:	cambriab.ttf
Source10:	cambriai.ttf
Source11:	cambriaz.ttf
Source12:	comicbd.ttf
Source13:	comic.ttf
Source14:	consolab.ttf
Source15:	consolai.ttf
Source16:	consola.ttf
Source17:	consolaz.ttf
Source18:	constanb.ttf
Source19:	constani.ttf
Source20:	constan.ttf
Source21:	constanz.ttf
Source22:	corbelb.ttf
Source23:	corbeli.ttf
Source24:	corbel.ttf
Source25:	corbelz.ttf
Source26:	courbd.ttf
Source27:	courbi.ttf
Source28:	couri.ttf
Source29:	cour.ttf
Source30:	georgiab.ttf
Source31:	georgiai.ttf
Source32:	georgia.ttf
Source33:	georgiaz.ttf
Source34:	impact.ttf
Source35:	timesbd.ttf
Source36:	timesbi.ttf
Source37:	timesi.ttf
Source38:	times.ttf
Source39:	trebucbd.ttf
Source40:	trebucbi.ttf
Source41:	trebucit.ttf
Source42:	trebuc.ttf
Source43:	verdanab.ttf
Source44:	verdanai.ttf
Source45:	verdana.ttf
Source46:	verdanaz.ttf
Source47:	webdings.ttf

BuildArch:	noarch

%description
Set of Microsoft fonts:
 - web-core - http://www.microsoft.com/typography/fonts/web.aspx
 - new Windows Vista and Windows 7 fonts

%prep
%build
%install
mkdir -p %{buildroot}%{_datadir}/fonts/microsoft-fonts/
cp %{_sourcedir}/*.ttf %{buildroot}%{_datadir}/fonts/microsoft-fonts/

%files
%{_datadir}/fonts/microsoft-fonts/*.ttf

%changelog
* Mon Apr 06 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20150406-1
- Updated font set

* Wed Dec 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20120826-2
- Remove unused clean section

* Sun Aug 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 20120826-1
- Initial version of package
