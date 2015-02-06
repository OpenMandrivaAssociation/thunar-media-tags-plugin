%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A tag plugin for the Thunar File Manager
Name:		thunar-media-tags-plugin
Version:	0.2.1
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
Source0:	http://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		thunar-media-tags-plugin-0.2.0-fix-linking.patch
Requires:	thunar >= 1.3.1
BuildRequires:	pkgconfig(thunarx-2) >= 1.3.1
BuildRequires:	pkgconfig(taglib) >= 1.4
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	pkgconfig(exo-1) >= 0.7.2

%description
The thunar-media-tags-plugin is a plugin for the Thunar File Manager, 
which adds ID3/OGG tag support to the bulk rename dialog. 

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/thunarx-2/*
