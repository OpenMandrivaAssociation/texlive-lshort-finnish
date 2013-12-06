# revision 15878
# category Package
# catalog-ctan /info/lshort/finnish
# catalog-date 2008-12-13 17:42:32 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-lshort-finnish
Version:	20081213
Release:	3
Summary:	Finnish introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/finnish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-finnish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-finnish.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is the Finnish translation of Short Introduction to
LaTeX2e, with added coverage of Finnish typesetting rules.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/README
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/lyhyt2e.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/asiat.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/erikois.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/esipuhe.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/grafiikka.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/kiitokset.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/kirjallisuus.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/ladonta.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/llyhyt2e.sty
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/lyhyt2e.ind
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/lyhyt2e.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/matikka.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/otsikko.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/symbolit.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/typeset.tex
%doc %{_texmfdistdir}/doc/latex/lshort-finnish/src/viritys.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081213-2
+ Revision: 753469
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081213-1
+ Revision: 718889
- texlive-lshort-finnish
- texlive-lshort-finnish
- texlive-lshort-finnish
- texlive-lshort-finnish

