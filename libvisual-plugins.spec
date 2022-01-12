%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Visualisation plugins for applications based on libvisual
Name:		libvisual-plugins
Version:	0.4.0
Release:	29
License:	LGPLv2+
Group:		System/Libraries
Url:		http://localhost.nl/~synap/libvisual-wiki/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-buffer-overflow.patch
#https://qa.mandriva.com/show_bug.cgi?id=49801
Patch1:		60_no-const-vispluginfo-in-nastyfft.patch
Patch2:		libvisual-plugins-0.4.0-link.patch
Patch3:        libvisual-plugins-0.4.0-fix-some-gcc-warnings.patch
Patch4:        libvisual-plugins-0.4.0-gcc5.patch

BuildRequires:	bison
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libvisual-0.4) >= %version
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: gettext-devel
Provides:	libvisual-nebulus
Provides:	libvisual-gforce

%description
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

This package contains the libvisual example plugins.

%prep
%setup -q
%autopatch -p1

%build
export CC=gcc
export CXX=g++
%ifarch %ix86
export CFLAGS="-mmmx %optflags"
%endif
LDFLAGS="-Wl,--allow-multiple-definition" 
%configure --disable-gstreamer-plugin
%make_build

%install
%make_install
%find_lang %{name}-0.4

%files -f %{name}-0.4.lang
%doc README AUTHORS ChangeLog NEWS
%{_libdir}/libvisual-0.4/*/*.so
%{_datadir}/%{name}-0.4/

