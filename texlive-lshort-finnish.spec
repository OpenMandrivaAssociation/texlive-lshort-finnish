%global tl_name lshort-finnish
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Finnish introduction to LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/finnish
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-finnish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-finnish.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the Finnish translation of Short Introduction to LaTeX2e, with
added coverage of Finnish typesetting rules.

