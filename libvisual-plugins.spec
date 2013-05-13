%define name libvisual-plugins
%define version 0.4.0

Summary: Visualisation plugins for applications based on libvisual
Name: %{name}
Version: %{version}
Release: %mkrel 16
Source0: %{name}-%{version}.tar.bz2
Patch0:	 %name-buffer-overflow.patch
#https://qa.mandriva.com/show_bug.cgi?id=49801
Patch1: 60_no-const-vispluginfo-in-nastyfft.patch
Patch2: libvisual-plugins-0.4.0-link.patch
License: LGPLv2+
Group: System/Libraries
Url: http://localhost.nl/~synap/libvisual-wiki/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: libvisual-nebulus
Obsoletes: libvisual-gforce
Provides: libvisual-nebulus
Provides: libvisual-gforce
BuildRequires: pkgconfig(libvisual-0.4) >= %version
BuildRequires: mesaglu-devel
BuildRequires: libalsa-devel
BuildRequires: libgdk_pixbuf2.0-devel
BuildRequires: bison

%description
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

This package contains the libvisual example plugins.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-14mdv2011.0
+ Revision: 661538
- mass rebuild

* Thu Dec 23 2010 Funda Wang <fwang@mandriva.org> 0.4.0-13mdv2011.0
+ Revision: 623956
- update url
- fix link

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-12mdv2011.0
+ Revision: 602612
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-11mdv2010.1
+ Revision: 520930
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.0-10mdv2010.0
+ Revision: 425875
- rebuild

* Sun Apr 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-9mdv2009.1
+ Revision: 366510
- fix crash (bug #49801)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-8mdv2009.0
+ Revision: 223017
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-7mdv2008.1
+ Revision: 179008
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Mar 16 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.4.0-5mdv2007.1
+ Revision: 144788
- Patch0: add patch to fix array overrun (from openSuSE)

* Sat Jan 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-4mdv2007.1
+ Revision: 108199
- use the right macros

* Sun Aug 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-3mdv2007.0
+ Revision: 53187
- remove debug files from the package
- fix buildrequires

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream version
    - import libvisual-plugins-0.2.0-4mdk

* Thu Feb 16 2006 Götz Waschk <waschk@mandriva.org> 0.2.0-4mdk
- enable mmx to make it build
- disable the infinite plugin
- use mkrel

* Tue Feb 15 2005 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-3mdk
- fix buildrequires

* Fri Feb 11 2005 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-2mdk
- remove rpaths
- obsoletes libvisual-nebulus and libvisual-gforce

* Thu Feb 10 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.2.0-1mdk
- 0.2.0

* Sat Oct 16 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.7-1mdk
- New release 0.1.7

* Tue Sep 14 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.6-1mdk
- requires new libvisual
- New release 0.1.6

* Fri Jul 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.5-1mdk
- initial package

