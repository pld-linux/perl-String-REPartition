#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	REPartition
Summary:	String::REPartition - Generates a regex to partition a data set
#Summary(pl):	
Name:		perl-String-REPartition
Version:	1.0
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports a single function -- make_partition_re.  It takes as
its first argument a number between 0 and 1, representing a percentage,
and as its second argument a reference to a list of strings.  It returns
a regular expression which is guaranteed to match the percentage of the
strings in the list represented by the number in the first argument.
More importantly, the regexreturned is guaranteed *not* to match the
rest of the string in the list.  That is, if the inputs were '0.6' and
a reference to a list of 100 strings, the returned regex would match 60
of the strings in the list and not match the other 40.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
