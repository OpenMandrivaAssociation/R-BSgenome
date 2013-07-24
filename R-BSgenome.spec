#%bcond_with internet
%bcond_with bootstrap
%global packname  BSgenome
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.28.0
Release:          1
Summary:          Infrastructure for Biostrings-based genome data packages
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/BSgenome_1.28.0.tar.gz
Requires:         R-methods R-IRanges R-GenomicRanges R-Biostrings R-RUnit
Requires:         R-Biobase
%if %{without bootstrap}
Requires:         R-BSgenome.Celegans.UCSC.ce2 R-BSgenome.Hsapiens.UCSC.hg19
Requires:         R-SNPlocs.Hsapiens.dbSNP.20100427 R-hgu95av2probe
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-IRanges R-GenomicRanges R-Biostrings R-RUnit R-Biobase
%if %{without bootstrap}
BuildRequires:    R-BSgenome.Celegans.UCSC.ce2 R-BSgenome.Hsapiens.UCSC.hg19
BuildRequires:    R-SNPlocs.Hsapiens.dbSNP.20100427 R-hgu95av2probe
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
    %if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
    %endif
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/BSgenomeDataPkg-template
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help


%changelog
* Wed Feb 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.22.0-2
+ Revision: 778889
- Rebuild with proper dependencies

* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.22.0-1
+ Revision: 775794
- Import R-BSgenome
- Import R-BSgenome


