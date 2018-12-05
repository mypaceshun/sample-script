Name:		sample-script
Version:	1.0
Release:	1%{?dist}
Summary:	sample script
License:	MIT

Source0:        sample-script-1.0.tar.gz

Patch0:         addmessage.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  tree

%description
sample
script


%prep
echo =====prep=====
rm -rf %{buildroot}
%setup
%patch0 -p1
exit 1

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

