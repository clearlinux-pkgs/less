#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : less
Version  : 633
Release  : 43
URL      : https://www.greenwoodsoftware.com/less/less-633.tar.gz
Source0  : https://www.greenwoodsoftware.com/less/less-633.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: less-bin = %{version}-%{release}
Requires: less-license = %{version}-%{release}
Requires: less-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : ncurses-dev
BuildRequires : pcre2-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: exec-configure.patch

%description
This is the source code distribution of "less".
This program is part of the GNU project (https://www.gnu.org).

%package bin
Summary: bin components for the less package.
Group: Binaries
Requires: less-license = %{version}-%{release}

%description bin
bin components for the less package.


%package license
Summary: license components for the less package.
Group: Default

%description license
license components for the less package.


%package man
Summary: man components for the less package.
Group: Default

%description man
man components for the less package.


%prep
%setup -q -n less-633
cd %{_builddir}/less-633
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689800854
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-regex=pcre2
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1689800854
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/less
cp %{_builddir}/less-%{version}/COPYING %{buildroot}/usr/share/package-licenses/less/31a3d460bb3c7d98845187c716a30db81c44b615 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/less/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/less.1
/usr/share/man/man1/lessecho.1
/usr/share/man/man1/lesskey.1
