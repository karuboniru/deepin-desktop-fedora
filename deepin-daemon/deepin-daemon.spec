# https://github.com/linuxdeepin/dde-daemon/issues/63
%global _smp_mflags -j1
%global repo dde-daemon

Name:           deepin-daemon
Version:        5.9.4.2
Release:        1%{?dist}
Summary:        Daemon handling the DDE session settings
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-daemon
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
# upstream default mono font set to 'Noto Mono', which is not yet available in
# Fedora. We change to 'Noto Sans Mono'
Source1:        fontconfig.json
Source2:        %{name}.sysusers
Source3:        deepin-auth
# https://git.archlinux.org/svntogit/community.git/plain/trunk/dde-daemon_5.9.4.2.diff?h=packages/deepin-daemon
Patch0:         dde-daemon_5.9.4.2.diff

ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  deepin-gettext-tools
BuildRequires:  deepin-gir-generator
BuildRequires:  fontpackages-devel
BuildRequires:  librsvg2-tools
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  golang(pkg.deepin.io/lib) >= 1.2.11
BuildRequires:  golang(pkg.deepin.io/lib/fsnotify)
BuildRequires:  golang(pkg.deepin.io/dde/api/dxinput) >= 3.1.26
BuildRequires:  golang(github.com/linuxdeepin/go-dbus-factory/org.bluez)
BuildRequires:  golang(github.com/linuxdeepin/go-x11-client)
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgbutil)
BuildRequires:  golang(github.com/axgle/mahonia)
BuildRequires:  golang(github.com/msteinert/pam)
BuildRequires:  golang(github.com/nfnt/resize)
BuildRequires:  golang(github.com/cryptix/wav)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(github.com/gosexy/gettext)
BuildRequires:  golang(github.com/jinzhu/gorm)
BuildRequires:  golang(github.com/jinzhu/gorm/dialects/sqlite)
BuildRequires:  golang(github.com/kelvins/sunrisesunset)
BuildRequires:  golang(github.com/rickb777/date)
BuildRequires:  golang(github.com/teambition/rrule-go)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)

Requires:       bamf-daemon
Requires:       bluez-libs
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       deepin-polkit-agent
%ifnarch s390 s390x %{arm} %{power64}
Obsoletes:      deepin-grub2-themes <= 1.0.0
Requires:       acpid
Requires:       rfkill
%endif
Requires:       gvfs
Requires:       iw
Requires:       libudisks2
Requires:       qt5-qtaccountsservice
Requires:       upower
Requires:       xdotool
Recommends:     NetworkManager-vpnc-gnome
Recommends:     NetworkManager-pptp-gnome
Recommends:     NetworkManager-l2tp-gnome
Recommends:     NetworkManager-strongswan-gnome
Recommends:     NetworkManager-openvpn-gnome
Recommends:     NetworkManager-openconnect-gnome
Recommends:     iso-codes
Recommends:     imwheel
Recommends:     mobile-broadband-provider-info
Recommends:     google-noto-sans-mono-fonts
Recommends:     google-noto-sans-fonts

%description
Daemon handling the DDE session settings

%prep
%setup -q -n %{repo}-%{version}
%patch0 -p1 -b dde-daemon-3.8.0
install -m 644 %{SOURCE3} misc/etc/pam.d/deepin-auth

# Fix library exec path
sed -i '/deepin/s|lib|libexec|' Makefile
sed -i '/systemd/s|lib|usr/lib|' Makefile
sed -i 's:/lib/udev/rules.d:%{_udevrulesdir}:' Makefile
sed -i 's|lib/NetworkManager|libexec|' network/utils_test.go
sed -i 's|/usr/lib|%{_libexecdir}|' \
    misc/*services/*.service \
    misc/systemd/services/*.service \
    misc/pam-configs/deepin-auth \
    misc/applications/deepin-toggle-desktop.desktop \
    misc/dde-daemon/gesture.json \
    misc/dde-daemon/keybinding/system_actions.json \
    keybinding/shortcuts/system_shortcut.go \
    session/power/constant.go \
    session/power/lid_switch.go \
    service_trigger/manager.go \
    bin/dde-system-daemon/main.go \
    bin/search/main.go \
    accounts/image_blur.go \
    network/secret_agent.go \
    grub2/modify_manger.go

# Fix grub.cfg path
sed -i 's|boot/grub|boot/grub2|' grub2/{grub2,grub_params,theme}.go

# Fix activate services failed (Permission denied)
# dbus service
pushd misc/system-services/
sed -i '$aSystemdService=deepin-accounts-daemon.service' com.deepin.system.Power.service \
    com.deepin.daemon.{Accounts,Apps,Daemon}.service \
    com.deepin.daemon.{Gesture,SwapSchedHelper,Timedated}.service
sed -i '$aSystemdService=dbus-com.deepin.dde.lockservice.service' com.deepin.dde.LockService.service
popd
# systemd service
cat > misc/systemd/services/dbus-com.deepin.dde.lockservice.service <<EOF
[Unit]
Description=Deepin Lock Service
Wants=user.slice dbus.socket
After=user.slice dbus.socket

[Service]
Type=dbus
BusName=com.deepin.dde.LockService
ExecStart=%{_libexecdir}/%{name}/dde-lockservice

[Install]
WantedBy=graphical.target
EOF

# Replace reference of google-chrome to chromium-browser
sed -i 's/google-chrome/chromium-browser/g' misc/dde-daemon/mime/data.json

%build
export GOPATH="$(pwd)/build:%{gopath}"
BUILDID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
%make_build GOBUILD="go build -compiler gc -ldflags \"-B $BUILDID\""

%install
export GOPATH="$(pwd)/build:%{gopath}"
BUILDID="0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')"
%make_install PAM_MODULE_DIR=%{_libdir}/security GOBUILD="go build -compiler gc -ldflags \"-B $BUILDID\""

install -Dm644 %{S:2} %{buildroot}/usr/lib/sysusers.d/%{name}.conf

# fix systemd/logind config
install -d %{buildroot}/usr/lib/systemd/logind.conf.d/
cat > %{buildroot}/usr/lib/systemd/logind.conf.d/10-%{name}.conf <<EOF
[Login]
HandlePowerKey=ignore
HandleSuspendKey=ignore
EOF

# install default settings
install -Dm644 %{SOURCE1} \
    %{buildroot}%{_datadir}/deepin-default-settings/fontconfig.json

%find_lang %{repo}

%post
if [ $1 -ge 1 ]; then
  systemd-sysusers %{name}.conf
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_libexecdir}/%{name}/default-terminal 30
fi

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator \
    %{_libexecdir}/%{name}/default-terminal
fi

%postun
if [ $1 -eq 0 ]; then
  rm -f /var/cache/deepin/mark-setup-network-services
  rm -f /var/log/deepin.log 
fi

%files -f %{repo}.lang
%doc README.md
%license LICENSE
%{_sysconfdir}/acpi/actions/deepin_lid.sh
%{_sysconfdir}/acpi/events/deepin_lid
%exclude %{_sysconfdir}/default/grub.d/10_deepin.cfg
%exclude %{_sysconfdir}/grub.d/35_deepin_gfxmode
%{_sysconfdir}/pulse/daemon.conf.d/
%{_sysconfdir}/pam.d/deepin-auth
%{_sysconfdir}/pam.d/deepin-auth-keyboard
%{_libdir}/security/pam_deepin_auth.so
# Debian specific, useless on Fedora
%exclude %{_datadir}/pam-configs
%{_libexecdir}/%{name}/
%exclude %{_libexecdir}/%{name}/grub2
%{_sysusersdir}/%{name}.conf
%{_prefix}/lib/systemd/logind.conf.d/10-%{name}.conf
%{_unitdir}/deepin-accounts-daemon.service
%{_unitdir}/dbus-com.deepin.dde.lockservice.service
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%exclude %{_datadir}/dbus-1/system-services/com.deepin.daemon.Grub2.service
%{_datadir}/dbus-1/system.d/*.conf
%exclude %{_datadir}/dbus-1/system.d/com.deepin.daemon.Grub2.conf
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/%{repo}/
%{_datadir}/dde/
%{_datadir}/polkit-1/actions/*.policy
%exclude %{_datadir}/polkit-1/actions/com.deepin.daemon.Grub2.policy
%{_datadir}/deepin-default-settings/
%{_var}/cache/appearance/
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Accounts.pkla
%{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Fprintd.pkla
%exclude %{_var}/lib/polkit-1/localauthority/10-vendor.d/com.deepin.daemon.Grub2.pkla
%{_udevrulesdir}/80-deepin-fprintd.rules

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Robin Lee <cheeselee@fedoraproject.org> - 5.0.0-1
- Release 5.0.0
- Disable grub-related functions

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.23.0-2
- Replace reference of google-chrome to chromium-browser

* Tue Feb 26 2019 Robin Lee <cheeselee@fedoraproject.org> - 3.23.0-1
- Update to 3.23.0
- default-settings update to 2019.1.30
- Disable parallel building by now

* Thu Jan 31 2019 mosquito <sensor.wen@gmail.com> - 3.22.0-1
- Update to 3.22.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.14.0-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Dec 12 2018 mosquito <sensor.wen@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Thu Nov 29 2018 mosquito <sensor.wen@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.7.0-3
- acpid is unavailable in ppc64le

* Wed Nov 21 2018 mosquito <sensor.wen@gmail.com> - 3.7.0-2
- Build test for ppc64le and aarch64

* Fri Nov  9 2018 mosquito <sensor.wen@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 3.2.20-1
- Update to 3.2.20

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 mosquito <sensor.wen@gmail.com> - 3.2.9-2
- Nothing providers grub2 in s390x and armv7hl.

* Fri Feb 16 2018 mosquito <sensor.wen@gmail.com> - 3.2.9-1
- Update to 3.2.9

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.2.8-2
- Rebuilt for switch to libxcrypt

* Fri Dec 22 2017 mosquito <sensor.wen@gmail.com> - 3.2.8-1
- Update to 3.2.8

* Mon Nov 27 2017 mosquito <sensor.wen@gmail.com> - 3.2.7-1
- Update to 3.2.7

* Fri Oct 27 2017 mosquito <sensor.wen@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Wed Aug 30 2017 mosquito <sensor.wen@gmail.com> - 3.1.19-2
- Add fontconfig settings

* Sat Aug 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.19-1
- Update to 3.1.19

* Mon Aug 21 2017 mosquito <sensor.wen@gmail.com> - 3.1.18-1
- Update to 3.1.18

* Wed Aug  2 2017 mosquito <sensor.wen@gmail.com> - 3.1.17-1
- Update to 3.1.17

* Tue Aug  1 2017 mosquito <sensor.wen@gmail.com> - 3.1.16.1-1
- Update to 3.1.16.1

* Thu Jul 20 2017 mosquito <sensor.wen@gmail.com> - 3.1.14-1.git0f8418a
- Update to 3.1.14

* Fri Jul 14 2017 mosquito <sensor.wen@gmail.com> - 3.1.13-1.git03541ad
- Update to 3.1.13

* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 3.1.9-1.git82313d2
- Update to 3.1.9

* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 3.1.3-1.git87df955
- Update to 3.1.3

* Fri Jan 20 2017 mosquito <sensor.wen@gmail.com> - 3.0.25.2-1.gitcfbe9c8
- Update to 3.0.25.2

* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 3.0.25.1-1.gitde04735
- Update to 3.0.25.1

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Changed GOLANG dependencies

* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to version 3.0.24

* Mon Oct 31 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.23-1
- Upgrade to version 3.0.23

* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build
