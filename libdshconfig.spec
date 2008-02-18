%define	name	libdshconfig
%define shortname dshconfig
%define	version	0.20.13
%define	release	 %mkrel 2
%define	major	1
%define	libname	%mklibname %shortname %{major}
%define develname %mklibname %shortname -d


Summary:	Library for parsing dsh-style configuration files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPL
Group:		Development/Other
Url:		http://www.netfort.gr.jp/~dancer/software/downloads/#libdshconfig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%package -n	%libname
Summary:	Library for parsing dsh-style configuration files
Group:		Development/Other

%package -n	%develname
Summary:	Library for parsing dsh-style configuration files devel
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description
Library for parsing dsh-style configuration files. Required by dsh and 
other applications.

%description -n %libname
Library for parsing dsh-style configuration files. Required by dsh and 
other applications.

%description -n	%develname
Library for parsing dsh-style configuration files. Required by dsh and 
other applications. Devel rpm.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS INSTALL COPYING NEWS README ChangeLog tests/*
%{_libdir}/libdshconfig.so.%{major}
%{_libdir}/libdshconfig.so.%{major}.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/libdshconfig.so
%{_libdir}/libdshconfig.a
%{_libdir}/libdshconfig.la
%{_includedir}/libdshconfig.h

