Summary:	Metapackage for MATE desktop environment
Name:		task-mate
Version:	1.26.0
Release:	2
Group:		Graphical desktop/GNOME
License:	GPLv2+
BuildArch:	noarch

# mate core
Requires:	%{name}-minimal
Requires:	mate-applets
Requires:	mate-calc
Requires:	mate-common
Requires:	mate-desktop
Requires:	mate-icon-theme-faenza
Requires:	mate-indicator-applet
Requires:	mate-media
Requires:	mate-menus
Requires:	mate-screensaver
Requires:	mate-sensors-applet
Requires:	mate-system-monitor
Requires:	mate-terminal
Requires:	mate-user-share
Requires:	mate-utils
Requires:	mozo
# MATE theme
Requires:	mate-themes
# MATE apps
Requires:	atril
Requires:	caja
Requires:	engrampa
Requires:	eom
Requires:	pluma
# other useful apps
#Requires:	gnome-keyring
Requires:	lightdm
Requires:	lightdm-gtk3-greeter
# optional
Recommends:	mate-user-guide
Recommends:	mate-netbook

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the MATE.

%files

#---------------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed for MATE desktop
Group:		Graphical desktop/GNOME

Requires:	caja
# MD mate made the switch, this really should be pulled by each pkg contains gschemas
Requires:	gsettings-desktop-schemas
Requires:	mate-backgrounds
Requires:	mate-control-center
Requires:	mate-icon-theme
Requires:	mate-notification-daemon
Requires:	mate-panel
Requires:	mate-polkit
Requires:	mate-power-manager
Requires:	mate-session-manager
Requires:	marco
#Requires:	preload
Requires:	task-pulseaudio
Requires:	task-x11
Requires:	libwnck3
Requires:	networkmanager-applet

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal MATE desktop environment.

%files minimal
