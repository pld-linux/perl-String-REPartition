#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	REPartition
Summary:	String::REPartition - Generates a regex to partition a data set
Summary(pl):	String::REPartition - generowanie wyra¿enia regularnego do podzia³u zbioru danych
Name:		perl-String-REPartition
Version:	1.0
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1d287fdbe6d471798f7a29ab668e816e
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl
Ten modu³ eksportuje jedn± funkcjê - make_partition_re. Przyjmuje ona
jako pierwszy argument liczbê miêdzy 0 a 1, reprezentuj±c± podzia³
procentowy, a jako drugi argument referencjê do listy ³añcuchów.
Zwraca wyra¿enie regularne, które gwarantuje dopasowanie do takiej
czê¶ci ³añcuchów w li¶cie, jaka zosta³a podana jako pierwszy argument.
Co wiêcej, zwrócone wyra¿enie gwarantuje, ¿e *nie* bêdzie pasowaæ do
reszty ³añcuchów z listy. To oznacza, ¿e np. je¶li parametrami by³y
0.6 i referencja do listy 100 ³añcuchów, zwrócone wyra¿enie regularne
bêdzie pasowa³o do 60 ³añcuchów i nie pasowa³o do pozosta³ych 40.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
