%define name libvisual-plugins
%define version 0.4.0
%define release %mkrel 5

Summary: Visualisation plugins for applications based on libvisual
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0:	 %name-buffer-overflow.patch
License: GPL
Group: System/Libraries
Url: http://localhost.nl/~synap/libvisual/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: libvisual-nebulus
Obsoletes: libvisual-gforce
Provides: libvisual-nebulus
Provides: libvisual-gforce
BuildRequires: libvisual-devel >= %version
BuildRequires: esound-devel
BuildRequires: bison
BuildRequires: chrpath
%if %mdkversion > 200600
BuildRequires:	X11-devel
%else
BuildRequires:	X11-devel
%endif

%description
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

This package contains the libvisual example plugins.
%prep
%setup -q
%patch0 -p0

%build
%ifarch %ix86
export CFLAGS="-mmmx %optflags"
%endif
%configure2_5x
%make

%install
rm -rf %buildroot

%makeinstall_std
%find_lang %name-0.4
%clean
rm -rf %buildroot

%files -f %name-0.4.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%_libdir/libvisual*
%_datadir/%{name}*



