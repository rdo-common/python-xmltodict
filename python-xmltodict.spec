%global srcname xmltodict
%global sum A Python to transform XML to JSON

%if 0%{?fedora}
%global with_python3 1
%endif

Name:               python-xmltodict
Version:            0.10.1
Release:            1%{?dist}
Summary:            %{sum}

License:            MIT
URL:                https://github.com/martinblech/xmltodict
Source0:            http://pypi.python.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:          noarch

%description
xmltodict is a Python module that makes working with XML feel like you are
working with JSON.  It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:      python2-devel
BuildRequires:      python2-nose

%description -n python2-%{srcname}
xmltodict is a Python module that makes working with XML feel like you are
working with JSON.  It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.

%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:      python3-devel
BuildRequires:      python3-nose

%description -n python3-%{srcname}
xmltodict is a Python module that makes working with XML feel like you are
working with JSON.  It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.
%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
nosetests-2.7
%if 0%{?with_python3}
pushd %{py3dir}
nosetests-%{py3ver}
popd
%endif

%files -n python2-%{srcname}
%doc README.md PKG-INFO
%license LICENSE
%{python2_sitelib}/%{srcname}.py*
%{python2_sitelib}/%{srcname}-%{version}*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc README.md LICENSE PKG-INFO
%license LICENSE
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-*
%{python3_sitelib}/__pycache__/%{srcname}*
%endif

%changelog
* Sun May 01 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.1-1
- Update to latest upstream reelase 0.10.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-1
- Cleanup
- Update to latest upstream reelase 0.9.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update spec file according guidelines 
- Update to upstream release 0.9.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Ralph Bean <rbean@redhat.com> - 0.4.2-1
- Latest upstream
- Included README and LICENSE
- Running tests now
- https://github.com/martinblech/xmltodict/pull/11
- Added Requires python3 to the python3 subpackage.

* Fri Jan 04 2013 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- Initial packaging for Fedora
