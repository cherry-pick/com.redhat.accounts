Name:           com.redhat.system
Version:        1
Release:        1%{?dist}
Summary:        Red Hat System API
License:        ASL2.0
URL:            https://github.com/varlink/%{name}
Source0:        https://github.com/varlink/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       python-varlink

BuildArch:      noarch
BuildRequires:  pkgconfig(python3) python3-rpm-macros

%description
Red Hat System API.

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
%{_prefix}/lib/%{name}/*

%changelog
* Tue Aug 29 2017 <info@varlink.org> 1-1
- com.redhat.system 1
