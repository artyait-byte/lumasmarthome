"""Copy for the camera pages (the "camera section" template in js/app.js).

The layout follows the owner-picked reference block by block (see
docs/SEO-PLAYBOOK.md, "camera section v2"). Every row here replaces the row of
the same city/service in seo_content.CITY_SERVICES and is rendered by
CameraSectionPage in js/app.js.

Rules: no reviews, install counts, years, certifications, warranty terms or
monitoring-centre claims. Prices only the three package "from" prices + tax.
Photos in /assets/photos/cameras/ are illustrations (Higgsfield, generated for
LUMA): alt text describes what is in the frame, never a client or a LUMA job.
Links in text use the [anchor](page-id) form.
"""
from __future__ import annotations

P = "/assets/photos/cameras/"

# Alt text per photo, used wherever the photo appears.
ALT = {
    "cam-hero-office": "Bright Sarasota-style office with a ceiling dome camera and palm trees outside the windows",
    "cam-hero-dome": "Dome security camera under a stucco soffit with palm trees behind it",
    "cam-hero-owner": "Boutique owner checking her store cameras on a phone at the counter",
    "cam-type-bullet": "Bullet camera on a stucco wall overlooking a palm-lined parking lot",
    "cam-type-dome": "Ceiling dome camera above the aisles of a small convenience store",
    "cam-type-turret": "Turret camera under the eave above an arched front door",
    "cam-type-panoramic": "Panoramic camera on the ceiling of a restaurant dining room with street windows",
    "cam-type-vandal": "Vandal-resistant dome camera on the ceiling of a parking garage",
    "cam-type-lpr": "License plate camera on a post at a gated entrance at dusk",
    "cam-type-doorbell": "Video doorbell next to a dark front door beside a potted palm",
    "cam-benefits-wide": "Owner reviewing a grid of camera views on a tablet at a desk by the window",
    "cam-why-rack": "Hands patching network cables into a PoE switch above a video recorder in a rack",
    "cam-scen-marina": "Dome camera on a pole above a marina dock with sailboats",
    "cam-scen-warehouse": "Box truck at a loading dock under a wall-mounted camera",
    "cam-scen-retail": "Customer paying at a shop counter with a dome camera on the ceiling",
    "cam-scen-office": "Visitor checking in at a bright reception desk with a small ceiling camera",
    "cam-monitor-phone": "Hand holding a phone with four camera views in front of a storefront at dusk",
    "cam-hero-wide-a": "Dome and bullet cameras on the corner of a stucco building at sunset over Sarasota Bay",
    "cam-hero-wide-b": "Bullet camera with infrared glow on a waterfront Florida home at dusk, pool and palms behind",
}


def ph(name: str) -> list[str]:
    return [P + name + ".jpg", ALT[name]]


# Camera types for the accordion. "home" copy is used on the main page,
# "business" copy on the business hub; segment pages carry their own text.
CAMERA_TYPES = {
    "bullet": {
        "name": "Bullet cameras",
        "photo": ph("cam-type-bullet"),
        "home": ["A long camera that points one way and sees far. The UniFi G6 Bullet, or the G6 Pro Bullet with optical zoom, is our usual pick for a driveway, a side yard or a long property line, with infrared for full darkness.",
                 "driveways, side gates, docks and long yards"],
        "business": ["Bullets are built for distance along one line. The G6 Pro Bullet adds optical zoom, so a face or a plate at the far end of a lot is still usable, and the visible housing tells people the area is recorded.",
                     "parking lots, building sides, fence lines and loading areas"],
    },
    "dome": {
        "name": "Dome cameras",
        "photo": ph("cam-type-dome"),
        "home": ["A low-profile dome that sits flush on a ceiling or under a soffit. The lens hides behind the cover, so it is hard to tell where it points, and it reads as part of the house rather than a gadget.",
                 "front entries, covered lanais, garages and porches"],
        "business": ["Ceiling domes cover an entrance or a counter without dominating the room. At the door they catch faces at a usable size; over a register they show the drawer, the screen and the customer's hands.",
                     "lobbies, reception desks, registers and hallways"],
    },
    "turret": {
        "name": "Turret cameras",
        "photo": ph("cam-type-turret"),
        "home": ["A ball-shaped camera on a short mount. The UniFi G6 Turret has no glass bubble in front of the lens, so its own infrared does not glare at night and there is no cover to fog in the humidity.",
                 "under eaves, back doors and pool areas"],
        "business": ["The all-round camera for doors and corridors: the G6 Turret records 4K, carries an IP66 weather rating and sees about 98 ft in the dark. It is easy to re-aim when a space is rearranged.",
                     "back doors, corridors, stock rooms and kitchens"],
    },
    "panoramic": {
        "name": "Panoramic 180° cameras",
        "photo": ph("cam-type-panoramic"),
        "home": ["The UniFi G6 180 sees a full 180° from one point, without the blind seam two cameras leave between them. One camera on a corner can watch a whole back yard or the width of a motor court.",
                 "wide yards, motor courts and pool decks"],
        "business": ["One G6 180 can replace two or three fixed cameras across an open floor or a wide storefront, with no gap in the middle. Fewer cameras also means fewer cable runs and a smaller recorder.",
                     "sales floors, dining rooms, open offices and warehouses"],
    },
    "vandal": {
        "name": "Vandal-resistant domes",
        "photo": ph("cam-type-vandal"),
        "home": ["A dome in a metal housing with an IK10 impact rating, for any camera someone could reach. It keeps recording after a kick or a thrown object, which matters on a ground-floor garage or a gate post.",
                 "garages, gate posts and anything within reach"],
        "business": ["Where people can reach a camera, sooner or later someone hits it. An IK10-rated dome in a metal housing survives the impact, keeps recording, and its shape gives nothing to grab or twist.",
                     "parking garages, stairwells, gates and exposed entrances"],
    },
    "lpr": {
        "name": "License plate (LPR) cameras",
        "photo": ph("cam-type-lpr"),
        "home": ["UniFi's AI LPR camera reads plates where cars slow down, day and night. For a private house it is only worth it on a long gated drive or a shared private road.",
                 "gated drives and private roads"],
        "business": ["The UniFi AI LPR reads plates where vehicles slow down, and Protect lets you search footage by plate. We pair it with an overview camera for the vehicle and driver. Plate data stays on your own recorder.",
                     "gates, lot entrances, loading yards and HOA entries"],
    },
    "doorbell": {
        "name": "Video doorbells",
        "photo": ph("cam-type-doorbell"),
        "home": ["A UniFi Protect video doorbell shows the face at the door, records deliveries and lets you answer from your phone. It is wired, so there is no battery to fail in August, and it records with the other cameras.",
                 "front doors and side entries"],
        "business": ["A video doorbell at a staff or delivery door lets the team see and talk to whoever is outside before opening. It records to the same recorder as every other camera on the site.",
                     "staff entrances, delivery doors and after-hours visitors"],
    },
}

TABS_FULL = [
    ["camera-packages", "Packages"],
    ["cameras", "Cameras"],
    ["benefits", "Benefits"],
    ["why", "Why LUMA"],
    ["where", "Where we install"],
    ["faq", "FAQ"],
]

ALL_TYPES = ["bullet", "dome", "turret", "panoramic", "vandal", "lpr", "doorbell"]

PARTNER = "Installation work is carried out with our Florida-licensed low-voltage partner."

# "Trusted by" row (owner-approved clients, names and links only).
TRUSTED = {
    "label": "Trusted by",
    "clients": [
        {"name": "Accent Florida Homes", "url": "https://accentfh.com/", "logo": "/assets/clients/accent-florida-homes.webp"},
        {"name": "The Twins Spa", "url": "https://www.thetwinspa.com/", "logo": "/assets/clients/twins-spa.webp"},
        {"name": "MVM Custom Homes", "url": "https://mvmch.com/", "logo": None},
    ],
}

# ---------------------------------------------------------------------------
# /service-areas/sarasota/security  (main page)
# ---------------------------------------------------------------------------
SARASOTA_SECURITY = {
    "city": "sarasota",
    "service": "security",
    "camera": "home",
    "h1": "Security Camera Installation in Sarasota, FL",
    "title": "Security Camera Installation Sarasota FL | UniFi | LUMA",
    "description": "Security camera installation in Sarasota, FL: wired UniFi cameras for homes and businesses, recorded on site with no monthly fee. From $2,900 + tax.",
    "lede": "Cameras that are easy to see stop most break-ins before they start. When something does happen, clear 4K footage shows who it was, when, and which way they went, in a form the police and your insurer can use.",
    "paragraphs": [
        "Sarasota is hard on electronics. Salt air off the Gulf and the bay, humidity in every season and summer storms finish off cheap cameras and battery doorbells. We install weather-rated UniFi cameras with sealed connections, wired with PoE, so one cable carries power and video and nothing needs charging.",
    ],
    "packages_h2": "Home security camera packages in Sarasota",
    "faq_h2": "Security cameras in Sarasota: common questions",
    "cam": {
        "eyebrow": "Video Surveillance",
        "hero_photos": [ph("cam-hero-office"), ph("cam-hero-dome"), ph("cam-hero-owner")],
        "hero_bg": ph("cam-hero-wide-b"),
        "tabs": TABS_FULL,
        "plan": {"h2": "Start your free camera plan",
                 "lede": "Two short steps. We call you back to book a free walk of the property."},
        "process": {
            "h2": "Expert Camera Installation Across Sarasota & Manatee",
            "text": [
                "A good camera system is planned on site, not from a catalogue. We walk the property with you, ideally at the hour the light is worst, mark what each camera has to see, and check where cable can run and where the recorder will live.",
                "Within 48 hours you get a camera-by-camera plan: position, model, what it covers and a fixed line-item price. Most homes and small businesses are then wired and installed in a day, with cameras on PoE, connections sealed and the recorder on a battery backup.",
                "Before we leave, the recorder and the UniFi Protect app are set up on your phone, detection zones are tuned so you only hear about people and vehicles that matter, and we walk you through finding and saving a clip.",
            ],
            "photo": ["/assets/photos/sarasota-downtown-bayfront.jpg", "Downtown Sarasota skyline seen across the bayfront"],
        },
        "types": {
            "h2": "Types of Security Cameras We Install in Sarasota",
            "lede": "Every camera we fit comes from Ubiquiti's UniFi Protect line, so one recorder and one app run them all. The right type depends on what a position has to see, how far away, and how exposed it is.",
            "variant": "home",
            "items": ALL_TYPES,
        },
        "benefits": {
            "h2": "Benefits of a Video Surveillance System",
            "lede": "Visible cameras change behaviour before anything happens. Recorded video settles the questions afterwards.",
            "photo": ph("cam-benefits-wide"),
            "cards": [
                ["shield", "Deter break-ins", "A camera that is plainly visible at the drive and the front door sends most opportunists on to the next house. Good lighting and a posted sign add to the effect."],
                ["tag", "Reduce shrinkage and theft", "For a shop or an office, cameras on the register, the stock room and the back door cut losses from both sides of the counter and settle disputes quickly."],
                ["file", "Evidence for police and insurance", "Time-stamped 4K video, exported as a clip in a few taps. It gives the police a face or a plate to work with and your insurer something to look at."],
                ["phone", "Every camera on your phone", "Live and recorded video from every camera in the UniFi Protect app, with person and vehicle alerts, wherever you happen to be."],
                ["cloudoff", "No monthly cloud fees", "Footage stays on a recorder in your home or building. No subscription per camera, and no third party holding a copy of your driveway."],
                ["home", "Lock-and-leave for seasonal homes", "When the house sits empty from May to November, you can check the dock, the drive and the lanai after a storm without calling a neighbour."],
            ],
        },
        "trusted": TRUSTED,
        "why": {
            "h2": "What Makes LUMA the Right Camera Company in Sarasota",
            "lede": "A small local studio that designs the network the cameras run on, not a national alarm brand.",
            "photo": ph("cam-why-rack"),
            "items": [
                ["A local Sarasota studio", "We are based in Sarasota and work across Sarasota and Manatee Counties. The people who walk your property are the people who plan and set up the system. " + PARTNER],
                ["Equipment chosen for coastal conditions", "IP66 weather-rated cameras, sealed cable entries, mounts placed under cover and away from direct spray, and a battery backup on the recorder for summer storms."],
                ["Cameras on their own network", "Cameras run on their own network segment, apart from your laptops and guest Wi-Fi. We can tie them into your Wi-Fi, lighting and alarm, so a camera event can switch on the lights. See [Wi-Fi and cabling in Sarasota](sa-sarasota-networking)."],
                ["Support from the same team", "After installation you call the same team that installed it, for a re-aim, a new login or one more camera."],
                ["A transparent, fixed price", "The plan lists every camera, every cable run and the recorder line by line. After the walk the price is fixed before any work starts."],
                ["NDAA-compliant UniFi hardware", "UniFi Protect cameras and recorders are NDAA-compliant, which matters to businesses that work with government agencies and to owners who care where their hardware comes from."],
            ],
        },
        "steps": {
            "eyebrow": "Installation",
            "h2": "How It Works",
            "lede": "Four steps from the first call to the app on your phone. Most homes and small businesses are installed in a single day.",
            "items": [
                ["map", "Walk and assess", "We walk the property with you, mark what each position has to see, and check cable routes, mounting points and where the recorder will live."],
                ["clipboard", "Camera plan in 48 hours", "A camera-by-camera plan with the model, the coverage and a fixed line-item price, within 48 hours of the walk."],
                ["tool", "Installation", "Wired PoE cameras, sealed connections, the recorder and switch on a battery backup. One day for most homes and small businesses."],
                ["app", "App setup and training", "UniFi Protect on your phones, alerts tuned to people and vehicles, and a short lesson on finding and exporting a clip."],
            ],
        },
        "scenarios": {
            "h2": "Common Sarasota Camera Installation Scenarios",
            "lede": "Where we install, and what each kind of property needs from its cameras.",
            "banner": ["/assets/photos/sarasota-marina.jpg", "Boats moored at a marina in Sarasota"],
            "cards": [
                {"title": "Waterfront homes and marinas", "photo": ph("cam-scen-marina"),
                 "text": "Docks, boat lifts and seawalls sit in salt spray all year. Cameras go on stainless mounts, under cover where possible, with sealed connections; a turret or a G6 180 covers the dock and the water side."},
                {"title": "Warehouses and light industrial", "photo": ph("cam-scen-warehouse"),
                 "text": "Loading docks, roll-up doors, the yard and the gate. Bullets with optical zoom along the long sides, a plate camera at the gate, and a recorder sized for weeks of footage.",
                 "links": [["sa-sarasota-warehouse-security-cameras", "Warehouse security cameras in Sarasota"]]},
                {"title": "Retail and restaurants", "photo": ph("cam-scen-retail"),
                 "text": "Registers, the sales floor, the back door and the parking lot. A dome over each register angled away from the PIN pad, a 180° camera for the floor, and the back door recorded around the clock.",
                 "links": [["sa-sarasota-retail-security-cameras", "Retail store security cameras"], ["sa-sarasota-restaurant-security-cameras", "Restaurant security cameras"]]},
                {"title": "Offices and medical or dental practices", "photo": ph("cam-scen-office"),
                 "text": "Entrances, reception and the corridors to records rooms. Placement is HIPAA-aware: cameras watch doors and waiting areas, never exam or treatment rooms, and screens with patient data stay out of frame.",
                 "links": [["sa-sarasota-business-security", "Office and business security camera systems in Sarasota"]]},
                {"title": "HOA gates and communities", "photo": ph("cam-type-lpr"),
                 "text": "A plate camera and an overview camera at each gate, plus the pool, the mail room and the garage. Plate data stays on the association's own recorder, with no cloud plate database.",
                 "links": [["sa-sarasota-hoa-security-cameras", "HOA and condo security cameras"]]},
                {"title": "Seasonal homes", "photo": ph("cam-type-turret"),
                 "text": "For owners who spend the summer up north: alerts only for the zones that matter, a look at the house after every storm, and no subscription running while the house sits empty.",
                 "links": [["journal-cameras-fees", "Home cameras without a monthly cloud fee"]]},
            ],
        },
        "choosing": {
            "h2": "Choosing the Right Camera for Your Property",
            "photo": ph("cam-type-bullet"),
            "text": [
                "Resolution comes first. A 4K camera lets you zoom into a recording and still identify a face or a plate; 2K is enough for a porch or a hallway where people pass close. More pixels also mean more storage, so we mix the two by position.",
                "Field of view trades against distance: a wide lens covers the whole yard but makes a face at the far end small. Night vision matters more than people expect. Infrared on UniFi outdoor cameras reaches roughly 100 ft or more, and landscape lighting brings back colour at night.",
                "Retention sets the recorder. Storage is cameras × bitrate × hours × days, so a four-camera house fits on one drive while a twelve-camera site needs a multi-drive recorder. Tell us how many days you want to keep and we size it.",
                "Wired PoE beats Wi-Fi and battery cameras in Florida: no batteries failing in the heat, no Wi-Fi dropouts across a lanai, one cable for power and video. A Wi-Fi camera is the fallback for a spot no cable can reach.",
                "All UniFi hardware we fit is NDAA-compliant. Audio is off by default: Florida requires the consent of everyone in a conversation before it is recorded (Fla. Stat. 934.03), so camera microphones stay switched off.",
            ],
        },
        "watch": {
            "h2": "Watch From Anywhere",
            "photo": ph("cam-monitor-phone"),
            "text": [
                "Every camera shows up in the UniFi Protect app on your phone, tablet or computer: live view, a timeline of person and vehicle detections, and clips you can save or share.",
                "Family members, a property manager or a house watcher can each get their own login with only the cameras they need, and you can remove access at any time.",
                "Alarm monitoring is available on request. The cameras themselves never need a subscription.",
            ],
        },
        "call": "to talk to the LUMA camera team today",
        "final": {
            "h2": "Request a Free Camera Installation Estimate in Sarasota",
            "text": "Tell us about the property and what the cameras should see. We call you back to book a free walk, and you get a camera-by-camera plan with a fixed price within 48 hours of it.",
        },
    },
    "faq": [
        {"q": "How much does security camera installation cost in Sarasota?", "a": "Our packages start from $2,900 for 4 cameras (Home 4), from $5,900 for 8 cameras (Office 8) and from $12,900 for 12 or more (Business Pro), plus tax. Each includes the cameras, a UniFi recorder and the installation. The final fixed price follows a free walk of the property."},
        {"q": "How many security cameras does a house need?", "a": "Most Sarasota houses need four to eight: the driveway, the front door, the back yard or lanai, and each side gate. Waterfront homes often add one for the dock. We count them with you on the walk."},
        {"q": "Is there a monthly fee?", "a": "No. Video records to a UniFi recorder on your property, with no subscription and no per-camera fee. Alarm monitoring is a separate option, only if you ask for it."},
        {"q": "How long does installation take?", "a": "Most homes and small businesses are installed in one day. Larger sites, long cable runs and gates take longer; the camera plan states the number of days before you commit."},
        {"q": "Wired or wireless cameras for a Florida home?", "a": "Wired PoE wherever a cable can reach. Batteries struggle in the heat and Wi-Fi drops across lanais and block walls. A wireless camera is the fallback for one spot no cable can reach."},
        {"q": "Can you replace or upgrade my existing cameras?", "a": "Usually, yes. If the old cameras run on network cable (Cat5e or Cat6), we can often reuse it for new PoE cameras, which saves time and drywall. Older coax systems usually need new cable. We check on the walk and tell you what can stay."},
        {"q": "Do your cameras record audio?", "a": "Audio is off by default. Florida law requires the consent of everyone in a conversation before it is recorded (Fla. Stat. 934.03), so we leave camera microphones switched off."},
        {"q": "Are UniFi cameras NDAA-compliant?", "a": "Yes. The UniFi Protect cameras and recorders we install are NDAA-compliant."},
        {"q": "Do you install cameras for businesses and HOAs?", "a": "Yes: offices, shops, restaurants, warehouses and associations. See [business security camera systems in Sarasota](sa-sarasota-business-security) and [HOA and condo security cameras](sa-sarasota-hoa-security-cameras)."},
        {"q": "Which areas do you serve?", "a": "Sarasota and Manatee Counties, including Lakewood Ranch, Bradenton, Venice, Osprey, Siesta Key, Longboat Key, Anna Maria Island and Palmetto. For Manatee County homes, see [home security cameras in Bradenton](sa-bradenton-security)."},
    ],
}

# ---------------------------------------------------------------------------
# /service-areas/sarasota/business-security  (business hub)
# ---------------------------------------------------------------------------
SARASOTA_BUSINESS = {
    "city": "sarasota",
    "service": "business-security",
    "camera": "business",
    "h1": "Business Security Camera Systems in Sarasota, FL",
    "title": "Office & Business Security Camera Systems Sarasota FL | LUMA",
    "description": "Office and business security camera systems in Sarasota, FL: UniFi cameras, an on-site recorder and manager logins, no per-camera fees. From $5,900 + tax.",
    "lede": "Office and business security camera systems do two jobs. They discourage theft and trouble before it starts, and afterwards they answer the hard questions, from a till that came up short to a slip-and-fall claim, with video you can hand to an insurer or the police.",
    "paragraphs": [
        "A Sarasota storefront or office takes the same coastal beating as a house: salt air near the water, humidity in every season, summer lightning. We fit weather-rated UniFi cameras with sealed connections, wired back to a recorder in your building, and keep them on their own network, apart from the office computers.",
    ],
    "packages_h2": "Business security camera system packages in Sarasota",
    "faq_h2": "Business camera systems in Sarasota: common questions",
    "cam": {
        "eyebrow": "Commercial Video Surveillance",
        "hero_photos": [ph("cam-hero-office"), ph("cam-scen-retail"), ph("cam-hero-dome")],
        "hero_bg": ph("cam-hero-wide-a"),
        "tabs": TABS_FULL,
        "plan": {"h2": "Start your free business camera plan",
                 "lede": "Two short steps. We call back to book a walk of the site at a time that suits the business."},
        "process": {
            "h2": "Commercial Camera Installation Across Sarasota & Manatee",
            "text": [
                "It starts with a walk of the site with the owner or manager: entrances, the counter or front desk, stock and equipment rooms, the back door and the lot. Each camera position is marked with what it must capture and why.",
                "Within 48 hours you get a camera-by-camera plan with models, coverage and a fixed price. Installation is scheduled around your hours, before opening or after closing if the floor cannot be disturbed, and most small businesses are finished in a day.",
                "You get a working system, not a box of parts: the recorder set up for the retention you need, a login for each manager, and a short session on finding an incident and exporting the clip.",
            ],
            "photo": ["/assets/photos/sarasota-downtown-bayfront.jpg", "Downtown Sarasota skyline seen across the bayfront"],
        },
        "types": {
            "h2": "Types of Business Security Cameras We Install",
            "lede": "We standardise on Ubiquiti UniFi Protect: G6 series cameras, the G6 180 for wide spaces, G6 Pro models for exposed positions and the AI LPR for gates, all on one recorder and in one app.",
            "variant": "business",
            "items": ALL_TYPES,
        },
        "benefits": {
            "h2": "Why Businesses Invest in Video Surveillance",
            "lede": "What owners and managers actually get back from a camera system.",
            "photo": ph("cam-benefits-wide"),
            "cards": [
                ["tag", "Less shrinkage", "Cameras over the register, the stock room and the back door cut losses from shoplifting, mistakes at the till and stock walking out the back."],
                ["file", "Fewer liability disputes", "A slip-and-fall claim, a scratched car in the lot or a short delivery becomes a clip to review, not an argument."],
                ["shield", "Safer staff", "Recorded entrances and a covered parking lot make opening and closing shifts safer, and a doorbell at the staff door means nobody opens it blind."],
                ["building", "Every location in one app", "Owners with more than one site see every store or office in the UniFi Protect app, each site with its own recorder."],
                ["users", "Access for managers", "Each manager gets a login limited to the cameras and history they need. Access is removed in seconds when someone leaves."],
                ["cloudoff", "No per-camera fees", "Footage stays on a recorder you own. Adding a camera later adds hardware, not another monthly line on the bill."],
            ],
        },
        "trusted": TRUSTED,
        "why": {
            "h2": "Why Sarasota Businesses Choose LUMA for Cameras",
            "lede": "A local team that treats the cameras and the network as one job.",
            "photo": ph("cam-why-rack"),
            "items": [
                ["Local and reachable", "A Sarasota studio working across Sarasota and Manatee Counties. You deal with the same small team from the walk to the support call. " + PARTNER],
                ["Hardware for the coast", "IP66 outdoor cameras, metal housings wherever a camera can be reached, sealed cable entries and covered mounts near the water."],
                ["The network done properly", "Cameras on their own network segment, the recorder and switches on a battery backup, and remote access that does not open the office network. If the Wi-Fi needs work, it is part of the same project. See [UniFi networking](networking)."],
                ["Built around your hours", "Installation before opening or after closing when needed, so the floor and the register keep working."],
                ["A line-item price", "Every camera, cable run and the recorder are listed in the plan. The price is fixed after the walk."],
                ["NDAA-compliant UniFi", "The cameras and recorders are NDAA-compliant UniFi Protect hardware, a requirement for many government contractors."],
            ],
        },
        "steps": {
            "eyebrow": "Installation",
            "h2": "How It Works for a Business",
            "lede": "From the first call to managers checking the cameras on their phones.",
            "items": [
                ["map", "Site walk", "We walk the premises with the owner or manager and agree what each camera must capture: faces at the door, the drawer at the register, plates at the gate."],
                ["clipboard", "Plan and price in 48 hours", "Models, positions, recorder size and retention, with a fixed price on every line."],
                ["tool", "Installation around your hours", "Cameras wired PoE, the recorder in a locked closet on a UPS, scheduled around opening hours."],
                ["app", "Logins and handover", "Accounts for owners and managers, alerts for after-hours activity, and a walkthrough of search and export."],
            ],
        },
        "scenarios": {
            "h2": "Business Camera Installations Around Sarasota",
            "lede": "The layouts we are asked for most, and what each one needs.",
            "banner": ["/assets/photos/sarasota-downtown-park.jpg", "Downtown Sarasota buildings beside a park"],
            "cards": [
                {"title": "Offices and medical practices", "photo": ph("cam-scen-office"),
                 "text": "Entrances, reception, corridors and the server or records room. In medical and dental offices cameras stay on doors and waiting areas, never exam rooms, and screens with patient information stay out of frame.",
                 "links": [["sa-bradenton-business-security", "Office cameras in Bradenton and Lakewood Ranch"]]},
                {"title": "Retail stores", "photo": ph("cam-scen-retail"),
                 "text": "A face-height camera at every customer door, a dome over each register aimed at the drawer and away from the PIN pad, the sales floor and the stock room.",
                 "links": [["sa-sarasota-retail-security-cameras", "Retail store security cameras in Sarasota"]]},
                {"title": "Restaurants and bars", "photo": ph("cam-type-panoramic"),
                 "text": "The bar and each POS, the dining room for incident claims, the kitchen line, the cash office and the back door where deliveries arrive.",
                 "links": [["sa-sarasota-restaurant-security-cameras", "Restaurant security cameras in Sarasota"]]},
                {"title": "Warehouses and yards", "photo": ph("cam-scen-warehouse"),
                 "text": "Dock doors, aisles, the yard and the gate, with a plate camera on the way in and long retention, because missing stock is often noticed weeks later.",
                 "links": [["sa-sarasota-warehouse-security-cameras", "Warehouse security cameras in Sarasota"]]},
                {"title": "HOAs and condo buildings", "photo": ph("cam-type-lpr"),
                 "text": "Gates, pools, mail rooms and garages, with a written policy on who sees footage and plate data kept on the association's own recorder.",
                 "links": [["sa-sarasota-hoa-security-cameras", "HOA and condo security cameras in Sarasota"]]},
                {"title": "Marinas and waterfront businesses", "photo": ph("cam-scen-marina"),
                 "text": "Docks, fuel and boat-lift areas and the gate, on stainless mounts with the cameras kept out of direct spray."},
            ],
        },
        "choosing": {
            "h2": "Choosing a Camera System for Your Business",
            "photo": ph("cam-type-vandal"),
            "text": [
                "Start from what the footage has to prove. Identifying a face at a door needs a camera mounted low, with the face filling a good part of the frame; watching a sales floor needs width, not detail. 4K where detail matters, 2K where people pass close.",
                "Retention is usually set by someone else: an insurer, a lease or your own incident policy. About 30 days is common for offices and shops; warehouses and associations often keep longer. The recorder, from a UNVR to a UNVR G2 Pro, follows from cameras × bitrate × hours × days.",
                "Placement has rules. At card terminals the camera sees the counter, not the PIN pad. In medical offices, doors and waiting rooms only. Restrooms and fitting rooms, never. Audio stays off: Florida requires all-party consent to record a conversation (Fla. Stat. 934.03).",
                "Wired PoE is the standard for a business: steadier video, no batteries, nothing for staff to recharge. All UniFi hardware we install is NDAA-compliant. For a house rather than a business, see [security camera installation in Sarasota](sa-sarasota-security).",
            ],
        },
        "watch": {
            "h2": "Watch Every Location From Anywhere",
            "photo": ph("cam-monitor-phone"),
            "text": [
                "The UniFi Protect app shows every camera at every site in one place. Search a day by person or vehicle instead of scrubbing hours of video, and export a clip for an insurer or the police in a few taps.",
                "Each manager gets a login for their own location and history; the owner sees everything. Alerts can be limited to after-hours activity, so phones stay quiet while the business is open.",
                "Alarm monitoring is available on request. The cameras never need a subscription.",
            ],
        },
        "call": "to talk to the LUMA team about your business",
        "final": {
            "h2": "Request a Free Business Camera Estimate in Sarasota",
            "text": "Tell us about the business: the kind of space, how many doors, whether there is a lot or a gate. We call back to book a walk of the site, and you get a plan with a fixed price within 48 hours of it.",
        },
    },
    "faq": [
        {"q": "How much does a business security camera system cost in Sarasota?", "a": "Most offices and shops start with Office 8, from $5,900 plus tax for eight cameras. Larger sites, gates and warehouses start with Business Pro, from $12,900 plus tax for twelve or more. A small office with four cameras can start from $2,900 plus tax. The price is fixed after a free site walk."},
        {"q": "Can I see several locations in one app?", "a": "Yes. Each location has its own UniFi recorder, and the owner sees every site in the UniFi Protect app. Managers can be limited to their own location."},
        {"q": "Can managers have their own access?", "a": "Yes. Each person gets a login with only the cameras and history you allow, and you can remove it at any time without touching anyone else's."},
        {"q": "How long should a business keep camera footage?", "a": "About 30 days is common for offices and shops. If your insurer, lease or policy asks for longer, we size the recorder drives for it. Clips of an incident can be exported and kept as long as you need."},
        {"q": "Where can cameras go in a medical or dental office?", "a": "Entrances, reception, waiting areas and corridors. We keep cameras out of exam and treatment rooms and aim them so screens with patient information are not recorded."},
        {"q": "Can a camera watch the register without recording card PINs?", "a": "Yes. Register cameras are mounted overhead and aimed at the drawer, the screen and the customer's hands, angled away from the PIN pad."},
        {"q": "Do business cameras need a monthly subscription?", "a": "No. UniFi Protect records to a recorder in your building, with no per-camera licence. Alarm monitoring is available on request as a separate service."},
        {"q": "Can you install outside business hours?", "a": "Yes. We can schedule the work before opening or after closing when the floor or the register cannot be disturbed."},
        {"q": "Do you cover Bradenton and Lakewood Ranch?", "a": "Yes, all of Sarasota and Manatee Counties. See [commercial security cameras in Bradenton](sa-bradenton-business-security)."},
        {"q": "Do the cameras record audio?", "a": "No, audio is off by default. Florida requires the consent of everyone in a conversation before it is recorded (Fla. Stat. 934.03)."},
    ],
}

# ---------------------------------------------------------------------------
# Segment pages: hero, form, packages, camera types, one focus section, FAQ,
# final form. Shorter template, own copy.
# ---------------------------------------------------------------------------


def seg_tabs(focus_label: str) -> list[list[str]]:
    return [["camera-packages", "Packages"], ["cameras", "Cameras"], ["layout", focus_label], ["faq", "FAQ"]]


BRADENTON_BUSINESS = {
    "city": "bradenton",
    "service": "business-security",
    "camera": "business",
    "h1": "Commercial Security Camera Systems in Bradenton, FL",
    "title": "Commercial Security Cameras Bradenton FL | UniFi | LUMA",
    "description": "Commercial security cameras for Bradenton, Lakewood Ranch and Palmetto businesses. UniFi Protect, wired 4K cameras, on-site recorder, no monthly fees.",
    "lede": "Bradenton businesses range from storefronts on Manatee Avenue and offices in Lakewood Ranch to workshops and storage yards along the river and in Palmetto. We design and install UniFi Protect commercial security camera systems for them: wired 4K cameras, recording on a box you own, and no per-camera monthly fees.",
    "paragraphs": [
        "A lot of Manatee County commercial property is spread out: a building, a yard, a fenced lot, sometimes a second building. That is where wired cameras earn their place. One cable per camera carries power and video, so there are no batteries to replace and no Wi-Fi links dropping across a yard. " + PARTNER,
    ],
    "packages_h2": "Commercial camera packages for Manatee County",
    "faq_h2": "Commercial cameras in Bradenton: common questions",
    "cam": {
        "eyebrow": "Commercial Video Surveillance · Manatee County",
        "hero_photos": [ph("cam-scen-office"), ph("cam-type-bullet"), ph("cam-scen-warehouse")],
        "hero_bg": ph("cam-hero-wide-a"),
        "tabs": seg_tabs("Layouts"),
        "plan": {"h2": "Start your free camera plan for a Manatee County site",
                 "lede": "Two short steps. We call back to set up a walk of the site in Bradenton, Lakewood Ranch or Palmetto."},
        "types": {
            "h2": "Commercial Cameras We Install in Bradenton",
            "lede": "Five UniFi Protect camera types cover nearly every office, shop and yard in Manatee County.",
            "items": [
                ["bullet", "Along fence lines and across lots the G6 Pro Bullet's optical zoom keeps a vehicle at the far end identifiable. Mounted high on the building, it also tells visitors the yard is recorded.", "fence lines, yards and parking lots"],
                ["turret", "The G6 Turret is the workhorse for corridors and back doors in office suites and workshops: 4K, IP66, about 98 ft of infrared.", "back doors, corridors and workshop bays"],
                ["dome", "At a Lakewood Ranch office entrance or a reception desk, a ceiling dome catches faces at a usable size without making the lobby feel watched.", "entrances, reception and waiting rooms"],
                ["lpr", "On a contractor's yard or a storage lot, the AI LPR at the gate records the plate of every vehicle in and out, searchable later in Protect.", "yard gates and lot entrances"],
                ["panoramic", "A G6 180 on the corner of a building covers a whole storage yard or a wide workshop floor from one mounting point.", "storage yards and open workshop floors"],
            ],
        },
        "focus": {
            "id": "layout",
            "h2": "Typical Layouts in Manatee County",
            "photo": ph("cam-why-rack"),
            "text": [
                "Office suites and medical offices in Lakewood Ranch usually need the entrance, the reception desk, the back door and the parking lot. A dome at the door, a turret in the corridor and a G6 Pro Bullet on the lot cover most of them.",
                "Workshops, contractors' yards and storage lots need the perimeter and the gate: G6 Pro Bullets along the fence line, an AI LPR at the gate, and a G6 PTZ when the yard is large enough that someone has to follow a vehicle across it.",
                "Video records to a UniFi recorder on the property, sized for how many days you need to keep (commonly about 30) and on a battery backup. Owners and managers view it in the UniFi Protect app, each with their own login.",
                "Riverfront and island sites see salt air and summer storms, so cameras go under eaves or covers where possible and every cable entry is sealed. The full camera-by-position guide is on [office and business security camera systems in Sarasota](sa-sarasota-business-security); for homes in Manatee County, see [home security cameras in Bradenton](sa-bradenton-security).",
            ],
        },
        "call": "to plan cameras for a Manatee County site",
        "final": {
            "h2": "Request a Free Commercial Camera Estimate in Bradenton",
            "text": "Tell us about the site: the building, the lot, any yard or gate. We call back to book a walk and send a plan with a fixed price within 48 hours of it.",
        },
    },
    "faq": [
        {"q": "What does a commercial camera system cost in Bradenton?", "a": "The same as in Sarasota: from $5,900 for 8 cameras and from $12,900 for 12 or more, plus tax, with a fixed price after a free walk of the site."},
        {"q": "Do you install commercial security cameras in Bradenton?", "a": "Yes. We cover Bradenton, Lakewood Ranch, Palmetto, Ellenton, Parrish and the rest of Manatee County from our Sarasota base."},
        {"q": "Is there a monthly fee for the cameras?", "a": "No. UniFi Protect records to a recorder on your property and Ubiquiti charges no per-camera licence."},
        {"q": "Can you cover a yard or a gate far from the building?", "a": "Usually yes. Cameras up to about 300 ft of cable from a switch run on one cable; beyond that we add a switch closer to the camera or use fiber."},
        {"q": "Can the system record licence plates at our gate?", "a": "Yes, with the UniFi AI LPR camera aimed where vehicles slow down at the gate or entrance."},
        {"q": "Can we add cameras later?", "a": "Yes. We size the recorder and the switch with spare capacity so more cameras can be added without replacing the core."},
        {"q": "Do the cameras record audio?", "a": "No, audio is off by default. Florida requires everyone's consent to record a conversation (Fla. Stat. 934.03)."},
    ],
}

RETAIL = {
    "city": "sarasota",
    "service": "retail-security-cameras",
    "camera": "business",
    "h1": "Retail Store Security Cameras in Sarasota, FL",
    "title": "Retail Store Security Cameras Sarasota FL | UniFi | LUMA",
    "description": "Security cameras for Sarasota retail stores and boutiques: register, entrance, sales floor, stock room. UniFi Protect, on-site recording, no monthly fees.",
    "lede": "A store needs four things from its cameras: a clear face at the door, a clear view of the register, the sales floor covered without blind aisles, and the stock room and back door recorded. We design UniFi Protect retail security camera systems for Sarasota shops and boutiques, from St. Armands and Main Street to the plazas along Tamiami Trail.",
    "paragraphs": [
        "Retail losses come from three directions: shoplifting on the floor, mistakes and theft at the register, and stock leaving by the back door. A good layout covers all three without making the store feel watched. Cameras are wired PoE and record to a recorder in the back office, with no monthly fee per camera. " + PARTNER,
    ],
    "packages_h2": "Camera packages for shops",
    "faq_h2": "Store cameras in Sarasota: common questions",
    "cam": {
        "eyebrow": "Retail Video Surveillance",
        "hero_photos": [ph("cam-scen-retail"), ph("cam-type-dome"), ph("cam-hero-owner")],
        "hero_bg": ph("cam-hero-wide-a"),
        "tabs": seg_tabs("Store layout"),
        "plan": {"h2": "Start your free store camera plan",
                 "lede": "Two short steps. We walk the store before opening or after closing."},
        "types": {
            "h2": "Cameras We Install in Sarasota Stores",
            "lede": "A typical boutique or shop uses five UniFi camera types, all on one recorder in the back office.",
            "items": [
                ["dome", "Over each register a dome looks down at the drawer, the screen and the customer's hands, angled away from the card reader's PIN pad. Another at the door records every face coming in.", "registers and customer entrances"],
                ["panoramic", "A G6 180 on one wall covers the whole sales floor without blind aisles, so one camera does the work of three.", "the sales floor and long display walls"],
                ["turret", "Stock rooms and back doors get a G6 Turret: easy to aim at the door, sealed against humidity, and clear in low light.", "the stock room, the back door and the fitting-room corridor"],
                ["bullet", "Outside, a G6 Pro Bullet records the sidewalk, the storefront and the lot, with optical zoom for faces and plates at a distance.", "storefronts, sidewalks and parking"],
                ["vandal", "In plazas and parking garages, cameras within reach get an IK10 metal housing that keeps recording after a knock.", "exposed entrances in plazas and garages"],
            ],
        },
        "focus": {
            "id": "layout",
            "h2": "Where the Cameras Go in a Store",
            "photo": ph("cam-scen-retail"),
            "text": ["This is the layout we start from for a typical Sarasota storefront, before the walk changes it:"],
            "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Customer entrance", "G6 Dome", "Every face coming in, at a size you could hand to the police."],
                ["Register", "Dome overhead", "The drawer, the screen and the customer's hands, angled away from the PIN pad."],
                ["Sales floor", "G6 180", "The floor from one wall, without blind aisles."],
                ["Fitting room corridor", "G6 Turret", "The corridor and entrance only. Never inside a fitting room."],
                ["Stock room and back door", "G6 Turret", "Who comes in and out, and deliveries arriving."],
                ["Storefront and parking", "G6 Pro Bullet", "The sidewalk, the lot and vehicles, with optical zoom."],
            ]},
            "after": [
                "UniFi Protect tags every person and vehicle the cameras see, so finding who stood at the register between 2 and 3 pm is a search, not an evening of scrubbing. Cameras never go inside fitting rooms or restrooms, and microphones stay off in customer areas. The general guide is on [office and business security camera systems in Sarasota](sa-sarasota-business-security).",
            ],
        },
        "call": "to plan cameras for your store",
        "final": {
            "h2": "Request a Free Store Camera Estimate in Sarasota",
            "text": "Tell us about the store: the number of doors and registers, the stock room, any parking. We call back to book a walk before or after opening hours.",
        },
    },
    "faq": [
        {"q": "What does a store camera system cost?", "a": "Our packages start from $2,900 for 4 cameras, $5,900 for 8 and $12,900 for 12 or more, plus tax. The fixed price for your store follows a free walk."},
        {"q": "How many cameras does a small retail store need?", "a": "A single-room boutique usually needs 4 to 6: the entrance, the register, one or two for the floor, and the stock room or back door."},
        {"q": "Can the cameras record audio at the register?", "a": "They can, but Florida requires everyone's consent to record a conversation, so we leave audio off in customer areas unless you have legal advice to use it."},
        {"q": "Is there a monthly fee?", "a": "No. Video records to a UniFi recorder in your store, with no per-camera subscription."},
        {"q": "Can I see more than one store in the same app?", "a": "Yes. Each location has its own recorder, and the owner sees all of them in the UniFi Protect app."},
    ],
}

RESTAURANT = {
    "city": "sarasota",
    "service": "restaurant-security-cameras",
    "camera": "business",
    "h1": "Restaurant Security Cameras in Sarasota, FL",
    "title": "Restaurant Security Cameras Sarasota FL | UniFi | LUMA",
    "description": "Security camera systems for Sarasota restaurants and bars: entrance, bar, POS, kitchen line, back door and deliveries. UniFi Protect, no monthly fees.",
    "lede": "A restaurant runs on cash, inventory and a back door that is open half the day. Its cameras have to cover the bar and the registers, the kitchen line, deliveries and the dumpster area, and still be useful at midnight when the owner wants to know who locked up. We install UniFi Protect restaurant security camera systems in Sarasota and Manatee County.",
    "paragraphs": [
        "Most of what owners ask us for is not about break-ins. It is about disputes at the register, a slip-and-fall claim, a delivery that came short, or a staff question that needs a clear answer. Cameras placed for those moments are different from cameras placed for a burglar. " + PARTNER,
    ],
    "packages_h2": "Camera packages for restaurants",
    "faq_h2": "Restaurant cameras in Sarasota: common questions",
    "cam": {
        "eyebrow": "Restaurant Video Surveillance",
        "hero_photos": [ph("cam-type-panoramic"), ph("cam-type-bullet"), ph("cam-hero-dome")],
        "hero_bg": ph("cam-hero-wide-a"),
        "tabs": seg_tabs("Restaurant layout"),
        "plan": {"h2": "Start your free restaurant camera plan",
                 "lede": "Two short steps. We walk the restaurant between services, when the floor is quiet."},
        "types": {
            "h2": "Cameras We Install in Sarasota Restaurants",
            "lede": "Five UniFi camera types, chosen for heat, grease, low light and long hours.",
            "items": [
                ["panoramic", "A G6 180 covers the dining room between tables from one wall, which is what a slip-and-fall or an incident claim needs.", "dining rooms and patios"],
                ["dome", "Over the bar and each POS a dome records pours, the register and the cash drawer without blocking the bartender's line of sight.", "the bar, POS stations and the host stand"],
                ["turret", "Kitchens get sealed G6 Turrets mounted out of the hood plume, so the line and the pass stay visible and the housing can be wiped down.", "the kitchen line, the cash office and the walk-in door"],
                ["bullet", "At the back door a G6 Pro Bullet records vendors, deliveries and the dumpster area, with the vehicle in frame.", "back doors, deliveries and parking"],
                ["doorbell", "A video doorbell at the staff entrance lets the closing manager see who is knocking before opening up.", "staff and delivery doors"],
            ],
        },
        "focus": {
            "id": "layout",
            "h2": "Where the Cameras Go in a Restaurant",
            "photo": ph("cam-monitor-phone"),
            "text": ["The starting layout for a typical Sarasota restaurant:"],
            "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Entrance and host stand", "G6 Dome", "Faces on the way in, and the door at closing."],
                ["Bar and POS stations", "Dome overhead", "Pours, the register and the cash drawer."],
                ["Dining room", "G6 180", "The floor between tables, for slip-and-fall and incident claims."],
                ["Kitchen line", "G6 Turret", "The line and the pass, out of fryer heat and grease."],
                ["Cash office and walk-in door", "G6 Turret", "Who opened the safe or the cooler, and when."],
                ["Back door and deliveries", "G6 Pro Bullet", "Vendors, deliveries and the dumpster area, with vehicles in frame."],
            ]},
            "after": [
                "Managers review from their phones and export a clip for an insurer or the police in a few taps; recording stays on a recorder in the office. Florida requires everyone's consent to record a conversation, so microphones stay off in the dining room and bar. See also [business security camera systems in Sarasota](sa-sarasota-business-security).",
            ],
        },
        "call": "to plan cameras for your restaurant",
        "final": {
            "h2": "Request a Free Restaurant Camera Estimate in Sarasota",
            "text": "Tell us about the restaurant: the bar, the number of POS stations, the kitchen and the back door. We call back to book a walk between services.",
        },
    },
    "faq": [
        {"q": "What does a restaurant camera system cost?", "a": "Most restaurants fit the Office 8 package, from $5,900 plus tax, or Business Pro for 12 or more cameras, from $12,900 plus tax. The fixed price follows a free walk of the restaurant."},
        {"q": "How many cameras does a restaurant need?", "a": "A small restaurant usually needs 8 to 12: the entrance, the bar and each POS, the dining room, the kitchen line, the cash office, the back door and the lot."},
        {"q": "Should restaurant cameras record audio?", "a": "In Florida we recommend no audio in guest areas, because recording a conversation requires everyone's consent."},
        {"q": "Can managers check the cameras from home?", "a": "Yes. Each manager gets a UniFi Protect login with the cameras and the history you choose."},
        {"q": "Will the cameras keep working in a hot kitchen?", "a": "Yes, if they are placed out of the direct heat and grease. We choose sealed turret cameras for kitchens and keep them out of the hood area."},
        {"q": "Is there a monthly fee?", "a": "No. Video records to a UniFi recorder in the restaurant, with no subscription and no per-camera fee."},
    ],
}

WAREHOUSE = {
    "city": "sarasota",
    "service": "warehouse-security-cameras",
    "camera": "pro",
    "h1": "Warehouse Security Cameras in Sarasota, FL",
    "title": "Warehouse Security Cameras Sarasota FL | UniFi | LUMA",
    "description": "Warehouse and yard security camera systems in Sarasota and Manatee: dock doors, aisles, yard, gate and plates. UniFi Protect 4K cameras, on-site recorder.",
    "lede": "A warehouse needs coverage where goods and vehicles move: dock doors, the yard, the gate, and the aisles where stock sits. We design UniFi Protect warehouse security camera systems for distribution space, workshops and storage buildings in Sarasota and Manatee County, with a licence plate camera at the gate and enough recorder for weeks of footage.",
    "paragraphs": [
        "Warehouses are big, tall and often dark at night. That changes the camera choice: longer infrared range, optical zoom for long aisles, and fewer, better cameras on the yard instead of many cheap ones. Every camera is wired, so there is nothing to recharge on a 30-foot ceiling. " + PARTNER,
    ],
    "packages_h2": "Camera packages for warehouses and yards",
    "faq_h2": "Warehouse cameras in Sarasota: common questions",
    "cam": {
        "eyebrow": "Warehouse Video Surveillance",
        "hero_photos": [ph("cam-scen-warehouse"), ph("cam-type-vandal"), ph("cam-why-rack")],
        "hero_bg": ph("cam-hero-wide-a"),
        "tabs": seg_tabs("Warehouse layout"),
        "plan": {"h2": "Start your free warehouse camera plan",
                 "lede": "Two short steps. We walk the building, the docks and the yard with you."},
        "types": {
            "h2": "Cameras We Install in Sarasota Warehouses",
            "lede": "Big spaces, long sight lines and darkness: five UniFi camera types for the job.",
            "items": [
                ["bullet", "Dock doors and long building sides get G6 Pro Bullets, whose optical zoom keeps a pallet label or a face readable at the far end.", "dock doors, building sides and the yard"],
                ["lpr", "The AI LPR at the gate records the plate of every truck and car in and out, searchable by plate in Protect, with a second camera on the vehicle and driver.", "yard gates and truck entrances"],
                ["panoramic", "A G6 180 covers a staging area or an open floor from one mounting point, which matters when every camera means a lift and a long cable run.", "staging areas and open floors"],
                ["vandal", "Cameras at the staff door and in the lot that people can reach get IK10 metal housings.", "staff entrances, lots and exposed corners"],
                ["turret", "Down the racking aisles a turret gives a long, narrow view and clean infrared without a dome cover collecting dust.", "aisles and racking"],
            ],
        },
        "focus": {
            "id": "layout",
            "h2": "Where the Cameras Go in a Warehouse",
            "photo": ph("cam-type-lpr"),
            "text": ["The layout we start from:"],
            "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Gate or yard entrance", "AI LPR + G6 Pro Bullet", "The plate on every vehicle in and out, and the vehicle itself."],
                ["Dock doors", "G6 Pro Bullet", "Trucks, pallets and people at each door, inside and out."],
                ["Aisles and racking", "G6 Turret", "Long, narrow views down the aisle."],
                ["Open floor and staging", "G6 180", "A wide floor area from one mounting point."],
                ["Yard and perimeter", "G6 PTZ", "Following a person or vehicle across open ground at night."],
                ["Offices and entrances", "G6 Dome", "Faces at the staff and visitor doors."],
            ]},
            "after": [
                "A missing pallet is often noticed weeks later, so warehouses need longer retention than an office: a UNVR Pro or UNVR G2 Pro with large drives, recording continuously at the dock and gate and on detection elsewhere, on a battery backup. Cameras beyond about 300 ft of copper get their own switch or a fiber run. See also [office and business security camera systems in Sarasota](sa-sarasota-business-security).",
            ],
        },
        "call": "to plan cameras for a warehouse or yard",
        "final": {
            "h2": "Request a Free Warehouse Camera Estimate in Sarasota",
            "text": "Tell us about the site: dock doors, the yard, the gate and how long you need to keep footage. We call back to book a walk.",
        },
    },
    "faq": [
        {"q": "What does a warehouse camera system cost?", "a": "Warehouses usually start with Business Pro: 12 or more cameras, a plate camera at the gate and a UNVR G2 Pro recorder, from $12,900 plus tax. The fixed price follows a free walk of the site."},
        {"q": "How far can a warehouse camera see at night?", "a": "It depends on the model. The G6 Turret's infrared reaches about 98 ft and the G6 Pro Bullet's further; large yards are covered with a PTZ or extra lighting."},
        {"q": "Can the system read licence plates at our gate?", "a": "Yes, with the UniFi AI LPR camera, mounted where vehicles slow down and at a low angle to the plate."},
        {"q": "How long should a warehouse keep footage?", "a": "Longer than an office, because losses are found later. We size the recorder for the number of days you choose."},
        {"q": "Do the cameras need Wi-Fi in the warehouse?", "a": "No. Every camera is wired PoE back to a switch, which is more reliable than Wi-Fi across racking and metal walls."},
        {"q": "Is there a monthly fee?", "a": "No. Footage and plate data stay on your recorder, with no subscription and no per-camera fee."},
    ],
}

HOA = {
    "city": "sarasota",
    "service": "hoa-security-cameras",
    "camera": "pro",
    "h1": "HOA and Condo Security Cameras in Sarasota, FL",
    "title": "HOA & Condo Security Cameras Sarasota FL | UniFi | LUMA",
    "description": "Security cameras for Sarasota HOAs and condo associations: gates, pools, mail rooms, garages and clubhouses. UniFi Protect with on-site recording, no fees.",
    "lede": "A community association needs cameras where residents share space: the gate, the pool, the mail room, the garage and the clubhouse. It also needs a system the board can explain to residents, with clear rules on who sees the footage. We install UniFi Protect HOA and condo security camera systems in Sarasota, Lakewood Ranch and Manatee County.",
    "paragraphs": [
        "The questions boards ask us are mostly about policy, not hardware: which areas can be recorded, who on the board or the management company gets access, how long footage is kept, and how a resident asks for a clip after a car is scratched in the garage. We set the system up so those answers are simple. " + PARTNER,
    ],
    "packages_h2": "Camera packages for associations",
    "faq_h2": "HOA and condo cameras: common questions",
    "cam": {
        "eyebrow": "Community Video Surveillance",
        "hero_photos": [ph("cam-type-lpr"), ph("cam-type-vandal"), ph("cam-scen-marina")],
        "hero_bg": ph("cam-hero-wide-a"),
        "tabs": seg_tabs("Policy & layout"),
        "plan": {"h2": "Start a free camera plan for your association",
                 "lede": "Two short steps. A board member or the manager can walk the common areas with us."},
        "types": {
            "h2": "Cameras We Install for Sarasota Associations",
            "lede": "Five UniFi camera types cover the gates and shared spaces of most communities and condo buildings.",
            "items": [
                ["lpr", "At each gate the AI LPR records every plate in and out, day and night, and footage can be searched by plate. Plate data stays on the association's recorder.", "entry and exit gates"],
                ["vandal", "Lobbies, elevator landings and garages get IK10 metal-housed domes that keep recording after a knock.", "lobbies, elevators and parking garages"],
                ["bullet", "A G6 Pro Bullet beside the plate camera records the vehicle and driver; others cover the pool deck and the pool gate.", "gate overviews and pool areas"],
                ["dome", "In the mail and package room a ceiling dome shows faces at the door and who takes which package.", "mail rooms and package lockers"],
                ["panoramic", "A G6 180 on a clubhouse wall or above a parking lot covers a wide shared space from one point.", "clubhouses, fitness rooms and lots"],
            ],
        },
        "focus": {
            "id": "layout",
            "h2": "Policy First, Then Cameras",
            "photo": ph("cam-hero-dome"),
            "text": [
                "Cameras belong in common areas only, never pointed into a unit, a balcony or a window. Association cameras run with audio off, because Florida requires everyone's consent to record a conversation, and signs at the entrances say the common areas are recorded.",
                "Before we install, the board decides who can view live video, who can export clips, and how many days are kept. UniFi Protect gives each person their own login with only the cameras and history the board allows, and keeps footage on a recorder in the building. Your association's attorney should approve the written policy; we make sure the system matches it.",
            ],
            "table": {"head": ["Position", "Camera", "What it should capture"], "rows": [
                ["Entry and exit gates", "AI LPR + G6 Pro Bullet", "Plates of every vehicle and the vehicle itself, day and night."],
                ["Pool and pool gate", "G6 Pro Bullet", "The deck and the gate, for incidents and after-hours use."],
                ["Mail and package room", "G6 Dome", "Faces at the door and who takes which package."],
                ["Lobby and elevators", "Vandal-resistant dome", "Entrances and the elevator lobby."],
                ["Parking garage", "G6 Turret", "Drive aisles and stairwell doors, infrared for low light."],
            ]},
            "after": [
                "On Siesta Key, Longboat Key and the bayfront, cameras go under overhangs where possible, every connection is sealed, and the recorder sits in a conditioned room on a battery backup. The camera range is covered on [business security camera systems in Sarasota](sa-sarasota-business-security); for a private home, see [security camera installation in Sarasota](sa-sarasota-security).",
            ],
        },
        "call": "to plan cameras for your community",
        "final": {
            "h2": "Request a Free HOA Camera Estimate in Sarasota",
            "text": "Tell us about the community: the gates, the pool, the mail room, the garage. We call back to book a walk with a board member or the manager.",
        },
    },
    "faq": [
        {"q": "What does an HOA camera system cost?", "a": "A gate with a plate camera plus the pool, mail room and garage usually means Business Pro, from $12,900 plus tax. Smaller buildings can start from Office 8, from $5,900 plus tax. The board gets a fixed price after a free walk."},
        {"q": "Can an HOA put security cameras in common areas in Florida?", "a": "Common areas such as gates, pools and mail rooms are usually recorded with the board's approval and posted signs. Your association's attorney should approve the written camera policy."},
        {"q": "Can HOA cameras record audio?", "a": "We install them with audio off. Florida requires everyone's consent to record a conversation."},
        {"q": "Who can see the footage?", "a": "Only the people the board names. Each gets a UniFi Protect login limited to the cameras and history they are allowed."},
        {"q": "Is there a monthly fee for the association?", "a": "No per-camera fee. Footage records to a recorder in the building."},
        {"q": "Where is the licence plate data stored?", "a": "On the association's own recorder in the building. There is no cloud plate database and no yearly per-camera fee, and plates are not shared with anyone unless the board exports a clip."},
    ],
}

CAMERA_ROWS = {
    f"{r['city']}/{r['service']}": r
    for r in (SARASOTA_SECURITY, SARASOTA_BUSINESS, BRADENTON_BUSINESS, RETAIL, RESTAURANT, WAREHOUSE, HOA)
}
