Name:           deepin-album
Version:        5.6.9.13
Release:        1%{?dist}
Summary:        A fashion photo manager from Deepin
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
BuildRequires:  freeimage-devel
BuildRequires:  udisks2-qt5-devel

# BuildRequires:  deepin-gettext-tools
# BuildRequires:  pkgconfig(dframeworkdbus)
# Requires:       hicolor-icon-theme

%description
This package provides a fashion photo manager for viewing and organizing
pictures.

%prep
%setup -q
# fedora not yet support DDE category
sed -i -e 's/DDE;//' %{name}.desktop

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

%changelog
