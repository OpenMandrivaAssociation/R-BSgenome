%bcond_without bootstrap
%global packname  BSgenome
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.22.0
Release:          1
Summary:          Infrastructure for Biostrings-based genome data packages
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-IRanges R-GenomicRanges R-Biostrings 
%if %{with bootstrap}
Requires:         R-RUnit R-Biobase 
%else
Requires:         R-RUnit R-BSgenome.Celegans.UCSC.ce2 R-BSgenome.Hsapiens.UCSC.hg19 R-SNPlocs.Hsapiens.dbSNP.20100427 R-hgu95av2probe R-Biobase 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-IRanges R-GenomicRanges R-Biostrings
%if %{with bootstrap}
BuildRequires:    R-RUnit R-Biobase 
%else
BuildRequires:    R-RUnit R-BSgenome.Celegans.UCSC.ce2 R-BSgenome.Hsapiens.UCSC.hg19 R-SNPlocs.Hsapiens.dbSNP.20100427 R-hgu95av2probe R-Biobase 
%endif

%description
Infrastructure shared by all the Biostrings-based genome data packages

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/BSgenomeDataPkg-template
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
