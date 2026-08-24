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
        "h1": "Smart home systems in Sarasota, Florida",
        "title": "Smart Home Installer Sarasota FL | Lighting, Shades & AV | LUMA",
        "description": "LUMA Smart Home designs and installs lighting control, motorized shades, audio, security, and Wi-Fi for Sarasota residences. Local studio — not luma.com, not Luma AI.",
        "lede": "If you searched smart home Sarasota, you are in the right place: LUMA is a residential technology studio based here, specifying Lutron, UniFi, Somfy, and Sonos for houses that live with Gulf sun, salt air, and seasonal occupancy.",
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
        "title": "Lakewood Ranch Smart Home Installer | Lighting & Wi-Fi | LUMA",
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
        "id": "punta-gorda",
        "name": "Punta Gorda",
        "county": "Charlotte County",
        "tagline": "Harbor, islands, and the missing county in a five-county map.",
        "h1": "Smart home installation in Punta Gorda & Charlotte County",
        "title": "Punta Gorda Smart Home Installer | Charlotte County | LUMA",
        "description": "Lighting control, cameras, and Wi-Fi for Punta Gorda, Port Charlotte, and Boca Grande. LUMA Smart Home covers Charlotte County from the Sarasota studio.",
        "lede": "Charlotte County is not an afterthought between Sarasota and Fort Myers. Harbor lots, Burnt Store, and Boca Grande each want a different shade and camera spec — and a network that survives lock-and-leave.",
        "paragraphs": [
            "Punta Gorda and Port Charlotte rebuilds and waterfront remodels are usually RadioRA 3 plus UniFi: scenes for the lanai and dock, cameras that stay on-prem so a summer away is not a camera-cloud bill. Boca Grande adds HOA and salt the way Siesta does — we bring cut sheets before we drill.",
            "Travel from the Sarasota studio is in the proposal, same as Lee and Collier. If you searched smart home Punta Gorda or lighting installer Port Charlotte, this silo is the city page — not a paragraph buried under Lighting.",
        ],
        "neighborhoods": [
            "Punta Gorda Isles",
            "Burnt Store",
            "Port Charlotte",
            "Boca Grande",
            "Englewood (Charlotte side)",
        ],
        "image": "/assets/photos/gulf-sunset.jpg",
        "services": ["lighting"],
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
        "id": "naples",
        "name": "Naples",
        "county": "Collier County",
        "tagline": "Estate scale, Port Royal glass, and a quieter control layer.",
        "h1": "Smart home installation in Naples, Florida",
        "title": "Naples FL Smart Home Installer | Lighting & Automation | LUMA",
        "description": "LUMA designs lighting control, home automation, and whole-home systems for Naples, Port Royal, Aqualane, and Marco Island. Collier County service.",
        "lede": "Naples projects are often larger envelopes, stricter design review, and homeowners who have already been burned by a dealer-locked system. We specify open platforms and a rack you can still service in ten years.",
        "paragraphs": [
            "Port Royal, Aqualane, and the gulf-front condos have different constraints — acoustics, millwork, and what a design review board will allow on the elevation. Lighting is usually the first trade we join: Ketra or HomeWorks where the architecture deserves it, RadioRA 3 where it does not. Automation sits on top only after lighting, shades, climate, and the network are honest.",
            "We already have finished work in Naples (including a Port Royal residence in Our Work). Travel from the Sarasota studio is planned into the proposal so you are not surprised by trip charges after the bid.",
        ],
        "neighborhoods": [
            "Port Royal",
            "Aqualane Shores",
            "Old Naples",
            "Pelican Bay",
            "Marco Island",
        ],
        "image": "/assets/photos/cases/spacious-modern/web-hero.jpg",
        "services": ["lighting", "automation"],
    },
    {
        "id": "fort-myers",
        "name": "Fort Myers",
        "county": "Lee County",
        "tagline": "Riverfront rebuilds, Sanibel-adjacent, and Lee County new work.",
        "h1": "Smart home installation in Fort Myers & Lee County",
        "title": "Fort Myers Smart Home Installer | LUMA Smart Home",
        "description": "Lighting control, networking, and whole-home systems for Fort Myers, Sanibel, Captiva, Estero, and Bonita Springs. LUMA serves Lee County from Sarasota.",
        "lede": "Lee County work since the storms is a mix of rebuilds and new construction. That is the moment to put Cat6A in the walls and Lutron on the lighting schedule — not a year after drywall, when every 'smart' decision is a surface mount.",
        "paragraphs": [
            "Fort Myers riverfront glass and Sanibel/Captiva salt are two different specs. We walk both. Lighting control is the usual first layer on a rebuild because the electrical is already open; shades and cameras follow once openings and millwork are known. UniFi stays on-prem so a lock-and-leave island house is not streaming your driveway to a vendor cloud.",
            "Estero, Bonita, and the Sanibel causeway sit inside our five-county window. Same line-item proposal as Sarasota, with travel called out up front.",
        ],
        "neighborhoods": [
            "Downtown Fort Myers / riverfront",
            "McGregor corridor",
            "Sanibel & Captiva",
            "Estero",
            "Bonita Springs",
        ],
        "image": "/assets/photos/hero-modern-home.jpg",
        "services": ["lighting"],
    },
]

# Unique city × service pages (not every city × every trade — doorway risk).
CITY_SERVICES = [
    {
        "city": "sarasota",
        "service": "lighting",
        "h1": "Lutron lighting control in Sarasota",
        "title": "Lutron Lighting Installer Sarasota FL | Ketra & RadioRA 3 | LUMA",
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
        "h1": "Home cameras & security in Sarasota",
        "title": "Home Security Cameras Sarasota FL | UniFi Protect | LUMA",
        "description": "On-premise UniFi Protect cameras in Sarasota — no monthly cloud fees. Property-walked placement, NVR on site, optional alarm monitoring.",
        "lede": "Sarasota homeowners are tired of doorbell brands that rent them their own driveway. UniFi Protect records on a box in your closet. We place cameras after walking sunset glare and neighbor angles — not from a floor plan in the office.",
        "paragraphs": [
            "Seasonal occupancy is the local twist: you need to see the house from somewhere else without paying a cloud tax all summer. On-prem storage plus optional encrypted off-site backup is the honest stack. We will also tell you where a camera is pointless because the HOA or the foliage will win.",
            "This is not Snap One's Luma camera line, and it is not a DIY kit. LUMA Smart Home is the Sarasota studio that designs the network the cameras sit on.",
        ],
        "bullets": [
            "UniFi Protect G-series, PoE, no batteries",
            "NVR on the property, 30+ day retention typical",
            "Placement after a property walk, including glare",
            "Optional alarm panel and monitoring",
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
        "title": "Home Automation Sarasota FL | Control4, Lutron, Josh.ai | LUMA",
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
    },
    {
        "city": "naples",
        "service": "lighting",
        "h1": "Lighting control in Naples",
        "title": "Lutron Lighting Installer Naples FL | LUMA Smart Home",
        "description": "Naples Lutron and Ketra lighting control for Port Royal, Aqualane, and Collier County residences. Architectural lighting under one keypad spec.",
        "lede": "Naples lighting is usually a design-review problem as much as an electrical one. Keypads have to match millwork, landscape lighting has to survive the board, and the gulf-west rooms need a color temperature that does not go grey at 5 p.m.",
        "paragraphs": [
            "We join the lighting designer early or we become one: load schedules, Ketra where the architecture is doing color, RadioRA 3 or HomeWorks depending on processor need. Estate scale in Port Royal is not a bigger RadioRA panel — it is a different conversation about processors, enclosures, and service access.",
            "Our Work includes a Naples Port Royal residence. Travel from Sarasota is in the proposal, not a surprise change order.",
        ],
        "bullets": [
            "Design-review-friendly keypads and trims",
            "Ketra / warm-dim for gulf-west glass",
            "Landscape on the same scenes as interior",
            "Estate and condo stacks, specified honestly",
        ],
    },
    {
        "city": "naples",
        "service": "automation",
        "h1": "Home automation in Naples",
        "title": "Home Automation Naples FL | LUMA Smart Home",
        "description": "Unified lighting, shades, climate, and AV for Naples estates and condos. Open platforms — not a dealer-locked processor you cannot service.",
        "lede": "Naples clients often arrive with a Crestron or Control4 system they cannot get serviced. We document what you have, keep what is honest, and only replace the control layer when the alternative is years of hostage-taking.",
        "paragraphs": [
            "New Naples work starts with network and lighting, then shades, then a UI. A processor that 'does everything' before those layers exist is how you get a $40k iPad that cannot open the shade in the guest room.",
            "We stay after turnover. Collier County is inside the five-county service map; urgent calls are queued with the same studio that designed the rack.",
        ],
        "bullets": [
            "Audit of existing Crestron / Control4 / Savant",
            "Open-platform replacements when lock-in is the problem",
            "Scenes written for seasonal occupancy",
            "Documented system you could hand to another firm",
        ],
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
        "city": "fort-myers",
        "service": "lighting",
        "h1": "Lighting control in Fort Myers",
        "title": "Lutron Lighting Installer Fort Myers FL | LUMA Smart Home",
        "description": "Lutron lighting control for Fort Myers rebuilds and Lee County new construction. Load schedules while the walls are open — not surface dimmers later.",
        "lede": "If you are rebuilding in Fort Myers or on Sanibel, lighting control is cheapest when the electrical is already exposed. That is the window. We write the Lutron load schedule with the electrician so you are not fishing travelers next year.",
        "paragraphs": [
            "Lee County west glass and riverfront reflections want warm-dim and scenes, not a wall of paddle switches that all read as 'on.' RadioRA 3 covers most rebuilds; larger envelopes get a processor conversation. Landscape and path lighting join the same keypad so the dock does not stay on until Tuesday.",
            "Travel from Sarasota is priced in the proposal. Sanibel and Captiva staging is called out, not hidden.",
        ],
        "bullets": [
            "Load schedules during rebuild, not after drywall",
            "RadioRA 3 or HomeWorks by envelope",
            "Lanai, dock, and path on interior scenes",
            "Lee County inside the five-county map",
        ],
    },
    {
        "city": "punta-gorda",
        "service": "lighting",
        "h1": "Lutron lighting control in Punta Gorda",
        "title": "Lutron Lighting Installer Punta Gorda FL | Charlotte County | LUMA",
        "description": "Lutron lighting control for Punta Gorda, Port Charlotte, and Boca Grande. RadioRA 3 scenes for canal-front and seasonal Charlotte County homes.",
        "lede": "Canal-front and seasonal homes in Punta Gorda need lighting that still works when the owners are away. LUMA designs Lutron from Sarasota and commissions it on the Charlotte County job.",
        "paragraphs": [
            "Punta Gorda Isles and Burnt Store houses sit empty for weeks, then fill up for season. Lighting control has to survive that cycle: scenes for occupancy, a sensible off state, and a processor that is not depending on a consumer cloud. We specify Lutron with the builder or overlay RadioRA 3 when the house is already finished.",
            "Port Charlotte, Boca Grande, and Englewood (Charlotte side) get the same documented stack — not a different product because the county line moved. If cameras and a network closet belong in the same phase, we design those too so the lighting job is not an island. Travel from the Sarasota studio is in the proposal.",
        ],
        "bullets": [
            "RadioRA 3 for existing Punta Gorda and Port Charlotte homes",
            "Away scenes that look occupied without looking theatrical",
            "Lanai, dock, and path lighting on the same keypad",
            "Charlotte County inside the five-county map",
        ],
    },
]

ARTICLES = [
    {
        "id": "journal-smart-home-sarasota",
        "slug": "smart-home-sarasota",
        "title": "What “smart home Sarasota” should actually mean | LUMA Journal",
        "h1": "What “smart home Sarasota” should actually mean",
        "description": "A practical definition of a smart home on Florida’s Gulf Coast: sun, salt, seasonal occupancy, and systems you still own. Written by LUMA Smart Home in Sarasota.",
        "og": "/assets/photos/sarasota-downtown-bayfront.jpg",
        "date": "2026-08-24",
        "dek": "The phrase is searched more than it is specified. Here is the local version — lighting, shades, network, and cameras that survive gulf light and a summer away.",
        "blocks": [
            {"type": "p", "text": "People type smart home Sarasota into Google and land on national blogs, big-box mesh kits, or a company named Luma that has nothing to do with a house on the bay. This studio is LUMA Smart Home in Sarasota. The rest of this note is what the phrase should mean if you actually live here."},
            {"type": "h2", "text": "Start with the hour, not the app"},
            {"type": "p", "text": "Gulf light is the brief. West glass from mid-afternoon, a lanai that is the living room, and a sky that goes gold then ink. A useful system dims and warms with that hour, drops solar screens before the sofa cooks, and does not leave the dock lights on until a neighbor texts. That is lighting control and motorized shades on a clock and occupancy — Lutron and Sivoia or Somfy — not a rainbow of consumer bulbs."},
            {"type": "h2", "text": "The network is the house"},
            {"type": "p", "text": "Cameras, audio, keypads, and thermostats all inherit the Wi-Fi. A single gateway in a hot laundry room is why 'the smart home' drops every storm season. UniFi, a wired spine where we can hide it, and a UPS on the rack are unglamorous and non-negotiable. If you only do one upgrade, do this one."},
            {"type": "h2", "text": "Seasonal occupancy is a first-class mode"},
            {"type": "p", "text": "Away should look lived-in, arm cameras, and close the elevations that take weather — without a monthly fee to rent your own driveway from a doorbell brand. On-premise UniFi Protect is how we do that. Lock-and-leave is normal on Siesta, Longboat, and Anna Maria; the system should assume you might be gone for months."},
            {"type": "h2", "text": "Open platforms, line-item paper"},
            {"type": "p", "text": "Dealer-locked processors are how Gulf Coast homeowners get stuck. We specify Lutron, UniFi, Somfy, Sonos, Control4, Josh.ai — professional gear with a service path if you ever leave us. Proposals list devices and labor. That is the opposite of a bundled mystery."},
            {"type": "p", "text": "If this is the search you meant, start with the [Sarasota smart home page](sa-sarasota), the [Lutron lighting note](sa-sarasota-lighting), or [book a walkthrough](contact). We are not luma.com — read [this LUMA, not the others](luma-smart-home-sarasota)."},
        ],
    },
    {
        "id": "journal-lutron-sarasota",
        "slug": "lutron-installer-sarasota",
        "title": "A Lutron installer in Sarasota: RadioRA 3 vs HomeWorks | LUMA Journal",
        "h1": "Choosing Lutron in a Sarasota house",
        "description": "When RadioRA 3 is enough, when Sarasota homes need HomeWorks or Ketra, and what a Lutron installer should put on the proposal. LUMA Smart Home.",
        "og": "/assets/photos/lighting-lutron-hero.jpg",
        "date": "2026-08-24",
        "dek": "Most finished Sarasota houses need an overlay, not a processor palace. Here is how we decide.",
        "blocks": [
            {"type": "p", "text": "Lutron is the lighting spine we trust on the Gulf Coast: keypads that still make sense if the phone is dead, dimming that does not buzz, and a dealer network that will still exist when the consumer hub of the year does not. 'Lutron installer Sarasota' should mean someone who will tell you which Lutron, not someone who only sells the SKU with the highest margin."},
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
            {"type": "p", "text": "LUMA is a Sarasota Lutron installer in that sense: we spec, program, and stay. Read [Lutron lighting control in Sarasota](sa-sarasota-lighting) or [start a project](contact) if you want that walkthrough."},
        ],
    },
    {
        "id": "journal-shades-gulf",
        "slug": "motorized-shades-gulf-coast",
        "title": "Motorized shades for Gulf Coast sun | LUMA Journal",
        "h1": "Motorized shades that respect Gulf Coast sun",
        "description": "Why Sarasota and Naples west glass needs layered motorized shades — solar screen, blackout, Sivoia or Somfy — not one fabric and a remote in a drawer.",
        "og": "/assets/photos/hero-shading.jpg",
        "date": "2026-08-24",
        "dek": "The view is why you bought the house. The infrared is why the sofa is fading. Both can be true.",
        "blocks": [
            {"type": "p", "text": "Gulf-west elevations in Sarasota, Longboat, Siesta, and Naples do not need 'window treatments' as decoration first. They need a solar-screen layer that keeps the water visible and a blackout layer that lets someone sleep after a late dinner. One dual-purpose fabric usually fails both jobs."},
            {"type": "h2", "text": "Sivoia when lighting is already Lutron"},
            {"type": "p", "text": "If the house is on RadioRA or HomeWorks, Lutron Sivoia QS keeps shades on the same keypad and clock as the lights. That is how sunset can drop the screens and warm the dining room without two apps arguing."},
            {"type": "h2", "text": "Somfy when the opening is the constraint"},
            {"type": "p", "text": "Wide lanai volumes, existing pockets, and outdoor rollers often land on Somfy. It is not a downgrade; it is the motor that fits. We still program astronomical clocks and Away. Salt-rated hardware is in the spec for barrier islands — indoor motors on a gulf lanai are how you buy the job twice."},
            {"type": "h2", "text": "HOA and glass"},
            {"type": "p", "text": "What the street is allowed to see matters on Siesta and in Naples design review. We bring fabric and exterior-roller cut sheets early. Measuring gulf-front openings twice is cheaper than a motor that racks in an out-of-square pocket."},
            {"type": "p", "text": "More on [motorized shades in Sarasota](sa-sarasota-shading), or the [Siesta Key service-area note](sa-siesta-key) if you are on the island."},
        ],
    },
    {
        "id": "journal-theater-sarasota",
        "slug": "home-theater-sarasota",
        "title": "Home theater in Sarasota: dedicated room vs media suite | LUMA Journal",
        "h1": "A home theater that survives Florida construction",
        "description": "How to decide between a dedicated cinema and a media suite in a Sarasota house — acoustics, CBS, tile, and calibration. LUMA Smart Home.",
        "og": "/assets/photos/hero-theater.jpg",
        "date": "2026-08-24",
        "dek": "A projector and a dark paint chip are not a theater. Tile and CBS will tell you that on night one.",
        "blocks": [
            {"type": "p", "text": "Sarasota bonus rooms over the garage are the usual candidate. Sometimes they become a cinema. Sometimes they should stay a media suite with a serious display, two good speakers, and lighting that can actually go down. We would rather say that in week one than calibrate a room that cannot hold bass."},
            {"type": "h2", "text": "What Florida does to sound"},
            {"type": "p", "text": "CBS, tile, and sliders are reflective. Dedicated rooms get absorption, bass management, and a door that closes. Media suites get honesty about what the sliders will do to dialogue. Either way, lighting and shades are part of Play — not a separate remote hunt when the movie starts."},
            {"type": "h2", "text": "Calibration is a file, not a vibe"},
            {"type": "p", "text": "We measure. You keep the file. If a prior installer 'set it by ear' with a demo disc, that is not a theater we will put our name on until we run the room again."},
            {"type": "p", "text": "See [home theater design in Sarasota](sa-sarasota-theaters) and [Our Work](work) for rooms that made it through first movie night."},
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
        "dek": "Three other products share a word. This is the integrator on Florida’s Gulf Coast.",
        "blocks": [
            {"type": "p", "text": "LUMA Smart Home (lumasmarthome.com) designs and installs lighting control, motorized shades, audio, security, and networking for homes in Sarasota, Manatee, Charlotte, Lee, and Collier Counties. Phone +1 (941) 217-1616. Email hello@lumasmarthome.com."},
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
                "The phone is (941) 217-1616",
            ]},
            {"type": "p", "text": "The longer entity page is [LUMA Smart Home Sarasota](luma-smart-home-sarasota). If you actually wanted lighting or a walkthrough, go to [service areas](service-areas) or [contact](contact)."},
        ],
    },
    {
        "id": "journal-cameras-fees",
        "slug": "home-cameras-without-monthly-fees",
        "title": "Home cameras without a monthly cloud | LUMA Journal",
        "h1": "Cameras you own, footage you keep",
        "description": "Why LUMA specs UniFi Protect in Sarasota instead of doorbell brands that charge rent for your own driveway. On-premise NVR, no required cloud.",
        "og": "/assets/photos/hero-security-v2.jpg",
        "date": "2026-08-24",
        "dek": "Seasonal Gulf Coast homes should not pay a subscription all summer to watch an empty lot.",
        "blocks": [
            {"type": "p", "text": "The default 'home camera' pitch is a cute doorbell, a cloud, and a price that returns every month. For a Siesta lock-and-leave or a Longboat seasonal house, that is rent on an empty driveway. We spec UniFi Protect: PoE cameras, a recorder in a closet you own, remote view when you want it."},
            {"type": "h2", "text": "Placement is the product"},
            {"type": "p", "text": "Sunset glare on Bird Key and foliage on a Manatee lot will beat a camera that was drawn in plan view. We walk the property. We will also tell you where a camera is wasted because the HOA or the neighbor angle makes it pointless."},
            {"type": "h2", "text": "Not the other Luma"},
            {"type": "p", "text": "If you searched Luma cameras, you may have meant Snap One's product line. Different company. Our camera page is [home cameras in Sarasota](sa-sarasota-security); the brand explainer is [LUMA vs luma.com](journal-not-luma-com)."},
        ],
    },
]

BRAND = {
    "id": "luma-smart-home-sarasota",
    "path": "/luma-smart-home-sarasota",
    "file": "luma-smart-home-sarasota.html",
    "title": "LUMA Smart Home Sarasota | Not luma.com, Luma AI, or Luma cameras",
    "h1": "LUMA Smart Home — Sarasota residential technology",
    "description": "LUMA Smart Home is a Sarasota, FL integrator for lighting, shades, AV, security, and Wi-Fi. Not luma.com, not Luma AI, not Snap One Luma cameras. (941) 217-1616.",
    "og": "/assets/photos/sarasota-marina.jpg",
    "lede": "This is the local studio. If a search for LUMA sent you to an events app, a video model, or a camera brand, read [the explainer](journal-not-luma-com) or [where we work](service-areas).",
}

NAP = {
    "name": "LUMA Smart Home",
    "legalName": "LUMA Home Systems LLC",
    "locality": "Sarasota",
    "region": "FL",
    "country": "US",
    "telephoneDisplay": "+1 (941) 217-1616",
    "telephone": "+1-941-217-1616",
    "telHref": "tel:+19412171616",
    "email": "hello@lumasmarthome.com",
    "hours": "Mon–Sat · 9am – 6pm",
    "area": "Sarasota, Manatee, Charlotte, Lee & Collier Counties",
    "mapsUrl": "https://www.google.com/maps/search/?api=1&query=LUMA+Smart+Home+Sarasota+FL",
    "mapsLabel": "LUMA Smart Home — Sarasota, Florida (Google Maps)",
}

HUB = {
    "id": "service-areas",
    "path": "/service-areas",
    "file": "service-areas.html",
    "title": "Service Areas | Sarasota to Naples | LUMA Smart Home",
    "h1": "Where we work on the Gulf Coast",
    "description": "LUMA Smart Home serves Sarasota, Bradenton, Lakewood Ranch, Venice, Punta Gorda, Siesta Key, Longboat Key, Fort Myers, and Naples. City pages live here — not in the Solutions menu.",
    "og": "/assets/photos/sarasota-downtown-bayfront.jpg",
    "lede": "Five counties, one studio. City pages sit in this silo so Sarasota still ranks as Sarasota — not as a diluted 'we serve everywhere' blob under Lighting.",
}

JOURNAL_HUB = {
    "id": "journal",
    "path": "/journal",
    "file": "journal.html",
    "title": "Journal | Smart Home Sarasota Notes | LUMA",
    "h1": "Notes from the studio",
    "description": "Practical writing from LUMA Smart Home: smart home Sarasota, Lutron, motorized shades, theaters, and how we differ from luma.com and other Lumas.",
    "og": "/assets/photos/gulf-sunset.jpg",
    "lede": "Shorter than a spec book, longer than an ad. Start with the Sarasota definition if you are new.",
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
        "sa-naples",
        "sa-bradenton",
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
    rel["work"] = _rel("sa-naples", "sa-sarasota", "sa-fort-myers", "contact")
    rel["contact"] = _rel("service-areas", "budget-calculator", "sa-sarasota", "journal")
    rel["designers"] = _rel("contact", "work", "lighting", "service-areas")
    rel["support"] = _rel("contact", "about")
    rel["budget-calculator"] = _rel("contact", "lighting", "service-areas")
    rel["smart-home-demo"] = _rel("contact", "lighting", "work")
    for case, city in (
        ("case-spacious", "sa-naples"),
        ("case-urban", "sa-sarasota"),
        ("case-family", "sa-fort-myers"),
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
        elif city["id"] == "naples":
            extra = ["journal-shades-gulf", "work", "contact"]
        elif city["id"] == "siesta-key":
            extra = ["journal-shades-gulf", "sa-sarasota", "contact"]
        elif city["id"] == "punta-gorda":
            extra = ["sa-sarasota-lighting", "sa-fort-myers", "contact"]
        rel[f"sa-{city['id']}"] = _rel(*ids, *extra)
    for row in CITY_SERVICES:
        pid = f"sa-{row['city']}-{row['service']}"
        rel[pid] = _rel(
            row["service"],
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
    rel["journal-shades-gulf"] = _rel("sa-sarasota-shading", "shading", "sa-siesta-key", "contact")
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
        "articleOrder": [a["id"] for a in ARTICLES],
        "related": related_map(),
    }
