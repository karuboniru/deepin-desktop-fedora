%global repo dde-control-center

Name:           deepin-control-center
Version:        5.2.0.3
Release:        1%{?dist}
Summary:        New control center for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Patch0:         deepin-control-center-build-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  deepin-dock-devel
BuildRequires:  udisks2-qt5-devel
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(geoip)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xext)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  qt5-linguist
Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-daemon
Requires:       deepin-qt5integration
Requires:       deepin-network-utils
Requires:       GeoIP-GeoLite-data
Requires:       GeoIP-GeoLite-data-extra
Requires:       gtk-murrine-engine
Requires:       proxychains-ng
Requires:       redshift
Requires:       startdde

%description
New control center for Linux Deepin.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
%patch0 -p1

sed -i 's|/bin/restore-tool|/usr/bin/restore-tool|' src/frame/window/modules/systeminfo/backupandrestoreworker.cpp \
                                                      com.deepin.controlcenter.restore.policy
sed -i 's| /bin| /usr/bin|' src/restore-tool/CMakeLists.txt

# remove after they obey -DDISABLE_SYS_UPDATE properly
sed -i '/new UpdateModule/d' src/frame/window/mainwindow.cpp

sed -i '/%{repo}/s|\.\./lib|%{_libdir}|' src/frame/pluginscontroller.cpp

sed -i '/TARGETS/s|lib|%{_lib}|' src/frame/CMakeLists.txt

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake . -DDCC_DISABLE_GRUB=YES \
         -DDISABLE_SYS_UPDATE=YES \
         -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
# place holder plugins dir
mkdir -p %{buildroot}%{_libdir}/%{repo}/plugins

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop ||:

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/autostart/deepin-ab-recovery.desktop
%{_bindir}/%{repo}
%{_bindir}/abrecovery
%{_bindir}/restore-tool
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{repo}/
%{_libdir}/%{repo}/
%{_datadir}/polkit-1/actions/com.deepin.*.policy
%{_libdir}/libdccwidgets.so

%files devel
%{_libdir}/cmake/DdeControlCenter/
%{_includedir}/%{repo}/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec  1 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-2
- BR pkgconfig(xext)

* Mon Aug 05 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Robin Lee <cheeselee@fedoraproject.org> - 4.9.4-1
- Update to 4.9.4

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 4.9.2.1-1
- Update to 4.9.2.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 4.8.6-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Sun Dec 23 2018 mosquito <sensor.wen@gmail.com> - 4.8.6-1
- Update to 4.8.6

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 4.8.2-1
- Update to 4.8.2

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 4.7.7-1
- Update to 4.7.7

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 4.7.6.1-1
- Update to 4.7.6.1

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 4.7.4-1
- Update to 4.7.4

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 4.6.4-1
- Update to 4.6.4

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 4.6.3-1
- Update to 4.6.3

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 4.6.1-1
- Update to 4.6.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 mosquito <sensor.wen@gmail.com> - 4.3.7-3
- Exclude ppc64le, ppc64 and aarch64

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec  2 2017 mosquito <sensor.wen@gmail.com> - 4.3.7-1
- Update to 4.3.7

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Thu Sep 21 2017 mosquito <sensor.wen@gmail.com> - 4.2.5.10-1
- Update to 4.2.5.10

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.5.4-1
- Update to 4.2.5.4

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 4.2.5-1
- Update to 4.2.5

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 4.2.4-1.git21d68b6
- Update to 4.2.4

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 4.2.3-1.git2f420f2
- Update to 4.2.3

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.1.2-1.git4d3827b
- Update to 4.1.2

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.0.7-1.git10c3be2
- Update to 4.0.7

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 3.0.24-1.git481255b
- Downgrade to 3.0.24 for end user

* Sat Jan 21 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-2.git8b1a736
- Fix can not start

* Thu Jan 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.2-1.git8b1a736
- Update to 4.0.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.1-1.gitd1c1c9a
- Update to 4.0.1

* Tue Dec 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Bump to newer release because of copr signature

* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to 3.0.24

* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build
