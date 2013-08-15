Name:		nelchael-release
Version:	1
Release:	1%{?dist}
Summary:	Nelchael Repository Configuration
License:	BSD

URL:		http://localhost

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
Version: GnuPG v1.4.14 (GNU/Linux)

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
v5zMP0bKKBRcJzW3yTgnXu0Q80voWdSs5y/e+KvJMIaE6426KHQWYWk6r7XS1ylt
E33jLonuzX/9JquSQ8L3WZ2HVe107rV11IheR5cQkurr+SWaf44a+om/XmyK3vKG
JAk9SWhXqubheS81J/aSmpy8bd11ErLkdgdMG7nFxjsCts0Gh7ySuwEGBk8wRb5i
QiM+/Qj6BmQM/xBHBVcGtQIequ+jW+CZOiNtI9nX/duv15T7s2SrkqTkyMxMoC5e
HqgMhVQDY8zTABEBAAGJASUEGAECAA8FAkuxE7sCGwwFCQlmAYAACgkQFnK/Wvao
DkZrWQf+M4qmVub4wHiRIBT91oSCXXLJ34kil4L+aJtOv9jdJts0Cq9Dq1UmoeDM
TGAJYsW1XKNPKN7uI2/4KlB+50Yw0DOFQip5eydvPlyL2dZQWK9G4PGb+uuZ+iZE
b8kUDBdtwKHg8XKL8X2Xl8EvKwT/+i6Yoc0D9XysWD0BX5A11q4rsr0TfcGeglji
552UNAizdE9BKo0LA5ceZTssoXbVS3Tqg/4GzmxUSLvWxFEHudlEnvVXhS+nnTZw
jKe/7+b4VBCIskVWpvGKnu9+/rWPxsK99pW4xHWXqXBDmbBx00hYfhycb+t8lBUf
iHVQpuDqAtYUR0U5e13TVzODOkqatA==
=OY27
-----END PGP PUBLIC KEY BLOCK-----
GPG_KEY

mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
cat > %{buildroot}%{_sysconfdir}/yum.repos.d/nelchael.repo <<REPO
[nelchael]
name=nelchael
baseurl=https://googledrive.com/host/0B27CFjB-gnGVSnRTQjBEYkIxX2M
enabled=1
gpgcheck=1
REPO

%files
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%post
/usr/bin/rpmkeys --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-nelchael

%changelog
* Thu Aug 15 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> - 1-1
- Initial version of package
