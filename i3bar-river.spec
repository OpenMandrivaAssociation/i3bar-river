%global debug_package %{nil}

Name:		i3bar-river
Version:	1.1.0
Release:	1
URL:		https://github.com/MaxVerevkin/i3bar-river
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	A Solution to your Wayland Wallpaper Woes
License:	GPL-3.0
Group:		Wayland/Utils

BuildRequires:	cargo
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)

%description
%summary

%prep
%autosetup -n %{name}-%{version} -a1
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release --verbose


%install
install -Dpm755 target/release/i3bar-river %{buildroot}%{_bindir}/i3bar-river

%files
%license LICENSE
%doc README.md
%{_bindir}/i3bar-river
