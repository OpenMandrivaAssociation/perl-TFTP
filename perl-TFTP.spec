%define module  TFTP
%define name	perl-%{module}
%define	modprefix TFTP/GSM

%define version 1
%define beta 0b3

%define release %mkrel 0.%{beta}.2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	TFTP Client class
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.%{beta}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(444,root,root,755)
%doc README
%{perl_vendorlib}/%{module}.pm
%{_mandir}/man3/*

