#
# Conditional build:
%bcond_without	tests	# do not perform "make check"
#
Summary:	Sample Rate Converter library
Summary(pl):	Biblioteka do konwersji cz�stotliwo�ci pr�bkowania
Name:		libsamplerate
Version:	0.1.2
Release:	2
License:	GPL
Group:		Libraries
#Source0Download:	http://www.mega-nerd.com/SRC/download.html
Source0:	http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
# Source0-md5:	06861c2c6b8e5273c9b80cf736b9fd0e
URL:		http://www.mega-nerd.com/SRC/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%{?with_tests:BuildRequires:	fftw3-devel}
BuildRequires:	libsndfile-devel >= 1.0.10
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

%description -l pl
Biblioteka libsamplerate (zwana tak�e Secret Rabbit Code lub Sample
Rate Converter - w skr�cie SRC) s�u�y do konwersji cz�stotliwo�ci
pr�bkowania d�wi�ku. SRC mo�e wykonywa� dowolnych konwersji - od
zmniejszania cz�stotliwo�ci do 12 razy do zwi�kszania o ten sam
wsp�czynnik. SRC udost�pnia niewielki zestaw konwerter�w
pozwalaj�cych na pogodzenie jako�ci i czasu trwania konwersji.
Aktualnie najlepszy konwerter udost�pnia wsp�czynnik sygna�/szum 97dB
z rozszerzeniem zakresu pasma -3dB z DC do 96% teoretycznie
najlepszego pasma dla danej pary cz�stotliwo�ci pr�bkowania wej�cia i
wyj�cia.

%package devel
Summary:	Header file for libsamplerate library
Summary(pl):	Plik nag��wkowy biblioteki libsamplerate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libsamplerate library.

%description devel -l pl
Plik nag��wkowy biblioteki libsamplerate.

%package static
Summary:	libsamplerate static library
Summary(pl):	Statyczna biblioteka libsamplerate
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libsamplerate static library.

%description static -l pl
Statyczna biblioteka libsamplerate.

%package tools
Summary:	libsamplerate utilities
Summary(pl):	Narz�dzia do libsamplerate
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description tools
libsamplerate utilities - currently include one program to resample
audio files read and written using libsndfile.

%description tools -l pl
Narz�dzia do libsamplerate - aktualnie zawieraj� program do zmiany
cz�stotliwo�ci pr�bkowania plik�w d�wi�kowych czytanych i zapisywanych
przez libsndfile.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc AUTHORS ChangeLog README doc/*.{html,css,png}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sndfile-resample
