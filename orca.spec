%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


%define python_version 2.5
%define pyorbit_version 2.0.1
%define pygtk2_version 2.6.2
%define gnome_python_version 2.6.2
%define gnome_python_version 2.6.2
%define brltty_version 3.7.2
%define atk_version 1.11.3
%define gail_version 1.8.11
%define gnome_speech_version 0.3.10
%define eel_version 2.14.0
%define libspi_version 1.7.6
%define brlapi_version 0.4.1
%define brltty_version 3.7.2
%define control_center_version 2.16.0-5

Name:		orca
Version:	2.23.6
Release: 	1%{?dist}
Summary:	Flexible, extensible, and powerful assistive technology

Group:		User Interface/Desktops
License:	LGPLv2+
URL:		http://www.gnome.org/projects/orca/
Source0:	http://download.gnome.org/sources/orca/2.23/orca-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-devel >= %{python_version}
BuildRequires:	brlapi-devel >= %{brlapi_version}
BuildRequires:	brltty >= %{brltty_version}
BuildRequires:	pyorbit-devel >= %{pyorbit_version}
BuildRequires: 	pygtk2-devel >= %{pygtk2_version}
BuildRequires:	atk-devel >= %{atk_version}
BuildRequires:	gail-devel >= %{gail_version}
BuildRequires:	eel2-devel >= %{eel_version}
BuildRequires:	at-spi-devel >= %{libspi_version}
BuildRequires:	gnome-speech-devel >= %{gnome_speech_version}
BuildRequires:	perl(XML::Parser)
BuildRequires:	gettext
BuildRequires:  gnome-python2-bonobo
BuildRequires:  gnome-python2-libwnck
Obsoletes:	gnopernicus
Provides:	gnopernicus

Requires:	gnome-mag
Requires:	control-center >= %{control_center_version}
Requires:	at-spi-python
Requires:	gnome-python2-bonobo
Requires:	gnome-python2-libwnck

%description
Orca is a flexible, extensible, and powerful assistive technology for people
with visual impairments. Using various combinations of speech synthesis,
braille, and magnification, Orca helps provide access to applications and
toolkits that support the AT-SPI (e.g., the GNOME desktop).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

#remove the .desktop file since we configure orca through the accessibility capplet
find $RPM_BUILD_ROOT -name '*.desktop' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
update-desktop-database &> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/orca
%{python_sitearch}/orca
%{_datadir}/icons/hicolor/*/apps/orca.png
%{_datadir}/icons/hicolor/scalable/apps/orca.svg
%dir %{_datadir}/orca
%dir %{_datadir}/orca/glade
%{_datadir}/orca/glade/*
%{_mandir}/man1/orca.1.gz


%changelog
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
