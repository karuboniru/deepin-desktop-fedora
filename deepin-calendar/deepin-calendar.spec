%global repo dde-calendar

Name:           deepin-calendar
Version:        5.7.0.3
Release:        1%{?dist}
Summary:        Calendar for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dde-calendar
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
Requires:       hicolor-icon-theme

%description
Calendar for Deepin Desktop Environment.

%prep
%setup -q -n %{repo}-%{version}
# sed -i '/QMenuBar/a #include <QMouseEvent>/' src/yearwindow.cpp
# sed -i '/<QQueue>/a #include <QMouseEvent>/' src/daymonthview.cpp
# sed -i '/<QStylePainter>/a #include <QMouseEvent>/' src/schcedulesearchview.cpp

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
%make_build
popd

%install
pushd %{_target_platform}
%make_install INSTALL_ROOT=%{buildroot}
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{repo}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{repo}
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/com.deepin.Calendar.service
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{repo}.svg

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.1-1
- Release 5.0.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 1.2.6-1
- Update to 1.2.6

* Fri Aug 10 2018 mosquito <sensor.wen@gmail.com> - 1.2.5-1
- Update to 1.2.5

* Thu Aug  2 2018 mosquito <sensor.wen@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Fri Jul 20 2018 mosquito <sensor.wen@gmail.com> - 1.2.3-1
- Update to 1.2.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 mosquito <sensor.wen@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Oct 23 2017 mosquito <sensor.wen@gmail.com> - 1.0.13-1
- Update to 1.0.13

* Sun Aug 20 2017 mosquito <sensor.wen@gmail.com> - 1.0.12-1
- Update to 1.0.12

* Sun Aug 06 2017 Zamir SUN <sztsian@gmail.com> - 1.0.11-2
- Add check for desktop file

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 1.0.11-1.gitd2c7b9e
- Update to 1.0.11

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 1.0.7-1.gita8a4f5b
- Update to 1.0.7

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 1.0.4-1.gitb59053f
- Update to 1.0.4

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 1.0.3-1.gitd7e42a1
- Update to 1.0.3

* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.3-1
- Update to version 1.0.3

* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-2
- Rebuild with newer deepin-tool-kit

* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-1
- Initial package build
