%define build_date %(date +"%%a %%b %%d %%Y")
%define build_timestamp %(date +"%%Y%%m%%d.%%H%M%%S")

Name:           com.redhat.system
Version:        1
Release:        %{build_timestamp}%{?dist}
Summary:        Red Hat System API
License:        ASL2.0
URL:            https://github.com/varlink/python-varlink
Source0:        https://github.com/varlink/python-varlink/archive/v%{version}.tar.gz
Requires:       python-varlink

BuildArch:      noarch
BuildRequires:  python3-devel

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
* %{build_date} <info@varlink.org> %{version}-%{build_timestamp}
- %{name} %{version}
