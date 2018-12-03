%global fontname nerd-hack
%global fontconf 60-%{fontname}.conf

Name:		  %{fontname}-fonts
Version:	2.0.0
Release:	1%{?dist}
Summary:	A typeface designed for source code
License:	SIL
URL:		  http://sourcefoundry.org/hack/
Source0:	https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/Hack.zip
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	   noarch
BuildRequires: fontpackages-devel
Requires:	     fontpackages-filesystem

%description
A typeface designed for source code

%prep
%setup -q -c %{name}-%{version}

%build
# No build necessary for now
# Cosider in the future generate through sources ?

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Mon Dec 03 2018 Sergey Korolev <korolev.srg@gmail.com> - 2.0.0-1
- Initial release
