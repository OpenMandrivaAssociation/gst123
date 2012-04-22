%define name gst123
%define version 0.3.1
%define release %mkrel 1

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

