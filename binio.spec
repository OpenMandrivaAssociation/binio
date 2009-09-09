%define name binio
%define version 1.4
%define release %mkrel 6
%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define staticname %mklibname -d -s %name
%define fname libbinio

Summary: Binary I/O stream class library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/libbinio/%{fname}-%{version}.tar.bz2
URL: http://libbinio.sourceforge.net
License: LGPLv2+
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

%package -n %libname
Summary: Shared library for lib%name
Group: System/Libraries

%description -n %libname
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

This package contains the shared library needed to run applications
based on %name.

%package -n %develname
Summary: Development files for lib%name
Group: Development/C++
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Requires: %libname = %version
Obsoletes: %mklibname -d %name 1

%description -n %develname
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

This package contains C++ header files, the shared library symlink and
the developer documentation for %name.

%package -n %staticname
Summary: Static library for lib%name
Group: Development/C++
Requires: %develname = %version
Provides: lib%name-static-devel = %version-%release
Obsoletes: %mklibname -s -d %name 1

%description -n %staticname
The binary I/O stream class library presents a platform-independent
way to access binary data streams in C++.

The library is hardware independent in the form that it transparently
converts between the different forms of machine-internal binary data
representation.

It further employs no special I/O protocol and can be used on
arbitrary binary data sources.

This package contains the static library of %name.

%prep
%setup -q -n %fname-%version

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%post -n %develname
%_install_info libbinio.info

%postun -n %develname
%_remove_install_info libbinio.info

%files -n %libname
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%_libdir/libbinio.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_includedir/libbinio/
%_libdir/*.so
%_libdir/*.la
%_infodir/*.info*
%_libdir/pkgconfig/*

%files -n %staticname
%defattr(-,root,root)
%_libdir/*.a


