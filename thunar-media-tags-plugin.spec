%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A tag plugin for the Thunar File Manager
Name:		thunar-media-tags-plugin
Version:	0.2.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
Source0:	http://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		thunar-media-tags-plugin-0.2.0-fix-linking.patch
Requires:	thunar >= 1.3.1
BuildRequires:	thunar-devel >= 1.3.1
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	exo-devel >= 0.7.2

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


%changelog
* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-2
+ Revision: 789809
- rebuild
- drop old stuff from spec file

* Sun Feb 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1
+ Revision: 777494
- fix file list
- Patch0: fix linking
- add exo-devel to buildrequires
- add buildrequires on intltool
- update to new version 0.2.0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-11mdv2010.1
+ Revision: 543282
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.1.2-10mdv2010.0
+ Revision: 445422
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-9mdv2009.1
+ Revision: 349180
- rebuild whole xfce

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-8mdv2009.1
+ Revision: 294886
- rebuild for new Thunar  (Xfce4.6 beta1)

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-7mdv2009.0
+ Revision: 261534
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-6mdv2009.0
+ Revision: 254534
- rebuild

* Sat Feb 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-4mdv2008.1
+ Revision: 174082
- drop requires on taglib (#37929)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-3mdv2008.1
+ Revision: 110639
- new license policy
- do not package COPYING and INSTALL files

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-2mdv2008.0
+ Revision: 33278
- drop __libtoolize
- spec file clean
- update url

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 30300
- new version


* Tue Jan 02 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.1-4mdv2007.0
+ Revision: 103177
- Rebuild for latest thunar

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add BuildRequires
    - import thunar-media-tags-plugin-0.1.1-1mdv2007.0

* Fri Aug 04 2006 Charles A Edwards <eslrahc@mandriva.org> 0.1.1-1mdv2007.0
- 0.1.1 (bugfix release)
- update URL

* Thu Jul 13 2006 Charles A Edwards <eslrahc@mandriva.org> 0.1.0-2mdv2007.0
- rebuild for xfce-4.3.90.2

* Sat Jun 24 2006 Charles A Edwards <eslrahc@mandriva.org> 0.1.0-1mdv2007.0
- initial mandriva package

