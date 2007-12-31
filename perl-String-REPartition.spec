#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	REPartition
Summary:	String::REPartition - generates a regex to partition a data set
Summary(pl.UTF-8):	String::REPartition - generowanie wyrażenia regularnego do podziału zbioru danych
Name:		perl-String-REPartition
Version:	1.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/AVIF/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11b32cffa1b03fc825b467261fa6b883
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports a single function - make_partition_re. It takes as
its first argument a number between 0 and 1, representing a
percentage, and as its second argument a reference to a list of
strings. It returns a regular expression which is guaranteed to match
the percentage of the strings in the list represented by the number in
the first argument. More importantly, the regex returned is guaranteed
*not* to match the rest of the string in the list. That is, if the
inputs were '0.6' and a reference to a list of 100 strings, the
returned regex would match 60 of the strings in the list and not match
the other 40.

%description -l pl.UTF-8
Ten moduł eksportuje jedną funkcję - make_partition_re. Przyjmuje ona
jako pierwszy argument liczbę między 0 a 1, reprezentującą podział
procentowy, a jako drugi argument referencję do listy łańcuchów.
Zwraca wyrażenie regularne, które gwarantuje dopasowanie do takiej
części łańcuchów w liście, jaka została podana jako pierwszy argument.
Co więcej, zwrócone wyrażenie gwarantuje, że *nie* będzie pasować do
reszty łańcuchów z listy. To oznacza, że np. jeśli parametrami były
0.6 i referencja do listy 100 łańcuchów, zwrócone wyrażenie regularne
będzie pasowało do 60 łańcuchów i nie pasowało do pozostałych 40.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
