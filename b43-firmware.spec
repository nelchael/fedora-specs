Name:		b43-firmware
Version:	6.30.163.46
Release:	1%{?dist}
Summary:	Broadcom firmware for b43 LP PHY and >=linux-3.2
License:	Broadcom

URL:		http://linuxwireless.org/en/users/Drivers/b43
Source0:	http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2

BuildArch:		noarch
BuildRequires:	b43-fwcutter

%description
Broadcom firmware for b43 LP PHY and >=linux-3.2.

The Broadcom wireless chip needs proprietary software (called "firmware") that
runs on the wireless chip itself to work properly. This firmware is copyrighted
by Broadcom and must be extracted from Broadcom's proprietary drivers.

%prep
%setup -c

%build
mkdir fw
b43-fwcutter -w fw broadcom-wl-%{version}.wl_apsta.o
chmod 755 fw/b43
chmod 644 fw/b43/*

%install
mkdir -p %{buildroot}/lib/firmware/
cp -r fw/b43 %{buildroot}/lib/firmware/

%files
/lib/firmware/b43

%changelog
* Sun Dec 14 2014 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 6.30.163.46-1
- Version bump

* Tue Aug 28 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 5.100.138-2
- Fix directory and file permissions for installed firmware

* Sun Aug 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 5.100.138-1
- Initial version of package
