%define realname   Wx-Perl-ProcessStream
%define version    0.11
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    use std handles of process via wx events
Source:     http://www.cpan.org/modules/by-module/Wx/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Wx)

BuildArch: noarch

%description
This module provides the STDOUT, STDERR and exit codes of asynchronously
running processes via events. It may be used for long running or blocking
processes that provide periodic updates on state via STDOUT. Simple IPC is
possible via STDIN.

Do not use this module simply to collect the output of another process. For
that, it is much simpler to do:

    my ($status, $output) = Wx::ExecuteStdout( 'perl -e"print qq($_\n) for(@INC);"' );

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# Do not make test because they need gtk display
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
