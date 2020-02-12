#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lensfun
Version  : 0.3.2
Release  : 13
URL      : https://sourceforge.net/projects/lensfun/files/0.3.2/lensfun-0.3.2.tar.gz
Source0  : https://sourceforge.net/projects/lensfun/files/0.3.2/lensfun-0.3.2.tar.gz
Summary  : database of photographic lenses and their characteristics
Group    : Development/Tools
License  : GPL-2.0
Requires: lensfun-bin = %{version}-%{release}
Requires: lensfun-data = %{version}-%{release}
Requires: lensfun-lib = %{version}-%{release}
Requires: lensfun-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : glib-dev
BuildRequires : libpng-dev
BuildRequires : python3

%description
This is a subset of the TRE regular expression library:
Home page: http://www.laurikari.net/tre/index.html

%package bin
Summary: bin components for the lensfun package.
Group: Binaries
Requires: lensfun-data = %{version}-%{release}
Requires: lensfun-license = %{version}-%{release}

%description bin
bin components for the lensfun package.


%package data
Summary: data components for the lensfun package.
Group: Data

%description data
data components for the lensfun package.


%package dev
Summary: dev components for the lensfun package.
Group: Development
Requires: lensfun-lib = %{version}-%{release}
Requires: lensfun-bin = %{version}-%{release}
Requires: lensfun-data = %{version}-%{release}
Provides: lensfun-devel = %{version}-%{release}
Requires: lensfun = %{version}-%{release}

%description dev
dev components for the lensfun package.


%package lib
Summary: lib components for the lensfun package.
Group: Libraries
Requires: lensfun-data = %{version}-%{release}
Requires: lensfun-license = %{version}-%{release}

%description lib
lib components for the lensfun package.


%package license
Summary: license components for the lensfun package.
Group: Default

%description license
license components for the lensfun package.


%prep
%setup -q -n lensfun-0.3.2
cd %{_builddir}/lensfun-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581532509
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DBUILD_LENSTOOL=ON
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DBUILD_LENSTOOL=ON
make  %{?_smp_mflags}  VERBOSE=1
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
%cmake .. -DBUILD_LENSTOOL=ON
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581532509
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lensfun
cp %{_builddir}/lensfun-0.3.2/libs/getopt/LICENSE %{buildroot}/usr/share/package-licenses/lensfun/2342b5a533465db8848a7b70870b9d15db736ab7
pushd clr-build-avx512
%make_install_avx512  || :
popd
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/g-lensfun-update-data
/usr/bin/haswell/avx512_1/lenstool
/usr/bin/haswell/lenstool
/usr/bin/lensfun-add-adapter
/usr/bin/lensfun-update-data
/usr/bin/lenstool

%files data
%defattr(-,root,root,-)
/usr/share/lensfun/version_1/6x6.xml
/usr/share/lensfun/version_1/actioncams.xml
/usr/share/lensfun/version_1/compact-canon.xml
/usr/share/lensfun/version_1/compact-casio.xml
/usr/share/lensfun/version_1/compact-fujifilm.xml
/usr/share/lensfun/version_1/compact-kodak.xml
/usr/share/lensfun/version_1/compact-konica-minolta.xml
/usr/share/lensfun/version_1/compact-leica.xml
/usr/share/lensfun/version_1/compact-nikon.xml
/usr/share/lensfun/version_1/compact-olympus.xml
/usr/share/lensfun/version_1/compact-panasonic.xml
/usr/share/lensfun/version_1/compact-pentax.xml
/usr/share/lensfun/version_1/compact-ricoh.xml
/usr/share/lensfun/version_1/compact-samsung.xml
/usr/share/lensfun/version_1/compact-sigma.xml
/usr/share/lensfun/version_1/compact-sony.xml
/usr/share/lensfun/version_1/contax.xml
/usr/share/lensfun/version_1/generic.xml
/usr/share/lensfun/version_1/mil-canon.xml
/usr/share/lensfun/version_1/mil-fujifilm.xml
/usr/share/lensfun/version_1/mil-nikon.xml
/usr/share/lensfun/version_1/mil-olympus.xml
/usr/share/lensfun/version_1/mil-panasonic.xml
/usr/share/lensfun/version_1/mil-pentax.xml
/usr/share/lensfun/version_1/mil-samsung.xml
/usr/share/lensfun/version_1/mil-samyang.xml
/usr/share/lensfun/version_1/mil-sigma.xml
/usr/share/lensfun/version_1/mil-sony.xml
/usr/share/lensfun/version_1/mil-tamron.xml
/usr/share/lensfun/version_1/mil-zeiss.xml
/usr/share/lensfun/version_1/misc.xml
/usr/share/lensfun/version_1/rf-leica.xml
/usr/share/lensfun/version_1/slr-canon.xml
/usr/share/lensfun/version_1/slr-hasselblad.xml
/usr/share/lensfun/version_1/slr-konica-minolta.xml
/usr/share/lensfun/version_1/slr-leica.xml
/usr/share/lensfun/version_1/slr-nikon.xml
/usr/share/lensfun/version_1/slr-olympus.xml
/usr/share/lensfun/version_1/slr-panasonic.xml
/usr/share/lensfun/version_1/slr-pentax.xml
/usr/share/lensfun/version_1/slr-ricoh.xml
/usr/share/lensfun/version_1/slr-samsung.xml
/usr/share/lensfun/version_1/slr-samyang.xml
/usr/share/lensfun/version_1/slr-schneider.xml
/usr/share/lensfun/version_1/slr-sigma.xml
/usr/share/lensfun/version_1/slr-soligor.xml
/usr/share/lensfun/version_1/slr-sony.xml
/usr/share/lensfun/version_1/slr-tamron.xml
/usr/share/lensfun/version_1/slr-tokina.xml
/usr/share/lensfun/version_1/slr-ussr.xml
/usr/share/lensfun/version_1/slr-vivitar.xml
/usr/share/lensfun/version_1/slr-zeiss.xml
/usr/share/lensfun/version_1/timestamp.txt

%files dev
%defattr(-,root,root,-)
/usr/include/lensfun/lensfun.h
/usr/lib64/haswell/avx512_1/liblensfun.so
/usr/lib64/haswell/liblensfun.so
/usr/lib64/liblensfun.so
/usr/lib64/pkgconfig/lensfun.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/liblensfun.so.0.3.2
/usr/lib64/haswell/avx512_1/liblensfun.so.1
/usr/lib64/haswell/liblensfun.so.0.3.2
/usr/lib64/haswell/liblensfun.so.1
/usr/lib64/liblensfun.so.0.3.2
/usr/lib64/liblensfun.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lensfun/2342b5a533465db8848a7b70870b9d15db736ab7
