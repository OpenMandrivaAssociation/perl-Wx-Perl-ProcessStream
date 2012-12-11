%define upstream_name    Wx-Perl-ProcessStream
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Use std handles of process via wx events
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Wx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Wx)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Do not make test because they need gtk display
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 657860
- rebuild for updated spec-helper

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1
+ Revision: 636639
- update to new version 0.30

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 612274
- update to new version 0.29

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 594311
- update to new version 0.28

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 512601
- update to 0.27

* Fri Feb 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.1
+ Revision: 511455
- update to 0.26

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 510974
- update to 0.25

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.1
+ Revision: 486377
- update to 0.24

* Tue Jan 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.1
+ Revision: 486309
- update to 0.23

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 461030
- update to 0.22

* Tue Sep 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 450782
- update to 0.20

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 449991
- update to 0.18

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 449780
- update to 0.17

* Sat Sep 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 449445
- adding missing buildrequires:
- update to 0.16

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 401881
- rebuild using %%perl_convert_version

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.11-1mdv2009.0
+ Revision: 277582
- import perl-Wx-Perl-ProcessStream


