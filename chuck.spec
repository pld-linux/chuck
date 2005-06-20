# TODO: optflags
Summary:	ChucK audio programming language
Summary(pl):	ChucK - jêzyk programowania d¼wiêku
Name:		chuck
Version:	1.1.5.6
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://chuck.cs.princeton.edu/release/files/%{name}-%{version}.tgz
# Source0-md5:	c065109c7bc24ab2a485c9718876ace4
URL:		http://chuck.cs.princeton.edu/
BuildRequires:	alsa-lib-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
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

%description -l pl
ChucK to nowy jêzyk programowania d¼wiêku do syntezy w czasie
rzeczywistym, komponowania i wykonywania, dzia³aj±cy na systemach
operacyjnych urz±dzeñ. ChucK prezentuje nowy model programowania
wspó³bie¿nego oparty na czasie, obs³uguj±cy wielokrotne, jednoczesne,
dynamiczne wspó³czynniki sterowania oraz umo¿liwiaj±cy dodawanie,
usuwanie i modyfikowanie kodu w locie, podczas dzia³ania programu, bez
jego zatrzymywania czy restartowania. Oferuje kompozytorom, badaczom i
wykonawcom potê¿ne i elastyczne narzêdzie do programowania
przeznaczone do tworzenia i eksperymentowania ze z³o¿onymi programami
syntezy d¼wiêku i interaktywnym sterowaniem w czasie rzeczywistym.

%prep
%setup -q

%build
%{__make} -C src linux-alsa

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}}

install src/chuck $RPM_BUILD_ROOT%{_bindir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS DEVELOPER doc PROGRAMMER QUICKSTART README THANKS TODO VERSIONS
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}
