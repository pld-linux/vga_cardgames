Summary:	Card games for the Linux VGA console
Summary(fr):	Jeux de cartes pour la console Linux
Summary(es):	Juego de carta de baraja para consola
Summary(pl):	Gry karciane dla linuksowek konsoli VGA
Summary(pt_BR):	Jogo de carta de baralho para console
Summary(tr):	Konsolda oynanan kaðýt oyunlarý
Name:		vga_cardgames
Version:	1.3.1
Release:	11
License:	distributable
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}.tgz
Patch0:		%{name}-misc.patch
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
%ifarch ppc
BuildRequires:	svgalib4ggi-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} alpha ppc

%description
A number of various card games for the Linux VGA console, including
Klondike, 'Oh Hell', Solitaire, and Spider, as well as some other
popular time-wasters :)

%description -l de
Eine Reihe verschiedener Kartenspiele für die Linux-Konsole, u.a.
Klondike, Oh Hell, Solitaire und Spider, plus andere beliebte Zeit-
vergeuder ...

%description -l es
Varios juegos de baraja para Linux, incluye Klondike, "Oh Hell",
Solitaire, y Spider, así como otros populares pasatiempos :)

%description -l fr
Divers jeux de cartes en mode console pour Linux, dont Klondike, 'Oh
Hell', Solitaire, et Spider, ainsi que d'autres passe-temps populaires
:).

%description -l pl
Wiele ró¿nych gier karcianych dla linuksowej konsoli VGA, w tym
Klondike, "Oh Hell", Solitaire i Spider, oraz inne popularne gry do
tracenia czasu.

%description -l pt_BR
Vários jogos de carta para o Linux, incluindo Klondike, "Oh Hell",
Solitaire, e Spider, assim como outros populares passatempos :)

%description -l tr
Metin ekranda oynanan çeþitli kaðýt oyunlarý. Klondike, Solitaire,
Spider gibi fal oyunlarý bu pakette yer alýr.

%prep
%setup -q -n vga_cardgames
%patch -p1

%build
%{__make} CC="%{__cc}" OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vga_klondike
%attr(755,root,root) %{_bindir}/vga_ohhell
%attr(755,root,root) %{_bindir}/vga_solitaire
%attr(755,root,root) %{_bindir}/vga_spider
%{_libdir}/games/Vga16font8x16.cards
%{_libdir}/games/Cards56x80
