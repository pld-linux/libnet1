Summary:	"libpwrite" Network Routine Library
Summary(pl.UTF-8):	Biblioteka czynności sieciowych
Summary(pt_BR.UTF-8):	API para funções de rede de baixo nível
Name:		libnet1
Version:	1.0.2a
Release:	4
License:	BSD
Group:		Libraries
Source0:	http://www.packetfactory.net/libnet/dist/deprecated/libnet-%{version}.tar.gz
# Source0-md5:	ddf53f0f484184390e8c2a1bd0853667
Patch0:		%{name}-shared.patch
Patch1:		%{name}-include.patch
Patch2:		%{name}-name.patch
URL:		http://www.packetfactory.net/libnet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Network Library provides a simple API for commonly used low-level
network functions (mainly packet injection). Using libnet, it is easy
to build and write arbitrary network packets. It provides a portable
framework for low-level network packet writing and handling (use
libnet in conjunction with libpcap and you can write some really cool
stuff). Libnet includes packet creation at the IP layer and at the
link layer as well as a host of supplementary and complementary
functionality.

%description -l pl.UTF-8
Biblioteka sieciowa (Network Library, libnet) dostarcza proste API
dla często używanych niskopoziomowych funkcji sieciowych (głównie
wstrzykujących pakiety). Przy użyciu libnet można łatwo tworzyć
dowolne pakiety sieciowe. Biblioteka jest przenośnym szkieletem do
niskopoziomowego tworzenia i obsługi pakietów sieciowych (szczególnie
w połączeniu z libpcap). Zawiera funkcje do tworzenia pakietów w
warstwie IP oraz w warstwie połączenia, a także wiele funkcji
uzupełniających.

%description -l pt_BR.UTF-8
Este pacote fornece uma API simples para funções de rede de baixo
nível comumente usadas (principalmente injeção de pacotes). Usando
libnet, é simples construir e enviar pacotes de rede arbitrários.

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libnet
Summary(pt_BR.UTF-8):	Arquivos do pacote libnet para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and develpment documentation for libnet.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libnet.

%description devel -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos que usam libnet.

%package static
Summary:	Static libnet library
Summary(pl.UTF-8):	Biblioteka statyczna libnet
Summary(pt_BR.UTF-8):	Arquivos do pacote libnet para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnet library.

%description static -l pl.UTF-8
Biblioteka statyczna libnet.

%description static -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam libnet.

%prep
%setup -q -n Libnet-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
mv include/libnet include/libnet1

%build
install %{_datadir}/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--with-pf_packet=yes
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

mv include/libnet.h include/libnet1.h
mv doc/libnet.3 doc/libnet1.3
mv libnet-config libnet1-config

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MAN_PREFIX=%{_mandir}/man3

ln -sf libnet1.so.1.0	$RPM_BUILD_ROOT%{_libdir}/libnet1.so
ln -sf libnet1.so	$RPM_BUILD_ROOT%{_libdir}/libpwrite1.so
ln -sf libnet1.a	$RPM_BUILD_ROOT%{_libdir}/libpwrite1.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/CHANGELOG*
%attr(755,root,root) %{_libdir}/libnet1.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libnet1-config
%attr(755,root,root) %{_libdir}/libnet1.so
%attr(755,root,root) %{_libdir}/libpwrite1.so
%{_includedir}/libnet1.h
%{_includedir}/libnet1
%{_mandir}/man3/libnet1.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnet1.a
%{_libdir}/libpwrite1.a
