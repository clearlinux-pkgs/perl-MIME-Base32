#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Base32
Version  : 1.303
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MIME-Base32-1.303.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MIME-Base32-1.303.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmime-base32-perl/libmime-base32-perl_1.303-1.debian.tar.xz
Summary  : 'Base32 encoder and decoder'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MIME-Base32-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
MIME::Base32 - Base32 encoder and decoder
# SYNOPSIS
#!/usr/bin/env perl
use strict;
use warnings;
use MIME::Base32;

%package dev
Summary: dev components for the perl-MIME-Base32 package.
Group: Development
Provides: perl-MIME-Base32-devel = %{version}-%{release}

%description dev
dev components for the perl-MIME-Base32 package.


%package license
Summary: license components for the perl-MIME-Base32 package.
Group: Default

%description license
license components for the perl-MIME-Base32 package.


%prep
%setup -q -n MIME-Base32-1.303
cd ..
%setup -q -T -D -n MIME-Base32-1.303 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/MIME-Base32-1.303/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MIME-Base32
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-MIME-Base32/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-MIME-Base32/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/MIME/Base32.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Base32.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MIME-Base32/LICENSE
/usr/share/package-licenses/perl-MIME-Base32/deblicense_copyright
