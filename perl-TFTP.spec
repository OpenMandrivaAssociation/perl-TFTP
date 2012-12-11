%define module  TFTP
%define	modprefix TFTP/GSM
%define beta 0b3

Name:		perl-%{module}
Version:	1
Release:	0.%{beta}.4
Summary:	TFTP Client class
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.%{beta}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

BuildRequires:	perl-devel
BuildArch:	noarch

%description 
TFTP is a class implementing a simple TFTP client in Perl as described
in RFC783.

%prep
%setup -q -n %{module}-%{version}.%{beta}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(444,root,root,755)
%doc README
%{perl_vendorlib}/%{module}.pm
%{_mandir}/man3/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1-0.0b3.3mdv2010.0
+ Revision: 430604
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1-0.0b3.2mdv2009.0
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1-0.0b3.2mdv2008.0
+ Revision: 87060
- rebuild


* Tue Sep 05 2006 Olivier Blin <blino@mandriva.com> 1-0.0b3.1mdv2007.0
- initial Mandriva release

