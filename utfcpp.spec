#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : utfcpp
Version  : 3.2.2
Release  : 6
URL      : https://github.com/nemtrif/utfcpp/archive/v3.2.2/utfcpp-3.2.2.tar.gz
Source0  : https://github.com/nemtrif/utfcpp/archive/v3.2.2/utfcpp-3.2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSL-1.0
Requires: utfcpp-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
# UTF8-CPP: UTF-8 with C++ in a Portable Way
## Introduction
C++ developers miss an easy and portable way of handling Unicode encoded strings. The original C++ Standard (known as C++98 or C++03) is Unicode agnostic. C++11 provides some support for Unicode on core language and library level: u8, u, and U character and string literals, char16_t and char32_t character types, u16string and u32string library classes, and codecvt support for conversions between Unicode encoding forms. In the meantime, developers use third party libraries like ICU, OS specific capabilities, or simply roll out their own solutions.

%package dev
Summary: dev components for the utfcpp package.
Group: Development
Provides: utfcpp-devel = %{version}-%{release}
Requires: utfcpp = %{version}-%{release}

%description dev
dev components for the utfcpp package.


%package license
Summary: license components for the utfcpp package.
Group: Default

%description license
license components for the utfcpp package.


%prep
%setup -q -n utfcpp-3.2.2
cd %{_builddir}/utfcpp-3.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668550730
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DUTF8_TESTS=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1668550730
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/utfcpp
cp %{_builddir}/utfcpp-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/utfcpp/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/utf8cpp/utf8.h
/usr/include/utf8cpp/utf8/checked.h
/usr/include/utf8cpp/utf8/core.h
/usr/include/utf8cpp/utf8/cpp11.h
/usr/include/utf8cpp/utf8/cpp17.h
/usr/include/utf8cpp/utf8/unchecked.h
/usr/lib64/cmake/utf8cpp/utf8cppConfig.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/utfcpp/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
