%define _disable_ld_no_undefined 1

Summary:	Visualisation plugins for applications based on libvisual
Name:		libvisual-plugins
Version:	0.4.0
Release:	23
License:	LGPLv2+
Group:		System/Libraries
Url:		http://localhost.nl/~synap/libvisual-wiki/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-buffer-overflow.patch
#https://qa.mandriva.com/show_bug.cgi?id=49801
Patch1:		60_no-const-vispluginfo-in-nastyfft.patch
Patch2:		libvisual-plugins-0.4.0-link.patch

BuildRequires:	bison
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libvisual-0.4) >= %version
Provides:	libvisual-nebulus
Provides:	libvisual-gforce

%description
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

This package contains the libvisual example plugins.

%prep
%setup -q
%apply_patches

%build
export CC=gcc
%ifarch %ix86
export CFLAGS="-mmmx %optflags"
%endif
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}-0.4

%files -f %{name}-0.4.lang
%doc README AUTHORS ChangeLog NEWS
%{_libdir}/libvisual-0.4/*/*.so
%{_datadir}/%{name}-0.4/

