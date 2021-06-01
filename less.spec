#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : less
Version  : 589
Release  : 37
URL      : http://www.greenwoodsoftware.com/less/less-589.tar.gz
Source0  : http://www.greenwoodsoftware.com/less/less-589.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0 GPL-3.0+
Requires: less-bin = %{version}-%{release}
Requires: less-license = %{version}-%{release}
Requires: less-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : pcre2-dev
Patch1: exec-configure.patch

%description
This is the source code distribution of "less".
This program is part of the GNU project (http://www.gnu.org).

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
%setup -q -n less-589
cd %{_builddir}/less-589
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622560240
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-regex=pcre2
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1622560240
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/less
cp %{_builddir}/less-589/COPYING %{buildroot}/usr/share/package-licenses/less/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/less-589/LICENSE %{buildroot}/usr/share/package-licenses/less/0319a1deb4e0dea715d8210caf27c2ae6795ebeb
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
/usr/share/package-licenses/less/0319a1deb4e0dea715d8210caf27c2ae6795ebeb
/usr/share/package-licenses/less/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/less.1
/usr/share/man/man1/lessecho.1
/usr/share/man/man1/lesskey.1
