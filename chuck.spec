Summary:	ChucK audio programming language
Name:		chuck
Version:	1.1.5.2
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://chuck.cs.princeton.edu/release/files/%{name}-%{version}.tgz
# Source0-md5:	e12df7852d1796d766bd68c0d1fafb03
URL:		http://chuck.cs.princeton.edu/
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ChucK is a new audio programming language for real-time synthesis,
composition, and performance, which runs on commodity operating
systems. ChucK presents a new time-based concurrent programming model,
which supports multiple, simultaneous, dynamic control rates, and the
ability to add, remove, and modify code, on-the-fly, while the program
is running, without stopping or restarting. It offers composers,
researchers, and performers a powerful and flexible programming tool
for building and experimenting with complex audio synthesis programs,
and real-time interactive control.

%prep
%setup -q

%build
cd src
%{__make} linux-alsa
cd -

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}}

cp src/chuck $RPM_BUILD_ROOT%{_bindir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS DEVELOPER doc PROGRAMMER QUICKSTART README THANKS TODO VERSIONS
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}
