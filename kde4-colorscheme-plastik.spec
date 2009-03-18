%define		kdever	4.2.1
%define		theme	plastik
Summary:	KDE Color Scheme KDE4
Name:		kde4-colorscheme-%{theme}
Version:	0.1.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/CONTENT/content-files/89804-Plastik.colors
# Source0-md5:	a2e9e93e5f3aa9e1e091b4adfe33d0da
URL:		http://kde-look.org/content/show.php/Plastik?content=89804
Requires:	kde4-kdebase-workspace >= %{kdever}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE 4 port of KDE 3 Plastik color scheme.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/color-schemes
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/apps/color-schemes/Plastik.colors

%files
%defattr(644,root,root,755)
%{_datadir}/apps/color-schemes/*.colors

%clean
rm -rf $RPM_BUILD_ROOT
