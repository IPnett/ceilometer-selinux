%define _prefix   /

Name:		ceilometer-selinux
Version:	1.0.0
Release:	1%{?dist}
Summary:	SELinux Policy for ceilometer

Group:		System Environment/Base
BuildArch:	noarch
License:	GPLv2
Requires:		policycoreutils, libselinux-utils
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):	policycoreutils
BuildRequires:		selinux-policy selinux-policy-devel
Source0: 		./ceilometer.pp


%description
SELinux Policy module for use with ceilometer


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/ceilometer/ceilometer.pp


%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/ceilometer/
%attr(0600, root, root) /usr/share/selinux/packages/ceilometer/ceilometer.pp

%post
	/usr/sbin/semodule -i /usr/share/selinux/packages/ceilometer/ceilometer.pp
	restorecon -R /usr/lib/systemd/system/openstack-ceilometer*
	restorecon -R /var/lib/ceilometer
	restorecon -R /var/log/ceilometer
	restorecon -R /var/run/ceilometer
	restorecon -R /usr/bin/ceilometer*

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/semodule -r ceilometer
	restorecon -R /usr/lib/systemd/system/openstack-ceilometer*
	restorecon -R /var/lib/ceilometer
	restorecon -R /var/log/ceilometer
	restorecon -R /var/run/ceilometer
	restorecon -R /usr/bin/ceilometer*
fi


%changelog
