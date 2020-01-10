Summary:	Metapackage for MATE desktop environment
Name:		task-mate
Version:	1.22.2
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

# mate core
Requires:	%{name}-minimal >= %{version}
Requires:	mate-applets >= %{version}
Requires:	mate-calc >= %{version}
Requires:	mate-common >= %{version}
Requires:	mate-desktop >= %{version}
Requires:	mate-icon-theme-faenza >= %{version}
Requires:	mate-indicator-applet >= %{version}
Requires:	mate-media >= %{version}
Requires:	mate-menus >= %{version}
Requires:	mate-screensaver >= %{version}
Requires:	mate-sensors-applet >= %{version}
Requires:	mate-system-monitor >= %{version}
Requires:	mate-terminal >= %{version}
Requires:	mate-user-share >= %{version}
Requires:	mate-utils >= %{version}
Requires:	mozo >= %{version}
# MATE theme
Requires:	mate-themes
# MATE apps
Requires:	atril
Requires:	caja
Requires:	engrampa
Requires:	eom
Requires:	pluma
# other useful apps
#Requires:	gnome-keyring >= %{version}
Requires:	lightdm
Requires:	lightdm-gtk3-greeter
# optional
Suggests:	mate-user-guide >= %{version}
Suggests:	mate-netbook >= %{version}

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the MATE.

%files

#---------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for MATE desktop
Group:		Graphical desktop/GNOME

Requires:	caja >= %{version}
# MD mate made the switch, this really should be pulled by each pkg contains gschemas
Requires:	gsettings-desktop-schemas
Requires:	mate-backgrounds >= %{version}
Requires:	mate-control-center >= %{version}
Requires:	mate-icon-theme >= %{version}
Requires:	mate-notification-daemon >= %{version}
Requires:	mate-panel >= %{version}
Requires:	mate-polkit >= %{version}
Requires:	mate-power-manager >= %{version}
Requires:	mate-session-manager >= %{version}
Requires:	marco >= %{version}
Requires:	preload
Requires:	task-pulseaudio
Requires:	task-x11
Requires:	libwnck3

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal MATE desktop environment.

%files minimal
