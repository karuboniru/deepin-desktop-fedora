Name:           deepin-reader
Version:        5.6.4
Release:        1%{?dist}
Summary:        A simple PDF reader from Deepin
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  kf5-karchive-devel
BuildRequires:  libspectre-devel
BuildRequires:  djvulibre-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  libuuid-devel
BuildRequires:  libtiff-devel

# BuildRequires:  deepin-gettext-tools
# BuildRequires:  pkgconfig(dframeworkdbus)
# Requires:       hicolor-icon-theme

%description
This package provides a simple PDF reader, supporting bookmarks, highlights and
annotations

%prep
%setup -q
# fedora not yet support DDE category
#sed -i -e 's/DDE;//' %{name}.desktop
sed -i '/include <QAbstractListModel>/a #include <QPointF>' application/pdfControl/imageviewmodel.h
sed -i '/include <QMetaType>/a #include <QRectF>' application/pdfControl/docview/commonstruct.h
sed -i '/target.path/s|lib|%{_lib}|' DBService/DBService.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
#license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%exclude %{_libdir}/libDBService.so
%{_libdir}/libDBService.so.1*

%changelog
