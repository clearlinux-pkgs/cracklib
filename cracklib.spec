#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cracklib
Version  : 2.9.6
Release  : 34
URL      : https://github.com/cracklib/cracklib/releases/download/cracklib-2.9.6/cracklib-2.9.6.tar.gz
Source0  : https://github.com/cracklib/cracklib/releases/download/cracklib-2.9.6/cracklib-2.9.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0+ LGPL-2.1
Requires: cracklib-bin
Requires: cracklib-lib
Requires: cracklib-data
Requires: cracklib-locales
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : python3-dev
Patch1: cve-2016-6318.patch

%description
This package is an updated/modernized distribution of CrackLib as
previously release by Alec Muffett. Pretty much all of the files have
been modified in some way to allow for this modernization and to
apply numerous bug fixes and patches.

%package bin
Summary: bin components for the cracklib package.
Group: Binaries
Requires: cracklib-data

%description bin
bin components for the cracklib package.


%package data
Summary: data components for the cracklib package.
Group: Data

%description data
data components for the cracklib package.


%package dev
Summary: dev components for the cracklib package.
Group: Development
Requires: cracklib-lib
Requires: cracklib-bin
Requires: cracklib-data
Provides: cracklib-devel

%description dev
dev components for the cracklib package.


%package lib
Summary: lib components for the cracklib package.
Group: Libraries
Requires: cracklib-data

%description lib
lib components for the cracklib package.


%package locales
Summary: locales components for the cracklib package.
Group: Default

%description locales
locales components for the cracklib package.


%prep
%setup -q -n cracklib-2.9.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519052496
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
%configure --disable-static --with-default-dict-path=/usr/share/cracklib/pw_dict
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1519052496
rm -rf %{buildroot}
%make_install
%find_lang cracklib
## make_install_append content
chmod 755 util/cracklib-format util/cracklib-packer
util/cracklib-format dicts/cracklib-small | util/cracklib-packer %{buildroot}%{_datadir}/cracklib/pw_dict
gzip -9 %{buildroot}%{_datadir}/cracklib/pw_dict.pwd
rm %{buildroot}%{_datadir}/cracklib/cracklib-small
rm %{buildroot}%{_datadir}/cracklib/cracklib.magic
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cracklib-check
/usr/bin/cracklib-format
/usr/bin/cracklib-packer
/usr/bin/cracklib-unpacker
/usr/bin/create-cracklib-dict

%files data
%defattr(-,root,root,-)
/usr/share/cracklib/pw_dict.hwm
/usr/share/cracklib/pw_dict.pwd.gz
/usr/share/cracklib/pw_dict.pwi

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libcrack.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcrack.so.2
/usr/lib64/libcrack.so.2.9.0

%files locales -f cracklib.lang
%defattr(-,root,root,-)

