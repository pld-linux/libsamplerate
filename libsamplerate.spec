#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_without	tests		# unit tests
#
Summary:	Sample Rate Converter library
Summary(pl.UTF-8):	Biblioteka do konwersji częstotliwości próbkowania
Name:		libsamplerate
Version:	0.2.2
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/libsndfile/libsamplerate/releases
Source0:	https://github.com/libsndfile/libsamplerate/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	97c010fc25156c33cddc272c1935afab
URL:		http://www.mega-nerd.com/SRC/
BuildRequires:	alsa-lib-devel >= 0.9
%{?with_tests:BuildRequires:	fftw3-devel >= 3.0.0}
BuildRequires:	libsndfile-devel >= 1.0.10
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libsamplerate

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README.md docs/*.md
%attr(755,root,root) %{_libdir}/libsamplerate.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsamplerate.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsamplerate.so
%{_libdir}/libsamplerate.la
%{_includedir}/samplerate.h
%{_pkgconfigdir}/samplerate.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsamplerate.a
%endif
