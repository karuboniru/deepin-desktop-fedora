%global repo qt5integration

Name:           deepin-qt5integration
Version:        5.1.0
Release:        1%{?dist}
Summary:        Qt platform theme integration plugins for DDE
# The entire source code is GPLv3+ except styles/ which is BSD,
# dstyleplugin/ which is GPLv3, dstyleplugin/dstyleanimation* which is LGPL
License:        GPLv3 and BSD and LGPLv2+
URL:            https://github.com/linuxdeepin/qt5integration
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# https://git.archlinux.org/svntogit/community.git/plain/trunk/deepin-qt5integration-qt5.14.patch?h=packages/deepin-qt5integration&id=b9bad53f20d27a15f9587f39db3e1a0243ec6880
Patch1:         deepin-qt5integration-qt5.14.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.0.0
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  qt5-qtbase-common
# for libQt5ThemeSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-qt5dxcb-plugin%{?_isa}

%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep
%setup -q -n %{repo}-%{version}

%patch1 -p1 -b .fix-build-with-qt5-14

sed -i 's/^.*DPlatformWindowHandle.*$/Dtk::Widget::DPlatformWindowHandle handle((QWidget *)w);/' styleplugins/dstyleplugin/config.tests/dtkwidget/main.cpp
sed -i 's/QSpinBox/DSpinBox/' styleplugins/chameleon/chameleonstyle.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_qt5_plugindir}/platformthemes/libqdeepin.so
%{_qt5_plugindir}/styles/libdstyleplugin.so
%{_qt5_plugindir}/iconengines/libdsvgicon.so
%{_qt5_plugindir}/imageformats/libdsvg.so
%{_qt5_plugindir}/iconengines/libdtkbuiltin.so
%{_qt5_plugindir}/styles/libchameleon.so

%changelog
* Tue Apr  7 2020 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-5
- Fix build with Qt 5.14.2

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.0-2
- rebuild (qt5)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.3.10-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 0.3.10-2
- rebuild (qt5)

* Mon Apr 08 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.3.10-1
- new version
- Split qt5dxcb-plugin

* Sat Mar  9 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.3.7.2-2
- Update qt5dxcb-plugin for qt5.12

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 0.3.7.2-1
- Update to 0.3.7.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.7.1-2
- rebuild (Qt5)

* Thu Dec 13 2018 mosquito <sensor.wen@gmail.com> - 0.3.7.1-1
- Update to 0.3.7.1

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.3.6-3
- rebuild (qt5)

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 0.3.6-2
- Update qt5dxcb to 1.1.14

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 0.3.6-1
- Update to 0.3.6
- Use of the gold linker by QMAKE_LFLAGS+="-fuse-ld=gold"
  https://bugreports.qt.io/browse/QTBUG-65071

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 0.3.4-2
- rebuild (qt5)

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 0.3.4-1
- Update to 0.3.4

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 0.3.1-1
- Update to 0.3.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-6
- rebuild (qt5)

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-5
- rebuild (qt5)

* Sun Feb 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-4
- rebuild (qt5)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8.3-2
- rebuild (qt5)

* Sat Dec  9 2017 mosquito <sensor.wen@gmail.com> - 0.2.8.3-1
- Update to 0.2.8.3

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2.3-3
- rebuild (qt5)

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 0.2.8.1-1
- Update to 0.2.8.1

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 0.2.7-1
- Update to 0.2.7

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 0.2.4-1
- Update to 0.2.4
- Included qt5xcbqpa private header files in the project

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.2.3-2
- BR: qt5-qtbase-private-devel

* Tue Aug 22 2017 mosquito <sensor.wen@gmail.com> - 0.2.3-1
- Update to 0.2.3

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1.git2cd7432
- Update to 0.2.1

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 0.1.8-1.gitb03be20
- Update to 0.1.8

* Tue Mar  7 2017 mosquito <sensor.wen@gmail.com> - 0.1.2-1.gitecde076
- Update to 0.1.2

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.1.1-1.gitaa563fd
- Update to 0.1.1

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 0.0.6-1.git40401af
- Update to 0.0.6

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.0.5-1.gitc0dc3cf
- Initial build
