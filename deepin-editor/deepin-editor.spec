Name:           deepin-editor
Version:        5.6.7
Release:        1%{?dist}
Summary:        Simple editor for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  freeimage-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-notifications
Requires:       deepin-qt5integration

%description
%{summary}.

%prep
%setup -q

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake -DCMAKE_BUILD_TYPE=Release .
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/dedit
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2.9.1-5
- rebuild (qt5)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.9.1-3
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.9.1-2
- rebuild (qt5)

* Sun Aug 11 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.9.1-1
- Release 1.2.9.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.2.6.3-5
- rebuild (qt5)

* Mon Jun 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.6.3-4
- Rebuild (Qt5)

* Wed Mar 13 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.6.3-3
- Requires private Qt symbols

* Thu Feb 28 2019 Robin Lee <cheeselee@fedoraproject.org> - 1.2.6.3-2
- Fix translations

* Sat Feb  9 2019 mosquito <sensor.wen@gmail.com> - 1.2.6.3-1
- Update to 1.2.6.3

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 1.2.6.2-1
- Update to 1.2.6.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Jul 23 2018 mosquito <sensor.wen@gmail.com> - 0.0.5-1
- Initial package build
