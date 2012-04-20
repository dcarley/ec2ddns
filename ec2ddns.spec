%{?_initddir:%define _initrddir %{_initrddir}}

Name:       ec2ddns
Version:    0.1
Release:    1%{?dist}
Summary:    EC2 dynamic DNS registration

Group:      System Tools
License:    ASL 2.0
URL:        https://github.com/dcarley/ec2ddns
Source0:    ec2ddns.py
Source1:    README.md
Source2:    LICENSE.md
BuildArch:  noarch
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:   python
Requires:   python-boto >= 2.0

%description
Python utility to register a CNAME record for an EC2 instance's public
hostname in route53 using python-boto.

%prep
%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install %{SOURCE0} %{buildroot}%{_sbindir}/ec2ddns.py

install %{SOURCE1} .
install %{SOURCE2} .

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%doc LICENSE.md
%attr(0755, root, root) %{_sbindir}/ec2ddns.py

%changelog
* Fri Apr 20 2012 Dan Carley <dan.carley@gmail.com> - 0.1-1
- Initial release.
