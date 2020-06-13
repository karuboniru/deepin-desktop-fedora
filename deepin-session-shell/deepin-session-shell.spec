%global repo dde-session-shell

Name:           deepin-session-shell
Version:        5.0.0098.0
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Session Shell module
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  deepin-gettext-tools
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(liblightdm-qt5-3)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pam-devel
BuildRequires:  qt5-linguist
Requires:       deepin-control-center
Requires:       deepin-daemon
Requires:       startdde
Requires:       lightdm
Provides:       lightdm-deepin-greeter%{?_isa} = %{version}-%{release}
Provides:       lightdm-greeter = 1.2
Provides:       deepin-notifications = %{version}-%{release}
Provides:       deepin-notifications%{?_isa} = %{version}-%{release}
Obsoletes:      deepin-notification         <= 3.3.4

%description
This project include the session shell module for Deepin desktop environment.

%prep
%setup -q -n %{repo}-%{version}
sed -i '/darrowrectangle/d' CMakeLists.txt src/widgets/widgets.pri
sed -i 's/include "darrowrectangle.h"/include <darrowrectangle.h>/' src/widgets/errortooltip.h
sed -i 's|/usr/lib|%{_libexecdir}|' scripts/lightdm-deepin-greeter

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
chmod 755 %{buildroot}%{_bindir}/deepin-greeter

%files
%config(noreplace) %{_sysconfdir}/deepin/
%{_bindir}/dde-*
%{_bindir}/deepin-greeter
%{_bindir}/lightdm-deepin-greeter
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/xgreeters/lightdm-deepin-greeter.desktop

%changelog
