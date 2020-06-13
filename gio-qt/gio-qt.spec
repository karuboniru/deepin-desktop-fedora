Name:           gio-qt
Version:        0.0.9
Release:        1%{?dist}
Summary:        Gio wrapper for Qt applications 
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  glibmm24-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  qt5-doctools

%description
This package provides a GIO wrapper class for Qt.


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}
Requires:       glibmm24-devel%{?isa}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|qt5/doc|doc/qt5|' CMakeLists.txt

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%cmake .
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_qt5_docdir}/%{name}.qch


%changelog
