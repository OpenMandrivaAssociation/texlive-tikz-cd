# revision 33126
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-cd
# catalog-date 2014-03-08 06:15:50 +0100
# catalog-license gpl3
# catalog-version 0.9b
Name:		texlive-tikz-cd
Version:	0.9e
Release:	2
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-cd
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The general-purpose drawing package TiKZ can be used to typeset
commutative diagrams and other kinds of mathematical pictures,
generating high-quality results. The purpose of this package is
to make the process of creation of such diagrams easier by
providing a convenient set of macros and reasonable default
settings. This package also includes an arrow tip library that
match closely the arrows present in the Computer Modern
typeface.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tikz-cd/tikzlibrarycd.code.tex
%{_texmfdistdir}/tex/latex/tikz-cd/tikz-cd.sty
%doc %{_texmfdistdir}/doc/latex/tikz-cd/README
%doc %{_texmfdistdir}/doc/latex/tikz-cd/tikz-cd-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-cd/tikz-cd-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
