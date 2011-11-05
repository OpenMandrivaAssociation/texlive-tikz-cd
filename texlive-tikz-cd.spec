# revision 24370
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-cd
# catalog-date 2011-10-23 20:08:22 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-tikz-cd
Version:	0.2
Release:	1
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-cd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The general-purpose drawing package TiKZ can be used to typeset
commutative diagrams and other kinds of mathematical pictures,
generating high-quality results. The purpose of this package is
to make the process of creation of such diagrams easier by
providing a convenient set of macros and reasonable default
settings. This package also includes an arrow tip library that
match closely the arrows present in the Computer Modern
typeface.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-cd/tikz-cd.sty
%doc %{_texmfdistdir}/doc/latex/tikz-cd/README
%doc %{_texmfdistdir}/doc/latex/tikz-cd/tikz-cd-doc.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-cd/tikz-cd-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
