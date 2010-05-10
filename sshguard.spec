%define		_rc	rc3
Summary:	sshguard - protect hosts from the plague of brute force attacks against SSH
Summary(pl.UTF-8):	sshguard - chroni hosty przed plagą ataków brute force na serwer SSH
Name:		sshguard
Version:	1.5
Release:	0.%{_rc}.1
License:	BSD
Group:		Applications
Source0:	http://downloads.sourceforge.net/sshguard/%{name}-%{version}%{_rc}.tar.bz2
# Source0-md5:	388315aa687168f838ae3d5c9a486b00
URL:		http://sshguard.sourceforge.net/
Patch0:		%{name}-iptables.patch
Patch1:		%{name}-getopt.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	iptables
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sshguard protects hosts from the plague of brute force attacks against
SSH. Unlike many similar tools written in interpreted languages, it's
independent, fast, and lightweight because it's completely written in
C.

%description -l pl.UTF-8
sshguard chroni hosty przed plagą ataków brute force na serwer SSH. W
przeciwieństwie do wielu podobnych narzędzi napisanych w
interpretowanych językach, jest niezależny, szybki i lekki, ponieważ
jest napisany w C.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p1
%patch1 -p1

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

%post
iptables -N sshguard

%postun
iptables -X sshguard

%files
%defattr(644,root,root,755)
%doc README examples/whitelistfile.example
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/sshguard.8*
