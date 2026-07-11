%global tl_name tikz-cd
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-cd
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The general-purpose drawing package TikZ can be used to typeset
commutative diagrams and other kinds of mathematical pictures,
generating high-quality results. The purpose of this package is to make
the process of creation of such diagrams easier by providing a
convenient set of macros and reasonable default settings. This package
also includes an arrow tip library that match closely the arrows present
in the Computer Modern typeface.

