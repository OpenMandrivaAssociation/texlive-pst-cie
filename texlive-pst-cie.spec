%global tl_name pst-cie
%global tl_revision 60959

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.06b
Release:	%{tl_revision}.1
Summary:	CIE color space
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-cie
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-cie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
pst-cie is a PSTricks related package to show the different CIE color
spaces: Adobe, CIE, ColorMatch, NTSC, Pal-Secam, ProPhoto, SMPTE, and
sRGB.

