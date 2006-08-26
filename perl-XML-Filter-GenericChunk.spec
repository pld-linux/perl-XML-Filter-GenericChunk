#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-GenericChunk
Summary:	XML::Filter::GenericChunk - base class for SAX filters parsing WellBallanced chunks
Summary(pl):	XML::Filter::GenericChunk - klasa bazowa dla filtrów SAX analizuj±cych fragmenty WellBallanced
Name:		perl-XML-Filter-GenericChunk
Version:	0.06
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2177460740dd40690caf42000ab07a3b
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
XML::Filter::GenericChunk itself is an abstract class, therefore as
a filter it will not result any useful output. If you need a simple
Chunk filter for your SAX pipeline, check XML::Filter::CharacterChunk
which is shipped with this module.

%description -l pl
XML::Filter::GenericChunk jest dziedziczona przez XML::SAX::Base.
Sama XML::Filter::GenericChunk jest abstrakcyjn± klas±, wiêc jako
filtr nie da ¿adnego przydatnego wyj¶cia. Je¶li potrzebny jest prosty
filtr Chunk dla potoków SAX, mo¿na sprawdziæ klasê
XML::Filter::CharacterChunk do³±czon± do tego modu³u.

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
