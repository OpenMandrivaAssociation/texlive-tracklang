Name:		texlive-tracklang
Version:	65263
Release:	1
Summary:	Language and dialect tracker
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tracklang
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tracklang.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tracklang.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tracklang.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tracklang package is provided for package developers who
want a simple interface to find out which languages the user
has requested through packages such as babel or polyglossia.
This package does not provide any translations! Its purpose is
simply to track which languages have been requested by the
user. Generic TeX code is in tracklang.tex for non-LaTeX users.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tracklang
%{_texmfdistdir}/tex/latex/tracklang
%{_texmfdistdir}/tex/generic/tracklang
%doc %{_texmfdistdir}/doc/generic/tracklang

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
