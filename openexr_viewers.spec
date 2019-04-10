#
# Conditional build:
%bcond_with	cg	# use NVIDIA Cg compiler
#
Summary:	Simple still OpenEXR image viewer
Summary(pl.UTF-8):	Prosta przeglądarka nieruchomych obrazów OpenEXR
Name:		openexr_viewers
Version:	2.2.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/openexr/%{name}-%{version}.tar.gz
# Source0-md5:	f68d5cb2c09420f26c967a6411c463a9
Patch0:		%{name}-am.patch
URL:		http://www.openexr.com/
BuildRequires:	OpenEXR-devel >= 2.2.1
BuildRequires:	OpenGL-devel
%{?with_cg:BuildRequires:	OpenGL-glut-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
%{?with_cg:BuildRequires:	cg-devel}
BuildRequires:	fltk-gl-devel >= 1.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	openexr_ctl-devel >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	OpenEXR >= 2.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
exrdisplay is a simple still image viewer that optionally applies
color transforms to OpenEXR images, using CTL.

%if %{with cg}
playexr is a program that plays back OpenEXR image sequences,
optionally with CTL support, applying rendering and display
transforms.
%endif

%description -l pl.UTF-8
exrdisplay to prosta przeglądarka nieruchomych obrazów opcjonalnie
stosująca na obrazach OpenEXR przekształcenia kolorów przy użyciu CTL.

%if %{with cg}
playexr to program odtwarzający sekwencje obrazów OpenEXR z opcjonalną
obsługą CTL i stosowaniem przekształceń renderingu i wyświetlania.
%endif

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless currently
%{__rm} $RPM_BUILD_ROOT%{_includedir}/OpenEXR/OpenEXR_ViewersConfig.h
# already packaged as doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/OpenEXR_Viewers-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README doc/OpenEXRViewers.pdf
%attr(755,root,root) %{_bindir}/exrdisplay
%if %{with cg}
%attr(755,root,root) %{_bindir}/playexr
%endif
