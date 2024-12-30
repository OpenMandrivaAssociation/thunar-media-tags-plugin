%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	A tag plugin for the Thunar File Manager
Name:		thunar-media-tags-plugin
Version:	0.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
Source0:	https://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Requires:	thunar
BuildRequires:	pkgconfig(thunarx-3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	pkgconfig(exo-2)

%description
The thunar-media-tags-plugin is a plugin for the Thunar File Manager, 
which adds ID3/OGG tag support to the bulk rename dialog. 

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%{_libdir}/thunarx-3/*
