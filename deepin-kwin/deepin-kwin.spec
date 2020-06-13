%global repo dde-kwin
#global _default_patch_fuzz 2
%global __provides_exclude_from ^%{_qt5_plugindir}.*\.so$

Name:           deepin-kwin
Version:        5.0.14.1
Release:        1%{?dist}
Summary:        KWin configuration for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Source1:        https://github.com/linuxdeepin/dde-kwin/pull/106.patch
Patch1:         https://github.com/linuxdeepin/dde-kwin/pull/109.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kwin-devel
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  gsettings-qt-devel
BuildRequires:  libepoxy-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dtkgui-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  qt5-linguist
# for libQt5EdidSupport.a
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-qt5integration%{?_isa}
Requires:       kwin%{?_isa} >= 5.17
# since F31
Obsoletes:      deepin-wm <= 1.9.38
Obsoletes:      deepin-wm-switcher <= 1.1.9
Obsoletes:      deepin-metacity <= 3.22.24
Obsoletes:      deepin-metacity-devel <= 3.22.24
Obsoletes:      deepin-mutter <= 3.20.38
Obsoletes:      deepin-mutter-devel <= 3.20.38

%description
This package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kwin-devel%{?_isa}
Requires:       qt5-qtx11extras-devel%{?_isa}
Requires:       gsettings-qt-devel%{?_isa}
Requires:       dtkcore-devel%{?_isa}
Requires:       kf5-kglobalaccel-devel%{?_isa}


%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
if [ $(rpm -q --qf '%%{version}' kwin-devel|cut -d. -f2) -ge 18 ]; then
  patch --fuzz=2 -p1 -i %{SOURCE1}
fi
%patch1 -p1
sed -i 's:/lib:/%{_lib}:' plugins/kwin-xcb/lib/CMakeLists.txt
sed -i 's:/usr/lib:%{_libdir}:' plugins/kwin-xcb/plugin/main.cpp
sed -i 's:/usr/lib:%{_libexecdir}:' deepin-wm-dbus/deepinwmfaker.cpp

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DKWIN_VERSION=$(rpm -q --qf '%%{version}' kwin-devel) .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
chmod 755 %{buildroot}%{_bindir}/kwin_no_scale

%ldconfig_scriptlets

%files
%doc CHANGELOG.md
%license LICENSE
%{_sysconfdir}/xdg/*
%{_bindir}/deepin-wm-dbus
%{_bindir}/kwin_no_scale
%{_libdir}/libkwin-xcb.so.*
%{_qt5_plugindir}/org.kde.kdecoration2/libdeepin-chameleon.so
%{_qt5_plugindir}/platforms/lib%{repo}-xcb.so
%{_qt5_plugindir}/kwin/effects/plugins/
%{_datadir}/dde-kwin-xcb/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kwin/scripts/*
%{_datadir}/kwin/tabbox/*

%files devel
%{_libdir}/libkwin-xcb.so
%{_libdir}/pkgconfig/%{repo}.pc
%{_includedir}/%{repo}

%changelog
* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.1.0-7
- rebuild (qt5)

* Thu Feb 27 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-6
- Fix path conflict with kdeplasma-addons (RHBZ#1807283)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.1.0-4
- Fix runtime issue with kwin 5.17

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 0.1.0-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 0.1.0-2
- rebuild (qt5)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 0.0.4-3
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 0.0.4-2
- rebuild (qt5)

* Mon Apr 22 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.4-1
- new version

* Mon Apr 15 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.3.2-1
- Update to 0.0.3.2

* Fri Apr 12 2019 Robin Lee <cheeselee@fedoraproject.org> - 0.0.3.1-1
- Initial packaging
