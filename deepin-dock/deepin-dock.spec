%global repo dde-dock
%global start_logo start-here
%global __provides_exclude_from ^%{_libdir}/%{repo}/.*\\.so$

Name:           deepin-dock
Version:        5.1.0.6
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Dock module
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbusmenu-qt5)
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  qt5-linguist
BuildRequires:  fedora-logos
Requires:       deepin-daemon
Recommends:     deepin-launcher
Requires:       deepin-menu
Requires:       deepin-qt5integration
Requires:       onboard
Requires:       deepin-icon-theme >= 2020.04.13

%description
Deepin desktop-environment - Dock module.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
sed -i '/TARGETS/s|lib|%{_lib}|' plugins/*/CMakeLists.txt
sed -i 's|/lib|/%{_lib}|' frame/controller/dockpluginscontroller.cpp \
    plugins/tray/system-trays/systemtrayscontroller.cpp
sed -i 's|/lib|/libexec|' plugins/show-desktop/showdesktopplugin.cpp \
    frame/panel/mainpanelcontrol.cpp
sed -i 's:libdir.*:libdir=%{_libdir}:' dde-dock.pc
# set icon to Fedora logo
sed -i 's|deepin-launcher|%{start_logo}|' frame/item/launcheritem.cpp

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DARCHITECTURE=%{_arch} -DDOCK_TRAY_USE_NATIVE_POPUP=YES .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%license LICENSE
%{_sysconfdir}/%{repo}/
%{_bindir}/%{repo}
%{_libdir}/%{repo}/
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/glib-2.0/schemas/*

%files devel
%doc plugins/plugin-guide
%{_includedir}/%{repo}/
%{_libdir}/pkgconfig/%{repo}.pc
%{_libdir}/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug  5 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.0-3
- Filter private library provides

* Thu Mar  7 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.0-2
- Change launcher icon to Fedora logo, Requires deepin-icon-theme and fedora-logos
- Requires onboard, required by a plugin
- Own %%{_sysconfdir}/%%{repo}/

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.8.9-1
- Update to 4.8.9

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.8.4.1-1
- Update to 4.8.4.1

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.4-1
- Update to 4.8.4

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 4.8.1-1
- Update to 4.8.1

* Mon Nov 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.0-1
- Update to 4.8.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 4.7.2-1
- Update to 4.7.2

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 4.7.1.1-1
- Update to 4.7.1.1

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 4.6.9-1
- Update to 4.6.9

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.6.7-1
- Update to 4.6.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 4.5.12-1
- Update to 4.5.12

* Sat Feb 10 2018 mosquito <sensor.wen@gmail.com> - 4.5.9.1-1
- Update to 4.5.9.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 mosquito <sensor.wen@gmail.com> - 4.5.9-1
- Update to 4.5.9

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 4.5.7.1-1
- Update to 4.5.7.1

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 4.5.7-1
- Update to 4.5.7

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 4.5.1-1
- Update to 4.5.1

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.4.1-1
- Update to 4.4.1

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 4.3.4-1
- Update to 4.3.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.3.3-1.gitbf79f1c
- Update to 4.3.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.2.1-1.git42610ae
- Update to 4.2.1

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 4.1.4-1.gitd772fe2
- Update to 4.1.4

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.1.3-1.git26f189d
- Update to 4.1.3

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.8-1.gita882590
- Update to 4.0.8

* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock

* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6

* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit

* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build
