#
# Conditional build:
%bcond_without	tests	# do not perform "make check"
#
Summary:	Sample Rate Converter library
Summary(pl.UTF-8):	Biblioteka do konwersji częstotliwości próbkowania
Name:		libsamplerate
Version:	0.1.7
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download:	http://www.mega-nerd.com/SRC/download.html
Source0:	http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
# Source0-md5:	ad093e60ec44f0a60de8e29983ddbc0f
URL:		http://www.mega-nerd.com/SRC/
%{?with_tests:BuildRequires:	fftw3-devel >= 0.15.0}
BuildRequires:	libsndfile-devel >= 1.0.10
BuildRequires:	pkgconfig
Requires:	libsndfile >= 1.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. SRC is capable of arbitrary and time varying conversions; from
downsampling by a factor of 12 to upsampling by the same factor. SRC
provides a small set of converters to allow quality to be traded off
against computation cost. The current best converter provides a
signal-to-noise ratio of 97dB with -3dB passband extending from DC to
96% of the theoretical best bandwidth for a given pair of input and
output sample rates.

%description -l pl.UTF-8
Biblioteka libsamplerate (zwana także Secret Rabbit Code lub Sample
Rate Converter - w skrócie SRC) służy do konwersji częstotliwości
próbkowania dźwięku. SRC może wykonywać dowolnych konwersji - od
zmniejszania częstotliwości do 12 razy do zwiększania o ten sam
współczynnik. SRC udostępnia niewielki zestaw konwerterów
pozwalających na pogodzenie jakości i czasu trwania konwersji.
Aktualnie najlepszy konwerter udostępnia współczynnik sygnał/szum 97dB
z rozszerzeniem zakresu pasma -3dB z DC do 96% teoretycznie
najlepszego pasma dla danej pary częstotliwości próbkowania wejścia i
wyjścia.

%package devel
Summary:	Header file for libsamplerate library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libsamplerate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libsamplerate library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libsamplerate.

%package static
Summary:	libsamplerate static library
Summary(pl.UTF-8):	Statyczna biblioteka libsamplerate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libsamplerate static library.

%description static -l pl.UTF-8
Statyczna biblioteka libsamplerate.

%package tools
Summary:	libsamplerate utilities
Summary(pl.UTF-8):	Narzędzia do libsamplerate
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description tools
libsamplerate utilities - currently include one program to resample
audio files read and written using libsndfile.

%description tools -l pl.UTF-8
Narzędzia do libsamplerate - aktualnie zawierają program do zmiany
częstotliwości próbkowania plików dźwiękowych czytanych i zapisywanych
przez libsndfile.

%prep
%setup -q

%build
%configure
%{__make}

%{?with_tests:%{__make} -C tests check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*.{html,css,png}
%attr(755,root,root) %{_libdir}/libsamplerate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsamplerate.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsamplerate.so
%{_libdir}/libsamplerate.la
%{_includedir}/samplerate.h
%{_pkgconfigdir}/samplerate.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsamplerate.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sndfile-resample
