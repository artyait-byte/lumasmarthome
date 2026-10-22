"""Location silo, journal, and brand copy for LUMA Smart Home.

Tony's remodeling SEO playbook, applied to this studio:
  - City and city×service URLs live under /service-areas/, not in the Solutions nav.
  - Start the keyword snowball with "smart home Sarasota", then tighter terms.
  - Unique copy on every URL (no doorway templates).
  - One NAP in the footer, with a Google Maps search link until a GBP CID exists.
"""

from camera_content import CAMERA_ROWS, CAMERA_TYPES


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
        "cameraTypes": CAMERA_TYPES,
    }
