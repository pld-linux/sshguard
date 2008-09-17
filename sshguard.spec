Summary:	sshguard - protect hosts from the plague of brute force attacks against SSH
Summary(pl.UTF-8):	sshguard - chroni hosty przed plagą ataków brute force na serwer SSH
Name:		sshguard
Version:	1.1
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/sshguard/%{name}-%{version}.tar.bz2
# Source0-md5:	673a22129487b8d8cb132fb0ced240e6
URL:		http://sshguard.sourceforge.net/
Patch0:		%{name}-iptables.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.337
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

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-iptables=/usr/sbin/iptables \
	--with-firewall=iptables
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README examples/whitelistfile.example
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/sshguard.8*
