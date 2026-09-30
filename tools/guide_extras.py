"""Extra sections for the "What am I flying over?" guide, in every site language.

Example routes, the four quick-start steps and three more FAQs. The English page is hand-written HTML, so
`build_localized_site.py` writes these sections into it between the GUIDE-EXTRAS markers; the other languages
render them from here. Button names are only used where the app's wording in that language is known (the
support page's My Flights / Download / Always); otherwise the step is described without quoting a button.
Example routes are hedged on purpose: real routings change with weather and air traffic.
"""

EXTRAS = {
    "en": dict(
        ex_h="What you might see: two example routes",
        ex_p="Routes change with the weather and air traffic, so treat these as examples of a typical routing, not a promise.",
        examples=[
            ("London to Rome", "After crossing the English Channel, a typical routing heads across eastern France. On a clear day you may see the Alps, around Mont Blanc, before the flight reaches the Italian coast near Genoa and follows it south towards Rome."),
            ("London to New York", "Flights often cross Ireland before several hours over the North Atlantic. Landfall is usually over Atlantic Canada, such as Newfoundland or Nova Scotia, and the last part of the flight often follows the coast of New England towards Long Island."),
        ],
        ex_note="AirReveal follows your actual flight with GPS, so it names what's really below you, whichever way your flight goes.",
        steps_h="How to see what's below you with AirReveal",
        steps=[
            "<strong>Add your flight.</strong> On the Flight screen, tap Create New Flight, choose From and To, and pick Live Trip.",
            "<strong>Download it.</strong> In <strong>My Flights</strong>, swipe your flight to the right and tap <strong>Download</strong> while you still have Wi-Fi.",
            "<strong>Allow location.</strong> When your Live Trip starts, choose <strong>Always</strong> so AirReveal keeps tracking while your phone is locked.",
            "<strong>Look out of the window.</strong> Switch to airplane mode when the crew asks; GPS keeps working. AirReveal names what's below and ahead, and which side to look.",
        ],
        faq=[
            ("How far can you see from a plane?", "From a typical cruising height of about 11 km (35,000 feet), the horizon is roughly 370 km (230 miles) away. In practice haze and cloud usually limit what you can make out to much less, so coastlines, mountain ranges and big cities are the easiest things to spot."),
            ("Why can't my phone find GPS on the plane?", "The aircraft's body blocks some of the satellite signal. Hold your phone near a window for a minute or two, and check that AirReveal is allowed to use your location."),
            ("Which side of the plane should I book?", "Preview the route before you go. In AirReveal, switch the Flight screen to Plan and drag along the progress bar to see what you'll pass and which side it will be on. Planning is always free."),
        ],
    ),
    "es": dict(
        ex_h="Qué podrías ver: dos rutas de ejemplo",
        ex_p="Las rutas cambian con el tiempo y el tráfico aéreo, así que tómalas como ejemplos de una ruta habitual, no como una promesa.",
        examples=[
            ("Londres a Roma", "Tras cruzar el canal de la Mancha, una ruta habitual atraviesa el este de Francia. Con el cielo despejado quizá veas los Alpes, en torno al Mont Blanc, antes de llegar a la costa italiana cerca de Génova y seguirla hacia el sur hasta Roma."),
            ("Londres a Nueva York", "Los vuelos suelen cruzar Irlanda antes de pasar varias horas sobre el Atlántico Norte. Normalmente tocan tierra sobre el Canadá atlántico, como Terranova o Nueva Escocia, y el último tramo a menudo sigue la costa de Nueva Inglaterra hacia Long Island."),
        ],
        ex_note="AirReveal sigue tu vuelo real con el GPS, así que nombra lo que de verdad hay debajo, vaya por donde vaya tu vuelo.",
        steps_h="Cómo ver lo que hay debajo con AirReveal",
        steps=[
            "<strong>Añade tu vuelo.</strong> Crea un vuelo nuevo en AirReveal, elige el origen y el destino, e indica que es un viaje en directo.",
            "<strong>Descárgalo.</strong> En <strong>Mis vuelos</strong>, desliza tu vuelo hacia la derecha y toca <strong>Descargar</strong> mientras aún tengas wifi.",
            "<strong>Permite la ubicación.</strong> Cuando empiece el viaje, elige <strong>Siempre</strong> para que AirReveal siga el vuelo con el teléfono bloqueado.",
            "<strong>Mira por la ventanilla.</strong> Activa el modo avión cuando lo pida la tripulación; el GPS sigue funcionando. AirReveal nombra lo que hay debajo y delante, y hacia qué lado mirar.",
        ],
        faq=[
            ("¿Hasta dónde se ve desde un avión?", "Desde una altitud de crucero habitual de unos 11 km (35.000 pies), el horizonte está a unos 370 km. En la práctica, la bruma y las nubes suelen limitar mucho lo que se distingue, así que lo más fácil de ver son las costas, las cordilleras y las grandes ciudades."),
            ("¿Por qué mi teléfono no encuentra el GPS en el avión?", "El fuselaje bloquea parte de la señal de los satélites. Acerca el teléfono a una ventanilla durante uno o dos minutos y comprueba que AirReveal tiene permiso para usar tu ubicación."),
            ("¿Qué lado del avión debo reservar?", "Mira la ruta antes de viajar. En AirReveal puedes planificar el vuelo y recorrerlo para ver qué pasarás y a qué lado quedará. Planificar es siempre gratis."),
        ],
    ),
    "fr": dict(
        ex_h="Ce que vous pourriez voir : deux exemples d'itinéraires",
        ex_p="Les itinéraires changent avec la météo et le trafic aérien : voyez-les comme des exemples de trajet habituel, pas comme une promesse.",
        examples=[
            ("Londres–Rome", "Après la Manche, un trajet habituel traverse l'est de la France. Par temps clair, vous verrez peut-être les Alpes, autour du mont Blanc, avant d'atteindre la côte italienne près de Gênes et de la longer vers le sud jusqu'à Rome."),
            ("Londres–New York", "Les vols survolent souvent l'Irlande avant plusieurs heures au-dessus de l'Atlantique Nord. Ils rejoignent en général la terre au-dessus du Canada atlantique, comme Terre-Neuve ou la Nouvelle-Écosse, et la fin du vol longe souvent la côte de la Nouvelle-Angleterre vers Long Island."),
        ],
        ex_note="AirReveal suit votre vol réel grâce au GPS : il nomme ce qui se trouve vraiment sous vous, quel que soit le trajet.",
        steps_h="Voir ce qu'il y a sous vous avec AirReveal",
        steps=[
            "<strong>Ajoutez votre vol.</strong> Créez un nouveau vol dans AirReveal, choisissez le départ et l'arrivée, puis indiquez qu'il s'agit d'un voyage en direct.",
            "<strong>Téléchargez-le.</strong> Dans <strong>Mes vols</strong>, faites glisser votre vol vers la droite et touchez <strong>Télécharger</strong> tant que vous avez le Wi-Fi.",
            "<strong>Autorisez la localisation.</strong> Au début du voyage, choisissez <strong>Toujours</strong> pour qu'AirReveal continue le suivi téléphone verrouillé.",
            "<strong>Regardez par le hublot.</strong> Passez en mode avion quand l'équipage le demande ; le GPS continue de fonctionner. AirReveal nomme ce qui est en dessous et devant, et de quel côté regarder.",
        ],
        faq=[
            ("Jusqu'où voit-on depuis un avion ?", "Depuis une altitude de croisière habituelle d'environ 11 km (35 000 pieds), l'horizon est à quelque 370 km. En pratique, la brume et les nuages limitent souvent beaucoup ce qu'on distingue : les côtes, les massifs montagneux et les grandes villes sont les plus faciles à repérer."),
            ("Pourquoi mon téléphone ne trouve-t-il pas le GPS dans l'avion ?", "La carlingue bloque une partie du signal des satellites. Tenez votre téléphone près d'un hublot pendant une minute ou deux et vérifiez qu'AirReveal a l'autorisation d'utiliser votre position."),
            ("De quel côté de l'avion réserver ?", "Regardez l'itinéraire avant de partir. Dans AirReveal, vous pouvez planifier le vol et le parcourir pour voir ce que vous survolerez et de quel côté. La planification est toujours gratuite."),
        ],
    ),
    "de": dict(
        ex_h="Was du sehen könntest: zwei Beispielrouten",
        ex_p="Routen ändern sich mit Wetter und Flugverkehr. Sieh diese also als Beispiele für eine übliche Route, nicht als Versprechen.",
        examples=[
            ("London–Rom", "Nach dem Ärmelkanal führt eine übliche Route über Ostfrankreich. Bei klarem Himmel siehst du vielleicht die Alpen rund um den Mont Blanc, bevor der Flug bei Genua die italienische Küste erreicht und ihr nach Süden Richtung Rom folgt."),
            ("London–New York", "Flüge überqueren oft Irland und dann mehrere Stunden den Nordatlantik. Land erreichen sie meist über dem atlantischen Kanada, etwa Neufundland oder Nova Scotia, und das letzte Stück folgt oft der Küste Neuenglands Richtung Long Island."),
        ],
        ex_note="AirReveal folgt deinem echten Flug per GPS und nennt, was wirklich unter dir liegt, egal welche Route dein Flug nimmt.",
        steps_h="So siehst du mit AirReveal, was unter dir liegt",
        steps=[
            "<strong>Füge deinen Flug hinzu.</strong> Lege in AirReveal einen neuen Flug an, wähle Start und Ziel und gib an, dass es eine Live-Reise ist.",
            "<strong>Lade ihn.</strong> Wische in <strong>Meine Flüge</strong> deinen Flug nach rechts und tippe auf <strong>Laden</strong>, solange du noch WLAN hast.",
            "<strong>Erlaube den Standort.</strong> Wähle zu Beginn der Reise <strong>Immer</strong>, damit AirReveal auch bei gesperrtem Telefon weiter verfolgt.",
            "<strong>Schau aus dem Fenster.</strong> Schalte den Flugmodus ein, wenn die Crew darum bittet; GPS funktioniert weiter. AirReveal nennt, was unter und vor dir liegt und auf welcher Seite du schauen solltest.",
        ],
        faq=[
            ("Wie weit sieht man aus einem Flugzeug?", "Aus einer üblichen Reiseflughöhe von etwa 11 km (35.000 Fuß) liegt der Horizont rund 370 km entfernt. In der Praxis begrenzen Dunst und Wolken meist deutlich, was man erkennt. Am leichtesten zu sehen sind Küsten, Gebirge und große Städte."),
            ("Warum findet mein Telefon im Flugzeug kein GPS?", "Der Rumpf schirmt einen Teil des Satellitensignals ab. Halte dein Telefon ein, zwei Minuten in die Nähe eines Fensters und prüfe, ob AirReveal deinen Standort verwenden darf."),
            ("Welche Seite im Flugzeug sollte ich buchen?", "Sieh dir die Route vorher an. In AirReveal kannst du den Flug planen und durchspielen, um zu sehen, was du überfliegst und auf welcher Seite es liegt. Planen ist immer kostenlos."),
        ],
    ),
    "it": dict(
        ex_h="Cosa potresti vedere: due rotte di esempio",
        ex_p="Le rotte cambiano con il meteo e il traffico aereo, quindi considerale esempi di una rotta tipica, non una promessa.",
        examples=[
            ("Londra–Roma", "Dopo la Manica, una rotta tipica attraversa la Francia orientale. Con il cielo sereno potresti vedere le Alpi, intorno al Monte Bianco, prima che il volo raggiunga la costa italiana vicino a Genova e la segua verso sud fino a Roma."),
            ("Londra–New York", "I voli spesso sorvolano l'Irlanda prima di diverse ore sull'Atlantico settentrionale. Di solito tornano sulla terraferma sopra il Canada atlantico, come Terranova o la Nuova Scozia, e l'ultimo tratto segue spesso la costa del New England verso Long Island."),
        ],
        ex_note="AirReveal segue il tuo volo reale con il GPS, quindi nomina ciò che c'è davvero sotto di te, qualunque rotta prenda il volo.",
        steps_h="Come vedere cosa c'è sotto di te con AirReveal",
        steps=[
            "<strong>Aggiungi il tuo volo.</strong> Crea un nuovo volo in AirReveal, scegli partenza e arrivo e indica che è un viaggio in tempo reale.",
            "<strong>Scaricalo.</strong> In <strong>I miei voli</strong>, scorri il tuo volo verso destra e tocca <strong>Scarica</strong> finché hai il Wi-Fi.",
            "<strong>Consenti la posizione.</strong> All'inizio del viaggio scegli <strong>Sempre</strong>, così AirReveal continua a seguire il volo con il telefono bloccato.",
            "<strong>Guarda dal finestrino.</strong> Attiva la modalità aereo quando l'equipaggio lo chiede; il GPS continua a funzionare. AirReveal nomina ciò che c'è sotto e davanti, e da che lato guardare.",
        ],
        faq=[
            ("Fin dove si vede da un aereo?", "Da una quota di crociera tipica di circa 11 km (35.000 piedi), l'orizzonte è a circa 370 km. In pratica foschia e nuvole di solito limitano molto ciò che si distingue: coste, catene montuose e grandi città sono le cose più facili da riconoscere."),
            ("Perché il telefono non trova il GPS in aereo?", "La fusoliera blocca parte del segnale dei satelliti. Tieni il telefono vicino a un finestrino per un paio di minuti e controlla che AirReveal abbia il permesso di usare la tua posizione."),
            ("Da che lato dell'aereo conviene prenotare?", "Guarda la rotta prima di partire. In AirReveal puoi pianificare il volo e scorrerlo per vedere cosa sorvolerai e da che lato. La pianificazione è sempre gratuita."),
        ],
    ),
    "pt-br": dict(
        ex_h="O que você pode ver: duas rotas de exemplo",
        ex_p="As rotas mudam com o tempo e o tráfego aéreo, então veja estes como exemplos de uma rota comum, não como uma promessa.",
        examples=[
            ("Londres–Roma", "Depois do Canal da Mancha, uma rota comum atravessa o leste da França. Com o céu limpo, você talvez veja os Alpes, perto do Mont Blanc, antes de o voo chegar à costa italiana perto de Gênova e segui-la para o sul até Roma."),
            ("Londres–Nova York", "Os voos costumam passar pela Irlanda antes de várias horas sobre o Atlântico Norte. Normalmente voltam a sobrevoar terra no Canadá atlântico, como a Terra Nova ou a Nova Escócia, e o trecho final muitas vezes segue a costa da Nova Inglaterra rumo a Long Island."),
        ],
        ex_note="O AirReveal acompanha o seu voo real pelo GPS, então mostra o nome do que está mesmo abaixo de você, seja qual for a rota.",
        steps_h="Como ver o que está abaixo de você com o AirReveal",
        steps=[
            "<strong>Adicione o seu voo.</strong> Crie um novo voo no AirReveal, escolha a origem e o destino e indique que é uma viagem ao vivo.",
            "<strong>Baixe o voo.</strong> Em <strong>Meus voos</strong>, deslize o voo para a direita e toque em <strong>Baixar</strong> enquanto ainda tiver Wi-Fi.",
            "<strong>Permita a localização.</strong> Quando a viagem começar, escolha <strong>Sempre</strong> para o AirReveal continuar acompanhando com o celular bloqueado.",
            "<strong>Olhe pela janela.</strong> Ative o modo avião quando a tripulação pedir; o GPS continua funcionando. O AirReveal mostra o que está abaixo e à frente, e de que lado olhar.",
        ],
        faq=[
            ("Até onde dá para ver de um avião?", "De uma altitude de cruzeiro comum, de cerca de 11 km (35.000 pés), o horizonte fica a uns 370 km. Na prática, a névoa e as nuvens costumam limitar bastante o que dá para distinguir, então litorais, cadeias de montanhas e cidades grandes são o mais fácil de ver."),
            ("Por que o meu celular não encontra o GPS no avião?", "A fuselagem bloqueia parte do sinal dos satélites. Deixe o celular perto da janela por um ou dois minutos e confira se o AirReveal tem permissão para usar a sua localização."),
            ("De que lado do avião devo reservar?", "Veja a rota antes de viajar. No AirReveal, você pode planejar o voo e percorrê-lo para ver o que vai sobrevoar e de que lado vai ficar. Planejar é sempre gratuito."),
        ],
    ),
}


def sections_html(lang, esc):
    """The example-routes and steps sections, as page HTML (placed after the GPS section)."""
    e = EXTRAS[lang]
    routes = "".join(f"<h3>{esc(a)}</h3><p>{esc(b)}</p>" for a, b in e["examples"])
    steps = "".join(f"<li>{s}</li>" for s in e["steps"])
    return (f'<section class="clause" id="examples"><h2 class="clause-title">{esc(e["ex_h"])}</h2><p>{esc(e["ex_p"])}</p>{routes}<p>{esc(e["ex_note"])}</p></section>'
            f'<section class="clause" id="how-to"><h2 class="clause-title">{esc(e["steps_h"])}</h2><ol>{steps}</ol></section>')
