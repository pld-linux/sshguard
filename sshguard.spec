Summary:	sshguard - protect hosts from the plague of brute force attacks against SSH
Summary(pl.UTF-8):	sshguard - chroni hosty przed plagą ataków brute force na serwer SSH
Name:		sshguard
Version:	0.9
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/sshguard/%{name}-%{version}.tar.bz2
# Source0-md5:	990f53b0213f8cc04cc8ea5882f086a1
Patch0:		%{name}-includes.patch
Patch1:		%{name}-path.patch
URL:		http://sshguard.sourceforge.net/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.337
BuildRequires:	scons
BuildRequires:	sed >= 4.0
Requires:	iptables
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sshguard protects hosts from the plague of brute force attacks against
SSH. Unlike many similar tools written in interpreted languages, it's
independent, fast, and lightweight because it's completely written in
C.

%description -l pl.UTF-8
sshguard chroni hosty przed plagą ataków brute force na serwer SSH.
W przeciwieństwie do wielu podobnych narzędzi napisanych
w interpretowanych językach jest niezależny, szybki i lekki, ponieważ
jest napisany w C.

%define		_fw	-Q FIREWALLTYPE=iptables

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%{__sed} -i -e "s@/usr/local@$RPM_BUILD_ROOT%{_prefix}@g" SConstruct

%build
%scons \
	%{_fw}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
%scons install \
	%{_fw}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
