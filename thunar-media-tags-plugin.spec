Summary:	A tag plugin for the Thunar File Manager
Name:		thunar-media-tags-plugin
Version:	0.1.2
Release:	%mkrel 7
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
Source0:	http://goodies.xfce.org/releases/thunar-media-tags-plugin/%{name}-%{version}.tar.bz2
Requires:	thunar >= 0.8.0
BuildRequires:	thunar-devel >= 0.2.2
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The thunar-media-tags-plugin is a plugin for the Thunar File Manager, 
which adds ID3/OGG tag support to the bulk rename dialog. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/thunarx-1/*
