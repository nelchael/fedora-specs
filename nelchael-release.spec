Name:		nelchael-release
Version:	1
Release:	5%{?dist}
Summary:	Nelchael Repository Configuration
License:	BSD

URL:		https://bitbucket.org/nelchael/specs

BuildArch:	noarch
Requires:	system-release >= %{version}

%description
Nelchael's RPM repository configuration (Yum repository configuration and GPG
public key).

%prep
:

%build
:

%install
mkdir -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
cat > %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-nelchael <<GPG_KEY
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

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
Hf2GLsTnllH74f568X9FcIPsjvOShg==
=RyNq
-----END PGP PUBLIC KEY BLOCK-----
GPG_KEY

mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
cat > %{buildroot}%{_sysconfdir}/yum.repos.d/nelchael.repo <<REPO
[nelchael]
name=nelchael
baseurl=https://googledrive.com/host/0B27CFjB-gnGVSnRTQjBEYkIxX2M
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-nelchael
REPO

%files
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
* Fri Apr 03 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1-5
- Fix GPG key installation

* Fri Apr 03 2015 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1-4
- New GPG public key

* Mon Nov 18 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1-3
- Change URL to Bitbucket

* Sun Aug 25 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1-2
- Add gpgkey location to repo file

* Thu Aug 15 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 1-1
- Initial version of package
