%{?scl:%scl_package nodejs-es6-iterator}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename es6-iterator
%global enable_tests 0
# tests disabled due to missing npm(tad) test suite

Name:		%{?scl_prefix}nodejs-es6-iterator
Version:	2.0.0
Release:	4%{?dist}
Summary:	Iterator abstraction based on ES6 specification

License:	MIT
URL:		https://github.com/medikoo/es6-iterator.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tad)
%endif

Requires:	%{?scl_prefix}nodejs

%description
Iterator abstraction based on ES6 specification

%prep
%setup -q -n package

%nodejs_fixdep d
# allow either the 0.1.x or 1.x.x series of npm(d)

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \#/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{__nodejs} -e 'require("./")'
%{__nodejs} %{nodejs_sitelib}/tad/bin/tad
%else
echo "Tests are disabled..."
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md CHANGES
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-4
- Rebuild for rhscl

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 22 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-2
- rebuilt to allow newer version of npm(d)

* Tue Nov 10 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
