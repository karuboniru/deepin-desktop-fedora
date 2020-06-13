Name:           dtkgui
Version:        5.2.0
Release:        1%{?dist}
Summary:        GUI module for DDE look and feel
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkgui
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)

BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Dtkgui is the GUI module for DDE look and feel.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|systembusconf.path = /etc/dbus-1/system.d|systembusconf.path = %{_datadir}/dbus-1/system.d|' src/src.pro

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir} \
           BIN_INSTALL_DIR=%{_libexecdir}/dtk2 \
           TOOL_INSTALL_DIR=%{_libexecdir}/dtk2
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_datadir}/dbus-1/system.d/*.conf
%{_libexecdir}/dtk2/deepin-gui-settings
%{_libexecdir}/dtk2/taskbar

%files devel
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/DtkGui/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
* Mon May  4 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.2.0-1
- Initial package build
