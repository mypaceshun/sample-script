Name:		sample-script
Version:	1.0
Release:	1%{?dist}
Summary:	sample script
License:	MIT

Source0:        sample.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  tree

%description
sample
script


%prep
rm -rf %{buildroot}
echo =====prep=====

%build
echo =====build=====

%install
echo =====install=====

%check
echo =====check=====

%clean
echo =====clean=====

%post
echo =====post=====

%pre
echo =====pre=====

%preun
echo =====preun=====

%postun
echo =====postun=====

%triggerin -- tree
echo =====triggerin=====

%triggerun -- tree
echo =====triggerun=====

%triggerpostun -- tree
echo =====triggerpostun=====

%verifyscript
echo =====verifyscript=====

%files
%doc

%changelog

