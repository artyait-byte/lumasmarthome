"""Location silo, journal, and brand copy for LUMA Smart Home.

Tony's remodeling SEO playbook, applied to this studio:
  - City and city×service URLs live under /service-areas/, not in the Solutions nav.
  - Start the keyword snowball with "smart home Sarasota", then tighter terms.
  - Unique copy on every URL (no doorway templates).
  - One NAP in the footer, with a Google Maps search link until a GBP CID exists.
"""

from camera_content import CAMERA_ROWS, CAMERA_TYPES, SECURITY_HUB


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
    CAMERA_ROWS["sarasota/security"],
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
    CAMERA_ROWS["sarasota/business-security"],
    CAMERA_ROWS["bradenton/business-security"],
    CAMERA_ROWS["sarasota/retail-security-cameras"],
    CAMERA_ROWS["sarasota/restaurant-security-cameras"],
    CAMERA_ROWS["sarasota/warehouse-security-cameras"],
    CAMERA_ROWS["sarasota/hoa-security-cameras"],
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
    {
        "id": "journal-hurricane-smart-home",
        "slug": "smart-home-hurricane-preparation-florida",
        "title": "Smart Home Hurricane Preparation in Florida | LUMA",
        "h1": "Smart home hurricane preparation in Florida",
        "description": "Getting a Florida smart home ready for hurricane season: backup power for the rack, shades and shutters, cameras and sensors you can check from away.",
        "og": "/assets/photos/live/sc-s-storm.jpg",
        "date": "2026-10-24",
        "category": "Storm season",
        "dek": "Power, shades and remote eyes. What a Gulf Coast system should do before, during and after a storm, and what it cannot do.",
        "blocks": [
            {"type": "p", "text": "Milton came ashore at Siesta Key in October 2024, two weeks after Helene pushed surge across Anna Maria and Longboat Key. Most Sarasota and Manatee owners now have a storm routine for the house: shutters, the generator, the patio furniture. Fewer have one for the systems inside it. Yet those systems decide whether you can see the house from Ohio, whether the rack survives the power coming back on twelve times, and whether a closed-up house sits at 80 percent humidity for a week without anyone knowing."},
            {"type": "p", "text": "This is how we prepare a smart home for hurricane season on the Gulf Coast. Some of it is equipment. Most of it is decisions made before June 1."},
            {"type": "h2", "text": "What a smart home can and cannot do in a hurricane"},
            {"type": "p", "text": "Start with the honest limits. Interior motorized shades are not storm protection. A Lutron Sivoia QS roller or a Somfy drapery track will not stop debris or hold a pane together. Impact glass and rated shutters do that, and they belong to your builder and window contractor, not to us. Cameras do not prevent damage either. What a well-built system does is narrower and still valuable: it keeps the house observable, it protects its own electronics, it closes up the house in one press, and it tells you early when something is going wrong while you are not there."},
            {"type": "p", "text": "That last point matters more here than almost anywhere else. Peak hurricane season, August through October, is exactly when many Sarasota, Siesta Key and Longboat Key houses are empty. The owner is up north, the house is on Away, and the first sign of trouble is often a neighbor's text."},
            {"type": "h2", "text": "Power and connectivity: the rack has to ride through the outage"},
            {"type": "p", "text": "A storm is rarely one outage. It is a dozen: flickers as the bands come through, a long drop when a feeder goes, then brownouts and surges while the utility restores the grid. That sequence is harder on electronics than a clean shutdown. A gateway or recorder that loses power mid-write can corrupt its storage, and a modem that comes back in the wrong order can leave the whole network unreachable until someone walks in and unplugs it."},
            {"type": "p", "text": "So the network closet gets three things. First, a properly sized UPS on the rack, carrying the UniFi gateway, the PoE switch and the camera recorder. If the house has a standby generator, the job of the UPS is to bridge the seconds before the transfer switch picks up so nothing hard-reboots. If there is no generator, it buys time to see the house go dark and record what happens next. Second, managed power, such as a WattBox, so outlets can be power-cycled remotely and the rack restarts in the right order after an outage instead of all at once. Third, surge protection at the rack, in addition to the whole-house surge device your electrician installs at the panel."},
            {"type": "p", "text": "Then there is the closet itself. In a raised house on Anna Maria Island or Longboat Key, the ground level is a flood zone by design. The rack does not go in the garage under the house, however convenient the cable runs look. It goes in conditioned space above the flood line, and we plan that on the drawings rather than after the drywall. More on how we build that layer on the [networking page](networking)."},
            {"type": "p", "text": "In most neighborhoods the cable or fiber line goes down with the power, even if the house itself is on a generator. Without a second path, every camera and sensor in the house is recording to a box nobody can reach. A cellular backup, such as a UniFi LTE or 5G backup unit, gives the gateway a failover link that kicks in when the primary line drops. It will not carry a 4K camera wall, but it is enough for alerts, a few live views and remote diagnostics."},
            {"type": "p", "text": "Be realistic about it. Cell towers lose power in a major storm too, and some carriers recover faster than others. Pick the carrier with the best signal at the house, not the one on your phone, and test the failover in May, not during the first tropical storm warning."},
            {"type": "h2", "text": "Shades, shutters and a storm scene"},
            {"type": "p", "text": "Where a house has motorized hurricane shutters or exterior rolling screens, they can sit on the same keypad and the same app as the interior shades. That turns closing the house from a forty-minute walk with a crank into one press, which matters when you are leaving early to beat the traffic on I-75. Somfy motors drive many of the exterior rolling products on the coast, and a Somfy wind sensor can retract exterior screens automatically when gusts build, before the fabric becomes a sail."},
            {"type": "p", "text": "We program a Storm scene that does the boring things in the right order: exterior screens up and secured, interior shades down to keep sun off the floors once the power and AC are out, landscape and pool lights off, cameras armed, and a notification to you that the house is closed. A matching Return scene opens everything back up, checks the network, and puts the house back on its normal schedule. If you are on [Longboat Key](sa-longboat-key) or the other islands, check with the HOA before adding exterior hardware; boards there care about what the street can see."},
            {"type": "h2", "text": "Remote eyes: cameras and sensors that report in"},
            {"type": "p", "text": "Cameras are the obvious part. UniFi Protect cameras on PoE draw power from the switch, so when the switch is on the UPS, the cameras stay up too, and the recorder keeps writing locally even when the internet is out. You can scroll back through the storm once the connection returns. A camera on the dock, one on the seawall side and one inside the garage usually tell you more after a storm than a dozen pointed at the street."},
            {"type": "p", "text": "Sensors tell you what cameras cannot. A leak sensor under the AC air handler, the water heater and the kitchen sink. A temperature and humidity sensor in the main living space and one in a closet. In a closed Florida house with the AC off after an outage, humidity climbs fast, and mold can take hold within days. An alert that the house has reached 70 percent humidity is your cue to call someone with a key, long before the drywall starts to smell."},
            {"type": "h2", "text": "A pre-season checklist for owners"},
            {"type": "ul", "items": [
                "Test the UPS: pull the plug on the rack and time how long the network stays up",
                "Test the cellular failover by unplugging the modem, then check the app from your phone on cellular data",
                "Confirm every camera is recording locally and that you can scroll back 24 hours",
                "Run the Storm and Return scenes once, with someone watching the shutters",
                "Replace batteries in leak and humidity sensors and confirm alerts reach your phone",
                "Write down who has a key and can walk in if an alert fires while you are away",
                "Make sure firmware updates are done before August, not during a watch",
            ]},
            {"type": "h2", "text": "After the storm"},
            {"type": "p", "text": "When power is restored, resist the urge to have someone flip everything on at once. Let the generator hand back to the utility, then let managed power bring the rack up in order. Check the recorder first, then the cameras, then the rest. If something did not come back, a remote diagnosis tells you whether it needs a technician or a reboot. That is the work our [LUMA Care plans](support) are built for. The Shoreline plan, at $75 a month, is designed for seasonal and lock-and-leave homes and includes weekday remote diagnostics on the gear we installed."},
            {"type": "p", "text": "If you want a storm review of an existing system, or you are building and want the rack, power and connectivity drawn correctly from the start, [book a walkthrough](contact). We will tell you what is worth adding and what is not."},
            {"type": "h2", "text": "Frequently asked questions"},
            {"type": "faq", "items": [
                {"q": "Will motorized shades protect my windows in a hurricane?", "a": "No. Interior motorized shades are for sun, glare and privacy. Impact-rated glass or rated hurricane shutters protect the openings. If you have motorized shutters, we can put them on the same keypad and app as the shades so the house closes in one press."},
                {"q": "How long will my smart home keep running on a UPS?", "a": "It depends on the size of the UPS and what it carries. We size it for the gateway, the PoE switch and the camera recorder. With a standby generator, the UPS only needs to bridge the transfer. Without one, it buys hours rather than days, so the network can report the outage and the cameras can record it."},
                {"q": "Can I see my cameras if the power and internet are out?", "a": "The recorder keeps writing locally as long as the rack has power, so the footage is there when you reconnect. Live viewing from away needs a path out of the house, which is what a cellular backup on the gateway provides, as long as the local towers are up."},
                {"q": "What should I set before leaving for the summer?", "a": "Test the UPS and the cellular failover, confirm cameras are recording locally, check leak and humidity sensor batteries, run the Storm scene once, and make sure someone local has a key. Then put the house on Away and keep alerts switched on."},
            ]},
        ],
    },
    {   'id': 'journal-snowbird-smart-home',
        'slug': 'smart-home-snowbirds-florida',
        'title': 'Smart Home for Snowbirds in Florida | LUMA',
        'h1': 'Smart home for snowbirds in Florida: running a seasonal house from up north',
        'description': 'Opening a Florida seasonal home, running it remotely all summer and closing it in '
                       'spring: humidity, leak sensors, cameras, lock codes and the network.',
        'og': '/assets/photos/live/a-away.jpg',
        'date': '2026-10-24',
        'category': 'Seasonal homes',
        'dek': 'What to check when you arrive in the fall, what has to keep working while you are away, and how '
               'to close the house in April.',
        'blocks': [   {   'type': 'p',
                          'text': 'Late October is when the Gulf Coast fills back up. Cars with Ohio and Ontario '
                                  'plates reappear on Gulf of Mexico Drive, the lanai furniture comes out of the '
                                  'garage, and a house that sat closed for six months has to become a home again '
                                  'in a weekend. In April it all runs in reverse. For a seasonal owner, the '
                                  'smart home is not about voice control or party scenes. It is the set of '
                                  'systems that keeps an empty house dry, secure and reachable from a thousand '
                                  'miles away, and makes the two changeovers each year predictable.'},
                      {   'type': 'p',
                          'text': 'This is how we think about a smart home for snowbirds in Florida: what to '
                                  'check when you arrive, what has to keep working while you are gone, and how '
                                  'to close the house in spring so that next October is uneventful.'},
                      {'type': 'h2', 'text': 'Opening the house on arrival'},
                      {   'type': 'p',
                          'text': 'The first hour in a seasonal house tells you how the summer went. Walk the '
                                  'systems in a fixed order, because each depends on the one before it.'},
                      {   'type': 'ul',
                          'items': [   'Network first: check that the gateway, switch and Wi-Fi access points '
                                       'are online and that the internet line is the speed you pay for. '
                                       'Everything else rides on it.',
                                       'Climate next: move the thermostats from the Away profile back to '
                                       'occupied setpoints, and look at the humidity history for the summer, not '
                                       "just today's reading.",
                                       'Water: open the main if it was shut, run every tap and shower for a '
                                       'minute, and confirm each leak sensor still reports to the app.',
                                       'Cameras and recorder: confirm the recorder kept writing all summer and '
                                       'check that the clock and storage are correct.',
                                       'Shades and lighting: run each scene once. Motors that sat idle for '
                                       'months sometimes need their limits reset.',
                                       'Locks and codes: retire the codes issued to summer contractors and '
                                       'confirm which ones your house manager still needs.']},
                      {   'type': 'p',
                          'text': 'Expect firmware updates to have piled up. A controller, a set of access '
                                  'points and a camera recorder that were left alone for six months may all want '
                                  'updates at once. Run them in sequence during the first week, not the night '
                                  'before guests arrive, and note what changed.'},
                      {   'type': 'h2',
                          'text': 'Humidity and HVAC: the system that matters most while you are away'},
                      {   'type': 'p',
                          'text': 'An empty Florida house does not usually fail through break-ins. It fails '
                                  'through moisture. A thermostat set too high to save power and a closed house '
                                  'can push indoor humidity well past 60 percent. Closets, mattresses and the '
                                  'backs of cabinets go first.'},
                      {   'type': 'p',
                          'text': 'The practical setup is a connected thermostat, such as an Ecobee or a '
                                  'Honeywell Home model, running an Away profile with a cooling setpoint chosen '
                                  'for humidity rather than for the lowest bill, plus a dehumidify setting where '
                                  'the equipment supports it. Your HVAC contractor should set the exact numbers '
                                  'for your equipment. Then add independent temperature and humidity sensors in '
                                  'a closet and an interior room, reporting through the hub rather than through '
                                  'the thermostat itself. If the air handler fails, the thermostat that controls '
                                  'it may not tell you. A separate sensor will.'},
                      {   'type': 'p',
                          'text': 'Set three alerts: humidity above your threshold for several hours, indoor '
                                  'temperature high enough that the AC is clearly not running, and the '
                                  'thermostat going offline. Three useful alerts beat twenty you learn to '
                                  'ignore.'},
                      {'type': 'h2', 'text': 'Water, cameras, presence and access for vendors'},
                      {   'type': 'p',
                          'text': 'Leak sensors are cheap insurance. Put them under the air handler and its '
                                  'condensate line, the water heater, the kitchen sink, the dishwasher, the ice '
                                  'maker and each toilet supply. A clogged condensate line is one of the most '
                                  'common summer failures in a closed Florida house, and a sensor in the drain '
                                  'pan catches it early. For a fuller answer, a whole-house shutoff valve such '
                                  'as a Moen Flo or a Phyn monitors flow at the main and can close the water '
                                  'automatically when it sees a leak, or when water runs while the house is '
                                  'supposed to be empty.'},
                      {   'type': 'p',
                          'text': 'Cameras should earn their place. A recorder on site, such as UniFi Protect, '
                                  'keeps footage locally and lets you look in from your phone without paying a '
                                  'monthly fee to watch an empty driveway. Point cameras at the entry, the '
                                  'garage, the dock or seawall side and the pool equipment rather than at the '
                                  'street. Glare and foliage decide placement more than the floor plan does.'},
                      {   'type': 'p',
                          'text': 'For presence, a Lutron system can run a randomized evening schedule in a few '
                                  'rooms, with landscape lighting on an astronomical clock. Keep it modest. A '
                                  'house lit like a dinner party every night reads as staged.'},
                      {   'type': 'p',
                          'text': 'Most seasonal owners rely on a house watch service, a cleaner, a pool company '
                                  'and the occasional contractor. A smart lock from Yale or Schlage that '
                                  'connects to the home system lets you give each one their own code, limited to '
                                  'the days and hours they work, and see each entry in a log. When the pool '
                                  'company changes staff, you delete one code instead of rekeying the house. '
                                  'Pair the lock with a camera at the door, and an entry alert tells you both '
                                  'who came in and that it was actually them.'},
                      {   'type': 'p',
                          'text': 'Gated communities add a layer. Many developments in Lakewood Ranch and Venice '
                                  'run their own gate access systems, and the HOA controls who gets a visitor '
                                  'pass. Your home system cannot open that gate, but it keeps a clean record of '
                                  'who entered your door and when.'},
                      {'type': 'h2', 'text': 'Network reliability: everything else depends on it'},
                      {   'type': 'p',
                          'text': 'Every alert in this article travels over the house network. If the modem '
                                  'locks up in July and nobody is there to unplug it, every camera and sensor '
                                  'goes silent and you will not know until something else goes wrong. A seasonal '
                                  'house needs a network built to recover by itself: a business-grade gateway '
                                  'such as UniFi, a UPS on the rack, managed power that can restart the modem '
                                  'remotely, and a cellular backup that takes over when the cable or fiber line '
                                  'drops. We cover that layer in more detail on the [networking '
                                  'page](networking), and the storm side of it in [hurricane preparation for a '
                                  'smart home](journal-hurricane-smart-home).'},
                      {   'type': 'p',
                          'text': 'Someone also has to watch the network while you are away. That is the work '
                                  'our [LUMA Care plans](support) are built for. The Shoreline plan, at $75 a '
                                  'month, is designed for seasonal residences and lock-and-leave homes and '
                                  'includes remote diagnostics and firmware guidance for the gear we installed.'},
                      {'type': 'h2', 'text': 'Closing the house in spring'},
                      {   'type': 'p',
                          'text': 'The close-up is where a little discipline pays off all summer. Run the same '
                                  'written checklist every year, and test the alerts before leaving rather than '
                                  'after landing up north.'},
                      {   'type': 'ul',
                          'items': [   'Switch thermostats to the Away profile and confirm the humidity setting '
                                       'is active',
                                       'Test one leak sensor by touching it with a damp cloth and confirm the '
                                       'alert reaches your phone',
                                       'Replace batteries in leak, humidity and door sensors, even if the app '
                                       'shows them as fine',
                                       'Decide whether the water main stays open for irrigation or is shut by '
                                       'the automatic valve',
                                       'Confirm the recorder has space for the summer and every camera is '
                                       'recording',
                                       'Set the lighting presence schedule and turn off scenes nobody needs',
                                       'Issue time-limited lock codes to the house watch, cleaner and pool '
                                       'service; delete the rest',
                                       'Unplug the modem for a minute and check the house still reports over the '
                                       'cellular backup',
                                       'Leave a written contact sheet for whoever has a key: who to call for '
                                       'HVAC, water and the network']},
                      {'type': 'h2', 'text': 'Island, condo and HOA realities'},
                      {   'type': 'p',
                          'text': 'Location changes the details. On [Longboat Key](sa-longboat-key) and Siesta '
                                  'Key, salt air shortens the life of exterior hardware, so outdoor cameras and '
                                  'fixtures need marine-rated finishes, and many residences are condos where the '
                                  'association controls the exterior walls, the roof and the common network '
                                  'closet. In a condo you usually cannot drill the facade for a camera or run '
                                  'cable through common areas without board approval, so plans have to work '
                                  'inside the unit. Leak sensors and an automatic shutoff matter even more '
                                  "there, because a leak in your unit becomes your downstairs neighbor's "
                                  'ceiling.'},
                      {   'type': 'p',
                          'text': 'In Lakewood Ranch and Venice, the typical seasonal home is a single-family '
                                  'house in a deed-restricted community. Architectural review boards often have '
                                  'rules on visible cameras, exterior lighting color and anything mounted to the '
                                  'roofline, so it is worth checking before work begins. Gated access is common, '
                                  'and many communities have their own house watch vendors who already know the '
                                  'neighborhood.'},
                      {   'type': 'p',
                          'text': 'If you are opening the house this season and want the systems checked, or you '
                                  'are planning what to add before spring, [book a walkthrough](contact). We '
                                  'will look at what you already have and tell you what is worth changing.'},
                      {'type': 'h2', 'text': 'Frequently asked questions'},
                      {   'type': 'faq',
                          'items': [   {   'q': 'What thermostat setting should I use when my Florida home is '
                                                'empty for the summer?',
                                           'a': 'Set it for humidity, not just temperature. Use dehumidification '
                                                'where the equipment supports it, and let your HVAC contractor '
                                                'set the exact numbers. Add a separate humidity sensor so you '
                                                'hear about a problem even if the thermostat does not.'},
                                       {   'q': 'Do I need a monthly subscription to watch my cameras from up '
                                                'north?',
                                           'a': 'Not with an on-site recorder. A system such as UniFi Protect '
                                                'stores footage in the house and lets you view it remotely from '
                                                'your phone. You need a reliable internet line, ideally with a '
                                                'cellular backup, but no paid cloud plan.'},
                                       {   'q': 'How do I give cleaners and contractors access without handing '
                                                'out keys?',
                                           'a': 'Use a connected smart lock with individual codes for each '
                                                'service, limited to their working days and hours. Every entry '
                                                'is logged, and a code can be deleted the day a vendor changes '
                                                'staff, without rekeying the house.'},
                                       {   'q': 'Can I add smart home equipment in a Longboat Key or Siesta Key '
                                                'condo?',
                                           'a': 'Usually yes, inside the unit. Thermostats, leak sensors, an '
                                                'automatic water shutoff, lighting control and interior '
                                                'networking rarely need board approval. Anything on the exterior '
                                                'walls, the roof or in common areas typically does, so check the '
                                                'association rules first.'}]}]},
    {   'id': 'journal-lutron-cost',
        'slug': 'lutron-radiora-3-cost-sarasota',
        'title': 'Lutron RadioRA 3 Cost in a Sarasota Home | LUMA',
        'h1': 'Lutron RadioRA 3 cost in a Sarasota home',
        'description': 'What drives Lutron RadioRA 3 cost in a Sarasota home: loads, keypads, retrofit vs new '
                       'build, shades and programming, plus what to ask in a quote.',
        'og': '/assets/photos/layers-lighting.jpg',
        'date': '2026-10-24',
        'category': 'Lighting',
        'dek': 'Loads, keypads, wiring and programming decide the number, not the brand. Here is how to budget '
               'and what a quote should show.',
        'blocks': [   {   'type': 'p',
                          'text': 'Ask three people what Lutron RadioRA 3 costs and you will get three numbers '
                                  'that are all correct for a different house. A Lutron system is not priced by '
                                  'the square foot or by the brand. It is priced by how many circuits it '
                                  'controls, what you touch on the wall, how hard it is to reach the wiring, and '
                                  'how much of the house the system is expected to run. This article walks '
                                  'through those drivers for a Sarasota or Manatee home, shows the ranges our '
                                  'own estimator uses, and lists what should be on a quote before you compare '
                                  'one against another.'},
                      {   'type': 'p',
                          'text': 'If you are still deciding between Lutron product lines, start with [choosing '
                                  'Lutron in a Sarasota house](journal-lutron-sarasota). This piece assumes you '
                                  'are leaning toward RadioRA 3 and want to understand the budget.'},
                      {'type': 'h2', 'text': 'What you are actually paying for in a RadioRA 3 system'},
                      {   'type': 'p',
                          'text': 'A RadioRA 3 job has four parts, and every honest quote shows all four.'},
                      {   'type': 'ul',
                          'items': [   'Hardware: the processor, dimmers and switches, keypads, any plug-in or '
                                       'lamp modules, sensors, and the wallplates that finish them',
                                       'Installation: replacing existing controls, adding boxes or wiring where '
                                       'a keypad needs to live, and testing every load',
                                       'Design: deciding which circuits belong to which scenes, where keypads '
                                       'go, and what each button is engraved with',
                                       'Programming: building the scenes, timeclock events, occupancy behaviour '
                                       'and the app, then adjusting them after you have lived with them']},
                      {   'type': 'p',
                          'text': 'Hardware is the part people look up online, and it is rarely the part that '
                                  'surprises them. The surprises come from design and installation: a great room '
                                  'with eleven circuits on one wall, a keypad location with no neutral, a lanai '
                                  'circuit nobody can find in the panel. That is why two houses of the same size '
                                  'can land far apart.'},
                      {'type': 'h2', 'text': 'The cost drivers, one by one'},
                      {   'type': 'p',
                          'text': 'Number of loads. A load is one circuit you want to dim or switch: the kitchen '
                                  'cans, the island pendants, the under-cabinet strip, the lanai fans. Each one '
                                  'needs a dimmer or a switch, wired or in a panel. Load count is the single '
                                  'best predictor of hardware cost, and Gulf Coast houses tend to have a lot of '
                                  'them. Open plans with tray ceilings, cove lighting, pendants over a long '
                                  'island and multiple sliders to the lanai can put fifteen or more loads in '
                                  'what is effectively one room.'},
                      {   'type': 'p',
                          'text': 'Keypads versus dimmers. A dimmer controls one load. A keypad controls scenes: '
                                  'Entertain, Dinner, Evening, Off. Keypads replace banks of dimmers and are '
                                  'what make the system feel finished, but each one is a device to buy, a '
                                  'location to wire and engraving to design. A house with a keypad at every '
                                  'entry and bedside costs more than one that keeps individual dimmers in '
                                  'secondary rooms and uses keypads only where people actually arrive and '
                                  'leave.'},
                      {   'type': 'p',
                          'text': 'Wired versus wireless, new build versus existing home. RadioRA 3 is designed '
                                  'for retrofit: wireless dimmers and keypads replace existing devices in the '
                                  "same wall boxes, talking to a processor over Lutron's radio network. In a "
                                  'finished house this avoids opening walls, which is why it is our usual '
                                  'recommendation for existing homes. New construction changes the math. '
                                  'Pre-wiring keypad locations, landing loads where you want them and planning a '
                                  'panel before drywall is cheaper than retrofitting later, and it opens the '
                                  'door to wired and panelized options.'},
                      {   'type': 'p',
                          'text': 'The processor and the size of the house. One RadioRA 3 processor covers a '
                                  'typical home. Large single-storey plans, concrete-block walls, detached guest '
                                  'suites and pool houses may need additional processors or repeaters so the '
                                  'radio signal reaches every device reliably. That is a site question, not a '
                                  'catalogue question, and it should be answered during a walkthrough.'},
                      {'type': 'h2', 'text': 'Caséta, RadioRA 3 or HomeWorks'},
                      {   'type': 'p',
                          'text': 'These three lines share a lot of thinking but are priced and scoped very '
                                  'differently.'},
                      {   'type': 'ul',
                          'items': [   'Caséta suits a handful of rooms, a condo or a first step. It is the '
                                       'least expensive Lutron option, but it has a smaller device limit and '
                                       'fewer keypad and engraving choices',
                                       'RadioRA 3 covers most finished single-family homes on the Gulf Coast: '
                                       'whole-house scenes, engraved keypads, occupancy sensors, shades on the '
                                       'same system, and an app that is not a toy',
                                       'HomeWorks fits large new builds and deep remodels with a lighting '
                                       'designer: panelized loads, more architectural keypads, larger systems '
                                       'and tighter integration with fixtures']},
                      {   'type': 'p',
                          'text': 'Ketra sits on top of the decision rather than beside it. Ketra fixtures and '
                                  'lamps change colour temperature through the day and need their own design '
                                  'work, so they move a project toward HomeWorks and a different budget '
                                  'conversation. If someone quotes Ketra on a straightforward retrofit, ask '
                                  'why.'},
                      {   'type': 'p',
                          'text': 'Shades on the same system. Many Sarasota homes add motorized shades on the '
                                  'same Lutron system, so sunset drops the solar screens and warms the dining '
                                  'room from one keypad. That is the strongest argument for putting lighting and '
                                  'shades on one platform, but shades are budgeted separately. Each shade is its '
                                  'own motor, fabric and bracket, and wide gulf-facing openings cost more than '
                                  'bedroom windows. More on the layers we use on west glass on the [motorized '
                                  'shades page](shading).'},
                      {'type': 'h2', 'text': 'How to budget for Lutron lighting control in Sarasota'},
                      {   'type': 'p',
                          'text': 'Our [budget estimator](budget-calculator) prices lighting control by how much '
                                  'of the house it covers. Its Gulf Coast ranges for the lighting-control line '
                                  'are:'},
                      {   'type': 'ul',
                          'items': [   'A few rooms only: $1,400 to $3,200',
                                       'Main areas plus exterior (most living areas, lanai, landscape lights): '
                                       '$3,800 to $9,500',
                                       'Whole house plus landscape: $12,000 to $38,000']},
                      {   'type': 'p',
                          'text': 'In the same estimator, motorized shades are counted per shade at $900 to '
                                  '$1,900 each, and the tool adds a design and project-management allowance on '
                                  'top of the line items. These are indicative ranges for planning, not a quote. '
                                  'Where a project lands inside a range depends on load count, keypad count, '
                                  'retrofit difficulty and how much programming the house needs.'},
                      {   'type': 'p',
                          'text': 'For context, the whole-home packages on the same page put Lutron RadioRA 3 '
                                  'lighting in the Foundation tier, $45k to $85k for 2,500 to 4,000 sq ft, '
                                  'alongside cabling, Wi-Fi and cameras. The Signature tier, $120k to $220k for '
                                  '4,000 to 7,500 sq ft, moves to Lutron HomeWorks lighting and shades. Those '
                                  'are whole-system figures, not lighting alone.'},
                      {   'type': 'p',
                          'text': 'A practical way to budget is to phase it. Start with the rooms you use every '
                                  'evening and the exterior, which is where scenes pay off first, and leave '
                                  'secondary bedrooms on standard dimmers that can join later. RadioRA 3 grows '
                                  'well, so a first phase does not lock you out of a whole-house system.'},
                      {'type': 'h2', 'text': 'Gulf Coast homes change the brief'},
                      {   'type': 'p',
                          'text': 'Lanais. The lanai is a living room here, and it usually brings fans, '
                                  'downlights, pool and landscape lighting onto the system. Outdoor loads are '
                                  'often on separate circuits with GFCI protection, sometimes in a sub-panel, '
                                  'and tracing them adds installation time. Exterior keypads and devices need '
                                  'the right location and enclosure for heat and humidity.'},
                      {   'type': 'p',
                          'text': 'Coastal homes. On Siesta Key, Longboat Key and Anna Maria Island, salt air '
                                  'and raised construction affect where equipment lives. The processor belongs '
                                  'in conditioned space above the flood line, not in a ground-level garage, and '
                                  'that can lengthen wire runs or add a repeater.'},
                      {   'type': 'p',
                          'text': 'Seasonal owners. If the house sits empty for months, the timeclock, an Away '
                                  'scene that varies lights in the evening, and remote access through the app '
                                  'matter more than a keypad in every room. Programming those behaviours '
                                  'carefully, and testing them before you leave in spring, is part of the '
                                  'budget, not an extra.'},
                      {'type': 'h2', 'text': 'What to ask in a Lutron quote'},
                      {   'type': 'ul',
                          'items': [   'Is every load, keypad, sensor and processor listed with a price, or is '
                                       'it one lump sum?',
                                       'How many loads did you count, and did you open the panel to confirm '
                                       'them?',
                                       'Which rooms get keypads, and what will each button say?',
                                       'Which devices are wireless retrofit and which need new wiring or boxes?',
                                       'Are shades, Ketra and landscape lighting included, quoted separately or '
                                       'excluded?',
                                       'How many hours of design and programming are included, and what does a '
                                       'change after move-in cost?',
                                       'Who owns the programming file, and can another integrator service the '
                                       'system later?']},
                      {   'type': 'p',
                          'text': 'A quote that answers these clearly is easier to compare than a lower number '
                                  'that does not. For how we approach the work locally, see [Lutron lighting '
                                  'control in Sarasota](sa-sarasota-lighting). When you want a number for your '
                                  'own house, [book a walkthrough](contact) and we will count the loads with '
                                  'you.'},
                      {'type': 'h2', 'text': 'Frequently asked questions'},
                      {   'type': 'faq',
                          'items': [   {   'q': 'How much does Lutron RadioRA 3 cost for a Sarasota home?',
                                           'a': 'It depends mostly on the number of loads, keypads and how much '
                                                'of the house is covered. Our budget estimator uses $1,400 to '
                                                '$3,200 for a few rooms, $3,800 to $9,500 for main areas plus '
                                                'exterior, and $12,000 to $38,000 for the whole house plus '
                                                'landscape. A walkthrough turns that range into a quote.'},
                                       {   'q': 'Can RadioRA 3 be installed in an existing home without opening '
                                                'walls?',
                                           'a': 'Usually, yes. RadioRA 3 dimmers and keypads are wireless and '
                                                'replace existing devices in the same wall boxes. Walls are '
                                                'opened only where a keypad needs a new location or a box lacks '
                                                'the wiring the device requires.'},
                                       {   'q': 'Is HomeWorks worth it over RadioRA 3?',
                                           'a': 'For most finished Gulf Coast homes, RadioRA 3 covers what '
                                                'owners need. HomeWorks makes sense in large new builds and deep '
                                                'remodels where a lighting designer, panelized loads or Ketra '
                                                'are part of the plan.'},
                                       {   'q': 'Are motorized shades included in a lighting quote?',
                                           'a': 'They can run on the same Lutron system, but they are priced '
                                                'separately because each shade has its own motor, fabric and '
                                                'hardware. Our estimator counts them at $900 to $1,900 per '
                                                'shade.'}]}]},
    {   'id': 'journal-permanent-vs-seasonal',
        'slug': 'permanent-outdoor-lighting-cost-sarasota',
        'title': 'Permanent Outdoor Lighting Cost in Sarasota | LUMA',
        'h1': 'Permanent outdoor lighting in Sarasota: cost and how it compares to a seasonal install',
        'description': 'Permanent roofline lighting vs a yearly holiday install in Sarasota: what drives the '
                       'cost, salt air, HOAs, tile roofs, and when each one makes sense.',
        'og': '/assets/photos/permanent-holiday.jpg',
        'date': '2026-10-24',
        'category': 'Outdoor lighting',
        'dek': 'A clip-on holiday install goes up and comes down every year; a permanent channel stays on the '
               'fascia and does more than December. Here is how to weigh the two on a Gulf Coast house.',
        'blocks': [   {   'type': 'p',
                          'text': 'Late October is when the question comes up. The neighbors are booking their '
                                  'holiday lights, the ladder is in the garage, and someone in the house asks '
                                  'whether it is time to stop doing this every year. On the Gulf Coast there are '
                                  'two serious ways to light a roofline for the season: a seasonal install of '
                                  'clip-on C9 bulbs or string lights that goes up in November and comes down in '
                                  'January, or a permanent LED channel fastened under the overhangs that stays '
                                  'there all year and runs warm white most nights.'},
                      {   'type': 'p',
                          'text': 'Both are reasonable, and they are paid for differently. Here is how each '
                                  'works, what drives the cost of permanent outdoor lighting in Sarasota and '
                                  'Manatee, and how to decide for your own house.'},
                      {'type': 'h2', 'text': 'Two ways to light a roofline'},
                      {   'type': 'p',
                          'text': 'A seasonal install is temporary by design. C9 or C7 bulbs or an LED string '
                                  'are clipped to the gutter, drip edge or shingles, plugged into an outdoor '
                                  'outlet and set on a timer. After the holidays everything comes down and goes '
                                  'into storage. Next year it repeats, including the roof access and the hunt '
                                  'for the strand that stopped working.'},
                      {   'type': 'p',
                          'text': 'A permanent system is installed once. A slim aluminum channel is '
                                  'powder-coated to match the fascia or soffit color, cut on site to the eaves, '
                                  'gables and returns, and fastened into the fascia rather than clipped to a '
                                  'gutter. Individually addressable LEDs sit inside the channel. A controller, '
                                  'usually in the garage or the network rack, drives the whole run. During the '
                                  'day it reads as trim. At night it can be a quiet 2700K warm white line that '
                                  'finishes the elevation, full-brightness white for security, team colors on '
                                  'game day, or a holiday preset in December. Nothing goes up in November and '
                                  'nothing comes down in January. The details of how we build it are on our '
                                  '[permanent outdoor lighting page](permanent-lighting).'},
                      {'type': 'h2', 'text': 'What drives the cost of permanent outdoor lighting in Sarasota'},
                      {   'type': 'p',
                          'text': 'There is no honest flat price for a permanent roofline, because the house '
                                  'sets most of the number. When we put together a range, these are the '
                                  'variables that move it:'},
                      {   'type': 'ul',
                          'items': [   'Linear feet of roofline: the length of every eave, gable and return you '
                                       'want lit, measured on the drawing, not estimated from the street',
                                       'Stories and access: a single-story ranch in Palmer Ranch is a ladder '
                                       'job; a two-story home in Lakewood Ranch or a raised house near the water '
                                       'can need a lift and more labor per foot',
                                       'Roof type and fascia condition: barrel tile, flat tile, metal and '
                                       'shingle each change how the channel is fastened and how corners and '
                                       'peaks are handled, and rotted fascia should be repaired before anything '
                                       'is mounted',
                                       'Number of zones: front elevation only, or front, garage side, lanai and '
                                       'pool cage on separate runs that can be lit independently',
                                       'Power and controller: where the power supplies live, whether a new '
                                       'circuit is needed, and whether the controller stands alone or ties into '
                                       'an existing lighting or automation system',
                                       'Channel color and finish: a standard color, or a custom match to an '
                                       'unusual fascia or trim paint']},
                      {   'type': 'p',
                          'text': 'A seasonal install is simpler but it repeats: labor to install, labor to take '
                                  'down, and storage or replacement of bulbs, clips and wire every year. Done '
                                  'yourself, it is a weekend on a ladder twice a year. The useful comparison is '
                                  'several seasons of install and takedown against one installation that also '
                                  'lights the house the other eleven months.'},
                      {   'type': 'p',
                          'text': 'To get a real range for your house, send us a photo of the front elevation '
                                  'and the address. We measure the roofline from the drawings or county records, '
                                  'and we come back with a run plan, a channel color and a range before anything '
                                  'is ordered.'},
                      {'type': 'h2', 'text': 'Gulf Coast conditions: salt, sun and storms'},
                      {   'type': 'p',
                          'text': 'Salt air corrodes exposed metal contacts. Seasonal strands spend only a '
                                  'couple of months outside, but the sockets, plugs and timers are rarely built '
                                  'for marine exposure, so a strand that worked last year can come out of '
                                  'storage with green contacts and dead sections. A permanent system keeps the '
                                  'diodes and connections inside a sealed channel, with the power supplies in a '
                                  'protected location. On barrier-island and bayfront homes we pay particular '
                                  'attention to connector sealing and to where the power supplies sit.'},
                      {   'type': 'p',
                          'text': 'UV is the second factor. Florida sun degrades plastics, and cheap wire '
                                  'jackets and bulb covers become brittle within a few seasons. A powder-coated '
                                  'aluminum channel shades the diodes from direct sun. Manufacturers generally '
                                  'rate LEDs for tens of thousands of hours, but real-world life depends on '
                                  'heat, moisture and the quality of the power supply, so treat any rating as a '
                                  'manufacturer figure, not a promise about your roofline.'},
                      {   'type': 'p',
                          'text': 'Then there are hurricanes. Clip-on lights are down long before the next storm '
                                  'season, which favors a seasonal install. A permanent channel stays up through '
                                  'summer, so fastening matters: ours goes into the fascia, not the gutter, so '
                                  'it stays put and does not interfere with drainage. After a major storm, give '
                                  'the roofline a visual check along with the gutters.'},
                      {'type': 'h2', 'text': 'HOA rules, roof types and two-story homes'},
                      {   'type': 'p',
                          'text': 'Many communities in Lakewood Ranch, Venice and Palmer Ranch have '
                                  'architectural review boards with rules on exterior lighting: allowed colors, '
                                  'hours, brightness and whether holiday displays are limited to certain dates. '
                                  'A permanent system usually helps here, because the daytime look is trim '
                                  'matched to the house and the nighttime default is a restrained warm white. '
                                  'Colors and holiday presets can be scheduled to fit the dates the HOA allows. '
                                  'Still, check the documents and submit to the board before installation if the '
                                  'community requires it. If you are in [Lakewood Ranch](sa-lakewood-ranch) or '
                                  '[Venice](sa-venice), we can help you prepare the drawing and product details '
                                  'the board typically asks for.'},
                      {   'type': 'p',
                          'text': 'Roof type matters for both options. Barrel tile is common in Sarasota and '
                                  'Venice, and clips that slide under tiles can crack or lift them, a common '
                                  'source of winter roof leaks after a seasonal install. Metal roofs dent and '
                                  'scratch, and clips on standing seam can slip. A fascia-mounted channel avoids '
                                  'walking the roof field at all after installation, since nothing has to be put '
                                  'up or taken down each year.'},
                      {   'type': 'p',
                          'text': 'Two-story homes are where a seasonal install costs most over time: upper '
                                  'eaves need taller ladders or a lift twice a season. A permanent system goes '
                                  'up once.'},
                      {'type': 'h2', 'text': 'When each option makes sense'},
                      {   'type': 'p',
                          'text': 'A seasonal install is a sensible choice if you only want lights in December, '
                                  'if you are selling or renting the house in the next year or two, if the HOA '
                                  "does not allow any permanent exterior fixtures, or if the house's trim and "
                                  'fascia need work before anything should be fastened to them. It is also the '
                                  'low-commitment way to find out how much you enjoy a lit roofline.'},
                      {   'type': 'p',
                          'text': 'A permanent system makes more sense if you plan to stay, if the house is two '
                                  'stories or has a tile or metal roof, if you would like the roofline lit '
                                  'year-round as part of the architecture, or if you are tired of the yearly '
                                  'install and takedown. It is also a fit for seasonal residents: the lights can '
                                  'follow a schedule and be checked from the app while you are away, and nobody '
                                  'has to climb up in January to take anything down.'},
                      {'type': 'h2', 'text': "How it ties into the home's lighting control"},
                      {   'type': 'p',
                          'text': "A permanent roofline works on its own with the manufacturer's app and a "
                                  'schedule: sunset on, midnight off, a preset for the date. It becomes more '
                                  'useful when it is part of the house. If the home has a Lutron system or a '
                                  'whole-home automation platform, the roofline can join the same scenes as the '
                                  'landscape, pool and lanai lights. An Evening scene turns it on with the rest '
                                  'of the exterior, Away turns it off with everything else, and a keypad button '
                                  'by the door handles it without a phone. Security mode can raise it to '
                                  'full-brightness white on a camera event. That is the same approach we take to '
                                  '[lighting control](lighting) inside the house: one schedule, one keypad, '
                                  'fewer apps.'},
                      {   'type': 'p',
                          'text': 'If you are weighing a permanent roofline against another year of clip-on '
                                  'lights, [send us a photo of the house](contact). We will tell you whether a '
                                  'permanent channel makes sense for your roofline, and if it does not, we will '
                                  'say so.'},
                      {'type': 'h2', 'text': 'Frequently asked questions'},
                      {   'type': 'faq',
                          'items': [   {   'q': 'How much does permanent outdoor lighting cost in Sarasota?',
                                           'a': 'It depends mainly on the linear feet of roofline, the number of '
                                                'stories, the roof type, the number of zones and how the '
                                                'controller is powered and integrated. We give a range for your '
                                                'house after measuring the roofline from a photo and drawings or '
                                                'county records, before anything is ordered.'},
                                       {   'q': 'Can permanent lights do Christmas and holiday colors?',
                                           'a': 'Yes. The LEDs are individually addressable, so the same channel '
                                                'that runs warm white most nights can switch to a holiday '
                                                'preset, team colors or full-brightness white. Presets can be '
                                                'scheduled for the dates you or your HOA choose.'},
                                       {   'q': 'Will permanent roofline lighting survive salt air and '
                                                'hurricanes?',
                                           'a': 'The diodes sit inside a sealed, powder-coated channel fastened '
                                                'into the fascia rather than clipped to a gutter, which is built '
                                                'for exposure. Manufacturers rate LEDs for tens of thousands of '
                                                'hours in general terms; warranty terms depend on the product '
                                                'line and are set out in writing in the proposal.'},
                                       {   'q': 'Does my HOA need to approve permanent lighting?',
                                           'a': 'Many communities in Lakewood Ranch, Venice and Palmer Ranch '
                                                'require architectural review for exterior fixtures or set rules '
                                                'on colors and hours. Check your documents first; we can supply '
                                                'the drawing and product details the board usually asks for.'},
                                       {   'q': 'Is a seasonal install ever the better choice?',
                                           'a': 'Yes, if you only want lights in December, plan to sell soon, '
                                                'your HOA does not allow permanent fixtures, or the fascia needs '
                                                'repair first. A seasonal install is also a low-commitment way '
                                                'to see how much you use a lit roofline.'}]}]},
    {   'id': 'journal-prewire-lwr',
        'slug': 'smart-home-pre-wire-lakewood-ranch',
        'title': 'Smart Home Pre-Wire in Lakewood Ranch | LUMA',
        'h1': 'Smart home pre-wire for a Lakewood Ranch new build',
        'description': 'What to run before drywall in a Lakewood Ranch new build: Cat6A home runs, shade power, '
                       'keypads, cameras, lanai conduit and the rack, and builder timing.',
        'og': '/assets/photos/trade-roughin.jpg',
        'date': '2026-10-24',
        'category': 'New construction',
        'dek': 'Cable, boxes and conduit are cheap before drywall and expensive after it. Here is what to run in '
               'a Lakewood Ranch new build and when.',
        'blocks': [   {   'type': 'p',
                          'text': 'If you are building in Lakewood Ranch, the cheapest moment to decide how the '
                                  'house will be wired is the few weeks between framing and drywall. In '
                                  'Waterside, Lake Club, Star Farms, Azario and the newer villages, production '
                                  'and semi-custom builders move quickly, and the low-voltage stage often passes '
                                  'before the owner has thought about where the rack, the access points or the '
                                  'shade motors go. Once insulation and drywall are in, every one of those '
                                  'decisions turns into cutting, fishing and patching.'},
                      {   'type': 'p',
                          'text': 'Here is what goes into a smart home pre-wire for a Lakewood Ranch new build, '
                                  "how it fits the builder's schedule, and what skipping it costs."},
                      {'type': 'h2', 'text': 'Why the pre-wire matters more in a Florida new build'},
                      {   'type': 'p',
                          'text': 'Many new homes on both the Manatee and Sarasota sides of the Ranch are '
                                  'concrete block (CBS) on the ground floor, with wood-framed interior walls, a '
                                  'wood-framed second floor where there is one, and a truss roof. That mix '
                                  'decides where cable can go later and where it cannot.'},
                      {   'type': 'p',
                          'text': 'Exterior block walls are the hard part. A cable or a box on an exterior wall '
                                  'either goes in the furring space before drywall or gets chased into the block '
                                  'afterward, which is slow, loud and visible. The attic is the other route, and '
                                  'in Southwest Florida it is a poor place to work: summer attic temperatures '
                                  'make retrofit pulls slow, and the trusses are tied down with hurricane straps '
                                  'and clips that nobody should be drilling through to save a few feet of cable. '
                                  'A house wired at rough-in avoids all of that.'},
                      {   'type': 'p',
                          'text': 'There is also the lanai. Screen enclosures (the aluminum lanai cage) usually '
                                  'go up late in the build, often by a separate contractor. If there is no '
                                  'conduit stubbed out to the cage posts and the outdoor ceiling, outdoor '
                                  'speakers, cameras and lighting end up on surface-mounted wiremold or wireless '
                                  'gear that struggles with the heat and humidity.'},
                      {'type': 'h2', 'text': 'What we run before drywall'},
                      {   'type': 'p',
                          'text': 'A pre-wire is not a box of spare cable. It is a plan: every location marked '
                                  'on the drawings, every cable labelled at both ends, and every run going back '
                                  'to one place. On a typical Lakewood Ranch new build that plan covers:'},
                      {   'type': 'ul',
                          'items': [   'Cat6A home runs to every TV location, office, media room and bedroom '
                                       'wall that may host a screen or a desk, each run returning to the rack '
                                       'rather than daisy-chained',
                                       'Ceiling access point locations, one Cat6A drop each, placed from a '
                                       'coverage plan rather than one per room by default, including the bonus '
                                       'room, the primary suite and the lanai',
                                       'Camera locations with a Cat6A drop for PoE at eaves, the garage, the '
                                       'front entry and the lanai, so cameras take power and data from the '
                                       'switch and need no outlet',
                                       'Shade pockets or recesses at the windows where the builder will frame '
                                       'them, with low-voltage or line-voltage power at the head of each window '
                                       'depending on the shade system',
                                       'Keypad locations in deep boxes at the main entries, the kitchen, the '
                                       'primary bedroom and wherever scenes will be used, so keypads stack '
                                       "cleanly with the electrician's switches",
                                       'In-ceiling and in-wall speaker locations with speaker wire back to the '
                                       'rack, plus backboxes or brackets so the ceiling is cut once, in the '
                                       'right place',
                                       'Conduit from the house to the lanai cage, pool equipment, a dock if the '
                                       'lot has water access, and a driveway gate or entry pillars, with pull '
                                       'string left in',
                                       'A rack location in conditioned space with its own dedicated circuit, '
                                       'room for airflow, and conduit to the attic and to the service entrance '
                                       'for the internet provider']},
                      {   'type': 'p',
                          'text': 'Two items deserve a word. Shades are where most retrofits go wrong: a '
                                  'motorized roller shade needs a pocket or a clean head detail and power at the '
                                  'window, and neither can be added cleanly after drywall and trim. If you are '
                                  'even considering motorized shades on the west and south elevations, wire for '
                                  'them now; the [shading page](shading) covers how we size and pick the motors. '
                                  'And the rack belongs inside the air-conditioned envelope, typically an '
                                  'interior closet or a corner of the laundry room, not the garage and not the '
                                  'attic. Heat is what shortens the life of switches, recorders and power '
                                  'supplies in this climate.'},
                      {'type': 'h2', 'text': "Low-voltage pre-wire vs the builder's tech package"},
                      {   'type': 'p',
                          'text': 'Most builders in the Ranch offer a structured wiring or technology package at '
                                  'the design center. Some are a handful of coax and Cat5e or Cat6 outlets and a '
                                  'small panel in a closet; others are more complete. Ask the same questions '
                                  'either way:'},
                      {   'type': 'ul',
                          'items': [   'What cable is it: Cat6A, Cat6 or Cat5e, and are the runs home runs or '
                                       'looped between outlets?',
                                       'Where does everything terminate, and is that location in conditioned '
                                       'space with power and room for a rack?',
                                       'Are there any ceiling drops for access points, or any camera drops at '
                                       'the eaves?',
                                       'Is there anything for shades, keypads or the lanai, or only data and TV '
                                       'outlets?',
                                       'Who labels and tests the cables, and do you get a map of what went '
                                       'where?']},
                      {   'type': 'p',
                          'text': "A builder's package is not wrong; it is usually just written for a different "
                                  "house than the one you want. Often the right answer is to keep the builder's "
                                  'electrical scope as it is, decline or trim the tech package, and have a '
                                  'dedicated low-voltage contractor rough in to a plan drawn for the systems you '
                                  'actually intend to install.'},
                      {'type': 'h2', 'text': "Coordinating with the builder's schedule"},
                      {   'type': 'p',
                          'text': 'Builders run on a sequence, and low-voltage has to fit inside it. First, we '
                                  'mark up the plan set before or at framing: device locations, box types, shade '
                                  'details, conduit and the rack. Those markups go to the builder and the '
                                  'electrician so nothing surprises them on site. Second, after framing and the '
                                  'electrical rough-in, and before insulation, we run the low-voltage rough-in, '
                                  'ideally in one visit,. Third, we walk the job with you and, if possible, the '
                                  'superintendent, confirming every location on the studs rather than on paper.'},
                      {   'type': 'p',
                          'text': 'After drywall and paint, trim-out is when devices go in: keypads, speakers, '
                                  'access points, cameras and the rack itself. Some builders allow trim before '
                                  'closing, others only after; both work if the rough-in was done right. We work '
                                  "from your builder's schedule, not ours, and we do not promise dates that "
                                  "depend on someone else's calendar. More on how we work alongside builders and "
                                  'designers is on the [designers and builders page](designers).'},
                      {   'type': 'p',
                          'text': 'One practical note for buyers: confirm early, in writing, that your builder '
                                  'allows an outside low-voltage contractor on site before closing. Policies '
                                  'differ by builder, and it is easier to settle at contract than after '
                                  'framing.'},
                      {'type': 'h2', 'text': 'Retrofit later vs wire now'},
                      {   'type': 'p',
                          'text': 'Skipping the pre-wire rarely saves money; it moves the cost later and makes '
                                  'it larger. In a finished Lakewood Ranch home, running a new cable to an '
                                  'exterior block wall means chasing or surface conduit. Pulling through a hot '
                                  'attic past straps, blocking and insulation takes far longer than the same run '
                                  'through open studs. Shades without pockets get mounted on the face of the '
                                  'window trim. Cameras without PoE drops end up on Wi-Fi with batteries or '
                                  'local power supplies. And the rack ends up where there happens to be space, '
                                  'which in many houses is the garage.'},
                      {   'type': 'p',
                          'text': 'There is a middle path if the budget is tight at build time: run the cable '
                                  'and conduit now, and install the equipment later. Cable and boxes are a small '
                                  'part of a finished system and the only part that is truly hard to add '
                                  'afterward. Speakers, keypads, shades and cameras can all be installed after '
                                  'you move in, as long as the wire is waiting for them.'},
                      {   'type': 'p',
                          'text': 'For a sense of scale, our [budget estimator](budget-calculator) uses a range '
                                  'of about $1.60 to $3.40 per square foot of heated and cooled space for '
                                  'new-construction pre-wire and infrastructure, before any devices or control '
                                  'systems. It is an indicative range, not a quote; the real number depends on '
                                  'how many locations you want and what the house looks like on paper.'},
                      {'type': 'h2', 'text': 'How to start before your framing date'},
                      {   'type': 'p',
                          'text': 'The best time to call is when you have a plan set and a rough idea of the '
                                  "builder's schedule, ideally before framing. Bring the floor plan and a short "
                                  'list of what you want the house to do: shades on the west side, music on the '
                                  'lanai, cameras at the gate, Wi-Fi in the bonus room. We mark up the plans and '
                                  'tell you what has to happen before drywall and what can wait. Our [Lakewood '
                                  'Ranch page](sa-lakewood-ranch) covers the kinds of homes we see across the '
                                  'Ranch, and when you are ready, [send us your plans](contact).'},
                      {'type': 'h2', 'text': 'Frequently asked questions'},
                      {   'type': 'faq',
                          'items': [   {   'q': 'When should I schedule a smart home pre-wire in Lakewood Ranch?',
                                           'a': 'Before framing if you can, so locations are on the plans. The '
                                                'low-voltage rough-in itself happens after framing and the '
                                                'electrical rough-in, and before insulation and drywall. Once '
                                                'drywall is up, the pre-wire window has closed.'},
                                       {   'q': "Is the builder's structured wiring package enough?",
                                           'a': 'Sometimes, but check what it includes: the cable type, whether '
                                                'runs are home runs, where they terminate, and whether there are '
                                                'any drops for access points, cameras, shades, keypads or the '
                                                'lanai. Many packages cover TV and data outlets only.'},
                                       {   'q': 'Why Cat6A instead of Cat6?',
                                           'a': 'Cat6A supports 10-gigabit Ethernet over full-length runs and '
                                                'handles PoE power for cameras and access points with less heat '
                                                'build-up in the bundle. The cable is a small share of the cost, '
                                                'and walls in a block house are expensive to reopen.'},
                                       {   'q': 'Can I pre-wire now and add equipment later?',
                                           'a': 'Yes. Running cable, conduit, deep boxes and shade power during '
                                                'construction, then installing speakers, cameras, keypads and '
                                                'shades after closing, is a common and sensible way to split the '
                                                'budget.'},
                                       {   'q': 'Where should the network rack go in a Florida new build?',
                                           'a': 'In conditioned space with a dedicated circuit and some airflow, '
                                                'usually an interior closet or part of the laundry room. Avoid '
                                                'the garage and the attic, where heat shortens equipment '
                                                'life.'}]}]},
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
        faq = [it for b in art["blocks"] if b["type"] == "faq" for it in b["items"]]
        paras += [f"{it['q']} {it['a']}" for it in faq]
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
                "faq": faq,
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
        "journal-hurricane-smart-home": "Smart home hurricane preparation",
        "journal-snowbird-smart-home": "Smart home for snowbirds",
        "journal-lutron-cost": "Lutron RadioRA 3 cost",
        "journal-permanent-vs-seasonal": "Permanent vs seasonal lighting",
        "journal-prewire-lwr": "Smart home pre-wire in Lakewood Ranch",
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
        "networking": "journal-hurricane-smart-home",
        "automation": "journal-hurricane-smart-home",
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
        "journal-hurricane-smart-home",
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
        ("case-urban", "work"),
        ("case-family", "work"),
        ("case-waterfront", "work"),
        ("case-golf", "sa-siesta-key"),
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
            extra = ["journal-shades-gulf", "journal-hurricane-smart-home", "sa-sarasota", "contact"]
        elif city["id"] in ("longboat-key", "anna-maria-island"):
            extra = ["journal-hurricane-smart-home", "security", "service-areas", "contact"]
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
        "sa-sarasota-security", "security", "journal-hurricane-smart-home", "contact"
    )
    rel["journal-hurricane-smart-home"] = _rel(
        "networking", "sa-sarasota-security", "sa-longboat-key", "support", "contact"
    )
    # Newer articles: own "keep reading" list plus a link in from each related page.
    rel["journal-snowbird-smart-home"] = _rel("support", "sa-longboat-key", "networking", "journal-hurricane-smart-home", "contact")
    rel["journal-lutron-cost"] = _rel("lighting", "sa-sarasota-lighting", "journal-lutron-sarasota", "budget-calculator", "contact")
    rel["journal-permanent-vs-seasonal"] = _rel("permanent-lighting", "lighting", "sa-lakewood-ranch", "sa-venice", "contact")
    rel["journal-prewire-lwr"] = _rel("sa-lakewood-ranch", "designers", "networking", "budget-calculator", "contact")
    for art_id, pages in (
        ("journal-snowbird-smart-home", ("support", "sa-longboat-key", "sa-siesta-key", "journal-hurricane-smart-home", "journal")),
        ("journal-lutron-cost", ("lighting", "sa-sarasota-lighting", "journal-lutron-sarasota", "budget-calculator", "journal")),
        ("journal-permanent-vs-seasonal", ("permanent-lighting", "lighting", "sa-lakewood-ranch", "sa-venice", "journal")),
        ("journal-prewire-lwr", ("sa-lakewood-ranch", "designers", "networking", "journal-hurricane-smart-home", "journal")),
    ):
        for pid in pages:
            links = rel.setdefault(pid, [])
            if all(r["id"] != art_id for r in links):
                links.insert(0, {"id": art_id, "label": _page_label(art_id)})
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
        "cameraTypes": CAMERA_TYPES,
        "cameraHub": SECURITY_HUB,
    }
