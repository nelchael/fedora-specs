%global commit 752e607ba78550de6ddace4f009ced4c5f7ae395
Name:		vim-json
Version:	0.12
Release:	1.git20130828%{?dist}
Summary:	Better JSON for VIM
License:	MIT

URL:		https://github.com/elzr/vim-json
Source0:	https://github.com/elzr/vim-json/archive/%{commit}.zip#/%{name}-%{version}-%{commit}.zip

BuildArch:	noarch

%description
Distinct highlighting of keywords vs values, JSON-specific (non-JS) warnings,
quote concealing.

%prep
%setup -q -n %{name}-%{commit}

%build
:

%install
for dir in ftplugin ftdetect syntax; do
	mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/${dir}
	cp ${dir}/json.vim %{buildroot}%{_datadir}/vim/vimfiles/${dir}/
done

%files
%doc readme.md
%{_datadir}/vim/vimfiles/ftdetect/*
%{_datadir}/vim/vimfiles/ftplugin/*
%{_datadir}/vim/vimfiles/syntax/*

%changelog
* Sat Feb 01 2014 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 0.12-1.git20130828
- Version bump

* Sun May 12 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 0.12-1.git20130512
- Initial version of package
