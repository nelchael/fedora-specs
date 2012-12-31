Name:		b43-firmware
Version:	5.100.138
Release:	2%{?dist}
Summary:	Broadcom firmware for b43 LP PHY and >=linux-3.2
License:	Broadcom
URL:		http://linuxwireless.org/en/users/Drivers/b43
Source:		http://www.lwfinger.com/b43-firmware/broadcom-wl-%{version}.tar.bz2

BuildArch:		noarch
BuildRequires:	b43-fwcutter

%description
Broadcom firmware for b43 LP PHY and >=linux-3.2.

The Broadcom wireless chip needs proprietary software (called "firmware") that
runs on the wireless chip itself to work properly. This firmware is copyrighted
by Broadcom and must be extracted from Broadcom's proprietary drivers.

%prep
%setup -q -n broadcom-wl-%{version}

%build
mkdir fw
b43-fwcutter -w fw linux/wl_apsta.o
chmod 755 fw/b43
chmod 644 fw/b43/*

%install
mkdir -p %{buildroot}/lib/firmware/
cp -r fw/b43 %{buildroot}/lib/firmware/

%files
%doc README
/lib/firmware/b43

%changelog
* Tue Aug 28 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 5.100.138-2
- Fix directory and file permissions for installed firmware

* Sun Aug 26 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 5.100.138-1
- Initial version of package
