%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory

Name:           deepin-qt-dbus-factory
Version:        5.2.0.3
Release:        1%{?dist}
Summary:        A repository stores auto-generated Qt5 dbus code
# The entire source code is GPLv3+ except
# libdframeworkdbus/qtdbusextended/ which is LGPLv2+
License:        GPLv3+ and LGPLv2+
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  python3
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
A repository stores auto-generated Qt5 dbus code.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|python|python3|' libdframeworkdbus/*.{pro,py}

%build
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%doc README.md CHANGELOG.md technology-overview.md
%license LICENSE
%{_libdir}/lib%{soname}.so.*

%files devel
%{_includedir}/lib%{soname}-2.0/
%{_libdir}/cmake/DFrameworkdbus/
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/lib%{soname}.so

%changelog
* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 5.0.1-2
- rebuild (qt5)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-4
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 1.1.0-3
- rebuild (qt5)

* Thu May 16 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.1.0-2
- Requires Qt private headers

* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Feb 25 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.0.6-2
- use %%ldconfig_scriptlets
- drop explicit Requires: cmake-filesystem (handled automatically now)
- -devel: own %%{_libdir}/cmake/DFrameworkdbus

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Wed Jul 25 2018 Zamir SUN <zsun@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Sat Aug  5 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1
- Fix license

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 0.2.1-1.gitbecf852
- Update to 0.2.1

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 0.2.0-1.git98d9901
- Update to 0.2.0

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 0.1.0-1.git9adc304
- Update to 0.1.0

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 0.0.4-1.gitefa4f7f
- Update to 0.0.4

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 0.0.3-1.gitffda1af
- Initial build
