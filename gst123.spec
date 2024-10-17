Summary: Command line audio player based on GStreamer
Name: gst123
Version: 0.3.5
Release: 1
Source0: http://space.twc.de/~stefan/gst123/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: Sound
Url: https://space.twc.de/~stefan/gst123.php
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: ncurses-devel

%description
The program gst123 is designed to be a more flexible command line
player in the spirit of ogg123 and mpg123, based on gstreamer. It
plays all file formats gstreamer understands, so if you have a music
collection which contains different file formats, like flac, ogg and
mp3, you can use gst123 to play all your music files.



%prep
%autosetup -p1
%configure2_5x

%build
%make_build

%install
%make_install

%files
%doc AUTHORS NEWS TODO
%_bindir/%name
%_mandir/man1/%name.1*
