Name:		texlive-pst-cie
Version:	60959
Release:	2
Summary:	CIE color space
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-cie
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-cie is a PSTricks related package to show the different CIE
color spaces: Adobe, CIE, ColorMatch, NTSC, Pal-Secam,
ProPhoto, SMPTE, and sRGB.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-cie
%{_texmfdistdir}/tex/generic/pst-cie
%{_texmfdistdir}/dvips/pst-cie
%doc %{_texmfdistdir}/doc/generic/pst-cie

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
