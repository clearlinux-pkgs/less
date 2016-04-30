#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : less
Version  : 481
Release  : 15
URL      : http://www.greenwoodsoftware.com/less/less-481.tar.gz
Source0  : http://www.greenwoodsoftware.com/less/less-481.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0 GPL-3.0+
Requires: less-bin
Requires: less-doc
BuildRequires : ncurses-dev
Patch1: exec-configure.patch

%description
Less, version 481
This is the distribution of less, version 481, released 31 Aug 2015.
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
%setup -q -n less-481
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
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
