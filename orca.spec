%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define python_version 2.4
%define pyorbit_version 2.0.1
%define pygtk2_version 2.6.2
%define gnome_python_version 2.6.2
%define brltty_version 3.7.2
%define atk_version 1.11.3
%define gail_version 1.8.11
%define gnome_speech_version 0.3.10
%define eel_version 2.14.0
%define libspi_version 1.7.6
%define brlapi_version 0.4.1
%define brltty_version 3.7.2

Name:		orca
Version:	0.9.0 
Release:	2%{?dist}
Summary:	flexible, extensible, and powerful assistive technology for people with visual impairments 

Group:		User Interface/Desktops
License:	LGPL
URL:		http://www.gnome.org/projects/orca/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/orca/0.9/orca-0.9.0.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-devel >= %{python_version}
BuildRequires:	brlapi-devel >= %{brlapi_version}
BuildRequires:	brltty >= %{brltty_version}
BuildRequires:	pyorbit-devel >= %{pyorbit_verion}
BuildRequires: 	pygtk2-devel >= %{pygtk2_version}
BuildRequires:	atk-devel >= %{atk_version}
BuildRequires:	gail-devel >= %{gail_version}
BuildRequires:	eel2-devel >= %{eel_version}
BuildRequires:	at-spi-devel >= %{libspi_version}
BuildRequires:	gnome-speech-devel >= %{gnome_speech_version}
BuildRequires:	perl(XML::Parser) 
BuildRequires:	gnome-python2-bonobo 
BuildRequires:	gettext
Obsoletes:	gnopernicus 
Obsoletes:	gnome-mag
Provides:	gnopernicus
Provides:	gnome-mag

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


%clean
rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database &> /dev/null ||:
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
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/orca
%dir %{python_sitearch}/orca
%{python_sitearch}/orca/*.py*
%{python_sitearch}/orca/brlmodule.so
%dir %{python_sitearch}/orca/scripts
%{python_sitearch}/orca/scripts/*.py*
%{_datadir}/applications/orca.desktop
%{_datadir}/icons/hicolor/48x48/apps/orca.png
%dir %{_datadir}/orca
%dir %{_datadir}/orca/glade
%{_datadir}/orca/glade/orca-setup.glade

%changelog
* Mon Aug 21 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-1
- Initial package
