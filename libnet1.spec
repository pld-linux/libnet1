Summary:	"libpwrite" Network Routine Library
Summary(pl):	Biblioteka czynno�ci sieciowych
Summary(pt_BR):	API para fun��es de rede de baixo n�vel
Name:		libnet1
Version:	1.0.2a
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.packetfactory.net/libnet/dist/libnet-%{version}.tar.gz
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

%description -l pl
Biblioteka dostarcza API dla popularnych nisko-poziomowych funkcji
sieciowych (g��wnie wstrzykuj�cych pakiety).

%description -l pt_BR
Este pacote fornece uma API simples para fun��es de rede de baixo
n�vel comumente usadas (principalmente inje��o de pacotes). Usando
libnet, � simples construir e enviar pacotes de rede arbitr�rios.

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl):	Pliki nag��wkowe i dokumetacja do libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libnet.

%description devel -l pl
Pliki nag��wkowe i dokumetacja do libnet.

%description devel -l pt_BR
Arquivos de cabe�alho e bibliotecas usadas no desenvolvimento de
aplicativos que usam libnet.

%package static
Summary:	Static libnet library
Summary(pl):	Biblioteka statyczna libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento est�tico
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libnet library.

%description static -l pl
Biblioteka statyczna libnet.

%description static -l pt_BR
Arquivos de cabe�alho e bibliotecas usadas no desenvolvimento de
aplicativos est�ticos que usam libnet.

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/libnet1
%{_mandir}/man*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
