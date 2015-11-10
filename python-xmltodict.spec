%if 0%{?fedora} > 12
%global with_python3 1
%{!?py3ver: %global py3ver %(%{__python3} -c "import sys ; print(sys.version[:3])")}
%else
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif
%{!?py2ver: %global py2ver %(%{__python2} -c "import sys ; print sys.version[:3]")}

%global srcname xmltodict

Name:               python-xmltodict
Version:            0.9.0
Release:            3%{?dist}
Summary:            Makes working with XML feel like you are working with JSON

Group:              Development/Libraries
License:            MIT
URL:                https://github.com/martinblech/xmltodict
Source0:            http://pypi.python.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python-nose

%if 0%{?with_python3}
BuildRequires:      python3-devel
BuildRequires:      python3-nose
%endif

%description
xmltodict is a Python module that makes working with XML feel like you are
working with JSON.  It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.

    >>> doc = xmltodict.parse("""
    ... <mydocument has="an attribute">
    ...   <and>
    ...     <many>elements</many>
    ...     <many>more elements</many>
    ...   </and>
    ...   <plus a="complex">
    ...     element as well
    ...   </plus>
    ... </mydocument>
    ... """)
    >>>
    >>> doc['mydocument']['@has']
    u'an attribute'
    >>> doc['mydocument']['and']['many']
    [u'elements', u'more elements']
    >>> doc['mydocument']['plus']['@a']
    u'complex'
    >>> doc['mydocument']['plus']['#text']
    u'element as well'


%if 0%{?with_python3}
%package -n python3-xmltodict
Summary:            Makes working with XML feel like you are working with JSON
Group:              Development/Libraries

Requires:           python3

%description -n python3-xmltodict
xmltodict is a Python module that makes working with XML feel like you are
working with JSON.  It's very fast (Expat-based) and has a streaming mode
with a small memory footprint, suitable for big XML dumps like Discogs or
Wikipedia.

    >>> doc = xmltodict.parse("""
    ... <mydocument has="an attribute">
    ...   <and>
    ...     <many>elements</many>
    ...     <many>more elements</many>
    ...   </and>
    ...   <plus a="complex">
    ...     element as well
    ...   </plus>
    ... </mydocument>
    ... """)
    >>>
    >>> doc['mydocument']['@has']
    u'an attribute'
    >>> doc['mydocument']['and']['many']
    [u'elements', u'more elements']
    >>> doc['mydocument']['plus']['@a']
    u'complex'
    >>> doc['mydocument']['plus']['#text']
    u'element as well'
%endif

%prep
%setup -q -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

%build
%{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%check
nosetests-%{py2ver}
%if 0%{?with_python3}
pushd %{py3dir}
nosetests-%{py3ver}
popd
%endif

%files
%doc README.md LICENSE PKG-INFO
%{python_sitelib}/%{srcname}.py*
%{python_sitelib}/%{srcname}-%{version}*

%if 0%{?with_python3}
%files -n python3-xmltodict
%doc README.md LICENSE PKG-INFO
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-*
%{python3_sitelib}/__pycache__/%{srcname}*
%endif

%changelog
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
