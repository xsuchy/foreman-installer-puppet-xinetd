%global foreman_root %{_datarootdir}/foreman-installer
%global foreman_hash .09540eb

Name:		foreman-installer-puppet-xinetd
Version:	0
Release:	1%{foreman_hash}%{?dist}
Summary:	Apache class for xinetd

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/theforeman/puppet-xinetd
# http://github.com/theforeman/puppet-xinetd/tarball/master
Source0:	%{name}-%{version}.tar.gz
BuildArch:  noarch

%description
Xinetd class for Puppet for Foreman installer.

%prep
%setup -q

%build
#nothing to do

%install
mkdir -p %{buildroot}/%{foreman_root}/xinetd
cp -a manifests %{buildroot}/%{foreman_root}/xinetd/

%files
%{foreman_root}

%changelog
* Tue Nov 20 2012 Miroslav Suchý <msuchy@redhat.com> 0-1.09540eb
- new package built with tito

