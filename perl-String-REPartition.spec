#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	REPartition
Summary:	String::REPartition - Generates a regex to partition a data set
Summary(pl):	String::REPartition - generowanie wyra�enia regularnego do podzia�u zbioru danych
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
Ten modu� eksportuje jedn� funkcj� - make_partition_re. Przyjmuje ona
jako pierwszy argument liczb� mi�dzy 0 a 1, reprezentuj�c� podzia�
procentowy, a jako drugi argument referencj� do listy �a�cuch�w.
Zwraca wyra�enie regularne, kt�re gwarantuje dopasowanie do takiej
cz�ci �a�cuch�w w li�cie, jaka zosta�a podana jako pierwszy argument.
Co wi�cej, zwr�cone wyra�enie gwarantuje, �e *nie* b�dzie pasowa� do
reszty �a�cuch�w z listy. To oznacza, �e np. je�li parametrami by�y
0.6 i referencja do listy 100 �a�cuch�w, zwr�cone wyra�enie regularne
b�dzie pasowa�o do 60 �a�cuch�w i nie pasowa�o do pozosta�ych 40.

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
