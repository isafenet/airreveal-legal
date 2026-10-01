"""
AirReveal 2 on the home pages (branch `v2-site`, published when v2 ships): a new hero around the tagline
"Discover what's above or below you!", with the app's two halves side by side, then Follow Me (your flight),
Follow You (the aircraft around you), the Watch, widgets and Live Activities, the games (and their off
switch) and the three skins. Replaces the hero and the "New in 1.6" band; everything below stays.

Art is drawn in HTML and CSS (a radar, a route, a split-flap word), so no screenshots are needed until the
v2 capture runs. Same tone as `site_i18n.py`: tú / du / tu / você, French "vous".
"""

from __future__ import annotations

V2 = {}

V2["en"] = dict(
    hero=dict(eyebrow="AirReveal 2", h1="Discover what's above or below you!",
              p="Your own flight and the aircraft around you, in one app. Look down from your seat and AirReveal names the world below. Look up from the ground and it reveals the plane overhead.",
              cta1="See what's new", cta2="Download on the App Store",
              below=("Below you", "On your flight: what you're flying over, which side to look, and a camera that labels it."),
              above=("Above you", "On the ground: every aircraft around you on a radar and a live map. Tap one to reveal its flight, then follow it.")),
    me=dict(eyebrow="Follow Me · your flight", h2="The world beneath your wings.",
            p="Track your flight by GPS, even in airplane mode, and AirReveal names the mountains, cities and coastlines below as you pass them.",
            cards=[("Live", "Your position on a full-screen map, with no Wi-Fi needed on board."),
                   ("Plan", "Fly the whole route before you go and see what's coming."),
                   ("Window View", "Hold your phone to the window: landmarks outside are labelled on the camera picture."),
                   ("Best side to sit", "Left or right, which landmarks you'll see, and whether you'll catch the sunset."),
                   ("Flight HUD", "Altitude, speed and heading over the map, and on the Lock Screen."),
                   ("Journal", "Every trip kept, replayed from where you left off.")]),
    you=dict(eyebrow="Follow You · the sky around you", h2="Who's flying over?",
             p="Above You Now shows every aircraft around you on a radar and a live map, from free community flight data. Tap one to reveal it.",
             cards=[("Above You Now", "The nearest aircraft, how far and which way, with the radar turning to where you face."),
                    ("A live map, day and night", "Choose the map type; after sunset, Night Lights shows the streets lit below."),
                    ("Look up with the camera", "Point at the sky and the planes are marked, with an arrow to the one you follow."),
                    ("Aircraft cards", "A photo of that very aircraft, its route, height, speed and type."),
                    ("Follow it", "Keep a plane on the map up to 500 miles away, along the track it really flew."),
                    ("Helicopters too", "Shown with their own icon, from air ambulances to traffic watch.")]),
    beyond=dict(eyebrow="Beyond the app", h2="On your wrist, Lock Screen and Home Screen.",
                cards=[("Apple Watch", "The radar on your wrist, the plane you follow with a tap as it comes close, and your flight's progress."),
                       ("Widgets", "Above You on the Home Screen and the Lock Screen, with the radar."),
                       ("Live Activities", "The plane you follow on the Lock Screen and in the Dynamic Island: how far, which way, how high."),
                       ("Light on data", "Your Watch asks your iPhone, not the internet. Nothing is fetched while monitoring is off.")]),
    games=dict(eyebrow="Play along, or don't", h2="Games for both halves, and a switch to turn them off.",
               p="Every game works on your own flights and with the planes above you, all on your iPhone.",
               cards=[("Spotter's Logbook", "Every aircraft you reveal, with your personal bests: highest, fastest, closest."),
                      ("Bingo", "Discovery Bingo on your flight; Sky Bingo from home: a helicopter, a cargo flight, a jumbo."),
                      ("Daily challenges", "Three small ones a day, new at midnight."),
                      ("Rare finds and trivia", "Common, rare or legendary aircraft, and a quick question about each type.")],
               note="Not your thing? Turn games off in Settings › Games for a clean flight tracker. Your logbook stays."),
    skins=dict(eyebrow="Make it yours", h2="Three looks, one app.",
               p="Choose a skin and every screen follows it, from the Above You board to Settings. Each meets the same accessibility standards.",
               cards=[("Split-Flap", "The flip-letter departure boards: amber on black."),
                      ("Information Board", "A modern airport screen: white and gold on deep navy."),
                      ("AirReveal Classic", "Cards in your colour theme, in Light or Dark.")]),
)

V2["es"] = dict(
    hero=dict(eyebrow="AirReveal 2", h1="¡Descubre lo que hay encima o debajo de ti!",
              p="Tu propio vuelo y los aviones a tu alrededor, en una sola app. Mira hacia abajo desde tu asiento y AirReveal nombra el mundo de abajo. Mira hacia arriba desde tierra y te revela el avión que pasa.",
              cta1="Ver las novedades", cta2="Descargar en la App Store",
              below=("Debajo de ti", "En tu vuelo: lo que sobrevuelas, desde qué lado mirar y una cámara que lo señala."),
              above=("Encima de ti", "En tierra: todos los aviones a tu alrededor en un radar y un mapa en directo. Toca uno para ver su vuelo y síguelo.")),
    me=dict(eyebrow="Sígueme · tu vuelo", h2="El mundo bajo tus alas.",
            p="Sigue tu vuelo por GPS, incluso en modo avión, y AirReveal nombra las montañas, ciudades y costas de abajo a medida que pasas.",
            cards=[("En directo", "Tu posición en un mapa a pantalla completa, sin wifi a bordo."),
                   ("Planificar", "Recorre toda la ruta antes de salir y mira lo que viene."),
                   ("Vista de ventanilla", "Acerca el teléfono a la ventanilla: los lugares de fuera aparecen señalados en la imagen de la cámara."),
                   ("El mejor lado", "Izquierda o derecha, qué lugares verás y si pillarás la puesta de sol."),
                   ("HUD de vuelo", "Altitud, velocidad y rumbo sobre el mapa y en la pantalla de bloqueo."),
                   ("Diario", "Cada viaje guardado, para revivirlo desde donde lo dejaste.")]),
    you=dict(eyebrow="Te sigo · el cielo a tu alrededor", h2="¿Quién vuela por encima?",
             p="Encima de ti ahora muestra todos los aviones a tu alrededor en un radar y un mapa en directo, con datos de vuelo comunitarios y gratuitos. Toca uno para descubrirlo.",
             cards=[("Encima de ti ahora", "El avión más cercano, a qué distancia y en qué dirección, con el radar girando hacia donde miras."),
                    ("Un mapa en directo, de día y de noche", "Elige el tipo de mapa; al anochecer, Luces nocturnas muestra las calles iluminadas."),
                    ("Mira arriba con la cámara", "Apunta al cielo y los aviones aparecen marcados, con una flecha hacia el que sigues."),
                    ("Fichas de avión", "Una foto de ese mismo avión, su ruta, altura, velocidad y modelo."),
                    ("Síguelo", "Mantén un avión en el mapa hasta a 800 km, por la ruta que ha volado de verdad."),
                    ("También helicópteros", "Con su propio icono, de ambulancias aéreas a control de tráfico.")]),
    beyond=dict(eyebrow="Más allá de la app", h2="En tu muñeca, en la pantalla de bloqueo y en la de inicio.",
                cards=[("Apple Watch", "El radar en tu muñeca, un toque cuando se acerca el avión que sigues y el progreso de tu vuelo."),
                       ("Widgets", "Encima de ti en la pantalla de inicio y en la de bloqueo, con el radar."),
                       ("Actividades en directo", "El avión que sigues en la pantalla de bloqueo y en la Dynamic Island: a qué distancia, hacia dónde, a qué altura."),
                       ("Pocos datos", "Tu reloj pregunta a tu iPhone, no a internet. No se descarga nada con la vigilancia desactivada.")]),
    games=dict(eyebrow="Juega, o no", h2="Juegos para las dos mitades, y un interruptor para quitarlos.",
               p="Todos los juegos funcionan en tus vuelos y con los aviones que tienes encima, todo en tu iPhone.",
               cards=[("Cuaderno de avistamientos", "Cada avión que descubres, con tus récords: el más alto, el más rápido, el más cercano."),
                      ("Bingo", "Bingo de Descubrimientos en tu vuelo; Bingo del cielo desde casa: un helicóptero, un vuelo de carga, un jumbo."),
                      ("Retos diarios", "Tres pequeños al día, nuevos a medianoche."),
                      ("Hallazgos raros y curiosidades", "Aviones comunes, raros o legendarios, y una pregunta rápida sobre cada modelo.")],
               note="¿No es lo tuyo? Desactiva los juegos en Ajustes › Juegos y tendrás solo el seguimiento de vuelos. Tu cuaderno se queda."),
    skins=dict(eyebrow="A tu manera", h2="Tres estilos, una app.",
               p="Elige un estilo y todas las pantallas lo siguen, del panel Encima de ti a los ajustes. Todos cumplen los mismos estándares de accesibilidad.",
               cards=[("Paletas", "Los paneles de salidas de letras giratorias: ámbar sobre negro."),
                      ("Panel informativo", "Una pantalla de aeropuerto moderna: blanco y dorado sobre azul marino."),
                      ("AirReveal clásico", "Tarjetas con tu tema de color, en modo claro u oscuro.")]),
)

V2["fr"] = dict(
    hero=dict(eyebrow="AirReveal 2", h1="Découvrez ce qui est au-dessus ou en dessous de vous !",
              p="Votre propre vol et les avions autour de vous, dans une seule app. Regardez en bas depuis votre siège : AirReveal nomme le monde sous vos ailes. Regardez en haut depuis le sol : il révèle l'avion qui passe.",
              cta1="Voir les nouveautés", cta2="Télécharger dans l'App Store",
              below=("En dessous", "En vol : ce que vous survolez, de quel côté regarder, et une caméra qui le désigne."),
              above=("Au-dessus", "Au sol : tous les avions autour de vous sur un radar et une carte en direct. Touchez-en un pour révéler son vol, puis suivez-le.")),
    me=dict(eyebrow="Suivez-moi · votre vol", h2="Le monde sous vos ailes.",
            p="Suivez votre vol par GPS, même en mode avion : AirReveal nomme les montagnes, villes et côtes en dessous à mesure que vous passez.",
            cards=[("En direct", "Votre position sur une carte plein écran, sans Wi-Fi à bord."),
                   ("Planifier", "Parcourez toute la route avant de partir et voyez ce qui vous attend."),
                   ("Vue hublot", "Tenez votre téléphone au hublot : les sites dehors sont nommés sur l'image de la caméra."),
                   ("Le meilleur côté", "Gauche ou droite, les sites que vous verrez, et si vous aurez le coucher de soleil."),
                   ("HUD de vol", "Altitude, vitesse et cap sur la carte, et sur l'écran verrouillé."),
                   ("Journal", "Chaque voyage gardé, à revoir là où vous l'aviez laissé.")]),
    you=dict(eyebrow="Je vous suis · le ciel autour de vous", h2="Qui vole au-dessus ?",
             p="Au-dessus de vous affiche tous les avions autour de vous sur un radar et une carte en direct, grâce à des données de vol communautaires et gratuites. Touchez-en un pour le révéler.",
             cards=[("Au-dessus de vous", "L'avion le plus proche, à quelle distance et dans quelle direction, avec le radar tourné vers où vous regardez."),
                    ("Une carte en direct, jour et nuit", "Choisissez le type de carte ; après le coucher du soleil, Lumières de nuit montre les rues éclairées."),
                    ("Levez les yeux avec la caméra", "Visez le ciel : les avions sont marqués, avec une flèche vers celui que vous suivez."),
                    ("Fiches avion", "Une photo de cet avion précis, sa route, son altitude, sa vitesse et son modèle."),
                    ("Suivez-le", "Gardez un avion sur la carte jusqu'à 800 km, le long de la route qu'il a vraiment suivie."),
                    ("Les hélicoptères aussi", "Avec leur propre icône, du SAMU aérien à la surveillance du trafic.")]),
    beyond=dict(eyebrow="Au-delà de l'app", h2="Au poignet, sur l'écran verrouillé et l'écran d'accueil.",
                cards=[("Apple Watch", "Le radar au poignet, une touche quand l'avion suivi approche, et la progression de votre vol."),
                       ("Widgets", "Au-dessus de vous sur l'écran d'accueil et l'écran verrouillé, avec le radar."),
                       ("Activités en direct", "L'avion suivi sur l'écran verrouillé et dans la Dynamic Island : à quelle distance, dans quelle direction, à quelle altitude."),
                       ("Économe en données", "Votre montre interroge votre iPhone, pas Internet. Rien n'est chargé quand la surveillance est coupée.")]),
    games=dict(eyebrow="Jouez, ou pas", h2="Des jeux pour les deux côtés, et un interrupteur pour les couper.",
               p="Chaque jeu fonctionne pendant vos vols et avec les avions au-dessus de vous, tout sur votre iPhone.",
               cards=[("Carnet d'observation", "Chaque avion révélé, avec vos records : le plus haut, le plus rapide, le plus proche."),
                      ("Bingo", "Bingo des découvertes en vol ; Bingo du ciel depuis chez vous : un hélicoptère, un vol cargo, un jumbo."),
                      ("Défis du jour", "Trois petits défis par jour, renouvelés à minuit."),
                      ("Raretés et anecdotes", "Avions courants, rares ou légendaires, et une petite question sur chaque modèle.")],
               note="Pas pour vous ? Désactivez les jeux dans Réglages › Jeux pour un simple suivi de vols. Votre carnet reste."),
    skins=dict(eyebrow="À votre goût", h2="Trois styles, une app.",
               p="Choisissez un style : chaque écran le suit, du tableau Au-dessus de vous aux réglages. Tous respectent les mêmes normes d'accessibilité.",
               cards=[("Palettes", "Les tableaux de départs à palettes : ambre sur noir."),
                      ("Écran d'information", "Un écran d'aéroport moderne : blanc et or sur bleu nuit."),
                      ("AirReveal classique", "Des cartes aux couleurs de votre thème, en mode clair ou sombre.")]),
)

V2["de"] = dict(
    hero=dict(eyebrow="AirReveal 2", h1="Entdecke, was über oder unter dir ist!",
              p="Dein eigener Flug und die Flugzeuge um dich herum, in einer App. Schau von deinem Sitz nach unten, und AirReveal benennt die Welt darunter. Schau vom Boden nach oben, und es enthüllt das Flugzeug über dir.",
              cta1="Neuheiten ansehen", cta2="Im App Store laden",
              below=("Unter dir", "Auf deinem Flug: was du überfliegst, auf welcher Seite du schauen solltest, und eine Kamera, die es beschriftet."),
              above=("Über dir", "Am Boden: alle Flugzeuge um dich herum auf einem Radar und einer Live-Karte. Tippe auf eins, um seinen Flug zu sehen, und folge ihm.")),
    me=dict(eyebrow="Folge mir · dein Flug", h2="Die Welt unter deinen Flügeln.",
            p="Verfolge deinen Flug per GPS, auch im Flugmodus, und AirReveal benennt Berge, Städte und Küsten unter dir, während du sie überfliegst.",
            cards=[("Live", "Deine Position auf einer Vollbildkarte, ohne WLAN an Bord."),
                   ("Planen", "Fliege die ganze Route vorab ab und sieh, was kommt."),
                   ("Fensterblick", "Halte dein Handy ans Fenster: Sehenswürdigkeiten draußen werden im Kamerabild beschriftet."),
                   ("Die beste Seite", "Links oder rechts, welche Sehenswürdigkeiten du siehst und ob du den Sonnenuntergang erwischst."),
                   ("Flug-HUD", "Höhe, Geschwindigkeit und Kurs über der Karte und auf dem Sperrbildschirm."),
                   ("Reisetagebuch", "Jede Reise gespeichert, abgespielt ab dort, wo du aufgehört hast.")]),
    you=dict(eyebrow="Ich folge dir · der Himmel um dich", h2="Wer fliegt da drüber?",
             p="„Gerade über dir“ zeigt alle Flugzeuge um dich herum auf einem Radar und einer Live-Karte, mit kostenlosen Flugdaten aus der Community. Tippe auf eins, um es zu enthüllen.",
             cards=[("Gerade über dir", "Das nächste Flugzeug, wie weit und in welche Richtung, mit einem Radar, das sich mit dir dreht."),
                    ("Eine Live-Karte, Tag und Nacht", "Wähle den Kartentyp; nach Sonnenuntergang zeigt Nachtlichter die beleuchteten Straßen."),
                    ("Mit der Kamera nach oben", "Richte sie auf den Himmel: Flugzeuge werden markiert, mit einem Pfeil zu dem, dem du folgst."),
                    ("Flugzeugkarten", "Ein Foto genau dieses Flugzeugs, seine Route, Höhe, Geschwindigkeit und sein Typ."),
                    ("Folge ihm", "Behalte ein Flugzeug bis 800 km weit auf der Karte, entlang seiner tatsächlichen Flugspur."),
                    ("Auch Hubschrauber", "Mit eigenem Symbol, vom Rettungshubschrauber bis zur Verkehrsüberwachung.")]),
    beyond=dict(eyebrow="Über die App hinaus", h2="Am Handgelenk, auf dem Sperr- und Home-Bildschirm.",
                cards=[("Apple Watch", "Das Radar am Handgelenk, ein Tippen, wenn das verfolgte Flugzeug näher kommt, und der Fortschritt deines Flugs."),
                       ("Widgets", "„Über dir“ auf dem Home-Bildschirm und dem Sperrbildschirm, mit Radar."),
                       ("Live-Aktivitäten", "Das verfolgte Flugzeug auf dem Sperrbildschirm und in der Dynamic Island: wie weit, wohin, wie hoch."),
                       ("Datensparsam", "Deine Watch fragt dein iPhone, nicht das Internet. Ist die Überwachung aus, wird nichts geladen.")]),
    games=dict(eyebrow="Spiel mit – oder nicht", h2="Spiele für beide Seiten, und ein Schalter zum Ausschalten.",
               p="Jedes Spiel funktioniert auf deinen Flügen und mit den Flugzeugen über dir, alles auf deinem iPhone.",
               cards=[("Spotter-Logbuch", "Jedes enthüllte Flugzeug, mit deinen Bestwerten: am höchsten, am schnellsten, am nächsten."),
                      ("Bingo", "Entdeckungsbingo auf deinem Flug; Himmelsbingo von zu Hause: ein Hubschrauber, ein Frachtflug, ein Jumbo."),
                      ("Tägliche Herausforderungen", "Drei kleine pro Tag, neu um Mitternacht."),
                      ("Seltene Funde und Wissen", "Häufige, seltene oder legendäre Flugzeuge und eine kurze Frage zu jedem Typ.")],
               note="Nichts für dich? Schalte Spiele unter Einstellungen › Spiele aus, für reines Flugtracking. Dein Logbuch bleibt."),
    skins=dict(eyebrow="Ganz nach deinem Geschmack", h2="Drei Stile, eine App.",
               p="Wähle einen Stil, und jeder Bildschirm folgt ihm, von der Tafel „Über dir“ bis zu den Einstellungen. Alle erfüllen dieselben Barrierefreiheitsstandards.",
               cards=[("Fallblatt", "Die klassischen Fallblattanzeigen: Bernstein auf Schwarz."),
                      ("Anzeigetafel", "Ein moderner Flughafenbildschirm: Weiß und Gold auf tiefem Marineblau."),
                      ("AirReveal Klassisch", "Karten in deinem Farbthema, hell oder dunkel.")]),
)

V2["it"] = dict(
    hero=dict(eyebrow="AirReveal 2", h1="Scopri cosa c'è sopra o sotto di te!",
              p="Il tuo volo e gli aerei intorno a te, in un'unica app. Guarda giù dal tuo posto e AirReveal dà un nome al mondo sotto di te. Guarda su da terra e ti svela l'aereo che passa.",
              cta1="Scopri le novità", cta2="Scarica su App Store",
              below=("Sotto di te", "In volo: cosa stai sorvolando, da che lato guardare e una fotocamera che lo indica."),
              above=("Sopra di te", "A terra: tutti gli aerei intorno a te su un radar e una mappa in diretta. Toccane uno per svelarne il volo, poi seguilo.")),
    me=dict(eyebrow="Seguimi · il tuo volo", h2="Il mondo sotto le tue ali.",
            p="Segui il tuo volo via GPS, anche in modalità aereo, e AirReveal dà un nome a montagne, città e coste sotto di te mentre passi.",
            cards=[("Live", "La tua posizione su una mappa a schermo intero, senza Wi-Fi a bordo."),
                   ("Pianifica", "Percorri tutta la rotta prima di partire e guarda cosa ti aspetta."),
                   ("Vista dal finestrino", "Avvicina il telefono al finestrino: i luoghi fuori sono indicati sull'immagine della fotocamera."),
                   ("Il lato migliore", "Sinistra o destra, quali luoghi vedrai e se vedrai il tramonto."),
                   ("HUD di volo", "Altitudine, velocità e rotta sulla mappa e sulla schermata di blocco."),
                   ("Diario", "Ogni viaggio salvato, da rivivere da dove l'avevi lasciato.")]),
    you=dict(eyebrow="Ti seguo · il cielo intorno a te", h2="Chi sta volando sopra?",
             p="Sopra di te ora mostra tutti gli aerei intorno a te su un radar e una mappa in diretta, con dati di volo gratuiti della community. Toccane uno per svelarlo.",
             cards=[("Sopra di te ora", "L'aereo più vicino, a che distanza e in che direzione, con il radar che ruota verso dove guardi."),
                    ("Una mappa in diretta, giorno e notte", "Scegli il tipo di mappa; dopo il tramonto, Luci notturne mostra le strade illuminate."),
                    ("Guarda su con la fotocamera", "Punta al cielo e gli aerei vengono segnati, con una freccia verso quello che segui."),
                    ("Schede degli aerei", "Una foto proprio di quell'aereo, la sua rotta, quota, velocità e modello."),
                    ("Seguilo", "Tieni un aereo sulla mappa fino a 800 km, lungo la rotta che ha davvero volato."),
                    ("Anche gli elicotteri", "Con la loro icona, dall'eliambulanza al controllo del traffico.")]),
    beyond=dict(eyebrow="Oltre l'app", h2="Al polso, sulla schermata di blocco e su quella Home.",
                cards=[("Apple Watch", "Il radar al polso, un tocco quando l'aereo che segui si avvicina e l'avanzamento del tuo volo."),
                       ("Widget", "Sopra di te sulla schermata Home e su quella di blocco, con il radar."),
                       ("Attività in tempo reale", "L'aereo che segui sulla schermata di blocco e nella Dynamic Island: a che distanza, in che direzione, a che quota."),
                       ("Pochi dati", "Il tuo Watch chiede all'iPhone, non a Internet. Con il monitoraggio spento non si scarica nulla.")]),
    games=dict(eyebrow="Gioca, o no", h2="Giochi per entrambe le metà, e un interruttore per spegnerli.",
               p="Ogni gioco funziona sui tuoi voli e con gli aerei sopra di te, tutto sul tuo iPhone.",
               cards=[("Diario di avvistamenti", "Ogni aereo che sveli, con i tuoi record: il più alto, il più veloce, il più vicino."),
                      ("Bingo", "Bingo delle scoperte in volo; Bingo del cielo da casa: un elicottero, un volo cargo, un jumbo."),
                      ("Sfide del giorno", "Tre piccole al giorno, nuove a mezzanotte."),
                      ("Scoperte rare e curiosità", "Aerei comuni, rari o leggendari, e una domanda veloce su ogni modello.")],
               note="Non fa per te? Disattiva i giochi in Impostazioni › Giochi per un semplice tracker di voli. Il tuo diario resta."),
    skins=dict(eyebrow="A modo tuo", h2="Tre stili, un'app.",
               p="Scegli uno stile e ogni schermata lo segue, dal tabellone Sopra di te alle impostazioni. Tutti rispettano gli stessi standard di accessibilità.",
               cards=[("Palette", "I tabelloni delle partenze a palette: ambra su nero."),
                      ("Tabellone informativo", "Uno schermo aeroportuale moderno: bianco e oro su blu notte."),
                      ("AirReveal classico", "Schede nel tuo tema di colore, in modalità chiara o scura.")]),
)

V2["pt-br"] = dict(
    hero=dict(eyebrow="AirReveal 2", h1="Descubra o que está acima ou abaixo de você!",
              p="Seu próprio voo e os aviões ao seu redor, em um só app. Olhe para baixo do seu assento e o AirReveal dá nome ao mundo lá embaixo. Olhe para cima do chão e ele revela o avião que passa.",
              cta1="Ver as novidades", cta2="Baixar na App Store",
              below=("Abaixo de você", "No seu voo: o que você está sobrevoando, de que lado olhar e uma câmera que mostra tudo."),
              above=("Acima de você", "No chão: todos os aviões ao seu redor em um radar e um mapa ao vivo. Toque em um para revelar o voo e siga.")),
    me=dict(eyebrow="Me siga · seu voo", h2="O mundo sob suas asas.",
            p="Acompanhe seu voo por GPS, mesmo no modo avião, e o AirReveal dá nome às montanhas, cidades e litorais lá embaixo conforme você passa.",
            cards=[("Ao vivo", "Sua posição em um mapa de tela cheia, sem Wi-Fi a bordo."),
                   ("Planejar", "Percorra toda a rota antes de ir e veja o que vem pela frente."),
                   ("Vista da janela", "Encoste o celular na janela: os lugares lá fora aparecem marcados na imagem da câmera."),
                   ("O melhor lado", "Esquerda ou direita, quais lugares você vai ver e se vai pegar o pôr do sol."),
                   ("HUD de voo", "Altitude, velocidade e rumo sobre o mapa e na Tela Bloqueada."),
                   ("Diário", "Cada viagem guardada, para rever de onde você parou.")]),
    you=dict(eyebrow="Te sigo · o céu ao seu redor", h2="Quem está voando por cima?",
             p="Acima de você agora mostra todos os aviões ao seu redor em um radar e um mapa ao vivo, com dados de voo gratuitos da comunidade. Toque em um para revelá-lo.",
             cards=[("Acima de você agora", "O avião mais próximo, a que distância e em que direção, com o radar girando para onde você olha."),
                    ("Um mapa ao vivo, dia e noite", "Escolha o tipo de mapa; depois do pôr do sol, Luzes noturnas mostra as ruas iluminadas."),
                    ("Olhe para cima com a câmera", "Aponte para o céu e os aviões aparecem marcados, com uma seta para o que você segue."),
                    ("Fichas de avião", "Uma foto daquele mesmo avião, sua rota, altura, velocidade e modelo."),
                    ("Siga", "Mantenha um avião no mapa a até 800 km, pela rota que ele realmente voou."),
                    ("Helicópteros também", "Com ícone próprio, do resgate aéreo ao monitoramento do trânsito.")]),
    beyond=dict(eyebrow="Além do app", h2="No pulso, na Tela Bloqueada e na Tela de Início.",
                cards=[("Apple Watch", "O radar no pulso, um toque quando o avião que você segue se aproxima e o progresso do seu voo."),
                       ("Widgets", "Acima de você na Tela de Início e na Tela Bloqueada, com o radar."),
                       ("Atividades ao Vivo", "O avião que você segue na Tela Bloqueada e na Dynamic Island: a que distância, para onde, a que altura."),
                       ("Poucos dados", "Seu relógio pergunta ao iPhone, não à internet. Nada é baixado com o monitoramento desligado.")]),
    games=dict(eyebrow="Jogue, ou não", h2="Jogos para os dois lados, e um botão para desligar.",
               p="Todos os jogos funcionam nos seus voos e com os aviões acima de você, tudo no seu iPhone.",
               cards=[("Diário de avistamentos", "Cada avião revelado, com seus recordes: o mais alto, o mais rápido, o mais próximo."),
                      ("Bingo", "Bingo de Descobertas no voo; Bingo do céu em casa: um helicóptero, um voo de carga, um jumbo."),
                      ("Desafios diários", "Três pequenos por dia, novos à meia-noite."),
                      ("Achados raros e curiosidades", "Aviões comuns, raros ou lendários, e uma pergunta rápida sobre cada modelo.")],
               note="Não curte? Desative os jogos em Ajustes › Jogos para ter só o rastreamento de voos. Seu diário continua."),
    skins=dict(eyebrow="Do seu jeito", h2="Três estilos, um app.",
               p="Escolha um estilo e todas as telas seguem, do painel Acima de você aos ajustes. Todos atendem aos mesmos padrões de acessibilidade.",
               cards=[("Painel de palhetas", "Os painéis de partidas de palhetas: âmbar sobre preto."),
                      ("Painel informativo", "Uma tela de aeroporto moderna: branco e dourado sobre azul-marinho."),
                      ("AirReveal clássico", "Cartões no seu tema de cor, no modo claro ou escuro.")]),
)


# Drawn art (no text a reader needs: hidden from assistive tech).
RADAR = ('<div class="v2-radar" aria-hidden="true"><span class="ring r1"></span><span class="ring r2"></span><span class="ring r3"></span>'
         '<span class="sweep"></span><span class="me"></span>'
         '<span class="blip b1">✈</span><span class="blip b2">✈</span><span class="blip b3">✈</span><span class="blip b4">✈</span></div>')
ROUTE = ('<svg class="v2-route" viewBox="0 0 320 160" aria-hidden="true"><path d="M10 140 Q160 -20 310 120" fill="none" stroke="#ffb23d" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>'
         '<circle cx="10" cy="140" r="6" fill="#fff"/><circle cx="310" cy="120" r="6" fill="#fff"/>'
         '<text x="150" y="58" font-size="26" fill="#fff" transform="rotate(20 150 58)">✈</text>'
         '<circle cx="90" cy="88" r="5" fill="#55d7d3"/><circle cx="215" cy="70" r="5" fill="#55d7d3"/></svg>')


def flap_word(word: str) -> str:
    return '<span class="v2-flap" aria-hidden="true">' + "".join(f"<b>{c if c != ' ' else '&nbsp;'}</b>" for c in word.upper()) + "</span>"


def render(lang: str, esc, download_href: str, base: str) -> str:
    """The v2 hero and sections. `base` is "" on English pages, "../" on translated ones."""
    v = V2[lang]
    h = v["hero"]
    cards = lambda items, cls="v2-card": "".join(f'<article class="{cls}"><h3>{esc(a)}</h3><p>{esc(b)}</p></article>' for a, b in items)
    section = lambda sid, s, inner, band="": (
        f'<section class="section v2 {band}" id="{sid}"><div class="wrap"><div class="section-head"><div class="eyebrow">{esc(s["eyebrow"])}</div>'
        f'<h2>{esc(s["h2"])}</h2>' + (f'<p>{esc(s["p"])}</p>' if s.get("p") else "") + f'</div>{inner}</div></section>')
    skins = v["skins"]["cards"]
    skin_cards = (
        f'<article class="v2-skin v2-skin-flap">{flap_word("ABOVE YOU")}<h3>{esc(skins[0][0])}</h3><p>{esc(skins[0][1])}</p></article>'
        f'<article class="v2-skin v2-skin-board"><div class="v2-board-row" aria-hidden="true"><span>✈ BAW507</span><span>12,000 ft</span><em>CLOSE</em></div><h3>{esc(skins[1][0])}</h3><p>{esc(skins[1][1])}</p></article>'
        f'<article class="v2-skin v2-skin-classic"><div class="v2-classic-chip" aria-hidden="true">✈ 3 mi NE</div><h3>{esc(skins[2][0])}</h3><p>{esc(skins[2][1])}</p></article>')
    return (
        f'<section class="v2-hero"><div class="wrap"><div class="eyebrow">{esc(h["eyebrow"])}</div><h1>{esc(h["h1"])}</h1><p class="v2-lede">{esc(h["p"])}</p>'
        f'<div class="cta-row"><a class="btn btn-primary" href="#follow-me">{esc(h["cta1"])}</a><a class="btn btn-secondary" href="{download_href}">{esc(h["cta2"])}</a></div>'
        f'<div class="v2-halves"><article class="v2-half below">{ROUTE}<h2>{esc(h["below"][0])}</h2><p>{esc(h["below"][1])}</p></article>'
        f'<article class="v2-half above">{RADAR}<h2>{esc(h["above"][0])}</h2><p>{esc(h["above"][1])}</p></article></div></div></section>'
        + section("follow-me", v["me"], f'<div class="v2-grid">{cards(v["me"]["cards"])}</div>')
        + section("follow-you", v["you"], f'<div class="v2-grid">{cards(v["you"]["cards"])}</div>', "v2-night")
        + section("beyond", v["beyond"], f'<div class="v2-grid v2-grid-4">{cards(v["beyond"]["cards"])}</div>')
        + section("games", v["games"], f'<div class="v2-grid v2-grid-4">{cards(v["games"]["cards"])}</div><p class="v2-note">{esc(v["games"]["note"])}</p>', "v2-night")
        + section("skins", v["skins"], f'<div class="v2-grid v2-grid-3">{skin_cards}</div>')
    )


CSS = """
/* v2: AirReveal 2 hero and sections */
.v2-hero{background:radial-gradient(circle at 80% 10%,#123a6b 0,#071b33 45%,#03070f 100%);color:#fff;padding:78px 0 70px;overflow:hidden}
.v2-hero h1{font-size:clamp(44px,6.4vw,86px);line-height:.98;letter-spacing:-.045em;margin:14px 0 22px;max-width:15ch}
.v2-lede{font-size:21px;color:#dcecff;max-width:720px}
.v2-halves{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:44px}
.v2-half{border-radius:28px;padding:26px;border:1px solid #ffffff22;background:linear-gradient(160deg,#0f2c52,#06142a)}
.v2-half.above{background:linear-gradient(160deg,#10261c,#050b0a)}
.v2-half h2{font-size:30px;margin:14px 0 6px;letter-spacing:-.02em}
.v2-half p{color:#d6e4f2;margin:0}
.v2-route{width:100%;height:auto;max-height:170px;display:block}
.v2-radar{position:relative;width:170px;height:170px;margin:0 auto;border-radius:50%;background:radial-gradient(circle,#16301f,#060d09 70%);overflow:hidden}
.v2-radar .ring{position:absolute;border:1px solid #7fd38a55;border-radius:50%;inset:0}
.v2-radar .r2{inset:28px}.v2-radar .r3{inset:56px}
.v2-radar .sweep{position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 0deg,#7fd38a55,transparent 70deg);animation:v2spin 4s linear infinite}
.v2-radar .me{position:absolute;left:50%;top:50%;width:10px;height:10px;margin:-5px;border-radius:50%;background:#7fd38a}
.v2-radar .blip{position:absolute;color:#ffb23d;font-size:16px}
.v2-radar .b1{left:62%;top:22%;transform:rotate(30deg)}.v2-radar .b2{left:24%;top:58%;transform:rotate(200deg);color:#e8e3d4}
.v2-radar .b3{left:70%;top:62%;transform:rotate(120deg);color:#e8e3d4}.v2-radar .b4{left:34%;top:26%;transform:rotate(80deg);color:#e8e3d4}
@keyframes v2spin{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.v2-radar .sweep{animation:none}}
.v2-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.v2-grid-4{grid-template-columns:repeat(4,1fr)}.v2-grid-3{grid-template-columns:repeat(3,1fr)}
.v2-card{background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px}
.v2-card h3{margin:0 0 8px;font-size:21px}.v2-card p{margin:0;color:var(--muted)}
.v2:not(.v2-night) .eyebrow{color:#0b6f6d}
.v2-night{background:linear-gradient(160deg,#060d1a,#0b2340);color:#fff}
.v2-night .section-head p{color:#d5e7f7}
.v2-night .v2-card{background:#0f1d33;border-color:#ffffff1f}
.v2-night .v2-card h3{color:#fff}.v2-night .v2-card p{color:#c9d6e6}
.v2-note{margin-top:22px;color:#d5e7f7;font-weight:600}
.v2-skin{border-radius:24px;padding:24px;min-height:220px}
.v2-skin h3{margin:16px 0 6px;font-size:22px}.v2-skin p{margin:0}
.v2-skin-flap{background:#0b0d10;border:6px solid #2b2f35;color:#e8e3d4}.v2-skin-flap p{color:#b9bec5}
.v2-flap{display:inline-flex;gap:2px;flex-wrap:wrap}
.v2-flap b{display:inline-grid;place-items:center;min-width:20px;height:30px;padding:0 2px;border-radius:3px;background:linear-gradient(#262a30 0 49%,#000 49% 51%,#1d2126 51%);color:#ffb23d;font:700 17px/1 ui-monospace,Menlo,monospace}
.v2-skin-board{background:linear-gradient(180deg,#121a2b,#0a0f1c);border:4px solid #3a414d;color:#fff}.v2-skin-board p{color:#c3cbda}
.v2-board-row{display:flex;justify-content:space-between;gap:8px;padding:10px 12px;border-radius:10px;background:#0d1422;font-weight:700}
.v2-board-row em{font-style:normal;color:#38d39f}
.v2-skin-classic{background:linear-gradient(140deg,#0b7373,#0d2b40);color:#fff}.v2-skin-classic p{color:#e2f1f3}
.v2-classic-chip{display:inline-block;padding:8px 14px;border-radius:999px;background:#00000040;font-weight:700}
@media(max-width:900px){.v2-halves{grid-template-columns:1fr}.v2-grid,.v2-grid-4,.v2-grid-3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.v2-grid,.v2-grid-4,.v2-grid-3{grid-template-columns:1fr}.v2-hero{padding-top:48px}}
"""
