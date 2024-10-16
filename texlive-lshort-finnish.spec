Name:		texlive-lshort-finnish
Version:	15878
Release:	2
Summary:	Finnish introduction to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/finnish
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-finnish.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-finnish.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
