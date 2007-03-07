Summary:	sshguard - protect hosts from the plague of brute force attacks agains ssh
Summary(pl.UTF-8):	sshguard - chroni hosty przed plagą ataków brute force na serwer ssh
Name:		sshguard
Version:	0.9
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/sshguard/%{name}-%{version}.tar.bz2
# Source0-md5:	990f53b0213f8cc04cc8ea5882f086a1
URL:		http://sshguard.sourceforge.net/
BuildRequires:	python
BuildRequires:	scons
Requires:	iptables
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sshguard protects hosts from the plague of brute force attacks against
ssh. Unlike many similar tools written in interpreted languages, it's
independent, fast, and lightweight because it's completely written in
C.

%description -l pl.UTF-8
sshguard chroni hosty przed plagą atakow brute force na serwer ssh. W
przeciwieństwie do wielu podobnych narzędzi jest on napisany w
interpretowanym języku, jest niezależny, szybki i lekki, ponieważ jest
napisany w C.

%prep
%setup -q

%build
python scons.py -Q FIREWALLTYPE=iptables

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
cp sshguard $RPM_BUILD_ROOT%{_sbindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
