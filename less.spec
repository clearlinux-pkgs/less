#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : less
Version  : 520
Release  : 19
URL      : http://www.greenwoodsoftware.com/less/less-520.tar.gz
Source0  : http://www.greenwoodsoftware.com/less/less-520.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0 GPL-3.0+
Requires: less-bin
Requires: less-doc
BuildRequires : ncurses-dev
Patch1: exec-configure.patch

%description
Less, version 520
This is the distribution of less, version 520, released 11 Sep 2017.
This program is part of the GNU project (http://www.gnu.org).

%package bin
Summary: bin components for the less package.
Group: Binaries

%description bin
bin components for the less package.


%package doc
Summary: doc components for the less package.
Group: Documentation

%description doc
doc components for the less package.


%prep
%setup -q -n less-520
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506449157
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1506449157
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
