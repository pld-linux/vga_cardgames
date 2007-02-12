Summary:	Card games for the Linux VGA console
Summary(fr.UTF-8):	Jeux de cartes pour la console Linux
Summary(es.UTF-8):	Juego de carta de baraja para consola
Summary(pl.UTF-8):	Gry karciane dla linuksowej konsoli VGA
Summary(pt_BR.UTF-8):	Jogo de carta de baralho para console
Summary(tr.UTF-8):	Konsolda oynanan kağıt oyunları
Name:		vga_cardgames
Version:	1.3.1
Release:	14
License:	distributable
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/solitaires/%{name}-%{version}.tgz
# Source0-md5:	550fa167ff4798ccb6c9419732397e0f
Patch0:		%{name}-misc.patch
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A number of various card games for the Linux VGA console, including
Klondike, 'Oh Hell', Solitaire, and Spider, as well as some other
popular time-wasters :)

%description -l de.UTF-8
Eine Reihe verschiedener Kartenspiele für die Linux-Konsole, u.a.
Klondike, Oh Hell, Solitaire und Spider, plus andere beliebte Zeit-
vergeuder ...

%description -l es.UTF-8
Varios juegos de baraja para Linux, incluye Klondike, "Oh Hell",
Solitaire, y Spider, así como otros populares pasatiempos :)

%description -l fr.UTF-8
Divers jeux de cartes en mode console pour Linux, dont Klondike, 'Oh
Hell', Solitaire, et Spider, ainsi que d'autres passe-temps populaires
:).

%description -l pl.UTF-8
Wiele różnych gier karcianych dla linuksowej konsoli VGA, w tym
Klondike, "Oh Hell", Solitaire i Spider, oraz inne popularne gry do
tracenia czasu.

%description -l pt_BR.UTF-8
Vários jogos de carta para o Linux, incluindo Klondike, "Oh Hell",
Solitaire, e Spider, assim como outros populares passatempos :)

%description -l tr.UTF-8
Metin ekranda oynanan çeşitli kağıt oyunları. Klondike, Solitaire,
Spider gibi fal oyunları bu pakette yer alır.

%prep
%setup -q -n vga_cardgames
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}" \
	LIBDIR=%{_libdir}/games

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}/games

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
