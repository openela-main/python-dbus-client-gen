%global srcname dbus-client-gen

Name:           python-%{srcname}
Version:        0.4
Release:        1%{?dist}
Summary:        Library for Generating D-Bus Client Code

License:        MPLv2.0
URL:            https://github.com/stratis-storage/dbus-client-gen
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This library contains a few methods that consume an XML specification\
of a D-Bus interface and return classes or functions that may be useful\
in constructing a python D-Bus client. The XML specification has the format\
of the data returned by the Introspect() method\
of the Introspectable interface.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-hs-dbus-signature

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/dbus_client_gen/
%{python3_sitelib}/dbus_client_gen-*.egg-info/

%changelog
* Tue Dec 11 2018 Andy Grover <agrover@redhat.com> - 0.4-1
- Update to 0.4

* Tue Aug 7 2018 Andy Grover <agrover@redhat.com> - 0.3-1
- Update to 0.3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2-1
- Initial package
