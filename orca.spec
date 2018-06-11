%global debug_package %{nil}

%define brlapi_version 0.5.1
%define brltty_version 3.9

Name:           orca
Version:        3.6.3
Release:        4%{?dist}
Summary:        Assistive technology for people with visual impairments

Group:          User Interface/Desktops
License:        LGPLv2+
URL:            http://projects.gnome.org/orca/
#VCS: git:git://git.gnome.org/orca
Source0:        http://download.gnome.org/sources/orca/3.6/orca-%{version}.tar.xz

BuildRequires:  brlapi-devel >= %{brlapi_version}
BuildRequires:  python-brlapi
BuildRequires:  brltty >= %{brltty_version}
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pygobject3-devel
BuildRequires:  pyatspi
BuildRequires:  at-spi2-core-devel
BuildRequires:  dbus-python
BuildRequires:  liblouis-python
BuildRequires:  liblouis-devel
BuildRequires:  speech-dispatcher-python
BuildRequires:  gtk3-devel
BuildRequires:  itstool
Obsoletes:      gnopernicus
Provides:       gnopernicus

Requires:       control-center
Requires:       libwnck3
Requires:       pyatspi
Requires:       speech-dispatcher
Requires:       speech-dispatcher-python
Requires:       liblouis-python
Requires:       python-brlapi >= %{brlapi_version}

%description
Orca is a flexible, extensible, and powerful assistive technology for people
with visual impairments. Using various combinations of speech synthesis,
braille, and magnification, Orca helps provide access to applications and
toolkits that support AT-SPI (e.g. the GNOME desktop).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &>/dev/null ||:
if [ $1 -eq 0 ]; then
   touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
   gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/orca
%{python_sitearch}/orca
%{_datadir}/icons/hicolor/*/apps/orca.png
%{_datadir}/icons/hicolor/scalable/apps/orca.svg
%{_datadir}/orca
%{_datadir}/applications/orca.desktop
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
%{_mandir}/man1/orca.1.gz


%changelog
* Tue Jan 28 2014 Rui Matos <rmatos@redhat.com> - 3.6.3-4
- Resolves: rhbz#1058678 - Remove dependency on PyXDG

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.6.3-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.6.3-2
- Mass rebuild 2013-12-27

* Wed Nov 14 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.3-1
- Update to 3.6.3

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Tue Sep 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.4-1
- Back down to 3.5.4, we want to stick with python 2.7 for now

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 3.7.0.4-1
- Update to 3.7.0.4

* Wed Jun 27 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.5.3-2
- Back down to 3.5.3, we want to stick with python 2.7 for now

* Tue Jun 26 2012 Richard Hughes <hughsient@gmail.com> - 3.7.0.3-1
- Update to 3.7.0.3

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-2
- Don't depend on gnome 2 python libs (#716719)
- Require pyxdg (#761306)

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Wed Nov 23 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> 3.1.92-1
- Update to 3.1.92

* Tue Sep  9 2011 Matthias Clasen <mclasen@redhat.com> 3.1.91-1
- Update to 3.1.91

* Thu Aug 18 2011 Matthias Clasen <mclasen@redhat.com> 3.1.5-1
- Update to 3.1.5

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> 3.1.4-1
- Update to 3.1.4

* Tue Jul 05 2011 Bastien Nocera <bnocera@redhat.com> 3.1.3-1
- Update to 3.1.3

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Wed May 11 2011 Tomas Bzatek <tbzatek@redhat.com> 3.1.1-1
- Update to 3.1.1

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Thu Apr  7 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-2
- Only autostart in GNOME

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-1
- Update to 3.0.0
- Bring the gnome-speech dependency back

* Sun Apr  3 2011 Matthias Clasen <mclasen@redhat.com> 2.91.93-2
- Drop PyYAML depencency (no longer used)
- Don't require gnome-speech (speech-dispatcher is preferred)

* Fri Mar 25 2011 Matthias Clasen <mclasen@redhat.com> 2.91.93-1
- Update to 2.91.93

* Fri Mar 25 2011 Bastien Nocera <bnocera@redhat.com> 2.91.92-2
- Use GSettings to check whether toolkit accessibility is enabled,
  patch from Frederic Crozat

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.92-1
- Update to 2.91.92

* Mon Mar  3 2011 Matthias Clasen <mclasen@redhat.com> 2.91.91-1
- Update to 2.91.91
- Drop a space-saving hack

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.90-1
- Update to 2.91.90

* Sun Feb 20 2011 Matthias Clasen <mclasen@redhat.com> 2.91.6-4
- Fix dependencies

* Thu Feb 17 2011 Bastien Nocera <bnocera@redhat.com> 2.91.6-3
- Don't remove the desktop files, as they are "no display" anyway
  (this would also have removed the autostart desktop file in
  newer versions of Orca)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> - 2.91.6-1
- Update to 2.91.6

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.5-1
- Update to 2.91.5

* Thu Dec  2 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Thu Nov 11 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.2-1
- Update to 2.91.2

* Wed Oct  6 2010 Matthias Clasen <mclasen@redhat.com> - 2.91.0-1
- Update to 2.91.0

* Mon Oct 04 2010 Ray Strode <rstrode@redhat.com> 2.32.0-2
- Require orbit at-spi python bindings
http://lists.fedoraproject.org/pipermail/desktop/2010-October/006568.html

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Thu Aug 19 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.90-1
- Update to 2.31.90

* Mon Aug 16 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-2
- Curb excessive BRs

* Tue Aug  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-1
- Update to 2.31.6

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.31.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 12 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-1
- Update to 2.31.5

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.4-1
- Update to 2.31.4

* Wed Jun 16 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-2
- Require pyatspi, not at-spi-python

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.3-1
- Update to 2.31.3

* Fri May 28 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.2-1
- Update to 2.31.2

* Sat May 15 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.1-1
- Update to 2.31.1

* Tue Apr 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Wed Mar 10 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.92-1
- Update to 2.29.92

* Sat Feb 20 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.91-1
- Update to 2.29.91

* Wed Feb 10 2010 Bastien Nocera <bnocera@redhat.com> 2.29.90-1
- Update to 2.29.90

* Tue Jan 26 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.6-1
- Update to 2.29.6

* Sun Jan 17 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.5-1
- Update to 2.29.5

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.29.4-1
- Update to 2.29.4

* Sat Dec  5 2009 Matthias Clasen <mclasen@redhat.com> - 2.29.2-1
- Update to 2.29.2

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Thu Jun 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-2
- We don't have debuginfo

* Tue Jun 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-1
- Update to 2.27.3

* Thu Jun 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-2
- Add a dependency on gnome-speech (#503193)

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-1
- Update to 2.27.2

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/orca/2.26/orca-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Tue Jan  6 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.4-1
- Update to 2.25.4

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-2
- Update to 2.25.3

* Wed Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-2
- Rebuild for Python 2.6

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-1
- Update to 2.25.2

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.25.1-3
- Rebuild for Python 2.6

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-2
- Tweak description

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Fri Oct 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Tue Aug 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-2
- Require gnome-python2-gnome

* Sat Aug 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-1
- Update to 2.23.5

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3-1
- Update to  2.23.3

* Wed May 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-3
- Add BuildRequires gnome-python2-bonobo back

* Wed May 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-2
- Require gnome-python2-bonobo and gnome-python2-libwnck

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-2
- Fix source url

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Apr  7 2008 Jon McCann <jmccann@redhat.com> - 2.22.1-2
- Fix signal handling (GNOME bug #525831)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5

* Fri Jan  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.4-2
- Require at-spi-python (#427432)

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.4-1
- Update to 2.21.4

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.3-1
- Update to 2.21.3

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-1
- Update to 2.20.0.1 (bug fixes and translation updates)

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-1
- Update to 2.19.90

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-2
- Update license field

* Sun Jul 29 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Mon Jul  9 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Sun Feb 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-1
- Update to orca 2.17.5

* Wed Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.4-1
- Update to orca 2.17.4

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.17.3-2
- rebuild for python 2.5

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to orca 2.17.3

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1
- Update to orca 2.17.2

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-2
- Fix typos in the spec

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

*  Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.0-3
- Add patch to shutdown orca

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.0-2
- Add requirements on gnome-mag and newer version of control-center
- remove .desktop file and make control-center start and configure orca

* Sun Sep  3 2006 Matthias Clasen <mclasen@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Thu Aug 31 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.0-4
- Obsolete gnome-mag-devel, too

* Tue Aug 29 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-3
- Spec file cleanups

* Mon Aug 21 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-1
- Initial package
