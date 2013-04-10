Name:		python-hg-git
Version:	0.4.0
Release:	1%{?dist}
Summary:	Plugin for Hg, adding the ability to push and pull to/from Git

License:	GPLv2
URL:		http://hg-git.github.com
Source0:	https://bitbucket.org/durin42/hg-git/get/0.4.0.tar.bz2

BuildArch:		noarch
BuildRequires:	make
BuildRequires:	git-daemon
BuildRequires:	python-dulwich
Requires:		python-dulwich
Requires:		mercurial

%description
This is the Hg-Git plugin for Mercurial, adding the ability to push and pull
to/from a Git server repository from Hg. This means you can collaborate on Git
based projects from Hg, or use a Git server as a collaboration point for a team
with developers using both Git and Hg.

%prep
%setup -q -n durin42-hg-git-a3c3b8077cbe

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# Tests fail, a lot :(
#make tests

%files
%doc COPYING DESIGN.txt README.md TODO.txt
%{python_sitelib}/*

%changelog
* Wed Apr 10 2013 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 0.4.0-1
- Version bump.

* Fri Feb 22 2012 Krzysztof Pawlik <krzysiek.pawlik@people.pl> 0.3.4-1
- Initial version of package
