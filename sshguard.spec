Summary:	sshguard - protect hosts from the plague of brute force attacks agains ssh
Summary(pl):	sshguard - chroni hosty przed plag± ataków brute force na serwer ssh
Name:		sshguard
Version:	0.9
Release:	2
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/sshguard/%{name}-%{version}.tar.bz2
# Source0-md5:	990f53b0213f8cc04cc8ea5882f086a1
Patch0:		%{name}-includes.patch
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
ssh. Unlike many similar tools written in interpreted languages, it's
independent, fast, and lightweight because it's completely written in
C.

%description -l pl
sshguard chroni hosty przed plag± ataków brute force na serwer ssh. W
przeciwieñstwie do wielu podobnych narzêdzi napisanych w
interpretowanych jêzykach jest niezale¿ny, szybki i lekki, poniewa¿
jest napisany w C.

%define		_fw	-Q FIREWALLTYPE=iptables

%prep
%setup -q
%patch0 -p0
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
