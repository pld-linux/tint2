Summary:	tint2 is a simple panel/taskbar intentionally made for openbox3
Summary(pl.UTF-8):	tint2 jest prostym panelem oryginalnie zaprojektowanym dla openbox3
Name:		tint2
Version:	17.0.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://gitlab.com/o9000/tint2/-/archive/v17.0.2/%{name}-v%{version}.tar.bz2
# Source0-md5:	60e5addfa33426229c00325a2e3af97b
URL:		https://gitlab.com/o9000/tint2/
BuildRequires:	cairo-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	imlib2-devel >= 1.4.2
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.12
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3
BuildRequires:	xorg-lib-libXrender-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires(post,postun):	desktop-file-utils
Suggests:	openbox
Obsoletes:	tint2-examples < 17.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tint2 is a simple panel/taskbar intentionally made for openbox3, but
should also work with other window managers. It's based on ttm code
http://code.google.com/p/ttm/

%description -l pl.UTF-8
tint2 jest prostym panelem/zasobnikiem oryginalnie zaprojektowanym dla
openbox3, ale powinien również współpracować z innymi menadżerami
okien. Jego kod oparty jest na ttm http://code.google.com/p/ttm/

%prep
%setup -q -n %{name}-v%{version}
mkdir build

%build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}

%find_lang tint2conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%update_mime_database

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%update_mime_database

%files -f tint2conf.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md doc/{tint2.md,images,manual.html,readme.html}
%attr(755,root,root) %{_bindir}/tint2
%attr(755,root,root) %{_bindir}/tint2conf
%dir %{_sysconfdir}/xdg/tint2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/tint2/tint2rc
%dir %{_datadir}/tint2
%{_datadir}/tint2/default_icon.png
%{_mandir}/man1/tint2.1.*
%{_desktopdir}/tint2conf.desktop
%{_desktopdir}/tint2.desktop
%{_iconsdir}/hicolor/scalable/apps/tint2.svg
%{_iconsdir}/hicolor/scalable/apps/tint2conf.svg
%{_datadir}/mime/packages/tint2conf.xml
%{_datadir}/tint2/*.tint2rc

