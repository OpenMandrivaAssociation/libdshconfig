%define	name	libdshconfig
%define	version	0.20.11
%define	release	1mdk
%define	major	0
%define	lib_name	%mklibname %name %{major}


Summary:	Library for parsing dsh-style configuration files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		Development/Other
Url:		http://www.netfort.gr.jp/~dancer/software/downloads/#libdshconfig
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%package -n	%{name}-devel
Summary:	Library for parsing dsh-style configuration files devel
Group:		Development/Other

%description
Library for parsing dsh-style configuration files. Required by dsh and 
other applications.

%description -n	%{name}-devel
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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL COPYING NEWS README ChangeLog tests/*
%{_libdir}/libdshconfig.so
%{_libdir}/libdshconfig.so.1
%{_libdir}/libdshconfig.so.1.0.0

%files -n %{name}-devel
%defattr(-,root,root)
%{_libdir}/libdshconfig.a
%{_libdir}/libdshconfig.la
%{_includedir}/libdshconfig.h

