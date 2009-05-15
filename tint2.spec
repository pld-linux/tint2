%define		_beta	0.7-beta1
Summary:	tint2 is a simple panel/taskbar intentionally made for openbox3
Summary(pl.UTF-8):	tint2 jest prostym panelem oryginalnie zaprojektowanym dla openbox3
Name:		tint2
Version:	0.7.beta1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://tint2.googlecode.com/files/%{name}-%{_beta}.tar.gz
# Source0-md5:	93b70b4603235b307d3707b2e51d23d9
URL:		http://code.google.com/p/tint2/
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	imlib2-devel
BuildRequires:	libpng-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXinerama-devel
Suggests:	openbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tint2 is a simple panel/taskbar intentionally made for openbox3, but
should also work with other window managers. It's based on ttm code
http://code.google.com/p/ttm/

%description -l pl.UTF-8
tint2 jest prostym panelem/zasobnikiem oryginalnie zaprojektowanym dla
openbox3 ale powinien również współpracować z innymi menadżerami
okien. Jego kod oparty jest na ttm http://code.google.com/p/ttm/

%prep
%setup -q -n %{name}-%{_beta}
rm src/tint2

%build
cd src
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/tint2-0.7.pdf
%attr(755,root,root) %{_bindir}/tint2
%dir %{_sysconfdir}/xdg/tint2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/tint2/tint2rc
%{_mandir}/man1/tint2.1.*
