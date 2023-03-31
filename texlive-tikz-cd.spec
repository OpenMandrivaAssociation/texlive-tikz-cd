Name:		texlive-tikz-cd
Version:	59133
Release:	2
Summary:	Create commutative diagrams with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-cd
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-cd.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/tikz-cd
%{_texmfdistdir}/tex/latex/tikz-cd
%doc %{_texmfdistdir}/doc/latex/tikz-cd

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
