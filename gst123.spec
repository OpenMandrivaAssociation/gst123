%define name gst123
%define version 0.3.1
%define release 2

Summary: Command line audio player based on GStreamer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://space.twc.de/~stefan/gst123/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: Sound
Url: http://space.twc.de/~stefan/gst123.php
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gtk+2-devel
BuildRequires: ncurses-devel

%description
The program gst123 is designed to be a more flexible command line
player in the spirit of ogg123 and mpg123, based on gstreamer. It
plays all file formats gstreamer understands, so if you have a music
collection which contains different file formats, like flac, ogg and
mp3, you can use gst123 to play all your music files.



%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README TODO
%_bindir/%name
%_mandir/man1/%name.1*



%changelog
* Sun Apr 22 2012 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2012.0
+ Revision: 792726
- update to new version 0.3.1
- readd mkrel for the backports

* Fri Mar 23 2012 Götz Waschk <waschk@mandriva.org> 0.3.0-1
+ Revision: 786340
- new version

* Mon Feb 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.2-1
+ Revision: 773775
- version update 0.2.2

* Sun Jul 31 2011 Götz Waschk <waschk@mandriva.org> 0.2.1-1
+ Revision: 692536
- update to new version 0.2.1

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - update to new version 0.2.0 (from goetz | 2011-04-12 15:15:52 +0200)

* Mon Jan 17 2011 Götz Waschk <waschk@mandriva.org> 0.1.4-1
+ Revision: 631161
- update to new version 0.1.4

* Sun Nov 28 2010 Götz Waschk <waschk@mandriva.org> 0.1.3-1mdv2011.0
+ Revision: 602504
- update to new version 0.1.3

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 550490
- update build deps
- new version

* Sat Apr 24 2010 Götz Waschk <waschk@mandriva.org> 0.0.1-1mdv2010.1
+ Revision: 538451
- import gst123


* Sat Apr 24 2010 Götz Waschk <waschk@mandriva.org> 0.0.1-1mdv2010.1
- initial package
