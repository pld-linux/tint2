#
# Conditional build:
%bcond_without  tintwizard	# build without tintwizard
#
Summary:	tint2 is a simple panel/taskbar intentionally made for openbox3
Summary(pl.UTF-8):	tint2 jest prostym panelem oryginalnie zaprojektowanym dla openbox3
Name:		tint2
Version:	0.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://tint2.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	866bc529cb7d0884e976f8fc9aef0eea
Source1:	http://tint2.googlecode.com/files/%{name}-0.7.pdf
# Source1-md5:	25980bd22fabc6a66660173fa639957b
Patch0:		%{name}-tintwizard_conf.patch
URL:		http://code.google.com/p/tint2/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	imlib2-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXinerama-devel
%if %{with tintwizard}
Requires:	python
Requires:	python-pygtk-gtk
%endif
Suggests:	openbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tint2 is a simple panel/taskbar intentionally made for openbox3, but
should also work with other window managers. It's based on ttm code
http://code.google.com/p/ttm/

%description -l pl.UTF-8
tint2 jest prostym panelem/zasobnikiem oryginalnie zaprojektowanym dla
openbox3, ale powinien również współpracować z innymi menadżerami
okien. Jego kod oparty jest na ttm http://code.google.com/p/ttm/

%package examples
Summary:        tint2 - example configurations
Summary(pl.UTF-8):      tint2 - przykładowe konfiguracje
Group:          Documentation
Requires:       %{name} = %{version}-%{release}

%description examples
tint2 - example configurations.

%description examples -l pl.UTF-8
tint2 - przykładowe konfiguracje.

%prep
%setup -q 
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{?with_tintwizard:install -d $RPM_BUILD_ROOT%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_tintwizard:cp src/tint2conf/tintwizard.py $RPM_BUILD_ROOT%{_bindir}}
cp %{SOURCE1} doc
install sample/*.tint2rc $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/tint2-0.7.pdf
%attr(755,root,root) %{_bindir}/tint2
%{?with_tintwizard:%attr(755,root,root) %{_bindir}/tintwizard.py}
%dir %{_sysconfdir}/xdg/tint2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/tint2/tint2rc
%{_mandir}/man1/tint2.1.*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
