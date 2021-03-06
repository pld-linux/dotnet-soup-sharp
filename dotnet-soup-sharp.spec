Summary:	C# Bindings for libsoup2.4
Summary(pl.UTF-8):	Wiązania C# do biblioteki libsoup2.4
Name:		dotnet-soup-sharp
Version:	2.42.2
Release:	2
License:	LGPL v3
Group:		Libraries
Source0:	https://github.com/xDarkice/soup-sharp/releases/download/%{version}/soup-sharp-%{version}.tar.gz
# Source0-md5:	f6376bd08ae5da39d6f7cf8998413e70
Patch0:		pkgconfig.patch
URL:		https://github.com/xDarkice/soup-sharp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp3-devel >= 2.99.2
BuildRequires:	libsoup-devel >= 2.42
BuildRequires:	libtool >= 2:2
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	monodoc >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	libsoup >= 2.42
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C# Bindings for libsoup2.4.

%description -l pl.UTF-8
Wiązania C# do biblioteki libsoup2.4.

%package devel
Summary:	C# Bindings for libsoup2.4 development files
Summary(pl.UTF-8):	Pliki programistyczne wiązań C# do biblioteki libsoup2.4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 2.6

%description devel
C# Bindings for libsoup2.4 development files.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań C# do biblioteki libsoup2.4.

%prep
%setup -q -n soup-sharp-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsoupsharpglue-%{version}.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoupsharpglue-%{version}.so
%{_prefix}/lib/mono/gac/soup-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/soup-sharp
%{_pkgconfigdir}/soup-sharp-2.4.pc
%{_prefix}/lib/monodoc/sources/soup-sharp-docs.*
