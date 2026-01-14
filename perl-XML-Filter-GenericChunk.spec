#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	XML
%define		pnam	Filter-GenericChunk
Summary:	XML::Filter::GenericChunk - base class for SAX filters parsing WellBallanced chunks
Summary(pl.UTF-8):	XML::Filter::GenericChunk - klasa bazowa dla filtrów SAX analizujących fragmenty WellBallanced
Name:		perl-XML-Filter-GenericChunk
Version:	0.07
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fd8f693dad2a239578cf135ce6d1b38d
URL:		http://search.cpan.org/dist/XML-Filter-GenericChunk/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 1.40
BuildRequires:	perl-XML-LibXML-SAX
BuildRequires:	perl-XML-SAX
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Filter::GenericChunk is inherited by XML::SAX::Base.
XML::Filter::GenericChunk itself is an abstract class, therefore as a
filter it will not result any useful output. If you need a simple
Chunk filter for your SAX pipeline, check XML::Filter::CharacterChunk
which is shipped with this module.

%description -l pl.UTF-8
XML::Filter::GenericChunk jest dziedziczona przez XML::SAX::Base. Sama
XML::Filter::GenericChunk jest abstrakcyjną klasą, więc jako filtr nie
da żadnego przydatnego wyjścia. Jeśli potrzebny jest prosty filtr
Chunk dla potoków SAX, można sprawdzić klasę
XML::Filter::CharacterChunk dołączoną do tego modułu.

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
%{perl_vendorlib}/XML/*/*.pm
%{_mandir}/man3/*
