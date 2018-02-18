Name:           com.redhat.accounts
Version:        1
Release:        1%{?dist}
Summary:        Accounts Interface
License:        ASL2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       python3-varlink

BuildArch:      noarch
BuildRequires:  pkgconfig(python3) python3-rpm-macros

%description
Accounts Interface.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*
%{_prefix}/lib/com.redhat/*

%changelog
* Tue Aug 29 2017 <info@varlink.org> 1-1
- com.redhat.accounts 1
