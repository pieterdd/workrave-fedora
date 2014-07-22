Name: workrave
Version: 1.10
Release: 6%{?dist}
Summary: Program that assists in the recovery and prevention of RSI
# Based on older packages by Dag Wieers <dag@wieers.com> and Steve Ratcliffe
License: GPLv3+
Group: Applications/Productivity
URL: http://www.workrave.org/
# Using github checkout:
# https://github.com/rcaelers/workrave
# Source0: http://downloads.sourceforge.net/workrave/%{name}-%{version}.tar.gz
Source0: https://github.com/rcaelers/workrave/archive/%{commit}/%{name}-%{version}.tar.gz
Patch1: workrave-6f9bc5d-fix-desktop-translation.patch

BuildRequires: glib2-devel >= 2.28.0
BuildRequires: gtk3-devel >= 3.0.0
BuildRequires: libsigc++20-devel >= 2.2.4.2
BuildRequires: glibmm24-devel >= 2.28.0
BuildRequires: gtkmm30-devel >= 3.0.0
BuildRequires: gobject-introspection-devel
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libXmu-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
BuildRequires: libXScrnSaver-devel
# Temporarily disabled because not usable without panel
#BuildRequires: dbus-devel
BuildRequires: gstreamer-devel
BuildRequires: intltool
BuildRequires: python-cheetah
BuildRequires: pulseaudio-libs-devel
BuildRequires: autoconf, automake, libtool

Requires: dbus

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%package devel
Requires: %{name} = %{version}-%{release}
Summary: Development files for workrave

%description devel
Development files for workrave.

%prep
%setup -q
%patch1 -p1 -b .fixpl
touch ChangeLog

%build
if [ ! -x configure ]; then
  ### Needed for snapshot releases.
  NOCONFIGURE=1 ./autogen.sh
fi

%configure --disable-dbus --disable-xml --enable-gnome3 --disable-static

make V=1

%install
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a

%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%{_datadir}/workrave/
%{_datadir}/sounds/workrave/
%{_datadir}/icons/hicolor/16x16/apps/workrave.png
%{_datadir}/icons/hicolor/24x24/apps/workrave.png
%{_datadir}/icons/hicolor/32x32/apps/workrave.png
%{_datadir}/icons/hicolor/48x48/apps/workrave.png
%{_datadir}/icons/hicolor/64x64/apps/workrave.png
%{_datadir}/icons/hicolor/96x96/apps/workrave.png
%{_datadir}/icons/hicolor/128x128/apps/workrave.png
%{_datadir}/icons/hicolor/scalable/workrave-sheep.svg
%{_datadir}/icons/hicolor/scalable/apps/workrave.svg
%{_datadir}/applications/workrave.desktop
#%{_datadir}/dbus-1/services/org.workrave.Workrave.service
#%{_datadir}/dbus-1/services/org.gnome.panel.applet.WorkraveAppletFactory.service
#%{_datadir}/glib-2.0/schemas/org.workrave.*.xml
#%{_datadir}/gnome-panel/4.0/applets/org.workrave.WorkraveApplet.panel-applet
#%{_datadir}/gnome-panel/ui/workrave-gnome-applet-menu.xml
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/
%{_libdir}/girepository-1.0/Workrave-1.0.typelib
#%{_libexecdir}/workrave-applet
%{_libdir}/libworkrave-private-1.0.so.*

%files devel
%{_datadir}/gir-1.0/Workrave-1.0.gir
%{_libdir}/libworkrave-private-1.0.so

%changelog
* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.10-6
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May  3 2013 Tomáš Mráz <tmraz@redhat.com> - 1.10-3
- do not build the panel applet

* Mon Mar 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.10-2
- Add missing distag

* Tue Feb 19 2013 Tomáš Mráz <tmraz@redhat.com> - 1.10-1
- new upstream release

* Fri Feb  8 2013 Tomáš Mráz <tmraz@redhat.com> - 1.9.911-0.2.20130107git6f9bc5d
- drop --vendor from desktop-file-install call

* Tue Jan  8 2013 Tom Callaway <spot@fedoraproject.org> - 1.9.911-0.1.20130107git6f9bc5d
- update to 1.9.911 checkout from github
- build for gnome3

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.4-3
- rebuilt with new libpng

* Tue Jun 28 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.4-2
- no longer needs gnet2

* Wed Apr 06 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.9.4-1
- New upstream bug fix release. Closes rhbz#693958
- https://github.com/rcaelers/workrave/blob/b491d9b5054b5571d5b4ff0f6c9137133735129d/NEWS
- Drop buildroot definition and clean section 

* Thu Feb 10 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.3-4
- due to changes in gnome applet API we have to build without
  gnome support

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Tomas Mraz <tmraz@redhat.com> - 1.9.3-2
- rebuilt with new gnome-panel

* Fri Dec 17 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.3-1
- new upstream release with bug fixes and usability improvements

* Wed Nov  3 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.2-1
- new upstream release hopefully fixing at least some of the aborts

* Mon Apr 26 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-4
- better guard for BadWindow errors in input monitor (#566156)

* Wed Mar 17 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-3
- fix FTBFS (#564917)

* Thu Jan 28 2010 Tomas Mraz <tmraz@redhat.com> - 1.9.1-2
- do not build against gdome2 - not too useful optional feature

* Tue Dec  8 2009 Tomas Mraz <tmraz@redhat.com> - 1.9.1-1
- new upstream version

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Tomas Mraz <tmraz@redhat.com> - 1.9.0-3
- fix build with new gcc 4.4 and glibc

* Fri Sep 26 2008 Tomas Mraz <tmraz@redhat.com> - 1.9.0-1
- new upstream version

* Fri Apr  4 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-4
- fix locking/unlocking with gnome-screensaver (#207058)
- make it build with current libsigc++

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.8.5-3
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-2
- make it build on gcc-4.3

* Mon Jan  7 2008 Tomas Mraz <tmraz@redhat.com> - 1.8.5-1
- upgrade to latest upstream version

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-4
- applet counters don't start properly
- license tag fix

* Wed Apr 18 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-3
- fixed applet crash (#236543)

* Mon Mar 26 2007 Tomas Mraz <tmraz@redhat.com> - 1.8.4-2
- new upstream version
- add datadir/pixmaps/workrave to files (#233815)

* Thu Sep  7 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.3-2
- rebuilt for FC6

* Wed May 31 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.3-1
- New upstream version

* Wed Feb 15 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.2-2
- Rebuilt with updated gcc

* Thu Feb  2 2006 Tomas Mraz <tmraz@redhat.com> - 1.8.2-1
- Updated version, dropped obsolete patch
- Added missing buildrequires for modular X
- Fixed compilation on gcc-4.1

* Sat Oct 22 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-4
- Added a desktop file
- Added find_lang
- Fixed wrong install extension for message translations

* Thu Oct 20 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-3
- Removed Prefix:, added BuildRequires gnome-panel-devel
- Group: Applications/Productivity

* Thu Sep 22 2005 Tomas Mraz <tmraz@redhat.com> - 1.8.1-2
- Initial package, reused spec from package by Steve Ratcliffe
