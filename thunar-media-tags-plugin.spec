%define __libtoolize /bin/true 

Summary:     A tag plugin for the Thunar File Manager
Name:       thunar-media-tags-plugin
Version:    0.1.2
Release:    %mkrel 1
License:    GPL
URL:        http://goodies.xfce.org/projects/panel-plugins
Source0:    %{name}-%{version}.tar.bz2
Group:      Graphical desktop/Xfce
BuildRoot:  %{_tmppath}/%{name}-buildroot
Requires:       thunar >= 0.2.3
Requires:   taglib >= 1.4
BuildRequires:  thunar-devel >= 0.2.2
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  perl(XML::Parser)

%description
The thunar-media-tags-plugin is a plugin for the Thunar File Manager, 
which adds ID3/OGG tag support to the bulk rename dialog. 

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{_libdir}/thunarx-1/*
