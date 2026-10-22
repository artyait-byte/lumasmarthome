"""Location silo, journal, and brand copy for LUMA Smart Home.

Tony's remodeling SEO playbook, applied to this studio:
  - City and city×service URLs live under /service-areas/, not in the Solutions nav.
  - Start the keyword snowball with "smart home Sarasota", then tighter terms.
  - Unique copy on every URL (no doorway templates).
  - One NAP in the footer, with a Google Maps search link until a GBP CID exists.
"""

SERVICES = {
    "lighting": {
        "id": "lighting",
        "name": "Smart lighting control",
        "nav": "Lighting",
        "page": "lighting",
        "short": "Lutron and Ketra scenes that follow the Gulf Coast hour.",
        "og": "/assets/photos/lighting-scene.jpg",
    },
    "shading": {
        "id": "shading",
        "name": "Motorized window treatments",
        "nav": "Shading",
        "page": "shading",
        "short": "Sivoia and Somfy shades cut west-facing glare without killing the view.",
        "og": "/assets/photos/hero-shading.jpg",
    },
    "theaters": {
        "id": "theaters",
        "name": "Home theater design",
        "nav": "Home theaters",
        "page": "theaters",
        "short": "Dedicated rooms and media suites designed from the walls out.",
        "og": "/assets/photos/hero-theater.jpg",
    },
    "audio": {
        "id": "audio",
        "name": "Whole-home audio",
        "nav": "Audio & video",
        "page": "audio",
        "short": "Invisible indoor and lanai speakers, one app across every zone.",
        "og": "/assets/photos/hero-audio-hifi.jpg",
    },
    "security": {
        "id": "security",
        "name": "Security & cameras",
        "nav": "Security",
        "page": "security",
        "short": "On-premise UniFi Protect — your footage stays on the property.",
        "og": "/assets/photos/hero-security-v2.jpg",
    },
    "networking": {
        "id": "networking",
        "name": "Wi-Fi & structured cabling",
        "nav": "Networking",
        "page": "networking",
        "short": "UniFi Wi-Fi 6/7 and Cat6A designed before drywall.",
        "og": "/assets/photos/hero-networking.jpg",
    },
    "business-security": {
        "id": "business-security",
        "name": "Business security cameras",
        "nav": "Business cameras",
        "page": "security",
        "short": "UniFi Protect camera systems for offices, shops and small commercial spaces.",
        "og": "/assets/photos/hero-security-v2.jpg",
    },
    "retail-security-cameras": {
        "id": "retail-security-cameras",
        "name": "Retail store security cameras",
        "nav": "Business cameras",
        "page": "security",
        "listed": False,
        "short": "Register, entrance, sales floor and stock room cameras for shops.",
        "og": "/assets/photos/cam-dome.jpg",
    },
    "restaurant-security-cameras": {
        "id": "restaurant-security-cameras",
        "name": "Restaurant security cameras",
        "nav": "Business cameras",
        "page": "security",
        "listed": False,
        "short": "Bar, POS, kitchen line and back-door cameras for restaurants.",
        "og": "/assets/photos/cam-dome.jpg",
    },
    "warehouse-security-cameras": {
        "id": "warehouse-security-cameras",
        "name": "Warehouse security cameras",
        "nav": "Business cameras",
        "page": "security",
        "listed": False,
        "short": "Dock, aisle, yard and gate cameras with plate recording.",
        "og": "/assets/photos/cam-bullet.jpg",
    },
    "hoa-security-cameras": {
        "id": "hoa-security-cameras",
        "name": "HOA and condo security cameras",
        "nav": "Business cameras",
        "page": "security",
        "listed": False,
        "short": "Gate, pool, mail room and garage cameras for associations.",
        "og": "/assets/photos/cam-bullet.jpg",
    },
    "automation": {
        "id": "automation",
        "name": "Home automation",
        "nav": "Automation",
        "page": "automation",
        "short": "One press moves lighting, shades, climate, audio, and security together.",
        "og": "/assets/photos/hero-automation.jpg",
    },
}

CITIES = [
    {
        "id": "sarasota",
        "name": "Sarasota",
        "county": "Sarasota County",
        "tagline": "Our home county — and the first place we spec a Gulf Coast hour.",
        "h1": "Smart home projects across Sarasota, neighborhood by neighborhood",
        "title": "Sarasota Smart Home Projects by Neighborhood | LUMA",
        "description": "LUMA Smart Home designs and installs lighting control, motorized shades, audio, security and Wi-Fi for Sarasota homes. Local studio, not luma.com.",
        "lede": "Bird Key, Lido, Palmer Ranch and downtown each ask different things of a house. This page is the Sarasota map of what we install where. For the studio itself, start with [smart home installation in Sarasota](home): LUMA is a residential technology studio based here, specifying Lutron, UniFi, Somfy, and Sonos for houses that live with Gulf sun, salt air, and seasonal occupancy.",
        "paragraphs": [
            "Sarasota is not a generic 'smart home market.' West-facing glass on the bay, lanais that become the living room eight months of the year, and HOA rules on Siesta and Lido all change how lighting, shades, and cameras should be drawn. We walk the property at the hour you actually use it — late afternoon glare, not a noon site visit.",
            "Most of our Sarasota work is existing homes and thoughtful remodels: RadioRA 3 where a full HomeWorks processor is overkill, Sivoia or Somfy on the elevations that cook, UniFi Protect with the NVR in a conditioned closet. New construction gets a wired spine first. Either way, proposals are line-item, and the same technicians who pull cable still answer the phone after turnover.",
            "We are LUMA Smart Home of Sarasota — a local integrator. We are not luma.com (the events platform), not Luma AI / Luma Labs, and not Snap One's Luma camera line. If a search result sent you looking for lighting control or a Lutron installer in Sarasota, start on [this LUMA, not the others](luma-smart-home-sarasota) or [Lutron lighting in Sarasota](sa-sarasota-lighting).",
        ],
        "neighborhoods": [
            "Downtown & Rosemary District",
            "Bird Key",
            "Lido Key",
            "Siesta Key",
            "Palmer Ranch",
            "Osprey & Casey Key",
            "Lakewood Ranch (south)",
        ],
        "image": "/assets/photos/sarasota-marina.jpg",
        "services": [
            "lighting",
            "shading",
            "theaters",
            "audio",
            "security",
            "networking",
            "automation",
        ],
    },
    {
        "id": "bradenton",
        "name": "Bradenton",
        "county": "Manatee County",
        "tagline": "River, bay, and inland neighborhoods — one low-voltage trade.",
        "h1": "Smart home installation in Bradenton & Manatee County",
        "title": "Smart Home Installation Bradenton FL | LUMA Smart Home",
        "description": "Lighting, motorized shades, UniFi cameras, and whole-home audio for Bradenton, Palmetto, and Anna Maria. LUMA Smart Home serves Manatee County from Sarasota.",
        "lede": "Bradenton jobs look different from downtown Sarasota: more CBS ranch and waterfront rebuilds, more Anna Maria lock-and-leave, more families who want cameras and Wi-Fi that actually cover the lot — not a big-box mesh kit.",
        "paragraphs": [
            "Manatee County stretches from the river through Palmetto and out to the islands. Salt, distance from the equipment closet, and HOA paint rules on Anna Maria all show up in the spec. We place UniFi access points from a heat map, not a floor-plan guess, and we put the recorder on the property so seasonal owners are not paying a camera cloud while the house sits empty.",
            "Lighting control here is often a RadioRA 3 overlay on an existing electrical plan — scenes for the lanai, path lights, and the rooms the family actually uses. If you are building in Lakewood Ranch or East Bradenton, we coordinate with the GC on Cat6A before drywall so you are not fishing cable later.",
        ],
        "neighborhoods": [
            "West Bradenton",
            "Palmetto",
            "Anna Maria Island",
            "Holmes Beach",
            "Lakewood Ranch (north)",
            "University Park",
        ],
        "image": "/assets/photos/waterfront-lanai.jpg",
        "services": ["lighting", "security"],
    },
    {
        "id": "lakewood-ranch",
        "name": "Lakewood Ranch",
        "county": "Manatee & Sarasota Counties",
        "tagline": "New construction and finished houses in a master-planned community.",
        "h1": "Smart home systems in Lakewood Ranch, Florida",
        "title": "Lakewood Ranch Smart Home Installer | LUMA Smart Home",
        "description": "LUMA specs lighting control, structured cabling, and motorized shades for Lakewood Ranch new construction and remodels — Manatee and Sarasota sides.",
        "lede": "Lakewood Ranch is where a smart home either gets designed into the walls or bolted on after closing. We prefer the first. Cat6A, a real rack, and Lutron on the lighting schedule beat a bag of consumer hubs in a kitchen drawer.",
        "paragraphs": [
            "Builders here move fast. If low-voltage is not on the first-round electrical drawings, you inherit Wi-Fi dead zones in the bonus room and a shade motor with no home-run. LUMA shows up as one trade: lighting control, shades, cameras, audio, and the network that makes them honest.",
            "Finished homes in the Ranch still get a proper survey — which elevations cook in west sun, where the HOA allows cameras, whether the existing Wi-Fi is a single gateway in the laundry. We do not rip working Lutron to sell a different brand; we document what you have and extend it.",
        ],
        "neighborhoods": [
            "Lakewood Ranch Main Street",
            "Country Club / Lake Club",
            "Isles & concession villages",
            "UTC-adjacent",
        ],
        "image": "/assets/photos/hero-modern-home.jpg",
        "services": [],
    },
    {
        "id": "venice",
        "name": "Venice",
        "county": "Sarasota County",
        "tagline": "South county light, historic fabric, and gulf-facing glass.",
        "h1": "Smart home installation in Venice, Florida",
        "title": "Venice FL Smart Home Installer | LUMA Smart Home",
        "description": "Lutron lighting, motorized shades, and UniFi networking for Venice, Casey Key, and south Sarasota County homes. Designed for gulf sun and older electrical.",
        "lede": "Venice mixes 1920s cottages, 1970s CBS, and new gulf-front glass. The lighting and shade spec has to respect that mix — warm-dim that does not fight original plaster, motors that fit existing pockets, and a network that is not hanging off a single modem in a hot garage.",
        "paragraphs": [
            "South county afternoon sun is unforgiving on west and southwest elevations. Motorized solar screens on the lanai and blackout in the primary are usually the first conversation, then lighting scenes so the house does not slam from 'all on' to dark. We program to the clock and to occupancy, not to a demo keypad in a showroom.",
            "If you are on Casey Key or down toward North Port, travel and staging still sit inside our Sarasota-county service window. Same line-item proposal, same technicians after turnover.",
        ],
        "neighborhoods": [
            "Venice Island",
            "The Venice Airport area",
            "Casey Key",
            "Nokomis",
            "South Venice",
        ],
        "image": "/assets/photos/gulf-sunset.jpg",
        "services": [],
    },
    {
        "id": "siesta-key",
        "name": "Siesta Key",
        "county": "Sarasota County",
        "tagline": "Salt, HOA rules, and glass that faces the gulf.",
        "h1": "Smart home & motorized shades on Siesta Key",
        "title": "Siesta Key Smart Home & Motorized Shades | LUMA Smart Home",
        "description": "Motorized shades, lighting control, and lock-and-leave cameras for Siesta Key condos and single-family homes. Salt-aware specs, HOA-friendly cameras.",
        "lede": "Siesta Key is a shade and salt problem before it is a gadget problem. West glass, rental calendars, and association rules decide what we can mount and how the house should behave when nobody is home.",
        "paragraphs": [
            "We spec outdoor-rated motors and fabrics that survive UV, and we program 'away' scenes that close solar screens, drop selected lights to a lived-in look, and arm cameras without a monthly cloud tax. Condos get a quieter stack: RadioRA 3, Somfy or Sivoia where pockets exist, UniFi in a hall closet instead of a consumer mesh on the fridge.",
            "If your search was 'smart home Siesta Key' because a previous installer left a dealer-locked iPad on the wall, we can document what you own and tell you honestly whether to keep it or replace the control layer.",
        ],
        "neighborhoods": [
            "Siesta Village",
            "Siesta Beach corridor",
            "North Siesta",
            "Midnight Pass",
        ],
        "image": "/assets/photos/hero-shading.jpg",
        "services": [],
    },
    {
        "id": "longboat-key",
        "name": "Longboat Key",
        "county": "Sarasota & Manatee Counties",
        "tagline": "Barrier-island light, long cable runs, and lock-and-leave.",
        "h1": "Smart home systems on Longboat Key",
        "title": "Longboat Key Smart Home Installer | LUMA Smart Home",
        "description": "Lighting, shades, cameras, and Wi-Fi for Longboat Key residences. Designed for salt air, gulf glare, and seasonal occupancy.",
        "lede": "Longboat Key punishes lazy networking and lazy shade cloth. Cable runs are long, closets are humid, and the view is the reason you bought the house — so shades have to kill glare without killing the water.",
        "paragraphs": [
            "We treat the network closet like a piece of mechanical: ventilation, a UPS, and UniFi gear that can be diagnosed remotely when you are north for the summer. Cameras sit on-prem so you are not paying a subscription for an empty driveway. Lighting scenes follow the gulf hour: late-day Ketra or warm-dim on the west elevation, path lights that do not flood the beach.",
            "HOA and condo boards here care about visible hardware. We bring cut sheets early and mount what the elevation can actually hide.",
        ],
        "neighborhoods": [
            "Longboat Key Club",
            "Mid-Key",
            "North Longboat",
            "St. Armands adjacent",
        ],
        "image": "/assets/photos/waterfront-lanai.jpg",
        "services": [],
    },
    {
        "id": "anna-maria-island",
        "name": "Anna Maria Island",
        "county": "Manatee County",
        "tagline": "Island houses, salt air, and owners who are often somewhere else.",
        "h1": "Smart home systems on Anna Maria Island",
        "title": "Anna Maria Island Smart Home Installer | LUMA Smart Home",
        "description": "Lighting control, motorized shades, cameras and Wi-Fi for Anna Maria, Holmes Beach and Bradenton Beach homes, built for salt air and owners away.",
        "lede": "Anna Maria Island is three small cities on one barrier island: Anna Maria, Holmes Beach and Bradenton Beach. A lot of the houses are second homes or rentals, which changes what a system has to do. It has to be run and checked from somewhere else.",
        "paragraphs": [
            "That usually means a network that can be diagnosed remotely, cameras that record on the property rather than to a subscription, and lighting and shade schedules that keep an empty house looking lived in. On the gulf side, shades that cut the afternoon glare without taking the water away are normally the first conversation.",
            "Many newer island houses are raised above the flood line, which puts the equipment closet and the cable runs in unusual places. We plan those on the drawings, before the walls close.",
        ],
        "neighborhoods": [
            "Anna Maria",
            "Holmes Beach",
            "Bradenton Beach",
            "Cortez",
        ],
        "image": "/assets/photos/gulf-sunset.jpg",
        "services": [],
    },
    {
        "id": "palmetto",
        "name": "Palmetto",
        "county": "Manatee County",
        "tagline": "River-front lots, older blocks, and new building north of the river.",
        "h1": "Smart home installation in Palmetto, Florida",
        "title": "Palmetto FL Smart Home Installer | Manatee County | LUMA",
        "description": "Lighting control, motorized shades, cameras, and Wi-Fi for Palmetto, Snead Island, and Terra Ceia homes, from the LUMA studio in Sarasota.",
        "lede": "Palmetto sits on the north bank of the Manatee River, across from Bradenton. It has older neighborhoods near the river, waterfront lots out toward Snead Island and Terra Ceia, and a lot of newer construction farther north.",
        "paragraphs": [
            "In older houses the honest approach is usually an overlay: lighting control that works with the switch boxes already in the walls, a proper network closet instead of a modem in a hot garage, and cameras that record on the property. New construction is the moment to put structured cabling and shade pockets on the drawings, before drywall.",
            "Waterfront lots on the river and the bays bring the same questions as the rest of the coast: afternoon glare on the water side, docks and seawalls that want lighting and a camera, and equipment that has to live with the humidity.",
        ],
        "neighborhoods": [
            "Downtown Palmetto",
            "Snead Island",
            "Terra Ceia",
            "Ellenton",
        ],
        "image": "/assets/photos/fl-golden-hour.jpg",
        "services": [],
    },
]

# Unique city × service pages (not every city × every trade — doorway risk).
CITY_SERVICES = [
    {
        "city": "sarasota",
        "service": "lighting",
        "h1": "Lutron lighting control in Sarasota",
        "title": "Lutron Installer Sarasota FL | Ketra & RadioRA 3 | LUMA",
        "description": "Sarasota Lutron installer for RadioRA 3, HomeWorks, and Ketra. Decorative and architectural lighting under one spec — gulf-hour scenes, not a wall of dimmers.",
        "lede": "Sarasota light changes fast: white-hot noon on the bay, then a long gold hour that makes cheap LEDs look sickly. We spec Lutron so the fixtures you already chose — or the ones your designer is drawing — dim, warm, and scene without a second app.",
        "paragraphs": [
            "Most Sarasota houses we see are not empty lots. They are finished electrical with a story of three remodel eras. RadioRA 3 is the honest overlay: designer keypads, occupancy where it belongs, and phone control without ripping every switch. New construction and deep remodels get HomeWorks or a Ketra conversation when the architecture is doing real color work.",
            "We program to how you live here — Good morning on the kitchen and lanai, Away that looks occupied without looking theatrical, Evening that keeps the art lit and the TV wall calm. The same crew that lands the processors still does scene tweaks after you move in. Next: [the lighting overview](lighting), [Our Work](work), or [a walkthrough](contact).",
        ],
        "bullets": [
            "RadioRA 3 for existing Sarasota homes and condos",
            "Ketra and warm-dim for gulf-facing rooms",
            "Landscape and path lighting on the same keypad",
            "Line-item proposals — every keypad, every load",
        ],
        "sections": [   {   'h2': 'RadioRA 3, HomeWorks or Ketra: which Lutron fits a Sarasota house',
                'text': [   'RadioRA 3 is the right system for most existing Sarasota homes and condos. '
                            'The dimmers and keypads replace the switches you have, the main repeater '
                            'talks to them wirelessly, and nothing has to be pulled back to a panel. A '
                            'house in Palmer Ranch or a Lido Key condo can be fully on Lutron in days, not '
                            'months.',
                            'HomeWorks is for new construction and deep remodels where the lighting design '
                            'is doing serious work: many loads, panelized dimming in a closet, and keypads '
                            'that need to look like architecture. Ketra adds tunable white and colour that '
                            'shifts through the day, which matters most on gulf-facing rooms where the '
                            'light outside changes fast. We explain the choice in plain terms in [RadioRA '
                            '3 vs HomeWorks in Sarasota](journal-lutron-sarasota).']},
            {   'h2': 'What a Lutron installation includes',
                'text': [   'A walkthrough at the hour you use the house, a load schedule that lists every '
                            'circuit and fixture, keypad engraving in your words, and programming on site '
                            'with you in the room. Shades from the same family, Lutron Sivoia, join the '
                            'same keypads and the same astronomical clock, so sunset can lower the screens '
                            'and warm the dining room in one step. See [motorized shades in '
                            'Sarasota](sa-sarasota-shading).',
                            'After turnover the same team adjusts scenes as you live with them. That is '
                            'part of the job, not an upsell.']}],
        "faq": [   {   'q': 'Do I need to rewire my house for Lutron?',
                'a': 'Usually not. RadioRA 3 replaces existing switches with wireless dimmers and keypads, '
                     'so most Sarasota homes keep their wiring. New construction and big remodels are the '
                     'time to consider HomeWorks with central panels.'},
            {   'q': 'Can Lutron control my shades and landscape lights too?',
                'a': 'Yes. Lutron Sivoia shades and exterior lighting circuits can sit on the same keypads '
                     'and schedules as the interior lighting, so one button sets the whole room.'},
            {   'q': 'Will my existing LED fixtures work with Lutron dimmers?',
                'a': 'Most quality LED fixtures do. We check each load during the walkthrough and flag '
                     'fixtures that flicker or will not dim smoothly before anything is installed.'},
            {   'q': 'Do you install Lutron outside Sarasota?',
                'a': 'Yes, across Sarasota and Manatee Counties, including '
                     '[Bradenton](sa-bradenton-lighting), Lakewood Ranch, Venice, Longboat Key and Siesta '
                     'Key.'}],
    },
    {
        "city": "sarasota",
        "service": "shading",
        "h1": "Motorized shades in Sarasota",
        "title": "Motorized Shades Sarasota FL | Lutron Sivoia & Somfy | LUMA",
        "description": "Motorized window treatments for Sarasota gulf glare: solar screens, blackout, Lutron Sivoia QS and Somfy, programmed to the hour of the day.",
        "lede": "Sarasota's problem is not 'windows.' It is west and southwest glass that cooks the living room from 3 p.m. on, plus HOA rules about what the street is allowed to see. Motorized shades are the architectural answer; a stick-on film is not.",
        "paragraphs": [
            "We layer solar screen for daytime view, blackout for sleep, and drapery where the designer wants cloth. Lutron Sivoia when the lighting is already Lutron; Somfy when the openings, pockets, or budget say so. Both get astronomical clocks and keypad scenes so you are not herding remotes at sunset.",
            "Siesta, Lido, and Bird Key add salt and wind. Outdoor-rated motors and fabrics are in the spec, not an afterthought. We measure twice because gulf-front out-of-square openings are the rule.",
        ],
        "bullets": [
            "Solar screen + blackout layers, not one compromised fabric",
            "Sivoia QS when the house is already Lutron",
            "Somfy for wide openings and outdoor volumes",
            "Programmed to sunrise, sunset, and Away",
        ],
        "sections": [   {   'h2': 'Interior shades, exterior screens and blackout',
                'text': [   'Most Sarasota houses need two or three kinds of motorized shading. Interior '
                            'roller shades with a solar-screen fabric cut glare and heat while you still '
                            'see the water. Blackout shades or motorized drapery make bedrooms dark after '
                            'a late dinner. Exterior motorized screens on the lanai block low western sun '
                            'and insects without enclosing the space.',
                            'We choose fabric openness by elevation: a denser screen on the west and '
                            'southwest glass that cooks from mid-afternoon, a lighter one where the view '
                            'and the morning light matter more.']},
            {   'h2': 'Lutron Sivoia or Somfy',
                'text': [   'If the lighting is already Lutron, Sivoia shades join the same keypads and '
                            'clock. Somfy motors are the better fit for very wide openings, existing '
                            'pockets and many outdoor screens. Both can be scheduled to sunrise and sunset '
                            'and grouped into scenes such as Away. Why layered shades beat one compromise '
                            'fabric is explained in [motorized shades for Gulf Coast '
                            'sun](journal-shades-gulf).']},
            {   'h2': 'Near the water',
                'text': [   'On Siesta Key, Lido Key, Bird Key and Longboat Key, salt and wind are part of '
                            'the spec: outdoor-rated motors and hardware, and fabrics chosen for UV. '
                            'Island homes have their own pages: [motorized shades on Siesta '
                            'Key](sa-siesta-key-shading) and [motorized shades on Longboat '
                            'Key](sa-longboat-key-shading).']}],
        "faq": [   {   'q': 'What is the difference between motorized shades and motorized blinds?',
                'a': 'Shades are fabric that rolls or folds; blinds have slats that tilt. For Gulf Coast '
                     'glare we usually recommend roller shades with a solar-screen fabric, because they '
                     'keep the view and are simpler to motorize and maintain.'},
            {   'q': 'Can motorized shades be added to an existing home?',
                'a': 'Yes. Battery or low-voltage motors can go into existing window openings. Hardwired '
                     'motors are easiest during a remodel, but they are not required.'},
            {   'q': 'Do you install exterior motorized screens for lanais?',
                'a': 'Yes. Exterior motorized screens are one of the most useful upgrades on west-facing '
                     'lanais. We specify outdoor-rated motors and hardware for salt air.'},
            {   'q': 'Can shades open and close on their own?',
                'a': 'Yes. Shades can follow an astronomical clock (sunrise and sunset for your address), '
                     'a scene button, or an Away mode when the house is empty for the summer.'}],
    },
    {
        "city": "sarasota",
        "service": "theaters",
        "h1": "Home theater design in Sarasota",
        "title": "Home Theater Installation Sarasota FL | LUMA Smart Home",
        "description": "Dedicated cinema rooms and media suites in Sarasota — acoustics, sightlines, calibration, and seating. Designed from the walls out, not a TV on a console.",
        "lede": "A Sarasota 'theater' is often a bonus room with a projector someone bought online. We will tell you if that room can become a cinema, or if you are better with a serious media wall and proper acoustics — before you buy a screen that does not fit the throw.",
        "paragraphs": [
            "CBS construction, tile, and gulf-facing glass fight two-channel and surround equally. We treat the room: absorption, bass management, and lighting scenes that actually go to black. Calibration is a measured pass, not a demo disc on install day.",
            "If the house already has whole-home audio, the theater still gets its own processor and a clean handoff so a movie does not duck the kitchen. See Our Work for rooms we will put our name on.",
        ],
        "bullets": [
            "Dedicated rooms and convertible media suites",
            "Acoustic design for Florida CBS and tile",
            "Lighting and shades tied to Play / Pause / Credits",
            "Measured calibration, files you keep",
        ],
    },
    {
        "city": "sarasota",
        "service": "audio",
        "h1": "Whole-home audio in Sarasota",
        "title": "Whole-Home Audio Sarasota FL | Sonos & Sonance | LUMA",
        "description": "Invisible in-ceiling and lanai audio for Sarasota homes. One app, every zone, tuned to each room — not a Bluetooth speaker on the counter.",
        "lede": "Sarasota living happens on the lanai. If the audio plan stops at the sliders, you have an indoor system and an outdoor apology. We design indoor, under-eave, and landscape speakers as one source list.",
        "paragraphs": [
            "Sonance architectural and Sonos where the budget and the millwork agree; James or equivalent outdoors where salt and storms are the brief. Every zone gets a name you would actually say out loud. We measure with REW when the room deserves it — dining, two-channel, and anything next to a theater.",
            "The network has to be real. Whole-home audio on a consumer mesh is how you get dropouts during a dinner you care about. UniFi first, then speakers.",
        ],
        "bullets": [
            "Lanai and pool as first-class zones",
            "Flush architectural speakers, paint-matched",
            "One app, keypads optional",
            "Wired backbone before wireless fills",
        ],
    },
    {
        "city": "sarasota",
        "service": "security",
        "camera": "home",
        "photo": "/assets/photos/stock/camera-under-eave.jpg",
        "photo_alt": "Wired bullet security camera mounted under a roof overhang",
        "packages_h2": "Home security camera packages in Sarasota",
        "h1": "Security camera installation in Sarasota",
        "title": "Security Camera Installation Sarasota FL | UniFi | LUMA",
        "description": "On-premise UniFi Protect cameras in Sarasota — no monthly cloud fees. Property-walked placement, NVR on site, optional alarm monitoring.",
        "lede": "Sarasota homeowners are tired of doorbell brands that rent them their own driveway. UniFi Protect records on a box in your closet. We place cameras after walking sunset glare and neighbor angles — not from a floor plan in the office.",
        "paragraphs": [
            "Seasonal occupancy is the local twist: you need to see the house from somewhere else without paying a cloud tax all summer. On-prem storage plus optional encrypted off-site backup is the honest stack. We will also tell you where a camera is pointless because the HOA or the foliage will win.",
            "Home security cameras in Sarasota start from $2,900 plus tax for four wired cameras with a recorder, installed. The packages and prices are below. This is not Snap One's Luma camera line, and it is not a DIY kit. LUMA Smart Home is the Sarasota studio that designs the network the cameras sit on. Work is carried out with our Florida-licensed low-voltage partner.",
        ],
        "bullets": [
            "UniFi Protect G6 cameras, PoE, no batteries",
            "Recorder in the house, no monthly subscription",
            "Placement after a property walk, including glare",
            "Optional video doorbell and alarm",
        ],
        "sections": [
            {"h2": "How many cameras a Sarasota house needs", "text": [
                "Most house security camera systems in Sarasota come down to four to eight positions. Four covers a typical single-family home; waterfront and corner lots, or houses with a detached garage, usually need more.",
            ], "bullets": [
                "The driveway and the street, with vehicles in frame",
                "The front door and the porch, with faces at a usable size",
                "The back yard, the lanai and the pool gate",
                "Each side yard or gate where someone could walk in",
                "The dock or the seawall on a waterfront lot",
            ], "after": [
                "We count the cameras on the walk, not from a floor plan, and tell you where a camera would add little.",
            ]},
            {"h2": "How we install house security cameras", "text": [
                "We walk the property first, at the time of day the glare is worst, and mark each camera on a plan with what it needs to see: drive, front door, side yards, dock, pool gate. Cameras are wired PoE, so there are no batteries to charge, and they record to a UniFi Protect recorder on the property. You see everything in one app from wherever you spend the summer.",
                "Because the cameras run on the home network, we design that too: cameras on their own network segment, the recorder on a UPS, and remote access without opening the house to the internet. See [Wi-Fi and cabling in Sarasota](sa-sarasota-networking).",
            ]},
            {"h2": "No monthly cloud fee", "text": [
                "Recordings stay on the recorder in your house, so there is no per-camera subscription. If you want an off-site copy, it can be added as an option. The trade-offs between cloud cameras and on-premise recording are covered in [home cameras without a monthly cloud](journal-cameras-fees).",
            ]},
            {"h2": "Seasonal homes and HOAs", "text": [
                "For owners who are away half the year, the system should tell you about real events and stay quiet the rest of the time: person and vehicle detection, alerts only for the zones that matter, and a view you can check from anywhere. On Siesta Key, Longboat Key and in many Sarasota HOAs, visible hardware needs approval; we bring cut sheets before we drill.",
            ]},
            {"h2": "Cameras for an office or a shop", "text": [
                "The same UniFi stack runs offices, shops and small warehouses, with more cameras and a larger recorder. See [office and business security camera systems in Sarasota](sa-sarasota-business-security).",
            ]},
        ],
        "faq": [
            {"q": "How much does security camera installation cost in Sarasota?", "a": "Our packages start from $2,900 for 4 cameras, from $5,900 for 8 cameras and from $12,900 for 12 or more, plus tax. Each includes the cameras, a UniFi recorder and the installation. The final fixed price comes after a free walk of the property, once we know the cable runs and mounting points."},
            {"q": "How many cameras do I need?", "a": "Most houses need four to eight: the driveway, the front door, the back yard or lanai, and each side gate. Waterfront homes often add one for the dock. We count them with you on the walk."},
            {"q": "Do I have to pay a monthly fee?", "a": "No. Video records to the UniFi recorder in your house. There is no subscription and no per-camera fee."},
            {"q": "Do you record audio?", "a": "Audio is off by default. Florida law requires the consent of everyone in a conversation before it is recorded (Fla. Stat. 934.03), so we leave camera microphones switched off."},
            {"q": "Can I see my cameras when I am out of state?", "a": "Yes. The UniFi Protect app shows live and recorded video from anywhere, with alerts for people and vehicles."},
            {"q": "Wired or wireless cameras for a Florida house?", "a": "Wired PoE cameras. They do not depend on batteries in the heat, the picture is steadier, and one cable carries both power and video."},
            {"q": "Do you install cameras in Bradenton and Manatee County?", "a": "Yes. See [home cameras in Bradenton](sa-bradenton-security). We cover Sarasota and Manatee Counties."},
            {"q": "Do you install cameras for offices and shops?", "a": "Yes. See [office and business security camera systems in Sarasota](sa-sarasota-business-security)."},
        ],
    },
    {
        "city": "sarasota",
        "service": "networking",
        "h1": "Wi-Fi & structured cabling in Sarasota",
        "title": "Wi-Fi 6/7 & Cabling Sarasota FL | UniFi | LUMA Smart Home",
        "description": "Enterprise UniFi Wi-Fi and Cat6A structured cabling for Sarasota homes. Wired spine first — the layer every other smart-home system sits on.",
        "lede": "Every failed 'smart home' we are asked to rescue in Sarasota starts with a single gateway in a laundry closet and mesh satellites the homeowner was told would 'just work.' Lighting, cameras, and audio all inherit that lie.",
        "paragraphs": [
            "We design heat maps, VLAN the cameras off the laptops, and put a UPS on the rack. New construction gets Cat6A to APs, TVs, and shade locations before drywall. Existing homes get the honest version: as much wire as we can hide, then UniFi APs where the masonry allows.",
            "If you only hire us for one trade, make it this one. Everything else is optional. The network is not.",
        ],
        "bullets": [
            "UniFi gateway, switching, and Wi-Fi 6/7 APs",
            "Cat6A during remodel or new construction",
            "Segmented cameras and guests",
            "Documented rack, not a nest of adapters",
        ],
    },
    {
        "city": "sarasota",
        "service": "automation",
        "h1": "Home automation in Sarasota",
        "title": "Home Automation Sarasota FL | Control4, Lutron | LUMA",
        "description": "Sarasota home automation that unifies lighting, shades, climate, audio, and security on open platforms — Control4, Lutron, Josh.ai — not a dealer lock.",
        "lede": "Automation is the last layer, not the first. In Sarasota we will not sell you a processor until lighting, shades, climate, and the network are systems you could still live with if the fancy UI disappeared.",
        "paragraphs": [
            "Good morning should open selected shades, set the Ketra or warm-dim to morning, and start the kitchen zone at a volume you chose. Away should look lived-in, arm cameras, and not fight the HOA floodlight. We write those scenes in your words after watching how you actually use the house.",
            "Open platforms mean you are not hostage if you sell the house or leave us. That is the opposite of the black-box integrator pitch you have already heard on the Gulf Coast.",
        ],
        "bullets": [
            "Lutron as the lighting spine",
            "Control4 or Josh.ai when a unified UI is earned",
            "Climate, audio, and security as citizens, not add-ons",
            "Twelve months of scene care included",
        ],
        "sections": [   {   'h2': 'What home automation does in a Sarasota house',
                'text': [   'Good automation is a few scenes that run the house the way you already live '
                            'in it. Good morning opens selected shades and sets the kitchen lights and '
                            'music. Away closes the exterior screens, keeps a lived-in lighting pattern, '
                            'arms the cameras and sets the thermostats for an empty summer. Movie dims the '
                            'room and lowers the shades in one press.',
                            'Each scene uses systems that also work on their own: [Lutron '
                            'lighting](sa-sarasota-lighting), [motorized shades](sa-sarasota-shading), '
                            '[cameras](sa-sarasota-security), [whole-home audio](sa-sarasota-audio) and '
                            'the network under all of them.']},
            {   'h2': 'Control4, Lutron or Josh.ai',
                'text': [   'For many homes, Lutron keypads and the Lutron app are enough. When the house '
                            'has audio, video, climate and security to bring together, Control4 gives one '
                            'remote, one touchscreen and one app. Josh.ai adds voice control that '
                            'understands rooms and scenes without a cloud speaker in every room. We '
                            'recommend the smallest system that does the job, and open platforms so you '
                            'are not tied to one installer.']}],
        "faq": [   {   'q': 'What is the difference between a smart home and home automation?',
                'a': 'Smart devices each have their own app. Home automation ties lighting, shades, '
                     'climate, audio and security together so one button or one schedule sets the whole '
                     'house.'},
            {   'q': 'Can you automate an existing home without opening walls?',
                'a': 'Mostly yes. Wireless Lutron dimmers, battery or low-voltage shade motors and Wi-Fi '
                     'controllers cover most existing homes. Cameras and speakers need some cable, which '
                     'we route with as little patching as possible.'},
            {   'q': 'Can I control the house when I am up north for the summer?',
                'a': 'Yes. Lights, shades, thermostats and cameras can be checked and changed from your '
                     'phone, and Away scenes run on their own.'},
            {   'q': 'Do you serve Lakewood Ranch and Bradenton?',
                'a': 'Yes. We work across Sarasota and Manatee Counties. See [Lakewood '
                     'Ranch](sa-lakewood-ranch) and [Bradenton](sa-bradenton).'}],
    },
    {
        "city": "bradenton",
        "service": "lighting",
        "h1": "Lighting control in Bradenton",
        "title": "Lutron Lighting Installer Bradenton FL | LUMA Smart Home",
        "description": "Lutron RadioRA 3 and lighting scenes for Bradenton and Manatee County homes — lanai, landscape, and the rooms you actually use.",
        "lede": "Bradenton lighting jobs are often 'the switches never made sense after the remodel.' We overlay RadioRA 3, name the keypads in your words, and put the lanai on the same scene as the kitchen.",
        "paragraphs": [
            "River and bay lots pick up glare later than Siesta, but the lanai is still the living room. Path lights, under-eave, and interior loads belong on one keypad, not three apps. Existing Manatee electrical is usually a RadioRA 3 job; new Lakewood Ranch construction can go further if we catch the drawings.",
            "Same Sarasota studio, same line-item proposal. Manatee is not a 'service trip extra' we invent after you sign.",
        ],
        "bullets": [
            "RadioRA 3 overlays on existing Bradenton homes",
            "Lanai and landscape on interior scenes",
            "New-construction load schedules with the GC",
            "Warm-dim options where LEDs already look cheap",
        ],
    },
    {
        "city": "bradenton",
        "service": "security",
        "h1": "Home cameras in Bradenton",
        "title": "Home Security Cameras Bradenton FL | UniFi Protect | LUMA",
        "description": "On-premise UniFi cameras for Bradenton, Palmetto, and Anna Maria — no monthly cloud. Placed for lots, docks, and lock-and-leave.",
        "lede": "Manatee lots are often wider, dock-side, or island HOA. Consumer doorbells miss the side yard and bill you forever. We walk the property, mount PoE cameras, and leave the recorder in a closet you own.",
        "paragraphs": [
            "Anna Maria and Holmes Beach add association rules and salt. We bring cut sheets before we drill, and we use hardware that can live outside. Seasonal owners get remote view without a camera-brand subscription.",
            "The cameras only work if the network does. UniFi is the same stack we use in Sarasota; Bradenton is not a downgrade SKU.",
        ],
        "bullets": [
            "Property-walked camera plans",
            "Dock, side-yard, and drive coverage",
            "HOA-aware mounts on the islands",
            "On-prem NVR, optional alarm",
        ],
    },
    {
        "city": "longboat-key",
        "service": "shading",
        "h1": "Motorized shades on Longboat Key",
        "title": "Motorized Shades Longboat Key FL | Lanai Screens | LUMA",
        "description": "Motorized interior shades, blackout and exterior lanai screens for Longboat Key homes and condos. Salt-rated motors, Lutron Sivoia and Somfy, HOA-ready.",
        "lede": "On Longboat Key the view is the house, and the afternoon sun off the Gulf is the problem. Motorized shades let you keep the water in sight at 4 p.m. and still sleep in a dark room, without a wall of cords and remotes.",
        "paragraphs": [
            "We plan three layers. Interior roller shades with a solar-screen fabric take the glare and heat off the living room while the Gulf stays visible. Blackout shades or motorized drapery handle the bedrooms. Exterior motorized screens close the lanai against low western sun and insects, and roll away when the breeze is welcome.",
            "Everything is chosen for the barrier island: outdoor-rated motors and hardware on the lanai, fabrics picked for UV, and shades on a sunrise and sunset schedule so the house looks after itself while you are away for the summer.",
        ],
        "bullets": [
            "Interior solar screen, blackout and drapery",
            "Exterior motorized lanai screens, salt-rated",
            "Lutron Sivoia or Somfy, on one schedule",
            "Away mode for seasonal owners",
        ],
        "sections": [
            {"h2": "Condos and association rules", "text": [
                "Many Longboat Key buildings control what the exterior can show: screen colour, housing size, where a cassette can mount. We bring fabric samples and cut sheets to the board before ordering, and we measure each opening twice, because gulf-front openings are rarely square.",
            ]},
            {"h2": "Shades that work with the rest of the house", "text": [
                "If the lighting is Lutron, Sivoia shades share its keypads, so one button can lower the screens and set the evening lights. Somfy motors fit wide sliders and existing pockets. Either way the shades can join an Away scene with the [cameras and Wi-Fi](sa-longboat-key) the house already depends on. More on fabrics and layers in [motorized shades for Gulf Coast sun](journal-shades-gulf).",
            ]},
        ],
        "faq": [
            {"q": "Do exterior motorized screens survive salt air on Longboat Key?", "a": "With the right spec, yes. We use outdoor-rated motors and hardware and fabrics chosen for UV, and we plan for wind: screens retract on a schedule or a button before a storm."},
            {"q": "Can motorized shades be installed in an existing condo?", "a": "Yes. Battery or low-voltage motors fit most existing openings. We confirm what the association allows before anything is ordered."},
            {"q": "Can the shades close on their own when nobody is home?", "a": "Yes. They can follow sunrise and sunset for your address and an Away scene, so the furniture is protected all summer."},
        ],
    },
    {
        "city": "siesta-key",
        "service": "shading",
        "h1": "Motorized shades on Siesta Key",
        "title": "Motorized Shades Siesta Key FL | Blinds & Screens | LUMA",
        "description": "Motorized shades, blinds and exterior lanai screens for Siesta Key homes, condos and rentals. Lutron Sivoia and Somfy with salt-rated hardware.",
        "lede": "Siesta Key glass faces the Gulf, the sand reflects even more light back in, and a lot of homes change hands between owners and renters through the year. Motorized shades fix the glare and make the house simple for whoever is staying there.",
        "paragraphs": [
            "Interior roller shades with a solar-screen fabric are the everyday layer: they cut glare and heat and keep the beach in view. Bedrooms get blackout shades. Lanais get exterior motorized screens that drop at sunset and roll up when you want the breeze.",
            "For rentals and second homes, fewer buttons is better. Shades run on a schedule, a single keypad in each room covers the rest, and an Away scene closes the house between stays.",
        ],
        "bullets": [
            "Roller shades with solar-screen fabric",
            "Blackout for bedrooms and media rooms",
            "Exterior lanai screens with outdoor motors",
            "Simple keypads for guests and renters",
        ],
        "sections": [
            {"h2": "Built for the island", "text": [
                "Salt and wind decide the hardware. Outdoor-rated motors and brackets go on every exterior screen, and fabrics are chosen for UV. In condos and HOA communities we bring cut sheets and colour samples before ordering, so the exterior stays approved.",
            ]},
            {"h2": "With lighting and cameras", "text": [
                "Shades can share keypads with Lutron lighting and join an Away scene with on-premise cameras, so the house looks lived-in and protected when it is empty. See [smart home on Siesta Key](sa-siesta-key) and [motorized shades in Sarasota](sa-sarasota-shading).",
            ]},
        ],
        "faq": [
            {"q": "Motorized shades or motorized blinds for a Siesta Key house?", "a": "Usually roller shades with a solar-screen fabric. They keep the view, handle heat well and have fewer parts to suffer in salt air than tilting blinds."},
            {"q": "Are motorized shades a good idea for a rental?", "a": "Yes. Guests cannot break cords or lose remotes, and shades on a schedule protect floors and furniture from sun between stays."},
            {"q": "Do you install exterior lanai screens on Siesta Key?", "a": "Yes, with outdoor-rated motors and hardware, and with association approval when the building requires it."},
        ],
    },
    {
        "city": "sarasota",
        "service": "business-security",
        "camera": "business",
        "photo": "/assets/photos/stock/cameras-office-building-corner.jpg",
        "photo_alt": "Three security cameras on the corner of a dark-clad office building",
        "packages_h2": "Business security camera system packages in Sarasota",
        "h1": "Office and business security camera systems in Sarasota",
        "title": "Office Security Camera Systems Sarasota FL | UniFi | LUMA",
        "description": "Security camera systems for Sarasota offices, shops and small commercial spaces. UniFi Protect, wired PoE cameras, on-site recording, no per-camera fees.",
        "lede": "An office, a showroom or a small warehouse needs the same thing a good home system gives: clear video of the doors, the counter and the lot, recorded on site, and an app the owner can check from anywhere. We design and install UniFi Protect office security camera systems for small commercial spaces in Sarasota and Manatee County.",
        "paragraphs": [
            "Every job starts with a walk of the space: entrances, the register or front desk, stock rooms, the parking lot and the back door. Cameras are wired PoE, so there are no batteries and one cable carries power and video. Recording stays on a UniFi recorder in your building, with no monthly fee per camera.",
            "Business security camera systems start from $5,900 plus tax for eight cameras (Office 8) and from $12,900 plus tax for twelve or more (Business Pro). The packages are below; the final fixed price follows a free walk of the site.",
            "The cameras sit on their own network segment, separate from the office computers and guest Wi-Fi. If the network itself needs work, we do that in the same project. See [Wi-Fi and cabling in Sarasota](sa-sarasota-networking). Installation work is carried out with our Florida-licensed low-voltage partner.",
        ],
        "bullets": [
            "Offices, shops, showrooms and small warehouses",
            "Wired PoE cameras, on-site UniFi recorder",
            "No per-camera monthly fees or licences",
            "One app for owners and managers",
        ],
        "sections": [
            {"h2": "What a business camera system covers", "text": [
                "Entrances and exits with faces at a usable size, the point of sale or reception desk, stock and storage rooms, and the parking lot with vehicles in frame. We plan each camera for what it must capture, and we tell you where a camera would add little.",
                "Owners and managers get their own logins with the access they need. Footage can be found by time and by person or vehicle detection, and exported as a clip when an incident needs to be shared with an insurer or the police.",
            ]},
            {"h2": "Which UniFi camera goes where", "text": [
                "These are the current UniFi Protect models we specify for small commercial spaces. The right mix depends on the building, but most Sarasota offices and shops come down to the same handful of positions.",
            ], "table": {"head": ["Position", "Camera", "Why"], "rows": [
                ["Front door and lobby", "G6 Dome", "4K, IK10 vandal-resistant housing. Mounted low enough that faces fill the frame as people walk in."],
                ["Reception or register", "G6 Dome or G6 Mini Dome", "Overhead view of the counter, the cash drawer and the customer side."],
                ["Open office or sales floor", "AI Theta Pro", "A small 360° ceiling camera that covers a whole room without looking like surveillance. Indoor only."],
                ["Back door, hallways, stock room", "G6 Turret", "4K, IP66, infrared to about 98 ft. A good all-round camera for doors and corridors."],
                ["Parking lot and building sides", "G6 Pro Bullet", "4K with a larger sensor and 2.36× optical zoom, so a vehicle across the lot is still identifiable."],
                ["Lot entrance or gate", "AI LPR", "UniFi's licence plate camera. Reads plates at the entrance day and night; paired with a second camera for the vehicle itself."],
                ["Large lots and yards", "G6 PTZ", "Pan, tilt and 10× hybrid zoom for following a person or vehicle across open ground."],
            ]}, "after": [
                "Every one of these cameras records 4K, runs on a single PoE cable and does person and vehicle detection on the camera. The G6 and AI models also support face and licence plate recognition in UniFi Protect.",
            ]},
            {"h2": "How we size the recorder", "text": [
                "Storage is a simple calculation: number of cameras, times the bitrate each records at, times the hours per day it records, times the days you need to keep. Continuous 4K on every camera fills drives fastest; recording on detection, or keeping recent days at full quality and older days at lower quality, stretches the same drives much further.",
                "Most offices and shops ask for about 30 days. A lease, an insurer or your own policy may ask for more, so we confirm the number before choosing the recorder:",
            ], "table": {"head": ["Recorder", "Drive bays", "Up to (4K cameras)"], "rows": [
                ["UNVR Instant", "1", "6 cameras: a small office or a single shop"],
                ["UNVR", "4", "18 cameras: most offices, restaurants and retail"],
                ["UNVR Pro", "7", "24 cameras: larger sites and longer retention"],
                ["UNVR G2 Pro", "8", "50 cameras: multi-building sites and warehouses"],
            ]}, "after": [
                "The recorder goes in a locked closet or rack with the network equipment, on a battery backup so a power blip does not cost you footage. Drives run in RAID, so one failed drive does not lose the recordings.",
            ]},
            {"h2": "Camera systems by type of business", "text": [
                "The positions change with the business. We have written up the common layouts:",
            ], "bullets": [
                "[Retail store security cameras](sa-sarasota-retail-security-cameras): register, fitting rooms entrance, stock room and the front door",
                "[Restaurant security cameras](sa-sarasota-restaurant-security-cameras): host stand, bar, kitchen line, back door and deliveries",
                "[Warehouse security cameras](sa-sarasota-warehouse-security-cameras): dock doors, yard, aisles and the perimeter",
                "[HOA and condo security cameras](sa-sarasota-hoa-security-cameras): gates, pools, mail rooms and garages",
                "Medical, dental and professional offices: entrances, reception and records rooms, never treatment rooms",
                "Marinas and waterfront buildings: docks and gates, with cameras mounted under cover away from direct spray",
            ]},
            {"h2": "Homes and businesses on one stack", "text": [
                "Many owners also want cameras at home. UniFi Protect at home and at the office means one app for both. For the house, see [home and house security cameras in Sarasota](sa-sarasota-security), or the [security systems overview](security). In Manatee County, see [commercial security cameras in Bradenton](sa-bradenton-business-security).",
            ]},
        ],
        "faq": [
            {"q": "How much does a business security camera system cost in Sarasota?", "a": "Our packages start from $5,900 for 8 cameras (Office 8) and from $12,900 for 12 or more (Business Pro), plus tax. A small office with four cameras starts from $2,900. The final fixed price comes after a free walk of the site."},
            {"q": "Do business security cameras need a monthly subscription?", "a": "Not with UniFi Protect. Video records to a recorder in your building, and Ubiquiti charges no licence or per-camera fee."},
            {"q": "Can I watch the cameras from my phone?", "a": "Yes. Owners and managers can view live and recorded video in the UniFi Protect app, each with their own login."},
            {"q": "How many cameras does a small office need?", "a": "Usually 4 to 8: the front door, reception, the back door, any room with equipment or records, and one or two on the parking lot. We count them on the walkthrough, not from a floor plan."},
            {"q": "How long should a business keep security camera footage?", "a": "About 30 days is common for offices and shops. If an insurer, a lease or your own policy asks for longer, we size the recorder drives for it."},
            {"q": "Can the cameras read licence plates?", "a": "Yes. UniFi makes a dedicated licence plate camera, the AI LPR, for a lot entrance or gate. It works best where cars slow down and the camera can be mounted at a low angle."},
            {"q": "Do cameras survive salt air near the water?", "a": "UniFi outdoor cameras carry an IP66 weather rating. Near the Gulf or the bay we mount them under eaves or covers wherever we can and keep connections sealed."},
            {"q": "Do you install office cameras in Bradenton and Lakewood Ranch?", "a": "Yes. We cover Sarasota and Manatee Counties. See [commercial security cameras in Bradenton](sa-bradenton-business-security)."},
            {"q": "Can you also fix the office network and Wi-Fi?", "a": "Yes. Cameras depend on the network, so we can design both together: switching, Wi-Fi and a separate segment for the cameras. See [UniFi networking](networking)."},
            {"q": "Do the cameras record audio?", "a": "Audio is off by default. Florida requires the consent of everyone in a conversation before it is recorded (Fla. Stat. 934.03), so we leave camera microphones switched off."},
        ],
    },
    {
        "city": "bradenton",
        "service": "business-security",
        "camera": "business",
        "photo": "/assets/photos/stock/camera-pole-office-district.jpg",
        "photo_alt": "Security camera on a pole in front of an office building",
        "packages_h2": "Commercial camera packages",
        "h1": "Commercial security camera systems in Bradenton",
        "title": "Commercial Security Cameras Bradenton FL | UniFi | LUMA",
        "description": "Commercial security camera systems for Bradenton, Lakewood Ranch and Palmetto businesses. UniFi Protect, wired 4K cameras, on-site recorder, no monthly fees.",
        "lede": "Bradenton businesses range from storefronts on Manatee Avenue and offices in Lakewood Ranch to workshops and storage yards along the river and in Palmetto. We design and install UniFi Protect commercial security camera systems for them: wired 4K cameras, recording on a box you own, and no per-camera monthly fees.",
        "paragraphs": [
            "We are based in Sarasota and work across Manatee County. The process is the same as anywhere: we walk the site, mark each camera on a plan with what it has to capture, and send a line-item proposal. Installation work is carried out with our Florida-licensed low-voltage partner.",
            "A lot of Manatee County commercial property is spread out: a building, a yard, a fenced lot, sometimes a second building. That is where wired cameras earn their place. One cable per camera carries power and video, so there are no batteries to replace and no Wi-Fi links dropping across a yard.",
        ],
        "bullets": [
            "Offices, retail, workshops, yards and storage",
            "4K PoE cameras with on-camera person and vehicle detection",
            "On-site UniFi recorder sized for your retention",
            "Licence plate camera for gates and lot entrances",
        ],
        "sections": [
            {"h2": "Typical layouts in Manatee County", "text": [
                "Office suites and medical offices in Lakewood Ranch usually need the entrance, the reception desk, the back door and the parking lot. A G6 Dome at the door, a G6 Turret in the corridor and a G6 Pro Bullet on the lot covers most of them.",
                "Workshops, contractors' yards and storage lots need the perimeter and the gate. G6 Pro Bullets along the fence line, an AI LPR at the gate to record plates, and a G6 PTZ when the yard is large enough that someone has to follow a vehicle across it.",
                "Storefronts and restaurants on the main corridors need the register, the front door and the back door. See [retail store security cameras](sa-sarasota-retail-security-cameras) and [restaurant security cameras](sa-sarasota-restaurant-security-cameras) for those layouts.",
            ]},
            {"h2": "Recording and remote access", "text": [
                "Video records to a UniFi recorder on the property: a UNVR Instant for up to 6 cameras, a UNVR for up to 18, larger recorders above that. We size the drives for how many days you need to keep, commonly about 30, and put the recorder on a battery backup.",
                "Owners and managers view the cameras in the UniFi Protect app from anywhere, each with their own login. Clips can be exported and handed to an insurer or the police.",
            ]},
            {"h2": "Weather, salt and power", "text": [
                "Riverfront and island sites see salt air and summer storms. UniFi outdoor cameras are rated IP66; we mount them under eaves or covers where we can, seal cable entries, and protect the recorder and switch with a UPS so a brief outage does not leave gaps in the recording.",
            ]},
            {"h2": "Related pages", "text": [
                "The full camera-by-position table and recorder sizing are on [office security camera systems in Sarasota](sa-sarasota-business-security). For homes in Manatee County, see [home security cameras in Bradenton](sa-bradenton-security). For everything we do in the area, see [smart home installation in Bradenton](sa-bradenton).",
            ]},
        ],
        "faq": [
            {"q": "What does a commercial camera system cost in Bradenton?", "a": "The same as in Sarasota: from $5,900 for 8 cameras and from $12,900 for 12 or more, plus tax, with a fixed price after a free walk of the site."},
            {"q": "Do you install commercial security cameras in Bradenton?", "a": "Yes. We cover Bradenton, Lakewood Ranch, Palmetto, Ellenton, Parrish and the rest of Manatee County from our Sarasota base."},
            {"q": "Is there a monthly fee for the cameras?", "a": "No. UniFi Protect records to a recorder on your property and Ubiquiti charges no per-camera licence."},
            {"q": "Can you cover a yard or a gate far from the building?", "a": "Usually yes. Cameras up to about 300 ft of cable from a switch run on one cable; beyond that we add a switch closer to the camera or use fiber."},
            {"q": "Can the system record licence plates at our gate?", "a": "Yes, with the UniFi AI LPR camera aimed where vehicles slow down at the gate or entrance."},
            {"q": "Can we add cameras later?", "a": "Yes. We size the recorder and the switch with spare capacity so more cameras can be added without replacing the core."},
            {"q": "Do the cameras record audio?", "a": "No, audio is off by default. Florida requires everyone's consent to record a conversation (Fla. Stat. 934.03)."},
        ],
    },
    {
        "city": "sarasota",
        "service": "retail-security-cameras",
        "camera": "business",
        "photo": "/assets/photos/stock/camera-storefront-corner.jpg",
        "photo_alt": "Security camera hanging under the overhang of a white brick building",
        "packages_h2": "Camera packages for shops",
        "h1": "Retail store security cameras in Sarasota",
        "title": "Retail Store Security Cameras Sarasota FL | UniFi | LUMA",
        "description": "Security cameras for Sarasota retail stores and boutiques: register, entrance, sales floor and stock room. UniFi Protect, on-site recording, no monthly fees.",
        "lede": "A store needs four things from its cameras: a clear face at the door, a clear view of the register, the sales floor covered without blind aisles, and the stock room and back door recorded. We design UniFi Protect retail security camera systems for Sarasota shops and boutiques, from St. Armands and Main Street to the plazas along Tamiami Trail.",
        "paragraphs": [
            "Retail losses come from three directions: shoplifting on the floor, mistakes and theft at the register, and stock leaving by the back door. A good layout covers all three without turning the store into something that feels watched. Cameras are wired PoE and record to a recorder in the back office, with no monthly fee per camera. Installation work is carried out with our Florida-licensed low-voltage partner.",
        ],
        "bullets": [
            "Face-height camera at every customer entrance",
            "Overhead view of each register and cash drawer",
            "360° ceiling cameras for the sales floor",
            "Stock room and back door recorded around the clock",
        ],
        "sections": [
            {"h2": "Where the cameras go in a store", "text": [
                "This is the layout we start from for a typical Sarasota storefront, before the walkthrough changes it:",
            ], "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Customer entrance", "G6 Dome", "Every face coming in, at a size you could hand to the police."],
                ["Register", "G6 Mini Dome overhead", "The drawer, the screen and the customer's hands at the counter, angled away from the card reader's PIN pad."],
                ["Sales floor", "AI Theta Pro", "A 360° view of the floor from one small ceiling camera."],
                ["Fitting room corridor", "G6 Turret", "The corridor and entrance only. Never inside a fitting room."],
                ["Stock room and back door", "G6 Turret", "Who comes in and out, and deliveries arriving."],
                ["Storefront and parking", "G6 Pro Bullet", "The sidewalk, the lot and vehicles, with optical zoom for distance."],
            ]}},
            {"h2": "Finding the moment that matters", "text": [
                "Scrubbing through hours of video is where most store systems fail. UniFi Protect tags every person and vehicle the cameras see, so you can jump to the people who stood at the register between 2 and 3 pm, or every vehicle at the back door after closing. A clip can be exported in a few taps for a police report or an insurance claim.",
                "Managers and owners get separate logins. A store manager can see live video and the last week, while the owner sees everything, including other locations on the same app.",
            ]},
            {"h2": "Privacy rules a store has to respect", "text": [
                "Cameras never go inside fitting rooms or restrooms. Florida also requires consent from everyone in a conversation before it is recorded, so we leave camera microphones switched off in customer areas unless you have taken advice that says otherwise. A visible sign at the door that the premises are recorded is good practice and often deters on its own.",
            ]},
            {"h2": "Related pages", "text": [
                "The general camera-by-position guide and recorder sizing are on [office and business security camera systems in Sarasota](sa-sarasota-business-security). Restaurants have their own layout: [restaurant security cameras](sa-sarasota-restaurant-security-cameras). For the network the cameras run on, see [Wi-Fi and cabling in Sarasota](sa-sarasota-networking).",
            ]},
        ],
        "faq": [
            {"q": "What does a store camera system cost?", "a": "Our packages start from $2,900 for 4 cameras, $5,900 for 8 and $12,900 for 12 or more, plus tax. The fixed price for your store follows a free walk."},
            {"q": "How many cameras does a small retail store need?", "a": "A single-room boutique usually needs 4 to 6: the entrance, the register, one or two for the floor, and the stock room or back door."},
            {"q": "Can the cameras record audio at the register?", "a": "They can, but Florida requires everyone's consent to record a conversation, so we leave audio off in customer areas unless you have legal advice to use it."},
            {"q": "Is there a monthly fee?", "a": "No. Video records to a UniFi recorder in your store, with no per-camera subscription."},
            {"q": "Can I see more than one store in the same app?", "a": "Yes. Each location has its own recorder, and the owner sees all of them in the UniFi Protect app."},
        ],
    },
    {
        "city": "sarasota",
        "service": "restaurant-security-cameras",
        "camera": "business",
        "photo": "/assets/photos/stock/camera-storefront-corner.jpg",
        "photo_alt": "Security camera hanging under the overhang of a white brick building",
        "packages_h2": "Camera packages for restaurants",
        "h1": "Restaurant security cameras in Sarasota",
        "title": "Restaurant Security Cameras Sarasota FL | UniFi | LUMA",
        "description": "Security camera systems for Sarasota restaurants and bars: entrance, bar, POS, kitchen line, back door and deliveries. UniFi Protect, no monthly fees.",
        "lede": "A restaurant runs on cash, inventory and a back door that is open half the day. Its cameras have to cover the bar and the registers, the kitchen line, deliveries and the dumpster area, and still be useful at midnight when the owner wants to know who locked up. We install UniFi Protect restaurant security camera systems in Sarasota and Manatee County.",
        "paragraphs": [
            "Most of what owners ask us for is not about break-ins. It is about disputes at the register, a slip-and-fall claim, a delivery that came short, or a staff question that needs a clear answer. Cameras placed for those moments are different from cameras placed for a burglar. Installation work is carried out with our Florida-licensed low-voltage partner.",
        ],
        "bullets": [
            "Bar, POS stations and cash office",
            "Dining room and entrance for incident claims",
            "Kitchen line and walk-in cooler door",
            "Back door, deliveries and dumpster area",
        ],
        "sections": [
            {"h2": "Where the cameras go in a restaurant", "text": [
                "The starting layout for a typical Sarasota restaurant:",
            ], "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Entrance and host stand", "G6 Dome", "Faces on the way in, and the door at closing."],
                ["Bar and POS stations", "G6 Mini Dome overhead", "Pours, the register and the cash drawer."],
                ["Dining room", "AI Theta Pro or G6 180", "The floor between tables, for slip-and-fall and incident claims."],
                ["Kitchen line", "G6 Turret", "The line and the pass. Mounted away from fryer heat and grease."],
                ["Cash office and walk-in door", "G6 Turret", "Who opened the safe or the cooler, and when."],
                ["Back door and deliveries", "G6 Pro Bullet", "Vendors, deliveries and the dumpster area, with vehicles in frame."],
                ["Patio and parking", "G6 Pro Bullet", "Outdoor seating and the lot after dark."],
            ]}},
            {"h2": "Heat, grease and humidity", "text": [
                "Kitchens are hard on electronics. We keep cameras out of the hood plume, use sealed IP66 turrets where they can be wiped down, and route cable so it is not in the cleaning path. Outdoor patio cameras on the water get the same treatment as any Gulf Coast install: under cover where possible, sealed connections.",
            ]},
            {"h2": "Answers in minutes, not hours", "text": [
                "UniFi Protect marks every person and vehicle it detects, so finding the moment of a dispute is a search, not an evening of scrubbing. Managers can review from their phones; clips are exported for an insurer or the police in a few taps. Recording stays on a recorder in the office, so there is no monthly fee per camera.",
                "Audio is a special case. Florida requires consent from everyone in a conversation before it is recorded, so we leave camera microphones off in the dining room and bar unless you have taken legal advice.",
            ]},
            {"h2": "Related pages", "text": [
                "The general guide to [business security camera systems in Sarasota](sa-sarasota-business-security) covers recorder sizing and the full camera range. Shops have their own layout: [retail store security cameras](sa-sarasota-retail-security-cameras). For the guest Wi-Fi and the network behind the cameras, see [UniFi networking](networking).",
            ]},
        ],
        "faq": [
            {"q": "What does a restaurant camera system cost?", "a": "Most restaurants fit the Office 8 package, from $5,900 plus tax, or Business Pro for 12 or more cameras, from $12,900 plus tax. The fixed price follows a free walk of the restaurant."},
            {"q": "How many cameras does a restaurant need?", "a": "A small restaurant usually needs 8 to 12: the entrance, the bar and each POS, the dining room, the kitchen line, the cash office, the back door and the lot."},
            {"q": "Should restaurant cameras record audio?", "a": "In Florida we recommend no audio in guest areas, because recording a conversation requires everyone's consent."},
            {"q": "Can managers check the cameras from home?", "a": "Yes. Each manager gets a UniFi Protect login with the cameras and the history you choose."},
            {"q": "Will the cameras keep working in a hot kitchen?", "a": "Yes, if they are placed out of the direct heat and grease. We choose sealed turret cameras for kitchens and keep them out of the hood area."},
            {"q": "Is there a monthly fee?", "a": "No. Video records to a UniFi recorder in the restaurant, with no subscription and no per-camera fee."},
        ],
    },
    {
        "city": "sarasota",
        "service": "warehouse-security-cameras",
        "camera": "pro",
        "photo": "/assets/photos/stock/camera-pole-office-district.jpg",
        "photo_alt": "Security camera on a pole in front of an office building",
        "packages_h2": "Camera packages for warehouses and yards",
        "h1": "Warehouse security cameras in Sarasota",
        "title": "Warehouse Security Cameras Sarasota FL | UniFi | LUMA",
        "description": "Warehouse and yard security camera systems in Sarasota and Manatee: dock doors, aisles, yard, gate and plates. UniFi Protect 4K cameras, on-site recorder.",
        "lede": "A warehouse needs coverage where goods and vehicles move: dock doors, the yard, the gate, and the aisles where stock sits. We design UniFi Protect warehouse security camera systems for distribution space, workshops and storage buildings in Sarasota and Manatee County, with a licence plate camera at the gate and enough recorder for weeks of footage.",
        "paragraphs": [
            "Warehouses are big, tall and often dark at night. That changes the camera choice: longer infrared range, optical zoom for long aisles, and fewer, better cameras on the yard instead of many cheap ones. Every camera is wired, so there is nothing to recharge on a 30-foot ceiling. Installation work is carried out with our Florida-licensed low-voltage partner.",
        ],
        "bullets": [
            "Dock doors and loading bays",
            "Gate with licence plate recording",
            "Long aisles with optical zoom",
            "Yard and perimeter at night",
        ],
        "sections": [
            {"h2": "Where the cameras go in a warehouse", "text": [
                "The layout we start from:",
            ], "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Gate or yard entrance", "AI LPR + G6 Pro Bullet", "The plate on every vehicle in and out, and the vehicle itself."],
                ["Dock doors", "G6 Pro Bullet", "Trucks, pallets and people at each door, inside and out."],
                ["Aisles and racking", "G6 Pro Turret", "Long, narrow views down the aisle with optical zoom."],
                ["Open floor and staging", "G6 180", "A wide floor area from one mounting point."],
                ["Yard and perimeter", "G6 PTZ", "Following a person or vehicle across open ground at night."],
                ["Offices and entrances", "G6 Dome", "Faces at the staff and visitor doors."],
            ]}},
            {"h2": "Recorder and retention", "text": [
                "Warehouses usually have more cameras and need longer retention than an office, because a missing pallet is often noticed weeks later. That points to a UNVR Pro (up to 24 4K cameras) or a UNVR G2 Pro (up to 50) with large drives, recording continuously at the dock and gate and on detection elsewhere.",
                "The recorder and switches go on a battery backup. Cameras far from the building get their own switch or a fiber run, since a copper network cable stops at about 300 ft.",
            ]},
            {"h2": "Plates, vehicles and search", "text": [
                "UniFi's AI LPR camera is built for plate capture at entrances, where vehicles slow down. Mounted low and at a shallow angle, it records the plate of every vehicle through the gate, and Protect lets you search footage by plate or by vehicle detection. A second camera next to it records the vehicle and driver.",
                "Plate data stays on your recorder. There is no cloud service and no per-camera subscription, and nothing is shared with third parties unless you export a clip.",
            ]},
            {"h2": "Related pages", "text": [
                "The full camera range and recorder sizing are on [office and business security camera systems in Sarasota](sa-sarasota-business-security). In Manatee County, see [commercial security cameras in Bradenton](sa-bradenton-business-security). For long cable runs, fiber and the network, see [Wi-Fi and cabling in Sarasota](sa-sarasota-networking).",
            ]},
        ],
        "faq": [
            {"q": "What does a warehouse camera system cost?", "a": "Warehouses usually start with Business Pro: 12 or more cameras, a plate camera at the gate and a UNVR G2 Pro recorder, from $12,900 plus tax. The fixed price follows a free walk of the site."},
            {"q": "How far can a warehouse camera see at night?", "a": "It depends on the model. The G6 Turret's infrared reaches about 98 ft and the G6 Pro Bullet's about 130 ft; large yards are covered with a PTZ or extra lighting."},
            {"q": "Can the system read licence plates at our gate?", "a": "Yes, with the UniFi AI LPR camera, mounted where vehicles slow down and at a low angle to the plate."},
            {"q": "How long should a warehouse keep footage?", "a": "Longer than an office, because losses are found later. We size the recorder for the number of days you choose."},
            {"q": "Do the cameras need Wi-Fi in the warehouse?", "a": "No. Every camera is wired PoE back to a switch, which is more reliable than Wi-Fi across racking and metal walls."},
            {"q": "Is there a monthly fee?", "a": "No. Footage and plate data stay on your recorder, with no subscription and no per-camera fee."},
        ],
    },
    {
        "city": "sarasota",
        "service": "hoa-security-cameras",
        "camera": "pro",
        "photo": "/assets/photos/stock/cameras-office-building-corner.jpg",
        "photo_alt": "Three security cameras on the corner of a dark-clad building",
        "packages_h2": "Camera packages for associations",
        "h1": "HOA and condo security cameras in Sarasota",
        "title": "HOA & Condo Security Cameras Sarasota FL | UniFi | LUMA",
        "description": "Security cameras for Sarasota HOAs and condo associations: gates, pools, mail rooms, garages and clubhouses. UniFi Protect with on-site recording, no fees.",
        "lede": "A community association needs cameras where residents share space: the gate, the pool, the mail room, the garage and the clubhouse. It also needs a system the board can explain to residents, with clear rules on who sees the footage. We install UniFi Protect HOA and condo security camera systems in Sarasota, Lakewood Ranch and Manatee County.",
        "paragraphs": [
            "The questions boards ask us are mostly about policy, not hardware: which areas can be recorded, who on the board or the management company gets access, how long footage is kept, and how a resident asks for a clip after a car is scratched in the garage. We help put the system together so those answers are simple. Installation work is carried out with our Florida-licensed low-voltage partner.",
        ],
        "bullets": [
            "Gates with licence plate recording",
            "Pools, mail rooms and clubhouses",
            "Parking garages and lots",
            "Separate logins for the board and management",
        ],
        "sections": [
            {"h2": "Where the cameras go in a community", "text": [
                "A starting layout for a gated community or condo building:",
            ], "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Entry and exit gates", "AI LPR + G6 Pro Bullet", "Plates of every vehicle and the vehicle itself, day and night."],
                ["Pool and pool gate", "G6 Pro Bullet", "The deck and the gate, for incidents and after-hours use."],
                ["Mail and package room", "G6 Dome", "Faces at the door and who takes which package."],
                ["Lobby and elevators", "G6 Dome", "Entrances and the elevator lobby, vandal-resistant housing."],
                ["Parking garage", "G6 Turret", "Drive aisles and stairwell doors, infrared for low light."],
                ["Clubhouse and fitness room", "AI Theta Pro", "A discreet 360° ceiling view of shared rooms."],
            ]}},
            {"h2": "Policy first, then cameras", "text": [
                "Cameras belong in common areas only, never pointed into a unit, a balcony or a window. Florida requires consent from everyone in a conversation before it is recorded, so association cameras run with audio off. Signs at the entrances say the common areas are recorded.",
                "Before we install, the board decides who can view live video, who can export clips, and how many days are kept. UniFi Protect gives each person their own login with only the cameras and history the board allows, and keeps the footage on a recorder in the building rather than a vendor's cloud. Your association's attorney should approve the written policy; we make sure the system matches it.",
            ]},
            {"h2": "Island and waterfront buildings", "text": [
                "On Siesta Key, Longboat Key and the bayfront, salt air and wind are the main enemies. UniFi outdoor cameras are IP66 rated; we mount them under overhangs where we can, seal every connection, and put the recorder in a conditioned room with a battery backup.",
            ]},
            {"h2": "Related pages", "text": [
                "The camera range and recorder sizing are on [business security camera systems in Sarasota](sa-sarasota-business-security). For cameras at a private home, see [security camera installation in Sarasota](sa-sarasota-security). The gate and building network is covered in [Wi-Fi and cabling in Sarasota](sa-sarasota-networking).",
            ]},
        ],
        "faq": [
            {"q": "What does an HOA camera system cost?", "a": "A gate with a plate camera plus the pool, mail room and garage usually means Business Pro, from $12,900 plus tax. Smaller buildings can start from Office 8, from $5,900 plus tax. The board gets a fixed price after a free walk."},
            {"q": "Can an HOA put security cameras in common areas in Florida?", "a": "Common areas such as gates, pools and mail rooms are usually recorded with the board's approval and posted signs. Your association's attorney should approve the written camera policy."},
            {"q": "Can HOA cameras record audio?", "a": "We install them with audio off. Florida requires everyone's consent to record a conversation."},
            {"q": "Who can see the footage?", "a": "Only the people the board names. Each gets a UniFi Protect login limited to the cameras and history they are allowed."},
            {"q": "Is there a monthly fee for the association?", "a": "No per-camera fee. Footage records to a recorder in the building."},
            {"q": "Can the gate camera read licence plates?", "a": "Yes. UniFi's AI LPR camera records plates at the gate, and footage can be searched by plate."},
            {"q": "Where is the licence plate data stored?", "a": "On the association's own recorder in the building. There is no cloud plate database and no yearly per-camera fee, and plates are not shared with anyone unless the board exports a clip."},
        ],
    },
]

ARTICLES = [
    {
        "id": "journal-smart-home-sarasota",
        "slug": "smart-home-sarasota",
        "title": "What a Gulf Coast Smart Home Actually Needs | LUMA Journal",
        "h1": "What a smart home on the Gulf Coast actually needs",
        "description": "A practical definition of a smart home on Florida’s Gulf Coast: sun, salt, seasonal occupancy, and systems you still own. From LUMA in Sarasota.",
        "og": "/assets/og/service-areas.jpg",
        "date": "2026-08-27",
        "category": "Smart home",
        "dek": "Lighting, shades, a network and cameras that cope with gulf light, humidity and a summer away. Here is where we start.",
        "blocks": [
            {"type": "p", "text": "Most of what is sold as a smart home is written for a house in a mild climate that is lived in all year. A house on the Gulf Coast is neither. The sun comes in low and hot across the water, the humidity gets into closets, and a lot of owners are away for months at a time. This is what we think a system here actually has to do."},
            {"type": "h2", "text": "Start with the hour, not the app"},
            {"type": "p", "text": "Gulf light is the brief. West glass from mid-afternoon, a lanai that is the living room, and a sky that goes gold then ink. A useful system dims and warms with that hour, drops solar screens before the sofa cooks, and does not leave the dock lights on until a neighbor texts. That is lighting control and motorized shades on a clock and occupancy — Lutron and Sivoia or Somfy — not a rainbow of consumer bulbs."},
            {"type": "h2", "text": "The network is the house"},
            {"type": "p", "text": "Cameras, audio, keypads, and thermostats all inherit the Wi-Fi. A single gateway in a hot laundry room is why 'the smart home' drops every storm season. UniFi, a wired spine where we can hide it, and a UPS on the rack are unglamorous and non-negotiable. If you only do one upgrade, do this one."},
            {"type": "h2", "text": "Seasonal occupancy is a first-class mode"},
            {"type": "p", "text": "Away should look lived-in, arm cameras, and close the elevations that take weather — without a monthly fee to rent your own driveway from a doorbell brand. On-premise UniFi Protect is how we do that. Lock-and-leave is normal on Siesta, Longboat, and Anna Maria; the system should assume you might be gone for months."},
            {"type": "h2", "text": "Open platforms, line-item paper"},
            {"type": "p", "text": "Dealer-locked processors are how Gulf Coast homeowners get stuck. We specify Lutron, UniFi, Somfy, Sonos, Control4, Josh.ai — professional gear with a service path if you ever leave us. Proposals list devices and labor. That is the opposite of a bundled mystery."},
            {"type": "p", "text": "If you want to see how that plays out in a real house, the [Sarasota page](sa-sarasota) and [our work](work) are the next step, or [book a walkthrough](contact)."},
        ],
    },
    {
        "id": "journal-lutron-sarasota",
        "slug": "lutron-installer-sarasota",
        "title": "Lutron in Sarasota: RadioRA 3 vs HomeWorks | LUMA Journal",
        "h1": "Choosing Lutron in a Sarasota house",
        "description": "When RadioRA 3 is enough, when Sarasota homes need HomeWorks or Ketra, and what a Lutron installer should put on the proposal. LUMA Smart Home.",
        "og": "/assets/photos/lighting-lutron-hero.jpg",
        "date": "2026-09-03",
        "category": "Lighting",
        "dek": "Most finished Sarasota houses need an overlay, not a processor palace. Here is how we decide.",
        "blocks": [
            {"type": "p", "text": "Lutron is the lighting spine we trust on the Gulf Coast: keypads that still make sense if the phone is dead, dimming that does not buzz, and a dealer network that will still exist when the consumer hub of the year does not. The useful question is not whether to use Lutron but which Lutron, and that depends on the house you already have."},
            {"type": "h2", "text": "RadioRA 3 for the house that already exists"},
            {"type": "p", "text": "If the electrical is closed and you are tired of a wall of dimmers, RadioRA 3 is usually the honest job. We replace the controls, add occupancy where hallways deserve it, and put the lanai on the same scene as the kitchen. You get phone control without fishing a HomeWorks processor into a closet that cannot cool it."},
            {"type": "h2", "text": "HomeWorks and Ketra when the architecture is doing the work"},
            {"type": "p", "text": "Deep remodels, new construction, and rooms where color temperature is part of the design — Ketra, or a HomeWorks enclosure with a real load schedule. That is a different drawing set, coordinated with the lighting designer and the electrician before drywall. We will not upsell it onto a 2,400 sq ft condo because the pitch sounds premium."},
            {"type": "h2", "text": "What should be on the paper"},
            {"type": "ul", "items": [
                "Every keypad, load, and processor — priced",
                "Which elevations get warm-dim or Ketra, and why",
                "How landscape and path lighting join interior scenes",
                "Who programs Good morning / Away / Evening, and how you change it later",
            ]},
            {"type": "p", "text": "We spec it, program it and stay after the install. More on [lighting control in Sarasota](sa-sarasota-lighting), or [start a project](contact)."},
        ],
    },
    {
        "id": "journal-shades-gulf",
        "slug": "motorized-shades-gulf-coast",
        "title": "Motorized shades for Gulf Coast sun | LUMA Journal",
        "h1": "Motorized shades that respect Gulf Coast sun",
        "description": "Why Sarasota and Manatee west glass needs layered motorized shades — solar screen, blackout, Sivoia or Somfy — not one fabric and a remote in a drawer.",
        "og": "/assets/photos/hero-shading.jpg",
        "date": "2026-09-10",
        "category": "Shading",
        "dek": "The view is why you bought the house. The infrared is why the sofa is fading. Both can be true.",
        "blocks": [
            {"type": "p", "text": "Gulf-west elevations in Sarasota, Longboat, Siesta, and Anna Maria do not need 'window treatments' as decoration first. They need a solar-screen layer that keeps the water visible and a blackout layer that lets someone sleep after a late dinner. One dual-purpose fabric usually fails both jobs."},
            {"type": "h2", "text": "Sivoia when lighting is already Lutron"},
            {"type": "p", "text": "If the house is on RadioRA or HomeWorks, Lutron Sivoia QS keeps shades on the same keypad and clock as the lights. That is how sunset can drop the screens and warm the dining room without two apps arguing."},
            {"type": "h2", "text": "Somfy when the opening is the constraint"},
            {"type": "p", "text": "Wide lanai volumes, existing pockets, and outdoor rollers often land on Somfy. It is not a downgrade; it is the motor that fits. We still program astronomical clocks and Away. Salt-rated hardware is in the spec for barrier islands — indoor motors on a gulf lanai are how you buy the job twice."},
            {"type": "h2", "text": "HOA and glass"},
            {"type": "p", "text": "What the street is allowed to see matters in Siesta Key and Longboat Key design review. We bring fabric and exterior-roller cut sheets early. Measuring gulf-front openings twice is cheaper than a motor that racks in an out-of-square pocket."},
            {"type": "p", "text": "More on [motorized shades in Sarasota](sa-sarasota-shading), or on the islands: [motorized shades on Siesta Key](sa-siesta-key-shading) and [motorized shades on Longboat Key](sa-longboat-key-shading)."},
        ],
    },
    {
        "id": "journal-theater-sarasota",
        "slug": "home-theater-sarasota",
        "title": "Sarasota Home Theater: Cinema Room vs Media Suite | LUMA",
        "h1": "A home theater that survives Florida construction",
        "description": "How to decide between a dedicated cinema and a media suite in a Sarasota house — acoustics, CBS, tile, and calibration. LUMA Smart Home.",
        "og": "/assets/photos/hero-theater.jpg",
        "date": "2026-09-17",
        "category": "Home theater",
        "dek": "A projector and a dark paint chip are not a theater. Tile and CBS will tell you that on night one.",
        "blocks": [
            {"type": "p", "text": "Sarasota bonus rooms over the garage are the usual candidate. Sometimes they become a cinema. Sometimes they should stay a media suite with a serious display, two good speakers, and lighting that can actually go down. We would rather say that in week one than calibrate a room that cannot hold bass."},
            {"type": "h2", "text": "What Florida does to sound"},
            {"type": "p", "text": "CBS, tile, and sliders are reflective. Dedicated rooms get absorption, bass management, and a door that closes. Media suites get honesty about what the sliders will do to dialogue. Either way, lighting and shades are part of Play — not a separate remote hunt when the movie starts."},
            {"type": "h2", "text": "Calibration is a file, not a vibe"},
            {"type": "p", "text": "We measure. You keep the file. If a prior installer 'set it by ear' with a demo disc, that is not a theater we will put our name on until we run the room again."},
            {"type": "p", "text": "More on [home theater design in Sarasota](sa-sarasota-theaters), and the theaters in [our work](work)."},
        ],
    },
    {
        "id": "journal-not-luma-com",
        "slug": "luma-smart-home-not-luma-com",
        "title": "LUMA Smart Home is not luma.com, Luma AI, or Luma cameras",
        "h1": "If you searched LUMA and landed in the wrong place",
        "description": "LUMA Smart Home is a Sarasota, Florida residential technology studio. We are not luma.com (events), not Luma AI / Luma Labs, and not Snap One Luma cameras.",
        "og": "/assets/photos/sarasota-marina.jpg",
        "date": "2026-08-24",
        "category": "About LUMA",
        "dek": "Three other products share a word. This is the integrator on Florida’s Gulf Coast.",
        "blocks": [
            {"type": "p", "text": "LUMA Smart Home (lumasmarthome.com) designs and installs lighting control, motorized shades, audio, security, and networking for homes in Sarasota and Manatee Counties. Phone +1 (941) 431-4640. Email hello@lumasmarthome.com."},
            {"type": "h2", "text": "We are not luma.com"},
            {"type": "p", "text": "luma.com is an events and invitation platform. If you are trying to RSVP, host a gathering, or find an event link, that is a different company. We do not run events software."},
            {"type": "h2", "text": "We are not Luma AI or Luma Labs"},
            {"type": "p", "text": "Luma AI (lumalabs.ai) builds generative video and 3D tools. If you searched for Dream Machine or a Luma Labs login, you want them. We install Lutron and UniFi in houses."},
            {"type": "h2", "text": "We are not Snap One Luma cameras"},
            {"type": "p", "text": "Snap One sells a camera line named Luma, often through security dealers. If you have a Luma NVR sticker on a box in a closet, that is hardware we did not manufacture. When we spec cameras, we use UniFi Protect on-premise — your footage on your property. We can still look at an existing Snap One system and tell you whether to keep it."},
            {"type": "h2", "text": "How to know you found the studio"},
            {"type": "ul", "items": [
                "The site is lumasmarthome.com",
                "The place is Sarasota, Florida",
                "The work is lighting, shades, AV, cameras, Wi-Fi",
                "The phone is (941) 431-4640",
            ]},
            {"type": "p", "text": "The longer entity page is [LUMA Smart Home Sarasota](luma-smart-home-sarasota). If you actually wanted lighting or a walkthrough, go to [service areas](service-areas) or [contact](contact)."},
        ],
    },
    {
        "id": "journal-cameras-fees",
        "slug": "home-cameras-without-monthly-fees",
        "title": "Home cameras without a monthly cloud | LUMA Journal",
        "h1": "Cameras you own, footage you keep",
        "description": "Why LUMA specs UniFi Protect instead of doorbell brands that charge a monthly fee for your own driveway. On-premise recorder, no required cloud.",
        "og": "/assets/photos/hero-security-v2.jpg",
        "date": "2026-09-24",
        "category": "Security",
        "dek": "Seasonal Gulf Coast homes should not pay a subscription all summer to watch an empty lot.",
        "blocks": [
            {"type": "p", "text": "The default 'home camera' pitch is a cute doorbell, a cloud, and a price that returns every month. For a Siesta lock-and-leave or a Longboat seasonal house, that is rent on an empty driveway. We spec UniFi Protect: PoE cameras, a recorder in a closet you own, remote view when you want it."},
            {"type": "h2", "text": "Placement is the product"},
            {"type": "p", "text": "Sunset glare on Bird Key and foliage on a Manatee lot will beat a camera that was drawn in plan view. We walk the property. We will also tell you where a camera is wasted because the HOA or the neighbor angle makes it pointless."},
        ],
    },
]

BRAND = {
    "id": "luma-smart-home-sarasota",
    "path": "/luma-smart-home-sarasota",
    "file": "luma-smart-home-sarasota.html",
    "title": "LUMA Smart Home Sarasota | Not luma.com or Luma AI",
    "h1": "LUMA Smart Home — Sarasota residential technology",
    "description": "LUMA Smart Home is a Sarasota, FL integrator for lighting, shades, AV, security and Wi-Fi. Not luma.com, Luma AI or Snap One Luma cameras.",
    "og": "/assets/photos/sarasota-marina.jpg",
    "lede": "This is the local studio. If a search for LUMA sent you to an events app, a video model, or a camera brand, read [the explainer](journal-not-luma-com) or [where we work](service-areas).",
}

NAP = {
    "name": "LUMA Smart Home",
    "legalName": "Tegra-Media LLC",
    "locality": "Sarasota",
    "region": "FL",
    "country": "US",
    "telephoneDisplay": "+1 (941) 431-4640",
    "telephone": "+1-941-431-4640",
    "telHref": "tel:+19414314640",
    "email": "hello@lumasmarthome.com",
    "hours": "Mon–Sat · 9am – 6pm",
    "area": "Sarasota & Manatee Counties",
    "mapsUrl": "https://www.google.com/maps/search/?api=1&query=LUMA+Smart+Home+Sarasota+FL",
    "mapsLabel": "LUMA Smart Home — Sarasota, Florida (Google Maps)",
}

HUB = {
    "id": "service-areas",
    "path": "/service-areas",
    "file": "service-areas.html",
    "title": "Service Areas | Sarasota & Manatee | LUMA Smart Home",
    "h1": "Where we work",
    "description": "LUMA Smart Home serves Sarasota and Manatee Counties: Sarasota, Bradenton, Lakewood Ranch, Venice, Siesta Key, Longboat Key, Anna Maria Island and Palmetto.",
    "og": "/assets/photos/sarasota-downtown-bayfront.jpg",
    "lede": "Two counties, one studio in Sarasota. Each place below has its own page: the kind of houses we find there and what they usually need.",
}

JOURNAL_HUB = {
    "id": "journal",
    "path": "/journal",
    "file": "journal.html",
    "title": "Journal | Smart Home Sarasota Notes | LUMA",
    "h1": "Notes from the studio",
    "description": "Practical writing from LUMA Smart Home: smart home Sarasota, Lutron, motorized shades, theaters, and how we differ from luma.com and other Lumas.",
    "og": "/assets/photos/gulf-sunset.jpg",
    "lede": "Notes from the studio on lighting, shades, theaters, cameras and networks in Gulf Coast houses.",
}


def city_by_id(city_id: str) -> dict:
    for city in CITIES:
        if city["id"] == city_id:
            return city
    raise KeyError(city_id)


def extra_routes() -> list[dict]:
    routes: list[dict] = []
    routes.append(
        {
            "id": HUB["id"],
            "path": HUB["path"],
            "file": HUB["file"],
            "title": HUB["title"],
            "description": HUB["description"],
            "h1": HUB["h1"],
            "og_image": HUB["og"],
            "priority": 0.85,
            "changefreq": "monthly",
            "kind": "areas-hub",
            "index": True,
            "paragraphs": [HUB["lede"]],
        }
    )
    for city in CITIES:
        routes.append(
            {
                "id": f"sa-{city['id']}",
                "path": f"/service-areas/{city['id']}",
                "file": f"service-areas/{city['id']}.html",
                "title": city["title"],
                "description": city["description"],
                "h1": city["h1"],
                "og_image": city["image"],
                "priority": 0.8 if city["id"] == "sarasota" else 0.7,
                "changefreq": "monthly",
                "kind": "city",
                "city": city["id"],
                "city_name": city["name"],
                "index": True,
                "paragraphs": [city["lede"], *city["paragraphs"]],
            }
        )
    for row in CITY_SERVICES:
        city = city_by_id(row["city"])
        svc = SERVICES[row["service"]]
        routes.append(
            {
                "id": f"sa-{row['city']}-{row['service']}",
                "path": f"/service-areas/{row['city']}/{row['service']}",
                "file": f"service-areas/{row['city']}/{row['service']}.html",
                "title": row["title"],
                "description": row["description"],
                "h1": row["h1"],
                "og_image": svc["og"],
                "priority": 0.75 if row["city"] == "sarasota" else 0.65,
                "changefreq": "monthly",
                "kind": "city-service",
                "city": row["city"],
                "city_name": city["name"],
                "service": row["service"],
                "service_name": svc["name"],
                "index": True,
                "paragraphs": [row["lede"], *row["paragraphs"]],
            }
        )
    routes.append(
        {
            "id": JOURNAL_HUB["id"],
            "path": JOURNAL_HUB["path"],
            "file": JOURNAL_HUB["file"],
            "title": JOURNAL_HUB["title"],
            "description": JOURNAL_HUB["description"],
            "h1": JOURNAL_HUB["h1"],
            "og_image": JOURNAL_HUB["og"],
            "priority": 0.7,
            "changefreq": "weekly",
            "kind": "journal-hub",
            "index": True,
            "paragraphs": [JOURNAL_HUB["lede"]],
        }
    )
    for art in ARTICLES:
        paras = [b["text"] for b in art["blocks"] if b["type"] == "p"]
        routes.append(
            {
                "id": art["id"],
                "path": f"/journal/{art['slug']}",
                "file": f"journal/{art['slug']}.html",
                "title": art["title"],
                "description": art["description"],
                "h1": art["h1"],
                "og_image": art["og"],
                "priority": 0.65,
                "changefreq": "monthly",
                "kind": "article",
                "datePublished": art["date"],
                "index": True,
                "paragraphs": [art["dek"], *paras],
            }
        )
    routes.append(
        {
            "id": BRAND["id"],
            "path": BRAND["path"],
            "file": BRAND["file"],
            "title": BRAND["title"],
            "description": BRAND["description"],
            "h1": BRAND["h1"],
            "og_image": BRAND["og"],
            "priority": 0.8,
            "changefreq": "monthly",
            "kind": "brand",
            "index": True,
            "paragraphs": [BRAND["lede"]],
        }
    )
    return routes


def _page_label(page_id: str) -> str:
    static = {
        "home": "Home",
        "service-areas": "All service areas",
        "journal": "Journal",
        "contact": "Start a project",
        "work": "Our work",
        "about": "About the studio",
        "budget-calculator": "Budget calculator",
        "luma-smart-home-sarasota": "This LUMA, not the others",
        "journal-smart-home-sarasota": "What smart home Sarasota means",
        "journal-lutron-sarasota": "Choosing Lutron in Sarasota",
        "journal-shades-gulf": "Motorized shades for Gulf sun",
        "journal-theater-sarasota": "Home theater in Sarasota",
        "journal-not-luma-com": "Not luma.com / Luma AI / Luma cameras",
        "journal-cameras-fees": "Cameras without a monthly cloud",
    }
    if page_id in static:
        return static[page_id]
    if page_id in SERVICES:
        return SERVICES[page_id]["nav"]
    for city in CITIES:
        if page_id == f"sa-{city['id']}":
            return f"{city['name']} smart home"
    for row in CITY_SERVICES:
        if page_id == f"sa-{row['city']}-{row['service']}":
            return row["h1"]
    for art in ARTICLES:
        if page_id == art["id"]:
            return art["h1"]
    return page_id


def _rel(*ids: str) -> list[dict]:
    seen = set()
    out = []
    for i in ids:
        if not i or i in seen:
            continue
        seen.add(i)
        out.append({"id": i, "label": _page_label(i)})
    return out


def related_map() -> dict:
    """In-content 'keep reading' links so every URL passes equity to neighbors."""
    rel: dict[str, list[dict]] = {}
    journal_for = {
        "lighting": "journal-lutron-sarasota",
        "shading": "journal-shades-gulf",
        "theaters": "journal-theater-sarasota",
        "security": "journal-cameras-fees",
        "audio": "journal-smart-home-sarasota",
        "networking": "journal-smart-home-sarasota",
        "automation": "journal-smart-home-sarasota",
    }
    for sid in SERVICES:
        if SERVICES[sid]["page"] != sid:
            continue  # no top-level page of its own (business-security)
        combo = f"sa-sarasota-{sid}"
        rel[sid] = _rel(
            combo,
            "sa-sarasota",
            journal_for.get(sid, "journal-smart-home-sarasota"),
            "service-areas",
            "journal",
            "contact",
        )
    rel["service-areas"] = _rel(
        "sa-sarasota",
        "sa-bradenton",
        "sa-lakewood-ranch",
        "journal-smart-home-sarasota",
        "luma-smart-home-sarasota",
        "journal",
        "contact",
    )
    rel["journal"] = _rel(
        "journal-smart-home-sarasota",
        "journal-lutron-sarasota",
        "journal-not-luma-com",
        "sa-sarasota",
        "luma-smart-home-sarasota",
        "contact",
    )
    rel["luma-smart-home-sarasota"] = _rel(
        "journal-not-luma-com",
        "about",
        "sa-sarasota",
        "service-areas",
        "contact",
    )
    rel["about"] = _rel("luma-smart-home-sarasota", "service-areas", "journal", "work", "contact")
    rel["work"] = _rel("sa-sarasota", "sa-bradenton", "service-areas", "contact")
    rel["contact"] = _rel("service-areas", "budget-calculator", "sa-sarasota", "journal")
    rel["designers"] = _rel("contact", "work", "lighting", "service-areas")
    rel["support"] = _rel("contact", "about")
    rel["budget-calculator"] = _rel("contact", "lighting", "service-areas")
    for case, city in (
        ("case-spacious", "work"),
        ("case-urban", "sa-sarasota"),
        ("case-family", "work"),
        ("case-modern", "work"),
        ("case-bighouse", "work"),
    ):
        rel[case] = _rel(city, "work", "contact", "service-areas")
    for city in CITIES:
        ids = [f"sa-{city['id']}-{row['service']}" for row in CITY_SERVICES if row["city"] == city["id"]]
        extra = ["lighting", "service-areas", "journal", "contact"]
        if city["id"] == "sarasota":
            extra = [
                "journal-smart-home-sarasota",
                "journal-lutron-sarasota",
                "luma-smart-home-sarasota",
                "work",
                "contact",
            ]
        elif city["id"] == "siesta-key":
            extra = ["journal-shades-gulf", "sa-sarasota", "contact"]
        rel[f"sa-{city['id']}"] = _rel(*ids, *extra)
    business = {"business-security", *[k for k, v in SERVICES.items() if v.get("listed") is False]}
    for row in CITY_SERVICES:
        pid = f"sa-{row['city']}-{row['service']}"
        if row["service"] in business:
            rel[pid] = _rel(
                "sa-sarasota-business-security",
                "sa-bradenton-business-security",
                *[f"sa-sarasota-{k}" for k in sorted(business - {"business-security"})],
                "sa-sarasota-security",
                "sa-sarasota-networking",
                "contact",
            )
            rel[pid] = [r for r in rel[pid] if r["id"] != pid]
            continue
        rel[pid] = _rel(
            SERVICES[row["service"]]["page"],
            f"sa-{row['city']}",
            journal_for.get(row["service"], "journal-smart-home-sarasota"),
            "service-areas",
            "work",
            "contact",
        )
    rel["journal-smart-home-sarasota"] = _rel(
        "sa-sarasota",
        "sa-sarasota-lighting",
        "luma-smart-home-sarasota",
        "journal",
        "contact",
    )
    rel["journal-lutron-sarasota"] = _rel("sa-sarasota-lighting", "lighting", "sa-sarasota", "contact")
    rel["journal-shades-gulf"] = _rel(
        "sa-sarasota-shading", "sa-siesta-key-shading", "sa-longboat-key-shading", "shading", "contact"
    )
    rel["journal-theater-sarasota"] = _rel("sa-sarasota-theaters", "theaters", "work", "contact")
    rel["journal-not-luma-com"] = _rel(
        "luma-smart-home-sarasota", "sa-sarasota", "journal-cameras-fees", "contact"
    )
    rel["journal-cameras-fees"] = _rel(
        "sa-sarasota-security", "security", "journal-not-luma-com", "contact"
    )
    return rel


def geo_payload() -> dict:
    return {
        "hub": HUB,
        "journalHub": JOURNAL_HUB,
        "brand": BRAND,
        "nap": NAP,
        "services": SERVICES,
        "cities": {c["id"]: c for c in CITIES},
        "cityServices": {
            f"{row['city']}/{row['service']}": row for row in CITY_SERVICES
        },
        "articles": {a["id"]: a for a in ARTICLES},
        "articleOrder": [a["id"] for a in sorted(ARTICLES, key=lambda a: a["date"], reverse=True)],
        "related": related_map(),
    }
