#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lensfun
Version  : 0.3.2
Release  : 32
URL      : https://github.com/lensfun/lensfun/archive/v0.3.2/lensfun-0.3.2.tar.gz
Source0  : https://github.com/lensfun/lensfun/archive/v0.3.2/lensfun-0.3.2.tar.gz
Summary  : database of photographic lenses and their characteristics
Group    : Development/Tools
License  : GPL-2.0
Requires: lensfun-bin = %{version}-%{release}
Requires: lensfun-data = %{version}-%{release}
Requires: lensfun-filemap = %{version}-%{release}
Requires: lensfun-lib = %{version}-%{release}
Requires: lensfun-license = %{version}-%{release}
Requires: lensfun-python = %{version}-%{release}
Requires: lensfun-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(glib-2.0)
BuildRequires : glib-dev
BuildRequires : libpng-dev
BuildRequires : python3
Patch1: 0001-Install-Python-libs-under-buildroot.patch

%description
This is a subset of the TRE regular expression library:
Home page: http://www.laurikari.net/tre/index.html

%package bin
Summary: bin components for the lensfun package.
Group: Binaries
Requires: lensfun-data = %{version}-%{release}
Requires: lensfun-license = %{version}-%{release}
Requires: lensfun-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the lensfun package.
Group: Default

%description filemap
filemap components for the lensfun package.


%package lib
Summary: lib components for the lensfun package.
Group: Libraries
Requires: lensfun-data = %{version}-%{release}
Requires: lensfun-license = %{version}-%{release}
Requires: lensfun-filemap = %{version}-%{release}

%description lib
lib components for the lensfun package.


%package license
Summary: license components for the lensfun package.
Group: Default

%description license
license components for the lensfun package.


%package python
Summary: python components for the lensfun package.
Group: Default
Requires: lensfun-python3 = %{version}-%{release}
Requires: lensfun-filemap = %{version}-%{release}

%description python
python components for the lensfun package.


%package python3
Summary: python3 components for the lensfun package.
Group: Default
Requires: python3-core

%description python3
python3 components for the lensfun package.


%prep
%setup -q -n lensfun-0.3.2
cd %{_builddir}/lensfun-0.3.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633755482
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%cmake .. -DBUILD_LENSTOOL=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake .. -DBUILD_LENSTOOL=ON
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake .. -DBUILD_LENSTOOL=ON
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1633755482
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lensfun
cp %{_builddir}/lensfun-0.3.2/libs/getopt/LICENSE %{buildroot}/usr/share/package-licenses/lensfun/2342b5a533465db8848a7b70870b9d15db736ab7
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build-avx512
%make_install_v4  || :
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/g-lensfun-update-data
/usr/bin/lensfun-add-adapter
/usr/bin/lensfun-update-data
/usr/bin/lenstool
/usr/share/clear/optimized-elf/bin*

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
/usr/lib64/liblensfun.so
/usr/lib64/pkgconfig/lensfun.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-lensfun

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblensfun.so.0.3.2
/usr/lib64/liblensfun.so.1
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lensfun/2342b5a533465db8848a7b70870b9d15db736ab7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
