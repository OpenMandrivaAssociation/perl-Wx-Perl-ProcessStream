%define upstream_name    Wx-Perl-ProcessStream
%define upstream_version 0.30

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    use std handles of process via wx events
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive::Tar)
BuildRequires: perl(Wx)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides the STDOUT, STDERR and exit codes of asynchronously
running processes via events. It may be used for long running or blocking
processes that provide periodic updates on state via STDOUT. Simple IPC is
possible via STDIN.

Do not use this module simply to collect the output of another process. For
that, it is much simpler to do:

    my ($status, $output) = Wx::ExecuteStdout( 'perl -e"print qq($_\n) for(@INC);"' );

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
