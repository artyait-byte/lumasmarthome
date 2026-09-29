const {useState, useEffect, useRef} = React;

/* ─── PATH ROUTING (crawlable URLs, not ?p=) ─── */
const ROUTE_KEYS = new Set(['home','shading','theaters','automation','audio','security','networking','lighting','permanent-lighting','designers','contact','budget-calculator','work','about','support','case-modern','case-bighouse','case-spacious','case-urban','case-family','smart-home-demo']);

function knownPages(){
  const keys = new Set(ROUTE_KEYS);
  try {
    Object.keys((window.LUMA_SEO && window.LUMA_SEO.routes) || {}).forEach(k=>keys.add(k));
  } catch(e) {}
  return keys;
}
function isKnownPage(id){
  return !!id && knownPages().has(id);
}
function geoData(){
  return window.LUMA_GEO || {cities:{}, services:{}, cityServices:{}, articles:{}, articleOrder:[], nap:{}, hub:{}, journalHub:{}, brand:{}};
}
function napInfo(){
  const nap = geoData().nap || {};
  const telephoneDisplay = nap.telephoneDisplay || '+1 (941) 217-1616';
  const email = nap.email || 'hello@lumasmarthome.com';
  const hours = nap.hours || 'Mon–Sat · 9am – 6pm';
  const area = nap.area || 'Sarasota & Manatee Counties';
  const telHref = nap.telHref || ('tel:' + String(nap.telephone || '+19412171616').replace(/[^\d+]/g, ''));
  const mailHref = 'mailto:' + email;
  const mapsUrl = nap.mapsUrl || 'https://www.google.com/maps/search/?api=1&query=LUMA+Smart+Home+Sarasota+FL';
  const mapsLabel = nap.mapsLabel || 'Find us on Google Maps';
  return Object.assign({}, nap, {telephoneDisplay, email, hours, area, telHref, mailHref, mapsUrl, mapsLabel});
}
function cityPageId(city){ return 'sa-'+city; }
function cityServicePageId(city, service){ return 'sa-'+city+'-'+service; }
function hasCityService(city, service){
  const g = geoData();
  return !!(g.cityServices && g.cityServices[city+'/'+service]);
}
function servicePageForCity(city, service){
  return hasCityService(city, service) ? cityServicePageId(city, service) : service;
}

function pathFor(page){
  const seo = window.LUMA_SEO;
  if (seo && seo.routes && seo.routes[page] && seo.routes[page].path) return seo.routes[page].path;
  if (page === 'home') return '/';
  return '/' + page;
}

function normalizePath(p){
  if (!p) return '/';
  p = String(p).split('?')[0].split('#')[0];
  p = p.replace(/\/index\.html$/, '/');
  p = p.replace(/\.html$/, '');
  p = p.replace(/\/+$/, '') || '/';
  return p;
}

function applySeo(page){
  const route = window.LUMA_SEO && window.LUMA_SEO.routes && window.LUMA_SEO.routes[page];
  if (!route) return;
  if (route.title) document.title = route.title;
  const desc = document.querySelector('meta[name="description"]');
  if (desc && route.description) desc.setAttribute('content', route.description);
  const canon = document.querySelector('link[rel="canonical"]');
  if (canon && window.LUMA_SEO.siteUrl) canon.setAttribute('href', window.LUMA_SEO.siteUrl + route.path);
  const ogUrl = document.querySelector('meta[property="og:url"]');
  if (ogUrl && window.LUMA_SEO.siteUrl) ogUrl.setAttribute('content', window.LUMA_SEO.siteUrl + route.path);
  const ogTitle = document.querySelector('meta[property="og:title"]');
  if (ogTitle && route.title) ogTitle.setAttribute('content', route.title);
}

function spaClick(e, page, navigate, extra){
  if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
  e.preventDefault();
  if (extra) extra();
  navigate(page);
}

function NavLink({page, className, children, navigate, style, onNavigate, ...rest}){
  return (
    <a href={pathFor(page)} className={className} style={style}
      onClick={e=>spaClick(e, page, navigate, onNavigate)} {...rest}>
      {children}
    </a>
  );
}

const MD_LINK = /\[([^\]]+)\]\(([^)]+)\)/g;
function LinkedText({text, navigate}){
  if (!text) return null;
  const parts = [];
  let last = 0;
  let m;
  const re = new RegExp(MD_LINK.source, 'g');
  let i = 0;
  while ((m = re.exec(text))) {
    if (m.index > last) parts.push(text.slice(last, m.index));
    parts.push(<NavLink key={'l'+i++} page={m[2]} navigate={navigate} className="inline-link">{m[1]}</NavLink>);
    last = m.index + m[0].length;
  }
  if (last < text.length) parts.push(text.slice(last));
  return parts;
}

function RelatedLinks({page, navigate}){
  const items = (geoData().related && geoData().related[page]) || [];
  if (!items.length) return null;
  return (
    <section className="related-links" aria-label="Related pages">
      <div className="related-links-inner">
        <div className="sec-label" style={{textAlign:'left'}}>Keep reading</div>
        <div className="geo-chip-row">
          {items.map(it=>(
            <NavLink key={it.id} page={it.id} navigate={navigate} className="geo-chip">{it.label}</NavLink>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ─── PHOTO URLS ─── */
// Local assets: /assets/photos/ — bump ?v= when you replace files (cache bust).
const lu = (path) => path + '?v=17';
const PHOTOS = {
  lighting:    lu('/assets/photos/interior-dining-warm.jpg'),
  window:      lu('/assets/photos/hero-shading.jpg'),
  theater:     lu('/assets/photos/hero-theater.jpg'),
  security:    lu('/assets/photos/hero-security-v2.jpg'),
  audio:       lu('/assets/photos/hero-audio-hifi.jpg'),
  networking:  lu('/assets/photos/hero-networking.jpg'),
  automation:  lu('/assets/photos/hero-automation.jpg'),

  heroHome:        lu('/assets/photos/sarasota-bay-house.jpg'),
  permanentHero:   lu('/assets/photos/permanent-warm.jpg'),
  permanentHoliday:lu('/assets/photos/permanent-holiday.jpg'),
  permDay:         lu('/assets/photos/permanent-day.jpg'),
  permWarm:        lu('/assets/photos/permanent-warm.jpg'),
  permGameday:     lu('/assets/photos/permanent-gameday.jpg'),
  permSecurity:    lu('/assets/photos/permanent-security.jpg'),
  permEaveDay:     lu('/assets/photos/permanent-eave-day.jpg'),
  permEaveNight:   lu('/assets/photos/permanent-eave-night.jpg'),
  tradeFlatlay:    lu('/assets/photos/trade-flatlay.jpg'),
  workBayfront:    lu('/assets/photos/work-bayfront.jpg'),
  workFamily:      lu('/assets/photos/work-family.jpg'),
  workRebuild:     lu('/assets/photos/work-rebuild.jpg'),
  heroSplash:      lu('/assets/photos/sarasota-downtown-bayfront.jpg'),
  heroAbout:       lu('/assets/photos/sarasota-marina.jpg'),
  heroShading:     lu('/assets/photos/hero-shading.jpg'),
  heroLighting:    lu('/assets/photos/lighting-lutron-hero.jpg'),
  lightingKetra:   lu('/assets/photos/lighting-scene.jpg'),
  lightingRania:   lu('/assets/photos/interior-recessed-warm.jpg'),
  handPhone:       lu('/assets/photos/hand-phone.jpg'),
  handPanel:       lu('/assets/photos/hand-panel.jpg'),
  handTheater:     lu('/assets/photos/hand-theater.jpg'),
  lightingDay:     lu('/assets/photos/lighting-day.jpg'),
  shadeFascia:     lu('/assets/photos/shade-fascia.jpg'),
  lightingLumaris: lu('/assets/photos/interior-living-fl.jpg'),
  heroDesigners:   lu('/assets/photos/hero-designers-new.jpg'),
  lumaVan:         lu('/assets/photos/luma-van.jpg'),
  theaterCinema:   lu('/assets/photos/theater-cinema.jpg'),
  theaterLiving:   lu('/assets/photos/theater-living.jpg'),
  theaterMedia:    lu('/assets/photos/theater-media.jpg'),

  moment1: lu('/assets/photos/shade-open.jpg'),
  moment2: lu('/assets/photos/shade-closed.jpg'),
  moment3: lu('/assets/photos/gulf-sunset.jpg'),
  moment4: lu('/assets/photos/scene-night.jpg'),

  theaterAnamorphic:    lu('/assets/photos/hero-theater.jpg'),
  theaterRoom:          lu('/assets/photos/hero-theater.jpg'),
  projectBayfront:      lu('/assets/photos/waterfront-lanai.jpg'),
  projectWarmInterior:  lu('/assets/photos/lighting-scene.jpg'),
  projectArchitectural: lu('/assets/photos/designers-chandelier.jpg'),
  gulfSunset:           lu('/assets/photos/gulf-sunset.jpg'),

  automationHero:     lu('/assets/photos/hero-automation.jpg'),
  automationKeypad:   lu('/assets/photos/lighting-lutron-hero.jpg'),
  projectAutomation1: lu('/assets/photos/networking-rack.jpg'),
  projectAutomation2: lu('/assets/photos/waterfront-lanai.jpg'),
  projectAutomation3: lu('/assets/photos/scene-midday.jpg'),

  audioHero:      lu('/assets/photos/hero-audio-hifi.jpg'),
  audioInvisible: lu('/assets/photos/audio-system.jpg'),
  securityHero:   lu('/assets/photos/hero-security-v2.jpg'),
  securityFootage:lu('/assets/photos/cam-nvr.jpg'),

  installDome:      lu('/assets/photos/cam-dome.jpg'),
  installDoorbell:  lu('/assets/photos/cam-doorbell.jpg'),
  installNvr:       lu('/assets/photos/cam-nvr.jpg'),
  installPanel:     lu('/assets/photos/cam-panel.jpg'),
  installDock:      lu('/assets/photos/cam-dock.jpg'),
  installPhone:     lu('/assets/photos/cam-phone.jpg'),
  installBullet:    lu('/assets/photos/cam-bullet.jpg'),
  installTablet:    lu('/assets/photos/wall-tablet.jpg'),
  networkingHero:   lu('/assets/photos/hero-networking.jpg'),
  networkingRack:   lu('/assets/photos/networking-rack.jpg'),
  netAP:            lu('/assets/photos/net-wifi-ap.jpg'),
  netSwitch:        lu('/assets/photos/net-switch.jpg'),
  netPatch:         lu('/assets/photos/net-patch.jpg'),
  netRack:          lu('/assets/photos/net-tech.jpg'),
  projectModernVilla: lu('/assets/photos/waterfront-lanai.jpg'),
  projectLuxuryPool:  lu('/assets/photos/gulf-sunset.jpg'),
  heroWork:           lu('/assets/photos/sarasota-sunset.jpg'),
  projMrExterior:     lu('/assets/photos/proj-mr-exterior.jpg'),
  projBmExterior:     lu('/assets/photos/proj-bm-exterior.jpg'),
  projBmTv:           lu('/assets/photos/proj-bm-tv.jpg'),
  projBmLiving:       lu('/assets/photos/proj-bm-living.jpg'),
  projBmRack:         lu('/assets/photos/proj-bm-rack.jpg'),
  projBmPatio:        lu('/assets/photos/proj-bm-patio.jpg'),
  projBmGameroom:     lu('/assets/photos/proj-bm-gameroom.jpg'),
  projBmKef:          lu('/assets/photos/proj-bm-kef.jpg'),
  projBmControl:      lu('/assets/photos/proj-bm-control.jpg'),
  projMrTv:           lu('/assets/photos/proj-mr-tv-fireplace.jpg'),
  projMrLiving:       lu('/assets/photos/proj-mr-living-view.jpg'),
  projMrAvRoom:       lu('/assets/photos/proj-mr-av-room.jpg'),
  projMrPatio:        lu('/assets/photos/proj-mr-patio.jpg'),
  projectLido:        lu('/assets/photos/sarasota-lido-day.jpg'),
  projectBridge:      lu('/assets/photos/sarasota-ringling-bridge.jpg'),
  projectIsland:      lu('/assets/photos/sarasota-turtle-aerial.jpg'),
  projectRetreat:     lu('/assets/photos/exterior-landscape-lighting.jpg'),

  'lit-cove':         lu('/assets/photos/fl-golden-hour.jpg'),
  'lit-keypad':       lu('/assets/photos/lighting-lutron-hero.jpg'),
  'lit-landscape-fl': lu('/assets/photos/exterior-landscape-lighting.jpg'),
  'lit-pendants':     lu('/assets/photos/designers-chandelier.jpg'),
  'lit-app':          lu('/assets/photos/scene-midday.jpg'),
  'lit-lanai-fl':     lu('/assets/photos/waterfront-lanai.jpg'),
  lightingDining:     lu('/assets/photos/interior-dining-warm.jpg'),
  heroModernHome:     lu('/assets/photos/hero-modern-home.jpg'),

  /* ── Case study: Spacious Modern (Sonos · WattBox · UniFi) ── */
  caseSpHero:         lu('/assets/photos/cases/spacious-modern/web-hero.jpg'),
  caseSpVan:          lu('/assets/photos/cases/spacious-modern/web-van.jpg'),
  caseSpCeiling:      lu('/assets/photos/cases/spacious-modern/web-ceiling-speakers.jpg'),
  caseSpSceneA:       lu('/assets/photos/cases/spacious-modern/web-scene-a.jpg'),
  caseSpSceneB:       lu('/assets/photos/cases/spacious-modern/web-scene-b.jpg'),

  /* ── Case study: Urban Home (B&W · UniFi · 7.1.2) ── */
  caseUrHero:         lu('/assets/photos/cases/urban-home/web-hero.jpg'),
  caseUrPool:         lu('/assets/photos/cases/urban-home/web-pool-audio.jpg'),
  caseUrRack:         lu('/assets/photos/cases/urban-home/web-rack.jpg'),
  caseUrSpeakerDetail:lu('/assets/photos/cases/urban-home/web-speaker-detail.jpg'),
  caseUrInWall:       lu('/assets/photos/cases/urban-home/web-in-wall-speaker.jpg'),

  /* ── Case study: Huge Family House (architectural lighting) ── */
  caseHfHero:         lu('/assets/photos/cases/huge-family/web-hero.jpg'),
  caseHfGreatRoom:    lu('/assets/photos/cases/huge-family/web-great-room.jpg'),
  caseHfLedCove:      lu('/assets/photos/cases/huge-family/web-led-cove.jpg'),
  caseHfLedDetail:    lu('/assets/photos/cases/huge-family/web-led-detail.jpg'),
  caseHfShower:       lu('/assets/photos/cases/huge-family/web-shower-niche.jpg'),
};

/* ─── ICON PATHS ─── */
const serviceIcons = {
  lighting: <g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><circle cx="15" cy="13" r="5"/><path d="M12.5 18.5h5M13 20.5h4"/><line x1="15" y1="6.5" x2="15" y2="5.5"/><line x1="19.5" y1="8.5" x2="20.3" y2="7.7"/><line x1="21" y1="13" x2="22" y2="13"/><line x1="10.5" y1="8.5" x2="9.7" y2="7.7"/><line x1="9" y1="13" x2="8" y2="13"/></g>,
  window:   <g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><rect x="8" y="7" width="14" height="17" rx="1"/><line x1="8" y1="11.5" x2="22" y2="11.5"/><line x1="8" y1="15.5" x2="22" y2="15.5"/><line x1="8" y1="19.5" x2="22" y2="19.5"/><line x1="15" y1="23" x2="15" y2="25"/><circle cx="15" cy="25.5" r="1" fill="white" stroke="none"/></g>,
  theater:  <g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><rect x="5" y="7" width="20" height="13" rx="1.5"/><polygon points="12.5,10.5 12.5,16.5 19.5,13.5" fill="rgba(255,255,255,.8)" stroke="none"/><line x1="9" y1="22" x2="21" y2="22"/><line x1="14" y1="20" x2="16" y2="22"/></g>,
  security: <g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><path d="M15 4.5L7 8v6c0 4.8 3.5 8.5 8 10 4.5-1.5 8-5.2 8-10V8L15 4.5z"/><path d="M11.5 13.5l2.5 2.5 4.5-5"/></g>,
  audio:    <g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><path d="M9 11.5h3l3.5-4.5v16.5L12 19H9V11.5z"/><path d="M18 11a5 5 0 010 8"/><path d="M20 8.5a8.5 8.5 0 010 13"/></g>,
  networking:<g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><path d="M5.5 11A12.8 12.8 0 0124.5 11" strokeOpacity=".4"/><path d="M8 14a10 10 0 0114 0" strokeOpacity=".65"/><path d="M10.5 17a6.5 6.5 0 019 0" strokeOpacity=".88"/><circle cx="15" cy="21" r="1.8" fill="white" stroke="none"/></g>,
  permanent:<g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><path d="M4 10h22"/><circle cx="8" cy="14" r="1.6" fill="white" stroke="none"/><circle cx="15" cy="14" r="1.6" fill="white" stroke="none"/><circle cx="22" cy="14" r="1.6" fill="white" stroke="none"/><path d="M8 17v4M15 17v6M22 17v4" strokeOpacity=".6"/></g>,
  automation:<g fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><polyline points="5,15 15,6 25,15"/><path d="M8.5 14.5v8.5h5.5v-5h2v5h5.5v-8.5"/><circle cx="22" cy="9" r="3" fill="rgba(197,114,56,.9)" stroke="white" strokeWidth="1.1"/><line x1="22" y1="7.4" x2="22" y2="10.6" strokeWidth=".9"/><line x1="20.4" y1="9" x2="23.6" y2="9" strokeWidth=".9"/></g>,
};

function HexIcon({type='lighting', size=30, color='#C57238'}) {
  return (
    <svg width={size} height={size} viewBox="0 0 30 30">
      <polygon points="15,0 27.99,7.5 27.99,22.5 15,30 2.01,22.5 2.01,7.5" fill={color}/>
      {serviceIcons[type]||serviceIcons.automation}
    </svg>
  );
}

/* ─── SERVICES DATA ─── */
const services = [
  {id:'lighting',   name:'Lighting Control',          sub:'Lutron · Ketra · scenes in every room', page:'lighting'},
  {id:'window',     name:'Window Treatments',          sub:'Motorized shades & drapery',           page:'shading'},
  {id:'theater',    name:'Home Theaters',              sub:'Calibrated rooms · cinema seating',    page:'theaters'},
  {id:'security',   name:'Security & Surveillance',    sub:'On-prem cameras · no monthly fees',    page:'security'},
  {id:'audio',      name:'Audio & Video',              sub:'Whole-home audio · indoor + lanai',    page:'audio'},
  {id:'networking', name:'Networking',                  sub:'Wi-Fi 6 / 7 · enterprise-grade',       page:'networking'},
  {id:'automation', name:'Home Automation',             sub:'Daily routines · one tap',             page:'automation'},
  {id:'permanent',  name:'Permanent Outdoor Lighting',  sub:'Roofline LEDs · warm white to holiday',  page:'permanent-lighting'},
];

/* ─── MEGA DROPDOWN ─── */
function MegaDropdown({active, hoverId, setHoverId, navigate}) {
  const left  = services.slice(0,4);
  const right = services.slice(4,7);
  const hovered = services.find(s=>s.id===hoverId)||services[0];
  return (
    <div className={`dropdown-wrap${active?' open':''}`}>
      <div className="dropdown-inner">
        <div className="dropdown-col">
          {left.map(s=>(
            <NavLink key={s.id} page={s.page} navigate={navigate}
              className={`dd-item${hoverId===s.id?' active':''}`}
              onMouseEnter={()=>setHoverId(s.id)}>
              <HexIcon type={s.id} size={30} color={hoverId===s.id?'#B5622A':'#C57238'}/>
              <div className="dd-text"><h4>{s.name}</h4><p>{s.sub}</p></div>
            </NavLink>
          ))}
        </div>
        <div className="dropdown-col">
          {right.map(s=>(
            <NavLink key={s.id} page={s.page} navigate={navigate}
              className={`dd-item${hoverId===s.id?' active':''}`}
              onMouseEnter={()=>setHoverId(s.id)}>
              <HexIcon type={s.id} size={30} color={hoverId===s.id?'#B5622A':'#C57238'}/>
              <div className="dd-text"><h4>{s.name}</h4><p>{s.sub}</p></div>
            </NavLink>
          ))}
        </div>
        <div className="dropdown-col">
          <div className="dd-preview">
            <img loading="lazy" decoding="async" src={PHOTOS[hovered.id]} alt={hovered.name}/>
            <div className="dd-preview-overlay">
              <div className="dd-preview-tag">Live Preview</div>
              <div className="dd-preview-name">{hovered.name}</div>
            </div>
          </div>
        </div>
        <div className="dd-foot">
          <NavLink page="service-areas" navigate={navigate} className="dd-foot-link">Service areas by city →</NavLink>
          <NavLink page="journal" navigate={navigate} className="dd-foot-link">Journal →</NavLink>
          <NavLink page="smart-home-demo" navigate={navigate} className="dd-foot-link">Interactive 3D demo →</NavLink>
        </div>
      </div>
    </div>
  );
}

/* ─── NAV ─── */
function Nav({navigate}) {
  /* The reference's header: transparent over a dark hero with white type,
     solid once you scroll or on a page with no hero; plain 18px links, one
     dropdown, two pills on the right. The mobile panel is a flat list with
     a single accordion for Solutions, the phone, and the same two pills. */
  const [ddOpen, setDdOpen] = useState(false);
  const [hoverId, setHoverId] = useState('lighting');
  const [mobOpen, setMobOpen] = useState(false);
  const [solOpen, setSolOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const navRef = useRef(null);
  useEffect(()=>{
    const h = e=>{if(navRef.current&&!navRef.current.contains(e.target))setDdOpen(false);};
    document.addEventListener('mousedown',h);
    const f = ()=>{ setScrolled(window.scrollY>40); setDdOpen(false); };
    const k = e=>{ if (e.key==='Escape') setDdOpen(false); };
    window.addEventListener('scroll',f,{passive:true}); document.addEventListener('keydown',k);
    setScrolled(window.scrollY>40);
    return()=>{document.removeEventListener('mousedown',h);window.removeEventListener('scroll',f);document.removeEventListener('keydown',k);};
  },[]);
  /* hover opens and closes the menu on a mouse; a tap still toggles it */
  const hoverable = ()=> window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const closeTimer = useRef(null);
  const openDd  = ()=>{ if (!hoverable()) return; clearTimeout(closeTimer.current); setDdOpen(true); };
  const closeDd = ()=>{ if (!hoverable()) return; clearTimeout(closeTimer.current); closeTimer.current = setTimeout(()=>setDdOpen(false), 140); };
  useEffect(()=>{
    document.body.style.overflow = mobOpen ? 'hidden' : '';
    return ()=>{ document.body.style.overflow=''; };
  },[mobOpen]);
  useEffect(()=>{
    try { const v = new URLSearchParams(window.location.search).get('menu'); if (v === '1' || v === 'open') setMobOpen(true); } catch(_) {}
  },[]);
  const nap = napInfo();
  const close = ()=>{setMobOpen(false);setSolOpen(false);};
  const LINKS = [
    {label:'Work', page:'work'},
    {label:'Service Areas', page:'service-areas'},
    {label:'Journal', page:'journal'},
    {label:'About', page:'about'},
  ];
  return (
    <div ref={navRef} className={`nav-shell${scrolled?' nav--solid':''}`} onMouseLeave={closeDd}>
      <nav className="nav">
        <NavLink page="home" navigate={navigate} className="nav-logo" aria-label="LUMA Smart Home home">
          <div className="logo-dot"/>
          <div className="logo-text">
            <span className="logo-luma">LUMA</span>
            <span className="logo-sub">Smart Home</span>
          </div>
        </NavLink>
        <div className="nav-links">
          <button type="button" className={`nav-link nav-link--dd${ddOpen?' open':''}`} onClick={()=>setDdOpen(v=>!v)} onMouseEnter={openDd} aria-expanded={ddOpen} aria-haspopup="true">
            Solutions
            <svg className={`chevron${ddOpen?' open':''}`} width="12" height="8" viewBox="0 0 12 8" fill="none"><path d="M1 1l5 5 5-5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/></svg>
          </button>
          {LINKS.map(({label,page})=>(
            <NavLink key={page} page={page} navigate={navigate} className="nav-link" onMouseEnter={closeDd}>{label}</NavLink>
          ))}
        </div>
        <div className="nav-actions">
          <NavLink page="support" navigate={navigate} className="nav-pill nav-pill--ghost">Customer Support</NavLink>
          <NavLink page="contact" navigate={navigate} className="nav-pill nav-pill--solid">Contact</NavLink>
        </div>
        <button type="button" className={`nav-burger${mobOpen?' open':''}`} onClick={()=>setMobOpen(v=>!v)} aria-label="Toggle menu" aria-expanded={mobOpen}>
          <span/><span/><span/>
        </button>
      </nav>
      <div onMouseEnter={openDd}>
        <MegaDropdown active={ddOpen} hoverId={hoverId} setHoverId={setHoverId} navigate={p=>{navigate(p);setDdOpen(false)}}/>
      </div>

      {/* MOBILE PANEL */}
      <div className={`nav-mobile-panel${mobOpen?' open':''}`}>
        <div className="nav-mobile-head">
          <NavLink page="home" navigate={navigate} className="nav-logo" onNavigate={close} aria-label="LUMA Smart Home home">
            <div className="logo-dot"/>
            <div className="logo-text"><span className="logo-luma">LUMA</span><span className="logo-sub">Smart Home</span></div>
          </NavLink>
          <button className="nav-mobile-close" onClick={close} aria-label="Close menu">×</button>
        </div>
        <ul className="nav-mobile-list">
          <li>
            <button type="button" className={`nav-mobile-row${solOpen?' open':''}`} onClick={()=>setSolOpen(v=>!v)} aria-expanded={solOpen}>
              Solutions <svg width="10" height="16" viewBox="0 0 10 16" fill="none"><path d="M2 2l6 6-6 6" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"/></svg>
            </button>
            {solOpen && (
              <ul className="nav-mobile-sub">
                {services.map(s=>(<li key={s.id}><NavLink page={s.page} navigate={navigate} onNavigate={close}>{s.name}</NavLink></li>))}
                <li><NavLink page="smart-home-demo" navigate={navigate} onNavigate={close}>3D demo</NavLink></li>
              </ul>
            )}
          </li>
          {LINKS.map(({label,page})=>(<li key={page}><NavLink page={page} navigate={navigate} className="nav-mobile-row" onNavigate={close}>{label}</NavLink></li>))}
          <li><NavLink page="support" navigate={navigate} className="nav-mobile-row" onNavigate={close}>Support</NavLink></li>
          <li><NavLink page="designers" navigate={navigate} className="nav-mobile-row" onNavigate={close}>Designers &amp; builders</NavLink></li>
        </ul>
        <a className="nav-mobile-phone" href={nap.telHref}>
          <span className="nav-mobile-phone-ic" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></span>
          {nap.telephoneDisplay}
        </a>
        <div className="nav-mobile-cta">
          <NavLink page="support" navigate={navigate} className="nav-pill nav-pill--outline" onNavigate={close}>Customer Support</NavLink>
          <NavLink page="contact" navigate={navigate} className="nav-pill nav-pill--solid" onNavigate={close}>Contact</NavLink>
        </div>
      </div>
    </div>
  );
}

/* ─── BENTO IMAGE MAP (data-img keys) ─── */
/* ─── BENTO ICONS (16px white SVG) ─── */
/* ─── SERVICE PHOTO CARD ─── */
function ServiceCard({id, name, height=240}) {
  return (
    <div className="photo-card" style={{height}}>
      <img loading="lazy" decoding="async" src={PHOTOS[id]} alt={name} style={{width:'100%',height:'100%',objectFit:'cover',display:'block',transition:'transform .5s'}}/>
      <div className="photo-card-overlay">
        <div className="photo-card-icon"><HexIcon type={id} size={30}/></div>
        <div className="photo-card-title" dangerouslySetInnerHTML={{__html:name}}/>
        <div className="photo-card-explore">EXPLORE →</div>
      </div>
    </div>
  );
}

/* ─── HOME PAGE ─── */
/* ═══════════════════════════════════════════════════════════════════════════
   FX SECTION KIT
   The Fusion A+V home page, section for section, rebuilt in LUMA's palette
   and voice. Their structure is followed literally — a hero carrying nothing
   but its headline, an intro split 96px apart, two 500px solution cards whose
   titles sit on the foot, a twelve-column media row, three work cards under
   320px of headroom, a 60%-wide quote carousel, a colour panel at eight-and-
   four, and a closing invitation with no form in it.
   ═══════════════════════════════════════════════════════════════════════════ */


/* The five real projects, taken verbatim from their case pages. Nothing on
   the site may describe a project that is not in this list. */
const LUMA_CASES = {
  'case-urban':    {title:'Urban Home',        place:'Sarasota · Bird Key',  photo:PHOTOS.caseUrHero,
    scope:'Bowers & Wilkins · 7.1.2 Dolby Atmos · UniFi network',
    lede:'A waterfront urban residence built around music: Bowers & Wilkins from the media room to the pool deck, and a UniFi network that just works.'},
  'case-family':   {title:'Huge Family House', place:'Bonita Bay',           photo:PHOTOS.caseHfHero,
    scope:'Cove lighting · Lutron RadioRA 3 · landscape lighting',
    lede:'A 9,000+ sq ft residence where the lighting was designed to disappear into the architecture. Hidden cove LEDs, layered scenes, one keypad in every room.'},
  'case-spacious': {title:'Spacious Modern',   place:'Naples · Port Royal',  photo:PHOTOS.caseSpHero,
    scope:'Sonos whole-home audio · UniFi network · Sonance in-ceiling',
    lede:'A 7,400 sq ft modern home wired end-to-end for music, network and effortless ownership.'},
  'case-modern':   {title:'Modern Residence',  place:'Tampa Bay Area',       photo:PHOTOS.projMrExterior,
    scope:'Five AV zones · Denon · Martin Logan · Sonos Arc',
    lede:'Five independent AV zones in a single hillside home, unified under one control layer.'},
  'case-bighouse': {title:'Big Modern House',  place:'Texas Hill Country',   photo:PHOTOS.projBmExterior,
    scope:'URC · 16 audio / 6 video zones · 7.2.4 Atmos theater · perimeter cameras',
    lede:'16 audio zones, 6 video zones and a full Dolby Atmos theater, all running from a single URC processor.'},
};

const FX_SOLUTIONS = [
  {page:'work',      photo:PHOTOS.heroHome,      title:'For owners',  cta:'See finished houses'},
  {page:'designers', photo:PHOTOS.tradeFlatlay,  title:'Designers & builders', cta:'How we work with you'}
];

const FX_WORK = ['case-urban','case-family','case-spacious'];

/* Real client reviews only (e.g. copied from the Google Business Profile, with
   permission). The home-page carousel stays hidden until this has entries. */
const FX_QUOTES = [];

/* Reel tiles render at 259x270 and 319x388 — serve crops cut for that,
   not the full-size hero photos. Ten files, under half a megabyte total. */
const FX_REEL = [
  'sarasota-bay-house','lighting-scene','hero-theater','permanent-warm','hero-designers-new',
  'hero-shading','reel-bedroom','work-bayfront','work-family','hero-automation'
].map(n => lu('/assets/photos/reel/' + n + '.jpg'));

function FxCall() {
  const nap = napInfo();
  return (
    <a className="fx-call" href={nap.telHref}>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/>
      </svg>
      {nap.telephoneDisplay}
    </a>
  );
}

/* Their pairing at every conversion point: one filled pill, one phone number.
   No inline name/email/phone block anywhere on the site but /contact. */
function FxActions({navigate, label='Book a consultation', page='contact', align, tone, onNavigate}) {
  return (
    <div className={'fx-actions'+(align==='start'?' fx-actions--start':'')+(tone==='dark'?' fx-actions--onDark':'')}>
      <NavLink page={page} navigate={navigate} onNavigate={onNavigate} className="fx-btn">{label}</NavLink>
      <FxCall/>
    </div>
  );
}

/* ── 1. HERO — the headline and nothing else ──────────────────────────── */
function FxHero() {
  return (
    <section className="fx-hero" aria-label="LUMA Smart Home">
      {/* the still sits under the clip, so the hero is a photograph whenever the
          video is not playing: reduced-motion, blocked autoplay, slow network */}
      <div className="fx-hero-still" style={{backgroundImage:"url('/assets/video/hero-sarasota-poster.jpg')"}} aria-hidden="true"/>
      <video className="fx-hero-media" autoPlay muted loop playsInline preload="metadata"
             poster="/assets/video/hero-sarasota-poster.jpg" aria-hidden="true">
        <source src="/assets/video/hero-sarasota.webm" type="video/webm"/>
        <source src="/assets/video/hero-sarasota.mp4" type="video/mp4"/>
      </video>
      <div className="fx-hero-scrim" aria-hidden="true"/>
      <div className="fx-field">
        <div className="fx-hero-stage">
          <h1 className="fx-d1">A house that answers <em>to the light.</em></h1>
        </div>
      </div>
    </section>
  );
}

/* ── 2. INTRO ─────────────────────────────────────────────────────────── */
function FxIntro({navigate}) {
  return (
    <section className="fx-band">
      <div className="fx-field" style={{paddingTop:96}}>
        <div className="fx-intro">
          <div>
            <h2 className="fx-d2">We draw the systems before the drywall goes up.</h2>
          </div>
          <div className="fx-lede">
            <p>Lighting, shade, sound, cameras and the network are one drawing set, issued to your architect and your electrician before a single box is hung.</p>
            <p>We are based in Sarasota and work across Sarasota and Manatee Counties. Controls are matched to your switch plates, speakers are flush-trimmed and painted, and the rack lives where nobody has to look at it.</p>
            <p style={{marginTop:16}}>
              <NavLink page="about" navigate={navigate} className="fx-more">Learn more <i aria-hidden="true">→</i></NavLink>
            </p>
          </div>
        </div>
      </div>
      <div className="fx-reel" aria-hidden="true">
        <div className="fx-reel-track">
          {FX_REEL.concat(FX_REEL).map((src,i) => (
            <img key={i} src={src} alt="" decoding="async" loading={i < 6 ? 'eager' : 'lazy'}/>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ── 3. SOLUTIONS ─────────────────────────────────────────────────────── */
function FxSolutions({navigate}) {
  return (
    <section className="fx-band fx-py-xl">
      <div className="fx-wide">
        <div className="fx-heads">
          <h2 className="fx-d3">Two ways we work</h2>
          <p className="fx-lede">Directly with owners on their own house, or behind an architect, designer or builder on a project already in drawings.</p>
        </div>
        <div className="fx-cards2">
          {FX_SOLUTIONS.map(s => (
            <NavLink key={s.page} page={s.page} navigate={navigate} className="fx-card">
              <img src={s.photo} alt={s.title} loading="lazy" decoding="async"/>
              <div className="fx-card-veil" aria-hidden="true"/>
              <div className="fx-card-foot">
                <h3 className="fx-d3">{s.title}</h3>
                <span className="fx-more">{s.cta} <i aria-hidden="true">→</i></span>
              </div>
            </NavLink>
          ))}
        </div>
      </div>
    </section>
  );
}


/* ── SCENES — one room, four states. The part a photograph of a nice room
   cannot show: the house doing something. Same camera, same furniture, only
   the light and the shades move; each state lists what the system changed.
   Advances on its own until someone picks a state, then stays put. ── */
const FX_SCENES = [
  {id:'alba',  time:'07:00', name:'Alba',  img:lu('/assets/photos/scenes/scene-morning.jpg'),
   what:'East shades rise, the west side stays down to hold the cool. Lights stay off; the coffee station wakes.',
   moved:['3 shades up','3 shades held','Lights off','Coffee on']},
  {id:'day',   time:'14:30', name:'Day',   img:lu('/assets/photos/scenes/scene-day.jpg'),
   what:'Solar shades drop to 75% on the pool side. The glare goes, the view stays, the AC stops fighting the glass.',
   moved:['6 shades to 75%','Lights off','Cooling eased']},
  {id:'sera',  time:'19:30', name:'Sera',  img:lu('/assets/photos/scenes/scene-evening.jpg'),
   what:'Every shade lifts for the sunset. Pendants and cove come up to 30%, the lamp by the sofa, the lanai and the pool.',
   moved:['6 shades up','Pendants 30%','Cove 30%','Lanai + pool on']},
  {id:'notte', time:'22:45', name:'Notte', img:lu('/assets/photos/scenes/scene-night.jpg'),
   what:'Shades close, pendants and cove go dark, footlights along the hall hold at 5%. Doors lock and the cameras arm.',
   moved:['6 shades down','Footlights 5%','Doors locked','Cameras armed']},
];

function FxScenes({heading, lede, band}) {
  const [i, setI] = React.useState(2);
  const [held, setHeld] = React.useState(false);
  React.useEffect(()=>{
    if (held) return;
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) return;
    const t = setInterval(()=>setI(v => (v+1) % FX_SCENES.length), 5200);
    return ()=>clearInterval(t);
  },[held]);
  const pick = (k)=>{ setI(k); setHeld(true); };
  const s = FX_SCENES[i];
  return (
    <section className={band===false ? 'fx-band--plain fx-py-lg' : 'fx-band fx-py-lg'}>
      <div className="fx-wide">
        <div className="fx-heads" style={{marginBottom:40}}>
          <h2 className="fx-d3" dangerouslySetInnerHTML={{__html: heading || 'One room, <em>four states</em>'}}/>
          <p className="fx-lede">{lede || 'An example programme for a Gulf Coast great room. Same room, same camera: only the light and the shades change, and nobody touched a switch. Tap a time to see what the house does on its own.'}</p>
        </div>
        <div className="fx-scenes">
          <div className="fx-scenes-stage" role="img" aria-label={`${s.name} scene at ${s.time}`}>
            {FX_SCENES.map((x,k)=>(
              <img key={x.id} src={x.img} alt="" loading={k===2?'eager':'lazy'} decoding="async" className={k===i?'on':''}/>
            ))}
            <div className="fx-scenes-chip" aria-live="polite">
              <span className="fx-scenes-dot" aria-hidden="true"/>
              <strong>{s.name}</strong><span>{s.time}</span>
            </div>
          </div>
          <div className="fx-scenes-side">
            <div className="fx-scenes-tabs" role="tablist" aria-label="Scenes">
              {FX_SCENES.map((x,k)=>(
                <button key={x.id} role="tab" aria-selected={k===i} className={`fx-scenes-tab${k===i?' on':''}`} onClick={()=>pick(k)}>
                  <span className="fx-scenes-time">{x.time}</span>
                  <span className="fx-scenes-name">{x.name}</span>
                  {!held && k===i && <i className="fx-scenes-bar" aria-hidden="true"/>}
                </button>
              ))}
            </div>
            <p className="fx-scenes-what">{s.what}</p>
            <ul className="fx-scenes-moved" aria-label="What the system changed">
              {s.moved.map(m=><li key={m}>{m}</li>)}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ── 4. CARE — copy left, video right ─────────────────────────────────── */
function FxSupport({navigate}) {
  return (
    <section className="fx-py-md">
      <div className="fx-wide">
        <div className="fx-row">
          <div className="fx-row-copy">
            <h2 className="fx-d3">The year after the install</h2>
            <div className="fx-lede">
              <p>Our service team is based in Sarasota and works across Sarasota and Manatee Counties. As the systems evolve, we keep them current.</p>
              <p>Take a care plan or call us when something drifts. Either way firmware, network health, camera storage and scene tuning stay someone's job, and that someone is us.</p>
            </div>
            <FxActions navigate={navigate} align="start"/>
          </div>
          <div className="fx-row-media">
            <video autoPlay muted loop playsInline preload="metadata"
                   poster="/assets/video/luma-care-poster.jpg"
                   aria-label="A LUMA technician walking a homeowner through the control app">
              <source src="/assets/video/luma-care.webm" type="video/webm"/>
              <source src="/assets/video/luma-care.mp4" type="video/mp4"/>
            </video>
          </div>
        </div>
      </div>
    </section>
  );
}


/* ── DISCIPLINES — the reference's card row: cream card, 16:9 photo on top,
   sans title, a 3px accent rule 100px wide, prose, "Learn more →". Seven
   cards, three in view, the rest a swipe away. ── */
const FX_DISCIPLINES = [
  {page:'lighting',   photo:PHOTOS.lightingKetra, title:'Lighting control',
   body:'Lutron and Ketra on every circuit, warm-dim tuned for evening, keypads matched to your plates.'},
  {page:'shading',    photo:PHOTOS.window,        title:'Motorized shades',
   body:'Three layers on the west glass, quiet drives, pockets drawn before the drywall goes up.'},
  {page:'security',   photo:PHOTOS.securityHero,  title:'Cameras & security',
   body:'Footage stored on the property, encrypted, no monthly fee and no cloud in the way.'},
  {page:'theaters',   photo:PHOTOS.theater,       title:'Home theaters',
   body:'Rooms designed for sound first, calibrated in place, with the gear out of sight.'},
  {page:'audio',      photo:PHOTOS.audio,         title:'Audio & video',
   body:'Speakers flush in the ceiling and out on the lanai, one source list across every zone.'},
  {page:'automation', photo:PHOTOS.handPanel,     title:'Home automation',
   body:'Morning, afternoon, evening, away. One press on a keypad and the house takes the state.'},
  {page:'networking', photo:PHOTOS.networkingRack,title:'Networking',
   body:'Wired wherever wire can land, Wi-Fi 6/7 where it cannot, and a rack somebody can read.'},
  {page:'permanent-lighting', photo:PHOTOS.permWarm, title:'Permanent outdoor lighting',
   body:'A colour-matched channel under the overhangs, invisible by day. A warm-white line every night; security, game day and December on a preset.'}
];

function FxDisciplines({navigate}) {
  const track = React.useRef(null);
  const step = (dir) => {
    const el = track.current; if (!el) return;
    const card = el.querySelector('.fx-panel-card');
    el.scrollBy({left: dir * (card ? card.offsetWidth + 16 : el.clientWidth / 3), behavior:'smooth'});
  };
  return (
    <section className="fx-band--plain fx-py-md">
      <div className="fx-wide">
        <div className="fx-heads" style={{maxWidth:768, marginBottom:48}}>
          <p className="fx-lede"><strong style={{color:'var(--dark)'}}>Seven disciplines, one drawing set.</strong><br/>
          Every layer of the house is designed together, so a keypad in the hall knows about the shades, the lights and the music behind it.</p>
        </div>
        <div className="fx-panels" ref={track}>
          {FX_DISCIPLINES.map(d => (
            <NavLink key={d.page} page={d.page} navigate={navigate} className="fx-panel-card">
              <span className="fx-panel-img"><img src={d.photo} alt={d.title} loading="lazy" decoding="async"/></span>
              <span className="fx-panel-body">
                <h3>{d.title}</h3>
                <i className="fx-panel-rule" aria-hidden="true"/>
                <p>{d.body}</p>
                <span className="fx-panel-more">Learn more <i aria-hidden="true">→</i></span>
              </span>
            </NavLink>
          ))}
        </div>
        <div className="fx-quotes-nav">
          <button className="fx-qbtn" onClick={()=>step(-1)} aria-label="Previous">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <button className="fx-qbtn" onClick={()=>step(1)} aria-label="Next">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M9 6l6 6-6 6"/></svg>
          </button>
        </div>
      </div>
    </section>
  );
}

/* ── 5. WORK ──────────────────────────────────────────────────────────── */
function FxWork({navigate}) {
  return (
    <section className="fx-band fx-py-lg">
      <div className="fx-wide">
        <div className="fx-heads" style={{marginBottom:0}}>
          <h2 className="fx-d3">Selected work</h2>
          <p className="fx-lede">Finished projects, each with its own case study: the brief, the systems and the equipment list.</p>
        </div>
        <div className="fx-work">
          {FX_WORK.map(id => { const c = LUMA_CASES[id]; return (
            <NavLink key={id} page={id} navigate={navigate} className="fx-work-card">
              <img src={c.photo} alt={c.title} loading="lazy" decoding="async"/>
              <div className="fx-work-meta"><span>{c.place}</span><span>{c.scope}</span></div>
              <h3>{c.title}</h3>
              <p>{c.lede}</p>
            </NavLink>
          );})}
        </div>
        <p style={{textAlign:'center',marginTop:32}}>
          <NavLink page="work" navigate={navigate} className="fx-more">All five projects <i aria-hidden="true">→</i></NavLink>
        </p>
      </div>
    </section>
  );
}

/* ── 6. QUOTES ────────────────────────────────────────────────────────── */
function FxQuotes() {
  const track = React.useRef(null);
  const step = (dir) => {
    const el = track.current; if (!el) return;
    const card = el.querySelector('.fx-quote');
    el.scrollBy({left: dir * (card ? card.offsetWidth : el.clientWidth * .6), behavior:'smooth'});
  };
  return (
    <section className="fx-band fx-py-lg">
      <div className="fx-wide">
        <div className="fx-heads">
          <h2 className="fx-d3">What owners say a year later</h2>
          <p className="fx-lede">The part you can only judge after the crew has gone home.</p>
        </div>
        <div className="fx-quotes-track" ref={track}>
          {FX_QUOTES.map((t,i) => (
            <div className="fx-quote" key={i}>
              <figure className="fx-quote-card">
                <div className="fx-stars" aria-label="Five out of five">
                  {[0,1,2,3,4].map(s => (
                    <svg key={s} width="20" height="20" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                      <path d="M10 1l2.5 6.5L19 8.5l-4.5 4.5L16 20l-6-3.5L4 20l1.5-7L1 8.5l6.5-1L10 1z"/>
                    </svg>
                  ))}
                </div>
                <blockquote>{t.q}</blockquote>
                <figcaption className="fx-quote-by">
                  <span className="fx-quote-av" aria-hidden="true">{t.n.split(' ').map(x=>x[0]).join('').slice(0,2)}</span>
                  <span>
                    <span className="fx-quote-name">{t.n}</span><br/>
                    <span className="fx-quote-where">{t.w}</span>
                  </span>
                </figcaption>
              </figure>
            </div>
          ))}
        </div>
        <div className="fx-quotes-nav">
          <button className="fx-qbtn" onClick={()=>step(-1)} aria-label="Previous testimonial">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <button className="fx-qbtn" onClick={()=>step(1)} aria-label="Next testimonial">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M9 6l6 6-6 6"/></svg>
          </button>
        </div>
      </div>
    </section>
  );
}

/* ── 7. REGION PANEL — the reference's "why homeowners choose" grid:
   photo in five columns, copy and a two-column icon list in seven. Here the
   list is the nine cities, so every city page keeps its link from home. ── */
function FxRegion({navigate}) {
  const nap = napInfo();
  const cities = geoData().cities || {};
  return (
    <section className="fx-values">
      <div className="fx-wide">
        <div className="fx-values-grid">
          <div className="fx-values-photo">
            <img src={PHOTOS.heroSplash} alt="Sarasota bayfront" loading="lazy" decoding="async"/>
          </div>
          <div className="fx-values-copy">
            <div>
              <h2 className="fx-d3">One studio, <em>five counties</em></h2>
              <div className="fx-lede">
                <p>We cover {nap.area} out of Sarasota. Same crew, same drawing set and same aftercare whether the house is on Siesta Key or forty minutes inland.</p>
              </div>
            </div>
            <div className="fx-values-list">
              {Object.keys(cities).map(id => {
                const c = cities[id];
                return (
                  <NavLink key={id} page={cityPageId(id)} navigate={navigate} className="fx-value">
                    <span className="fx-tile" aria-hidden="true">
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s7-7.5 7-12a7 7 0 1 0-14 0c0 4.5 7 12 7 12z"/><circle cx="12" cy="10" r="2.4"/></svg>
                    </span>
                    <span>
                      <strong>{c.name}</strong>
                      <small>{c.county}</small>
                      <p>{c.tagline}</p>
                    </span>
                  </NavLink>
                );
              })}
            </div>
            <p><NavLink page="service-areas" navigate={navigate} className="fx-more">All service areas <i aria-hidden="true">→</i></NavLink></p>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ── 7b. BRANDS — the reference's logo row. Each card shows the maker's
   own mark when /assets/brands/<slug>.svg is present and falls back to a
   typeset name until it is, so real logos drop in without a code change. ── */
const FX_BRANDS = [
  ['lutron','Lutron'], ['clare','Clare'], ['rti','RTI'], ['sonos','Sonos'], ['sonance','Sonance'],
  ['ubiquiti','Ubiquiti'], ['bowers-wilkins','Bowers & Wilkins'], ['kef','KEF'], ['urc','URC'], ['wattbox','WattBox']
];
/* Add a slug here once its SVG is in /assets/brands/ — the card then shows
   the mark instead of the typeset name, and nothing is requested before that. */
const FX_BRAND_LOGOS = new Set([]);
function FxBrandCard({slug, name}) {
  return (
    <div className="fx-brand" title={name}>
      {FX_BRAND_LOGOS.has(slug)
        ? <img src={'/assets/brands/'+slug+'.svg'} alt={name} loading="lazy"/>
        : <span className="fx-brand-name">{name}</span>}
    </div>
  );
}
function FxBrands() {
  return (
    <section className="fx-band--plain fx-py-md">
      <div className="fx-wide">
        <h2 className="fx-d3" style={{fontSize:36, marginBottom:32}}>What we install</h2>
        <div className="fx-brands">
          {FX_BRANDS.map(([slug,name]) => <FxBrandCard key={slug} slug={slug} name={name}/>)}
        </div>
      </div>
    </section>
  );
}

/* ── 7c. JOURNAL — four notes in the reference's card row, no photo ── */
function FxJournal({navigate}) {
  const g = geoData();
  const articles = g.articles || {};
  const order = (g.articleOrder || []).slice(0,4);
  return (
    <section className="fx-band fx-py-lg">
      <div className="fx-wide">
        <div className="fx-heads" style={{marginBottom:48}}>
          <h2 className="fx-d3">From the journal</h2>
          <p className="fx-lede">Notes for the searches that are not a trade name yet: smart home Sarasota, then Lutron, shades and cameras.</p>
        </div>
        <div className="fx-panels">
          {order.map(id => {
            const a = articles[id]; if (!a) return null;
            return (
              <NavLink key={id} page={id} navigate={navigate} className="fx-panel-card fx-panel-card--text">
                <span className="fx-panel-body">
                  <small>{a.category} · {fmtDate(a.date)}</small>
                  <h3>{a.h1}</h3>
                  <i className="fx-panel-rule" aria-hidden="true"/>
                  <p>{a.dek}</p>
                  <span className="fx-panel-more">Read the note <i aria-hidden="true">→</i></span>
                </span>
              </NavLink>
            );
          })}
        </div>
        <p style={{textAlign:'center', marginTop:32}}>
          <NavLink page="journal" navigate={navigate} className="fx-more">All notes <i aria-hidden="true">→</i></NavLink>
          <span style={{margin:'0 16px', color:'var(--cream3)'}}>·</span>
          <NavLink page="luma-smart-home-sarasota" navigate={navigate} className="fx-more">This LUMA, not the others <i aria-hidden="true">→</i></NavLink>
        </p>
      </div>
    </section>
  );
}

/* ── 8. CTA ───────────────────────────────────────────────────────────── */
function FxCta({navigate, title, body, label, onNavigate}) {
  return (
    <section className="fx-cta">
      <div className="fx-cta-inner">
        <h2 className="fx-d3" dangerouslySetInnerHTML={{__html: title || 'Tell us what the house should do'}}/>
        <div className="fx-lede">
          <p>{body || "New build, rebuild, or a system you inherited and have never liked. Send the plans or just describe the rooms, and we will come back with a scope and an honest range."}</p>
        </div>
        <FxActions navigate={navigate} onNavigate={onNavigate} label={label || 'Book a consultation'}/>
      </div>
    </section>
  );
}

function HomePage({navigate}) {
  return (
    <div className="page">
      <FxHero/>
      <FxIntro navigate={navigate}/>
      <FxSolutions navigate={navigate}/>
      <FxScenes/>
      <FxSupport navigate={navigate}/>

      <FxDisciplines navigate={navigate}/>

      <FxWork navigate={navigate}/>
      {FX_QUOTES.length > 0 && <FxQuotes/>}
      <FxRegion navigate={navigate}/>
      <FxBrands/>
      <FxJournal navigate={navigate}/>
      <FxCta navigate={navigate}/>
    </div>
  );
}

/* ─── SHADING PAGE ─── */
function ShadingPage({navigate}) {
  const I = (d) => <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d={d}/></svg>;
  return <ServicePageShell navigate={navigate}
    hero={{eyebrow:'Motorized shades', h1:'Three layers <em>of shade.</em>',
      lead:'A Gulf Coast home needs solar shades for heat and glare, blackout for sleep and privacy, and drapery for the room. We design all three as one system, on the drawings, before the pockets are framed.',
      image: PHOTOS.heroShading, primaryLabel:'Plan my shading →', primaryAction:()=>navigate('contact'),
      secondaryLabel:'See finished houses', secondaryAction:()=>navigate('work')}}
    intro={{lead:'The sun moves; the shades already know.',
      body:'Lutron Sivoia QS and Somfy drives, quiet enough for a bedroom, on a schedule built around the actual sun on your actual glass. West-facing solar shades drop before the afternoon heat, every shade lifts ten minutes before sunset so the view comes back, and blackout closes when the house goes to bed.'}}
    values={{h2:'Four moments <em>your shades already know</em>',
      lead:'Scenes built around the sun, not around a timer.',
      items:[
        {icon:I('M12 3v2M5.6 5.6l1.4 1.4M3 12h2M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z'), title:'07:10 · Open east', desc:'Morning-facing shades rise. West stays closed to hold the cool until the sun swings around.'},
        {icon:I('M12 3v18M3 12h18M12 8l4 4-4 4-4-4z'), title:'14:30 · Shield west', desc:'Solar shades drop on west-facing glass. AC load drops with them, and the finishes stay out of the UV.'},
        {icon:I('M3 17h18M6 17V9l6-5 6 5v8'), title:'19:40 · Open all', desc:'Ten minutes before sunset every shade lifts. The view comes back to the room for the best light of the day.'},
        {icon:I('M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z'), title:'22:45 · Close privacy', desc:'Blackout in the bedrooms, drapery across the living areas. Night mode, one press on the keypad by the bed.'},
      ]}}
    panels={{h2:'Three layers, <em>one pocket</em>',
      items:[
        {photo: PHOTOS.shadeFascia, title:'Solar shades', body:'Openness-weave fabric that tames glare and heat on the water side while keeping the view. The everyday layer on every gulf-facing pane.'},
        {photo: PHOTOS.moment1,     title:'Drapery', body:'Motorized tracks for the linen and sheers your designer chose, so the room still reads as a room and not as hardware.'},
        {photo: lu('/assets/photos/reel-bedroom.jpg'), title:'Blackout', body:'Side-channel blackout in bedrooms and the theater, quiet drives, and a keypad by the bed that closes the house for the night.'},
      ]}}
    ctaTitle='Ready to take the glare <em>out of the day?</em>'
    ctaBody='Tell us which windows fight you and when. We will come back with a shade plan, fabric, drive and pockets, and an honest range before anything is ordered.'
  />;
}
/* ─── LIGHTING PORTFOLIO ROW ─── */
const PORTFOLIO_ITEMS = [
  {
    img: 'lightingDining',
    eyebrow: 'Scene Design',
    headline: 'Every moment has its light.',
    desc: 'Morning coffee, focused work, candlelit dinner, movie night — we pre-program each scene to the exact colour temperature and intensity your life calls for. One keypad tap shifts the entire home.',
    cta: 'See How Scenes Work →',
    flip: false,
  },
  {
    img: 'lightingRania',
    eyebrow: 'Fixture Coordination',
    headline: 'Your spec, perfectly executed.',
    desc: 'We work downstream of your interior designer and lighting consultant. Visual Comfort chandeliers, RH pendants, custom cove in the millwork — every fixture is tuned to dim smoothly, hold colour across levels, and respond to the right scene.',
    cta: 'Talk to a Lighting Specialist →',
    flip: true,
  },
  {
    img: 'lightingLumaris',
    eyebrow: 'Unified Control',
    headline: 'One system. Every zone.',
    desc: 'Keypads, app, voice — all unified under a single control layer. We match keypad finishes to your hardware and wood tones, commission every zone on-site, and leave you with a system that any family member can use without a manual.',
    cta: 'Start Your Project →',
    flip: false,
  },
];

function PortfolioRow({item, navigate}) {
  return (
    <div className={`portfolio-row${item.flip ? ' portfolio-row--flip' : ''}`}>
      <div className="portfolio-row-img">
        <img loading="lazy" decoding="async" src={PHOTOS[item.img]} alt={item.headline}/>
      </div>
      <div className="portfolio-row-text">
        <span className="portfolio-row-eyebrow">{item.eyebrow}</span>
        <h3 className="portfolio-row-title">{item.headline}</h3>
        <p className="portfolio-row-body">{item.desc}</p>
        <button className="btn-solid" style={{alignSelf:'flex-start',marginTop:6,fontSize:15,padding:'13px 22px'}} onClick={()=>navigate('contact')}>{item.cta}</button>
      </div>
    </div>
  );
}

/* ─── LIGHTING MOSAIC ("What we install") ─── */
const MOSAIC_TILES = [
  {area:'a', img:'lit-cove',         eyebrow:'Architectural',  name:'Cove & soffit',           detail:'Hidden warm 2700K LED tape, dimmable to 0.1%',
    icon:(<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><path d="M2 5.5h12"/><path d="M3 8h10" strokeOpacity=".7"/><path d="M4 10.5h8" strokeOpacity=".45"/><path d="M5 13h6" strokeOpacity=".25"/></svg>)},
  {area:'b', img:'lit-keypad',       eyebrow:'Wall control',   name:'Lutron Palladiom keypad', detail:'Engraved buttons in your own words',
    icon:(<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round"><rect x="3" y="2.5" width="10" height="11" rx="1"/><line x1="5" y1="5" x2="11" y2="5"/><line x1="5" y1="7.5" x2="11" y2="7.5"/><line x1="5" y1="10" x2="11" y2="10"/><line x1="5" y1="12.5" x2="11" y2="12.5"/></svg>)},
  {area:'c', img:'lit-landscape-fl', eyebrow:'Exterior',       name:'Landscape uplighting',    detail:'Sabal palms, oak canopies, façade wash',
    icon:(<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><path d="M8 2.5c-2.2 0-3.5 1.8-3 3.5.5-.6 1.4-.9 2.2-.5C6.6 6 6 6.7 6.2 7.6c.6-.5 1.4-.4 1.8.2-.4.6-.4 1.4 0 1.9V14"/><line x1="6" y1="14.5" x2="10" y2="14.5"/><path d="M3.5 13.5l1-2M12.5 13.5l-1-2" strokeOpacity=".55"/></svg>)},
  {area:'d', img:'lit-pendants',     eyebrow:'Decorative',     name:'Pendants & sconces',      detail:'Phase-cut to ELV, no flicker on camera',
    icon:(<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><line x1="8" y1="1.5" x2="8" y2="6"/><path d="M5 6h6l-1 4.5H6z"/><path d="M6.3 11l-.5 2M9.7 11l.5 2" strokeOpacity=".55"/></svg>)},
  {area:'e', img:'lit-app',          eyebrow:'In hand',        name:'Mobile scenes',           detail:'One press: Alba · Day · Sera · Notte',
    icon:(<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><rect x="4.5" y="1.5" width="7" height="13" rx="1.2"/><path d="M6 5.5c0 1.1.9 2 2 2s2-.9 2-2"/><circle cx="8" cy="12" r=".7" fill="white" stroke="none"/></svg>)},
  {area:'f', img:'lit-lanai-fl',     eyebrow:'Outdoor living', name:'Lanai & path',            detail:'Warm path tape, gulf-side glare control',
    icon:(<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"><polyline points="2.5,13 5,13 5,10 8,10 8,7 11,7 11,4 13.5,4"/></svg>)},
];

function LightingMosaic() {
  return (
    <section className="svc-mosaic">
      <style>{`
        .svc-mosaic{background:var(--cream);padding:clamp(4rem,8vw,6.5rem) 0}
        .svc-mosaic-inner{max-width:1280px;margin:0 auto;padding:0 80px}
        .svc-mosaic-head{text-align:center;max-width:680px;margin:0 auto 44px}
        .svc-mosaic-head .sec-label{margin-bottom:12px}
        .svc-mosaic-head h2{font-family:var(--serif);font-size:clamp(2rem,3.4vw,3rem);line-height:1.1;font-weight:600;text-wrap:pretty}
        .svc-mosaic-head h2 em{color:var(--accent);font-style:italic}
        .svc-mosaic-head .lead{margin-top:14px;color:var(--mid);line-height:1.7;font-size:15px}
        .svc-mosaic-grid{display:grid;gap:.5rem;grid-template-columns:1.4fr 1fr 1fr;grid-template-rows:repeat(2,320px);grid-template-areas:"a b c" "a d e" "f f e"}
        .svc-tile{position:relative;overflow:hidden;border-radius:14px;margin:0;background:#1B1A28;isolation:isolate}
        .svc-tile[data-area="a"]{grid-area:a}
        .svc-tile[data-area="b"]{grid-area:b}
        .svc-tile[data-area="c"]{grid-area:c}
        .svc-tile[data-area="d"]{grid-area:d}
        .svc-tile[data-area="e"]{grid-area:e}
        .svc-tile[data-area="f"]{grid-area:f}
        .svc-tile .svc-bg{position:absolute;inset:0;background-size:cover;background-position:center;transform:scale(1);transition:transform 600ms cubic-bezier(.2,.7,.2,1);z-index:0}
        .svc-tile:hover .svc-bg{transform:scale(1.05)}
        .svc-tile .svc-grad{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,transparent 0%,transparent 40%,rgba(15,74,66,0.85) 100%);transition:background 420ms ease}
        .svc-tile:hover .svc-grad{background:linear-gradient(180deg,transparent 0%,rgba(15,74,66,0.25) 30%,rgba(15,74,66,0.95) 100%)}
        .svc-tile .hex{position:absolute;top:1.25rem;left:1.25rem;z-index:3;width:38px;height:38px;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;clip-path:polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%)}
        .svc-tile .svc-text{position:absolute;left:0;right:0;bottom:0;z-index:2;padding:1.25rem;color:#fff}
        .svc-tile .svc-eyebrow{display:block;font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.7);margin-bottom:6px}
        .svc-tile h4{font-family:var(--sans);font-size:1.05rem;font-weight:500;color:#fff;margin:0;display:inline-block;position:relative;padding-bottom:3px;line-height:1.3}
        .svc-tile h4::after{content:'';position:absolute;left:0;right:0;bottom:0;height:1.5px;background:var(--accent);transform:scaleX(0);transform-origin:left;transition:transform 320ms ease}
        .svc-tile:hover h4::after{transform:scaleX(1)}
        .svc-tile p{font-family:var(--sans);font-size:.85rem;color:rgba(255,255,255,.7);margin:6px 0 0;line-height:1.45}
        .svc-mosaic-foot{text-align:center;margin-top:36px;color:var(--mid);font-size:.9rem;font-style:italic}
        @media (max-width:1099px){
          .svc-mosaic-inner{padding:0 40px}
          .svc-mosaic-grid{grid-template-columns:1fr 1fr;grid-template-rows:auto;grid-template-areas:"a a" "b c" "d e" "f f"}
          .svc-tile{min-height:280px}
        }
        @media (max-width:759px){
          .svc-mosaic-inner{padding:0 24px}
          .svc-mosaic-grid{grid-template-columns:1fr;grid-template-areas:"a" "b" "c" "d" "e" "f"}
          .svc-tile{aspect-ratio:4/3;min-height:0}
        }
      `}</style>
      <div className="svc-mosaic-inner">
        <header className="svc-mosaic-head">
          <span className="sec-label">What we install</span>
          <h2>Light is <em>six layers</em>, not one switch.</h2>
          <p className="lead">Recessed downs, cove, accent, decorative, task, and exterior — each on its own dimming track, all on one keypad. Designed with the architect, not after.</p>
        </header>
        <div className="svc-mosaic-grid">
          {MOSAIC_TILES.map(t=>(
            <figure key={t.area} className="svc-tile" data-area={t.area} aria-label={`${t.eyebrow} — ${t.name}`}>
              <div className="svc-bg" data-img={t.img} style={{backgroundImage:`url(${PHOTOS[t.img]})`}}/>
              <div className="svc-grad"/>
              <span className="hex" aria-hidden="true">{t.icon}</span>
              <div className="svc-text">
                <span className="svc-eyebrow">{t.eyebrow}</span>
                <h4>{t.name}</h4>
                <p>{t.detail}</p>
              </div>
            </figure>
          ))}
        </div>
        <p className="svc-mosaic-foot">All on Lutron RadioRA 3. One scene, one press, the whole house responds.</p>
      </div>
    </section>
  );
}

/* ─── LIGHTING PAGE ─── */
function LightingPage({navigate}) {
  const I = (d) => <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d={d}/></svg>;
  return <ServicePageShell navigate={navigate}
    hero={{eyebrow:'Lighting control', h1:'Your fixtures. <em>Our controls.</em>',
      lead:'Lighting is the most personal layer of a home. LUMA coordinates your fixture specification with a control design that makes every room feel exactly as intended, at 8am and at 8pm.',
      image: PHOTOS.lightingKetra, primaryLabel:'Start your lighting project →', primaryAction:()=>navigate('contact'),
      secondaryLabel:'For designers & builders', secondaryAction:()=>navigate('designers')}}
    intro={{lead:'Light is six layers, not one switch.',
      body:'Recessed downs, cove, accent, decorative, task and exterior, each on its own dimming track and all on one keypad. We design it with the architect and the interior designer before the drywall, on Lutron RadioRA 3 and Ketra, so the decorative fixtures you chose dim the way they were meant to.'}}
    values={{h2:'What the system <em>does for you</em>',
      lead:'Four things you feel the first evening, none of which need a manual.',
      items:[
        {icon:I('M3 12h18M12 3v18'), title:'Warm-dim evenings', desc:'Ketra and warm-dim LEDs slide from 2700K to 1800K as they dim, so the house goes candle-warm at night instead of grey.'},
        {icon:I('M4 6h16v12H4zM8 10h.01M12 10h.01M16 10h.01'), title:'Controls in your words', desc:'Touch panels and keypads with scenes named "Dinner", "Reading", "Goodnight", finished to match your plates, hardware and wood tones.'},
        {icon:I('M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M2 12h4M18 12h4M4.9 19.1l2.8-2.8M16.3 7.7l2.8-2.8'), title:'Cove, soffit and accent', desc:'Hidden 2700K tape dimmable to 0.1%, art and niche accents on their own track, no visible hardware in the ceiling plane.'},
        {icon:I('M12 22s7-7.5 7-12a7 7 0 1 0-14 0c0 4.5 7 12 7 12zM12 10h.01'), title:'Landscape and lanai', desc:'Sabal palms, oak canopies and the façade washed from the same keypad; warm path tape on the lanai with gulf-side glare kept off the glass.'},
      ]}}
    pair={{
      h2:'Same room, <em>eight in the morning and eight at night.</em>',
      lead:'Nothing in the room changes but the light. The pendants, the cove and the lamp each hold their own level, and one keypad press moves all of them.',
      items:[
        {photo: PHOTOS.lightingDay,   label:'Day, no artificial light'},
        {photo: PHOTOS.lightingKetra, label:'Evening scene, 2700K'},
      ]
    }}
    panels={{h2:'How we work <em>the light</em>',
      items:[
        {photo: PHOTOS.lightingKetra, title:'Scene design', body:'Morning coffee, focused work, candlelit dinner, movie night. Each scene pre-programmed to the exact colour temperature and level your life calls for, one press shifts the whole home.'},
        {photo: PHOTOS.lightingRania, title:'Fixture coordination', body:'We work downstream of your interior designer and lighting consultant. Visual Comfort chandeliers, RH pendants, custom cove in the millwork: every fixture tuned to dim smoothly and hold colour.'},
        {photo: PHOTOS.handPanel, title:'Unified control', body:'Keypads, app and voice under a single control layer. We match keypad finishes to your hardware, commission every zone on site, and leave a system any family member can use.'},
      ]}}
    cases={['case-family']}
    ctaTitle='Ready to light the house <em>properly?</em>'
    ctaBody='Send us the fixture schedule, or just the floor plan. We will come back with a control design that matches what your designer specified, and an honest range.'
  />;
}
/* ─── DESIGNERS PAGE ─── */
/* ─── DESIGNERS & BUILDERS PAGE ─── */
/* ─── DESIGNERS & BUILDERS ───
   Built from the reference's inner-page pieces: hero, one centred paragraph,
   the values panel, the tabbed block from their About page, a two-column
   list, the wave CTA. */
const DB_DESIGNER_STEPS = [
  {n:'01', title:'You send us your FF&E schedule',
   body:'Share fixture specs, CAD drawings, or even a rough list. We review your decorative selections and flag anything that needs a dimmer, driver, or special wiring before walls close.'},
  {n:'02', title:'We write a single coordinated proposal',
   body:'One line-item document covers all fixtures, LED drivers, Lutron or Ketra dimmers, wall plates, and commissioning, formatted for your client presentation and matched to your interior finishes.'},
  {n:'03', title:'On-site coordination at your pace',
   body:'We attend your site visits or schedule separately. If something changes after demolition (ceiling height, beam location, a last-minute fixture swap) we adjust the spec the same day.'},
  {n:'04', title:'Submittal packages your way',
   body:'Cut sheets, dimmer curves, wiring diagrams. Formatted for your workflow: PDF, Revit, or email to the GC. The electrician gets exactly what they need, once.'},
];

const DB_BUILDER_STEPS = [
  {n:'01', title:'Pre-construction meeting',
   body:'We join your kickoff call or site walk. We review the architectural plans and mark up every conduit run, J-box location, and equipment room so nothing needs to be re-opened later.'},
  {n:'02', title:'Rough-in package for your electrician',
   body:'A single PDF: conduit layout, home-run map, box heights, rack dimensions, and PoE drop locations. Your electrician installs in one pass.'},
  {n:'03', title:'Milestone check-ins through framing and drywall',
   body:'We walk the job before insulation and before drywall so the GC can catch issues at cost, not at trim-out. We document everything and update the package if the plan shifts.'},
  {n:'04', title:'Trim-out and commissioning',
   body:'We install all devices, pull and terminate every cable, and program the system while other trades finish. Our work does not hold up your certificate of occupancy.'},
  {n:'05', title:'Punch-list and client handoff',
   body:'We attend the final walk with you. Every scene, shade, and camera is verified. The client gets a 60-minute orientation and a printed quick-reference card for the home.'},
];

const DB_WHY = [
  {icon:'people', title:'One trade, not four',
   desc:'Lighting control, shading, AV, security, and networking under one contractor. Your GC has one contact, one schedule, and one RFI queue for all of it.'},
  {icon:'shield', title:'Florida licensed · insured',
   desc:'Low-voltage contractor of record. We carry general liability and workers\' comp. Certificate of insurance on request.'},
  {icon:'gift', title:'Referral program',
   desc:'For designers and builders who refer projects: a referral fee on signed contracts, paid at commissioning. Ask us for the one-page agreement.'},
];

const DB_LISTS = [
  {kicker:'For designers & architects', title:'What you get', items:[
    'A single coordinated proposal: fixtures, drivers, control, commissioning',
    'Submittal packages in PDF or Revit format',
    'Site visits on your schedule, spec changes the same day',
    'Referral fee on signed contracts, paid at commissioning',
  ]},
  {kicker:'For builders', title:'What we deliver', items:[
    'Pre-construction walk and marked-up plan set',
    'Rough-in package for the electrician: conduit, J-box, home-run map',
    'Milestone inspections before insulation and before drywall',
    'Full trim-out and commissioning on your schedule',
    'Client orientation and printed quick-reference guide',
    'Referral fee on signed contracts, paid at commissioning',
  ]},
];

function FxSteps({steps}){
  return (
    <div className="fx-steps">
      {steps.map(s => (
        <div key={s.n} className="fx-step">
          <small>Step {s.n}</small>
          <h3>{s.title}</h3>
          <i className="fx-panel-rule" aria-hidden="true"/>
          <p>{s.body}</p>
        </div>
      ))}
    </div>
  );
}

function DesignersPage({navigate}) {
  const trade = () => { CONTACT_PRESET = 'Designer or builder'; };
  return (
    <div className="page">
      <FxInnerHero kicker="Designers & builders" h1="Your vision. Our wiring." image={PHOTOS.heroDesigners} alt="Architectural lighting in a finished Gulf Coast living room"/>

      <section className="fx-band--plain fx-py-md">
        <div className="fx-field">
          <div className="fx-intro-prose">
            <p><strong>LUMA works alongside interior designers, architects, and custom builders across Sarasota and Manatee.</strong> We fit our process to yours: FF&amp;E coordination, submittal packages, pre-wire rough-in, and final punch-list. One contractor for lighting, shading, AV, security, and networking. One schedule. One proposal your client can actually read.</p>
          </div>
        </div>
      </section>

      <FxValuesPanel h2="Built to fit your workflow." items={DB_WHY}/>

      <section className="fx-band--plain fx-py-lg">
        <div className="fx-wide">
          <div className="fx-heads" style={{marginBottom:40}}><h2 className="fx-d3">A clear process, start to finish.</h2></div>
          <FxTabs tabs={[
            {label:'Designers & architects', body:<FxSteps steps={DB_DESIGNER_STEPS}/>},
            {label:'Builders & developers', body:<FxSteps steps={DB_BUILDER_STEPS}/>},
          ]}/>
        </div>
      </section>

      <section className="fx-band fx-py-lg">
        <div className="fx-wide">
          <div className="fx-lists">
            {DB_LISTS.map(l => (
              <div key={l.kicker} className="fx-list">
                <span className="fx-panel-kicker">{l.kicker}</span>
                <h3 className="fx-d3">{l.title}</h3>
                <ul className="fx-checks">{l.items.map(it => <li key={it}>{it}</li>)}</ul>
                <NavLink page="contact" navigate={navigate} onNavigate={trade} className="fx-btn">Start a trade inquiry</NavLink>
              </div>
            ))}
          </div>
        </div>
      </section>

      <FxCta navigate={navigate} onNavigate={trade}
        title="Ready to work together?"
        body="Send us your plans or a quick note about the project, and we will come back with a scope."
        label="Start a trade inquiry"/>
    </div>
  );
}

/* ─── THEATERS PAGE ─── */
const TH_LAYERS = [
  {k:'projection', title:'Projection', icon:(
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><rect x="2.5" y="6" width="12" height="8" rx="1.5"/><circle cx="8" cy="10" r="2"/><path d="M14.5 8.5l3-1.5v6l-3-1.5z"/></svg>
  ), desc:'JVC NZ-series or Sony VPL laser projectors paired with Stewart Filmscreen or Seymour AT canvas. 4K HDR, anamorphic option for 2.40:1 rooms.'},
  {k:'sound', title:'Sound', icon:(
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><rect x="3" y="6" width="14" height="8" rx="1.2"/><circle cx="6.5" cy="10" r="1.4"/><circle cx="13.5" cy="10" r="1.4"/><line x1="9.5" y1="9" x2="10.5" y2="9"/><line x1="9.5" y1="11" x2="10.5" y2="11"/></svg>
  ), desc:'Trinnov Altitude or Storm Audio processing. Dolby Atmos and DTS:X in 7.4.4 or 9.4.6 layouts, every channel tuned to the room.'},
  {k:'speakers', title:'Speakers', icon:(
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><rect x="6" y="2.5" width="8" height="15" rx="1.2"/><circle cx="10" cy="7.5" r="1.4"/><circle cx="10" cy="13" r="2.2"/></svg>
  ), desc:'Sonance Reference or James Loudspeaker behind acoustically transparent screens. The room reads as architecture; nothing visible.'},
  {k:'acoustics', title:'Acoustics', icon:(
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M3.5 10c1.5-2 3-2 4.5 0s3 2 4.5 0 3-2 4.5 0"/><path d="M3.5 13.5c1.5-2 3-2 4.5 0s3 2 4.5 0 3-2 4.5 0" strokeOpacity=".55"/><path d="M3.5 6.5c1.5-2 3-2 4.5 0s3 2 4.5 0 3-2 4.5 0" strokeOpacity=".35"/></svg>
  ), desc:'Fabric-wrapped absorbers and diffusers designed in from day one. Bass traps in corners. No flutter, no slap echo, no audible room.'},
  {k:'seating', title:'Seating', icon:(
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M4 14v-4a2 2 0 012-2h8a2 2 0 012 2v4"/><path d="M3 14h14v2.5H3z"/><line x1="6" y1="14" x2="6" y2="17"/><line x1="14" y1="14" x2="14" y2="17"/></svg>
  ), desc:'Cineak or Fortress motorized seats with butt-kickers and cup-cooled holders. Risers cut on-site so every seat owns a sightline.'},
  {k:'control', title:'Control', icon:(
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="3" width="14" height="14" rx="2"/><circle cx="7" cy="7" r="1"/><circle cx="13" cy="7" r="1"/><circle cx="7" cy="13" r="1"/><circle cx="13" cy="13" r="1"/></svg>
  ), desc:'One Crestron or Josh.ai press: lights dim, shades drop, projector wakes, source ready. Zero remotes on the coffee table.'},
];

const TH_ROOMS = [
  {name:'Living room theater', desc:'Visible TV, hidden subs, ambient-friendly. Movie nights without darkening the whole room.'},
  {name:'Dedicated theater',   desc:'Light-controlled, riser seating, reference sound. Built for the film, not the furniture.'},
  {name:'Outdoor cinema',      desc:'Weatherized lanai screen, all-weather speakers. Sunset to credits.'},
];

const TH_WHY = [
  {n:'01', text:'Acoustically modeled before construction. We send REW data, not vibes — predicted response, treatment placement, and seat-by-seat coverage maps.'},
  {n:'02', text:'CEDIA-aligned design process. We build theaters every month, not once a year. The mistakes are out of our system.'},
  {n:'03', text:'Calibrated and recalibrated. Every theater includes a 12-month tune-up visit at no charge — speakers settle, rooms breathe, ears recalibrate.'},
];


const TH_CREDS = [
  'CEDIA Member','THX-Aligned Design','Trinnov Certified','ISF Calibrator','12-Month Tune-Up Included',
];

function TheatersPage({navigate}) {
  const I = (d) => <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d={d}/></svg>;
  return <ServicePageShell navigate={navigate}
    hero={{eyebrow:'Home theaters', h1:'Designed for <em>sound,</em> not retrofitted.',
      lead:'The difference between a TV in a media room and a true home theater is acoustic intent: walls, seating, screen and speakers designed together, then calibrated in the room they live in.',
      image: PHOTOS.theater, primaryLabel:'Plan my theater →', primaryAction:()=>navigate('contact'),
      secondaryLabel:'See recent rooms', secondaryAction:()=>navigate('work')}}
    intro={{lead:'A room built for the first movie night, and the thousandth.',
      body:'We start with the room, not the projector: dimensions, sightlines, where the sound will reflect and where it must not. Then the screen size follows the seating distance, the speakers follow the screen, and the acoustic treatment follows all three. The gear goes out of sight and the room gets calibrated in place before you see a frame.'}}
    values={{h2:'Four layers, <em>one room</em>',
      lead:'What actually makes a theater, in the order we design it.',
      diagram:{image:lu('/assets/photos/theater-layers.jpg'), alt:'Cutaway of a dedicated home theater: acoustic panels, screen and speakers, two rows of recliners on a riser, a measurement microphone at the main seat',
        pins:[[73,40],[36,33],[40,67],[46,45]]},
      items:[
        {icon:I('M3 5h18v14H3zM3 10h18M8 5v14'), title:'Acoustic treatment', desc:'Fabric-wrapped absorption and diffusion placed by measurement, so dialogue lands and bass does not boom. The walls look like walls.'},
        {icon:I('M2 7h20v10H2zM6 21h12'), title:'Screen and projection', desc:'Screen size from the seating distance, not the wall. 4K laser projection or a direct-view LED wall, calibrated to reference.'},
        {icon:I('M4 20V10l8-6 8 6v10M9 20v-6h6v6'), title:'Seating and sightlines', desc:'Rows, risers and aisle set so every seat sees the whole screen and sits in the sound, not behind it.'},
        {icon:I('M12 3v18M6 8v8M18 8v8M3 11v2M21 11v2'), title:'Calibration', desc:'ISF-calibrated picture, speakers time-aligned and equalised in the finished room, with Atmos placed to the ceiling you actually have.'},
      ]}}
    panels={{h2:'From <em>media room</em> to private cinema',
      items:[
        {photo: PHOTOS.theaterCinema, title:'Dedicated cinema', body:'A room with one job: fabric walls, tiered recliners, a star ceiling if you want one, and the projector and rack out of sight.'},
        {photo: PHOTOS.theaterLiving, title:'Living-room theater', body:'A great room that turns into a cinema at 8pm: hidden screen, in-ceiling surrounds, shades and lights on one press.'},
        {photo: PHOTOS.theaterMedia, title:'Media room', body:'A family room with a large display, a proper soundbar-free system, and acoustics that keep game day from taking over the house.'},
      ]}}
    cases={['case-bighouse', 'case-urban', 'case-modern']}
    ctaTitle='Start a <em>theater conversation</em>'
    ctaBody='Tell us about the room: square footage, ceiling height, how you will use it. We answer with a calibration plan, not a quote form.'
  />;
}
/* ─── AUTOMATION PAGE ─── */
const AU_STATES = [
  {time:'06:30', name:'Alba',   hour:6,  min:30, desc:'Shades east rise. Hallway keypads warm to 2700K. Coffee station wakes. Front cameras armed-stay clears.'},
  {time:'10:00', name:'Day',    hour:10, min:0,  desc:'Glare side shades drop on the sun. Office overheads to task. Alarm to "armed-away" if everyone has left.'},
  {time:'sunset – 30', name:'Sera', hour:18, min:30, desc:'Lanai lights to 30%. Kitchen pendants warm. Music fades up where you are.'},
  {time:'22:30', name:'Notte',  hour:22, min:30, desc:'Doors lock, perimeter cameras armed, hallways at 5% footlights, primary bedroom shades close, theater off.'},
];

function ClockIcon({hour, min}) {
  // 12-hour analog face with hands at hour/min
  const h = ((hour % 12) + min/60) * 30 - 90; // degrees from 3 o'clock
  const m = (min/60) * 360 - 90;
  const r = 18;
  const cx = 22, cy = 22;
  const hx = cx + Math.cos(h*Math.PI/180)*9;
  const hy = cy + Math.sin(h*Math.PI/180)*9;
  const mx = cx + Math.cos(m*Math.PI/180)*13;
  const my = cy + Math.sin(m*Math.PI/180)*13;
  return (
    <svg width="22" height="22" viewBox="0 0 44 44" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round">
      <circle cx={cx} cy={cy} r={r}/>
      <line x1={cx} y1={cy} x2={hx} y2={hy} strokeWidth="2"/>
      <line x1={cx} y1={cy} x2={mx} y2={my}/>
    </svg>
  );
}

const AU_CONTROLS = [
  {label:'Lighting',   page:'lighting'},
  {label:'Shading',    page:'shading'},
  {label:'Climate',    page:null},
  {label:'Audio',      page:'audio'},
  {label:'Security',   page:'security'},
  {label:'Networking', page:'networking'},
];

const AU_WHY = [
  {n:'01', text:'We program the routines with you for 90 days, not just once on day one. The first month is observation — the second and third are the real tuning.'},
  {n:'02', text:'Every keypad button is documented and labeled in your own words — "Reading," "Movie," "Goodnight" — not LED1 / Scene 4 / Group 12.'},
  {n:'03', text:'Annual visit included. We re-tune as your habits change — kids grow up, work hours shift, the lanai becomes a gym. The routines move with you.'},
];


function AutomationPage({navigate}) {
  const I = (d) => <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d={d}/></svg>;
  return <ServicePageShell navigate={navigate}
    hero={{eyebrow:'Home automation', h1:'One press, <em>the right state.</em>',
      lead:'Automation is the quiet layer that lets lighting, shades, climate, audio and security move together. Four states the house already knows; you can override any of them, but most days you will not need to.',
      image: PHOTOS.automationHero, primaryLabel:'Plan my system →', primaryAction:()=>navigate('contact'),
      secondaryLabel:'Try the 3D demo', secondaryAction:()=>navigate('smart-home-demo')}}
    intro={{lead:'We build on open, professional platforms.',
      body:'Lutron RadioRA 3 is the spine: every light, shade and keypad on a single mesh that does not depend on anyone\'s cloud to dim a sconce. Above it, Control4 or Josh.ai for the rest of the house. No closed consumer ecosystems, no rented automations that vanish when a startup pivots. Your house\'s logic lives in your house.'}}
    scenes={{h2:'Four states <em>the house already knows</em>',
      lead:'Alba, Day, Sera, Notte: named in your words and tuned with you for ninety days. The same great room at four times of day, and what the system moved each time.'}}
    panels={{h2:'Routines that <em>survive real life</em>',
      items:[
        {photo: PHOTOS.handPhone, title:'Tuned for ninety days', body:'We program the routines with you for three months, not once on day one. The first month is observation; the second and third are the real tuning.'},
        {photo: PHOTOS.installPanel, title:'Scenes in your words', body:'Every scene named the way you say it, Reading, Movie, Goodnight, on the touch panel by the door and in the app. Never LED1, Scene 4, Group 12.'},
        {photo: PHOTOS.heroHome, title:'An annual visit, included', body:'We re-tune as your habits change. Kids grow up, work hours shift, the lanai becomes a gym. The routines move with you.'},
      ]}}
    cases={['case-bighouse', 'case-family']}
    ctaTitle='Start an <em>automation conversation</em>'
    ctaBody='Tell us how the house is used through the day. We map it to scenes, then show you the plan before anything is ordered.'
  />;
}
/* ─── SHARED VALUE-PROP / WHY / WORK BLOCKS ─── */
function ServicePageShell({hero, valueProp, why, projects, credentials, ctaCopy, formName, installGrid, navigate, intro, values, panels, pair, faq, ctaTitle, ctaBody, scenes, cases}) {
  /* The reference's inner page, section for section: a short hero, one
     centred paragraph with a bold lead, a "what it does for you" grid (copy
     in five columns, four icon items in seven), a row of photo cards, and
     the wave CTA. Pages that still pass the older hero/valueProp/why/projects
     props are mapped onto those slots here; pages built for this shell pass
     intro / values / panels / pair / faq directly. */
  const stripEm = (h) => String(h||'').replace(/<\/?em>/g,'');
  const introLead = intro ? intro.lead : hero.lead;
  const introBody = intro ? intro.body : (valueProp && valueProp.lead);
  const vals = values || (valueProp && {
    h2: valueProp.h2,
    lead: why ? stripEm(why.h2) : '',
    items: [
      ...valueProp.cards.map(c => ({icon:c.icon, title:c.title, desc:c.desc})),
      ...(valueProp.split && valueProp.split.rows ? [{title:valueProp.split.rows[0].name, desc:valueProp.split.rows[0].desc}] : [])
    ].slice(0,4)
  });
  const cards = panels;
  const pin = <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></svg>;
  return (
    <div className="page">
      {/* 1. hero — the site's inner hero, kicker + headline + lead */}
      <section style={{display:'grid',gridTemplateColumns:'1fr 1fr',minHeight:'min(88vh,780px)',background:'var(--dark)',overflow:'hidden'}} className="lit-hero-wrap">
        <div style={{display:'flex',flexDirection:'column',justifyContent:'center',padding:'88px 64px 88px 80px',background:'var(--dark)',color:'#FCFAF6'}} className="lit-hero-text">
          <div style={{fontSize:12,letterSpacing:'.16em',textTransform:'uppercase',color:'var(--accent)',fontWeight:600,marginBottom:22}}>{hero.eyebrow}</div>
          {/* the reference's inner hero carries the kicker and the headline, nothing
              else; the lead opens the intro paragraph and the buttons live in the
              header and the closing CTA */}
          <h1 style={{fontFamily:'var(--serif)',color:'#FCFAF6',margin:0}} dangerouslySetInnerHTML={{__html: hero.h1.replace(/<em>/g,'<em style="color:#F4C9A8;font-style:italic">')}}/>
        </div>
        <div style={{position:'relative',overflow:'hidden',minHeight:480}}>
          <img loading="eager" fetchpriority="high" decoding="async" src={hero.image} alt={hero.eyebrow} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:'center center',display:'block'}}/>
        </div>
      </section>

      {/* 2. intro — one centred paragraph, bold lead */}
      <section className="fx-band--plain fx-py-md">
        <div className="fx-field">
          <div className="fx-intro-prose">
            <p><strong>{introLead}</strong> {introBody}</p>
          </div>
        </div>
      </section>

      {scenes && <FxScenes heading={scenes.h2} lede={scenes.lead} band={false}/>}

      {/* 3. what it does for you — copy left, four icon items right; or, where a
          page has one, a cutaway with numbered pins tied to the same items */}
      {vals && vals.diagram && <FxDiagram vals={vals}/>}
      {vals && !vals.diagram && (
        <section className="fx-values fx-values--plain">
          <div className="fx-wide">
            <div className="fx-values-grid">
              <div className="fx-values-copy" style={{gap:16}}>
                <h2 className="fx-d3" style={{fontSize:'clamp(28px,2.4vw,32px)'}} dangerouslySetInnerHTML={{__html: vals.h2}}/>
                {vals.lead && <div className="fx-lede"><p>{vals.lead}</p></div>}
              </div>
              <div className="fx-values-list">
                {vals.items.map((it,i) => (
                  <div key={i} className="fx-value">
                    <span className="fx-tile" aria-hidden="true">{it.icon || pin}</span>
                    <span><strong>{it.title}</strong><p>{it.desc}</p></span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>
      )}

      {/* 3b. day / night pair — only pages that have one */}
      {pair && (
        <section className="fx-band--plain fx-py-md">
          <div className="fx-wide">
            <div className="fx-heads" style={{marginBottom:40}}>
              <h2 className="fx-d3" dangerouslySetInnerHTML={{__html: pair.h2}}/>
              {pair.lead && <p className="fx-lede">{pair.lead}</p>}
            </div>
            <div className="fx-pair">
              {pair.items.map((p,i) => (
                <figure key={i}><img src={p.photo} alt={p.label} loading="lazy" decoding="async"/><figcaption>{p.label}</figcaption></figure>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* 4. photo cards */}
      {cards && (
        <section className="fx-band--plain fx-py-lg">
          <div className="fx-wide">
            {cards.h2 && <div className="fx-heads" style={{marginBottom:40}}><h2 className="fx-d3" dangerouslySetInnerHTML={{__html: cards.h2}}/>{cards.lead && <p className="fx-lede">{cards.lead}</p>}</div>}
            <div className="fx-panels fx-panels--static">
              {cards.items.map((c,i) => (
                <div key={i} className="fx-panel-card">
                  <span className="fx-panel-img"><img src={c.photo} alt={c.title} loading="lazy" decoding="async"/></span>
                  <span className="fx-panel-body">
                    <h3>{c.title}</h3>
                    <i className="fx-panel-rule" aria-hidden="true"/>
                    <p>{c.body}</p>
                  </span>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* 4b. install strip — pages with a parts list */}
      {installGrid && (
        <section className="th-section" style={{paddingTop:0,paddingBottom:64}}>
          <div className="sec-label">{installGrid.eyebrow || 'On the property'}</div>
          <h2 className="sec-title" dangerouslySetInnerHTML={{__html: installGrid.h2}}/>
          {installGrid.lead && <p className="sec-body">{installGrid.lead}</p>}
          <div className="th-install-grid">
            {installGrid.items.map((it,i)=>(
              <div key={i} className={`th-install-cell${it.size?' '+it.size:''}`}>
                <img loading="lazy" decoding="async" src={PHOTOS[it.key]} alt={it.cap}/>
                <div className="th-install-cap">{it.cap}</div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* 4c. real projects that used this system — linked to their case studies */}
      {cases && cases.length > 0 && (
        <section className="fx-band fx-py-lg">
          <div className="fx-wide">
            <div className="fx-heads" style={{marginBottom:40}}><h2 className="fx-d3">Where we have done this</h2></div>
            <div className="fx-cases">
              {cases.map(id => { const c = LUMA_CASES[id]; return (
                <NavLink key={id} page={id} navigate={navigate} className="fx-work-card">
                  <img src={c.photo} alt={c.title} loading="lazy" decoding="async"/>
                  <div className="fx-work-meta"><span>{c.place}</span></div>
                  <h3>{c.title}</h3>
                  <p>{c.scope}</p>
                </NavLink>
              );})}
            </div>
          </div>
        </section>
      )}

      {/* 5. FAQ — the reference's accordion, only where a page has questions */}
      {faq && (
        <section className="fx-band fx-py-lg">
          <div className="fx-field">
            <div className="fx-heads" style={{marginBottom:32}}><h2 className="fx-d3">Questions we get asked</h2></div>
            <div className="fx-faq">
              {faq.map((q,i) => (
                <details key={i} className="fx-faq-item" open={i===0}>
                  <summary>{q.q}<i aria-hidden="true">+</i></summary>
                  <p>{q.a}</p>
                </details>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* 6. CTA — the wave field, form-free */}
      <FxCta navigate={navigate}
        title={ctaTitle || (ctaCopy && ctaCopy.h2)}
        body={ctaBody || (ctaCopy && ctaCopy.lead)}
        label="Book a consultation"/>
    </div>
  );
}

/* A cutaway with numbered pins; hovering a pin or a list item lights both. */
function FxDiagram({vals}){
  const [on, setOn] = useState(-1);
  const d = vals.diagram;
  return (
    <section className="fx-band fx-py-lg">
      <div className="fx-wide">
        <div className="fx-heads" style={{marginBottom:48}}>
          <h2 className="fx-d3" dangerouslySetInnerHTML={{__html: vals.h2}}/>
          {vals.lead && <p className="fx-lede">{vals.lead}</p>}
        </div>
        <div className="fx-diagram">
          <figure className="fx-diagram-art">
            <img src={d.image} alt={d.alt} loading="lazy" decoding="async"/>
            {d.pins.map(([x,y],i) => (
              <button key={i} type="button" className={'fx-pin'+(on===i?' on':'')} style={{left:x+'%',top:y+'%'}}
                aria-label={vals.items[i].title} onMouseEnter={()=>setOn(i)} onMouseLeave={()=>setOn(-1)}
                onFocus={()=>setOn(i)} onBlur={()=>setOn(-1)} onClick={()=>setOn(on===i?-1:i)}>{i+1}</button>
            ))}
          </figure>
          <ol className="fx-diagram-list">
            {vals.items.map((it,i) => (
              <li key={it.title} className={on===i?'on':''} onMouseEnter={()=>setOn(i)} onMouseLeave={()=>setOn(-1)}>
                <span className="fx-diagram-n" aria-hidden="true">{i+1}</span>
                <span><strong>{it.title}</strong><p>{it.desc}</p></span>
              </li>
            ))}
          </ol>
        </div>
      </div>
    </section>
  );
}

/* ─── AUDIO PAGE ─── */
function AudioPage({navigate}) {
  return <ServicePageShell
    navigate={navigate}
    formName="audio-inquiry"
    hero={{
      eyebrow:'Audio & video',
      h1:'Sound that <em>fills the room,</em> not the architecture.',
      lead:'Whole-home audio that disappears into the architecture — invisible in-ceiling, in-wall, and outdoor speakers tuned to each room\'s geometry, with one app and one source list across every zone.',
      image: PHOTOS.audioHero,
      primaryLabel:'Hear a finished system →', primaryAction:()=>navigate('work'),
      secondaryLabel:'Talk to us', secondaryAction:()=>navigate('contact'),
    }}
    valueProp={{
      eyebrow:'What we install',
      h2:'Audio you <em>can\'t see,</em> control you <em>don\'t think about.</em>',
      lead:'Three layers per home — the speakers in the architecture, the matrix that routes them, and the control surface that makes it all feel like one room.',
      cards:[
        {title:'Speakers',  icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5"><circle cx="10" cy="10" r="7"/><circle cx="10" cy="10" r="2.5"/></svg>,
         desc:'Sonance Reference and Architectural in-ceiling, James Loudspeaker outdoor, Sonos Architectural for budget zones. Flush-trim, paint-matched.'},
        {title:'Matrix',    icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5"><rect x="2.5" y="6" width="15" height="8" rx="1"/><line x1="6" y1="6" x2="6" y2="14"/><line x1="10" y1="6" x2="10" y2="14"/><line x1="14" y1="6" x2="14" y2="14"/></svg>,
         desc:'Sonos, Crestron DM NVX, or Savant audio matrices. 16+ zones, lossless streaming, every source available in every room.'},
        {title:'Control',   icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><circle cx="10" cy="10" r="7"/><line x1="10" y1="3" x2="10" y2="6"/><line x1="10" y1="14" x2="10" y2="17"/></svg>,
         desc:'One app for the family, keypads for the wall, voice through Josh.ai. Zones named in your words — "kitchen," not "Output 7."'},
      ],
      split:{
        eyebrow:'Acoustic detail',
        h2:'Tuned to <em>each room,</em> not the spec sheet.',
        image: PHOTOS.audioInvisible,
        alt:'Invisible in-ceiling audio',
        rows:[
          {name:'REW measurement pass',  desc:'Every zone measured with Room EQ Wizard. Bass response, decay, and time alignment captured before final EQ.'},
          {name:'Lanai & poolside',       desc:'James Loudspeaker AT or LANDSCAPE Series — IP-rated, hurricane-tested, voiced for outdoor air.'},
          {name:'Theater & two-channel',  desc:'Reference rooms designed alongside our home theater team. Trinnov processing optional.'},
        ],
      },
    }}
    why={{
      h2:'Sound that <em>ages well.</em>',
      rows:[
        {n:'01', text:'We tune speakers with REW measurements, not by ear in the showroom. Every zone gets a target curve and a measured-response file you keep.'},
        {n:'02', text:'Every zone is named in your own words ("kitchen," not "Zone 3"). The app you actually use looks like the house you actually live in.'},
        {n:'03', text:'One-year service visit included — drivers age, rooms change. We re-measure, re-tune, and replace anything that drifts.'},
      ],
    }}
    cases={['case-urban', 'case-spacious', 'case-bighouse']}
    credentials={['CEDIA Member','THX-Aligned Design','Trinnov Certified','ISF Calibrator','Insured & bonded']}
    ctaCopy={{
      h2:'Start an <em>audio conversation.</em>',
      lead:'Tell us about the home and the rooms that matter most. We\'ll send a zone plan within 48 hours.',
      placeholder:'Square footage, indoor + outdoor zones, listening preferences…',
      onSubmit:()=>navigate('contact'),
    }}
  />;
}

/* ─── SECURITY PAGE ─── */
function SecurityPage({navigate}) {
  return <ServicePageShell
    navigate={navigate}
    formName="security-inquiry"
    hero={{
      eyebrow:'Security & surveillance',
      h1:'Your footage. <em>Your property.</em>',
      lead:'On-premise camera systems with no monthly cloud fees and no third party with a copy of your driveway. Cameras placed by walking the property, not by floor plan.',
      image: PHOTOS.securityHero,
      primaryLabel:'See a finished install →', primaryAction:()=>navigate('work'),
      secondaryLabel:'Talk to us', secondaryAction:()=>navigate('contact'),
    }}
    installGrid={{
      eyebrow:'On the property',
      h2:'What a LUMA install <em>looks like.</em>',
      lead:'Cameras, recorder, panels, and the app — what actually goes on the wall, in the closet, and in your hand.',
      items:[
        {key:'installBullet',   cap:'G6 Pro Bullet under the soffit', size:'tall'},
        {key:'installDome',     cap:'G6 Dome at the entry'},
        {key:'installDoorbell', cap:'UniFi doorbell'},
        {key:'installNvr',      cap:'UNVR in the rack'},
        {key:'installPanel',    cap:'Control4 in-wall touchscreen'},
        {key:'installDock',     cap:'Dock camera on Sarasota Bay'},
        {key:'installPhone',    cap:'Protect app on your phone'},
      ],
    }}
    valueProp={{
      eyebrow:'How it works',
      h2:'A system <em>you don\'t manage.</em>',
      lead:'Three layers — the cameras at the perimeter, the recorder in your network closet, and the alarm system that ties everything to your phone and your local responders.',
      cards:[
        {title:'Cameras', icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5"><circle cx="10" cy="10" r="6"/><circle cx="10" cy="10" r="2.5"/><circle cx="14.5" cy="6" r="0.7" fill="currentColor"/></svg>,
         desc:'Ubiquiti UniFi Protect G6 series: G6 Pro Bullet at the perimeter, G6 Dome at the doors, AI Theta indoors where a camera should not look like one. 4K, on-camera AI detection, PoE, no batteries.'},
        {title:'NVR & storage', icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><rect x="2.5" y="5" width="15" height="3.5" rx="0.6"/><rect x="2.5" y="11.5" width="15" height="3.5" rx="0.6"/><circle cx="14.5" cy="6.75" r="0.6" fill="currentColor"/><circle cx="14.5" cy="13.25" r="0.6" fill="currentColor"/></svg>,
         desc:'UniFi Protect on-prem NVR. RAID storage, 30+ days retention, encrypted at rest. Your footage stays on your property.'},
        {title:'Alarm & monitoring', icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><path d="M10 2.5l-7 3v5c0 4 3 7 7 8 4-1 7-4 7-8v-5l-7-3z"/></svg>,
         desc:'Alarm.com or DSC PowerSeries integrated with cameras. Glass-break, motion, door contacts. Local response, optional UL monitoring.'},
      ],
      split:{
        eyebrow:'Footage philosophy',
        h2:'Your video <em>stays on your property.</em>',
        image: PHOTOS.securityFootage,
        alt:'On-prem network video recorder',
        rows:[
          {name:'No monthly cloud fees',  desc:'UniFi Protect runs on hardware you own. No subscription, no rented storage, no vendor with a backdoor.'},
          {name:'Walked, not drawn',       desc:'Camera placement done on-site, in the conditions you actually live in — sunset glare, landscape lighting, neighbor angles.'},
          {name:'Encrypted off-site backup',desc:'Optional encrypted cold backup to a property of your choosing — a second home, an office, a safe deposit drive.'},
        ],
      },
    }}
    why={{
      h2:'Surveillance that <em>respects the home.</em>',
      rows:[
        {n:'01', text:'All footage stored on-prem on UniFi Protect — no monthly cloud fees, no third party reviewing your driveway, no rented retention windows.'},
        {n:'02', text:'Cameras placed after a property walkthrough, not from a floor plan. Sunset glare, foliage growth, and neighbor sightlines factored in before mounting.'},
        {n:'03', text:'Two-year hardware warranty, parts and labor. Anything that fails in normal use, we replace — including the labor to swap it.'},
      ],
    }}
    cases={['case-bighouse']}
    credentials={['Ubiquiti UVP Partner','UniFi Protect Certified','CEDIA Member','Insured & bonded']}
    ctaCopy={{
      h2:'Start a <em>security conversation.</em>',
      lead:'Tell us about the property. We\'ll send a camera placement plan within 48 hours.',
      placeholder:'Property size, perimeter, areas of concern, existing system…',
      onSubmit:()=>navigate('contact'),
    }}
  />;
}


/* ─── PERMANENT LIGHTING PAGE ─── */
function PermanentLightingPage({navigate}) {
  const I = (d) => <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d={d}/></svg>;
  return <ServicePageShell
    navigate={navigate}
    hero={{
      eyebrow:'Permanent outdoor lighting',
      h1:'The roofline, <em>drawn in light.</em>',
      lead:'A slim channel under the overhangs, colour-matched to the fascia and invisible by day. At night it traces the architecture in warm white, and the same line does security, game day and the holidays from a preset.',
      image: PHOTOS.permWarm,
      primaryLabel:'See a lit house →', primaryAction:()=>navigate('work'),
      secondaryLabel:'Talk to us', secondaryAction:()=>navigate('contact'),
    }}
    intro={{
      lead:'Architectural lighting for the part of the house landscape lights never reach.',
      body:'LUMA installs permanent roofline lighting on Gulf Coast residences across Sarasota and Manatee Counties: a channel matched to the fascia, individually addressed diodes inside it, and a controller in the rack with the rest of the house. Most nights it is a quiet warm-white line that finishes the elevation. When you want the house bright for security, in your team\'s colours, or dressed for December, it is one preset, and nothing goes up or comes down.'
    }}
    values={{
      h2:'What the system <em>does for you</em>',
      lead:'Four things owners tell us they use every week, none of which need a ladder, a timer plug or a bin of tangled strings.',
      items:[
        {icon:I('M12 6v6l4 2M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z'), title:'Set it and forget it',
         desc:'Sunset-on, midnight-off, a schedule for the season and a preset for the date. The lights remember the plan; you stop thinking about them.'},
        {icon:I('M3 9h18M3 15h18M9 3v18M15 3v18'), title:'Zone by zone',
         desc:'Front roofline, lanai, dock and the garage side each on their own run, so the pool cage can glow while the street side stays warm white.'},
        {icon:I('M12 3a9 9 0 1 0 9 9c0-1.5-1-2-2-2h-2a2 2 0 0 1-2-2V6c0-1.5-1-3-3-3zM7 10h.01M10 7h.01M15 8h.01'), title:'Sixteen million colours',
         desc:'A 2700K warm white that reads like landscape lighting, and every team, flag and holiday colour on top. Patterns and animations for the nights you want them.'},
        {icon:I('M12 2l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V6l8-4z'), title:'Part of the house',
         desc:'A sealed channel fastened into the fascia, not clipped to a gutter, so the line stays straight and nothing goes up or comes down with the seasons.'},
      ]
    }}
    pair={{
      h2:'Invisible by day, <em>bright by night.</em>',
      lead:'The channel is colour-matched to your fascia or soffit before it is ordered. From the street in daylight it reads as trim; from the street at night it reads as the house.',
      items:[
        {photo: PHOTOS.permEaveDay,   label:'The eave at noon'},
        {photo: PHOTOS.permEaveNight, label:'The same eave at nine'},
      ]
    }}
    panels={{
      h2:'One house, <em>four evenings.</em>',
      lead:'The same Sarasota residence in the settings owners actually use. Switched from the app, a Lutron keypad by the door, or the evening scene.',
      items:[
        {photo: PHOTOS.permWarm,     title:'Architectural warm white',   body:'A quiet 2700K line under every overhang that finishes the elevation the way uplighting finishes the palms. This is the everyday setting.'},
        {photo: PHOTOS.permSecurity, title:'Security',                   body:'Full-brightness cool white on demand or on a camera event, so the whole front of the house and the motor court are evenly lit.'},
        {photo: PHOTOS.permGameday,  title:'Game day',                   body:'Pewter and red for the Bucs, blue and white for the Rays, kept restrained enough for this house. Scheduled to kick-off if you like.'},
        {photo: PHOTOS.permanentHoliday, title:'December',               body:'Warm white and deep red for the holidays, a preset you set once. Nothing goes up in November and nothing comes down in January.'},
      ]
    }}
    faq={[
      {q:'How does it look during the day?', a:'Like trim. The channel is a slim extrusion powder-coated to match your fascia or soffit colour, and the diodes sit inside it. Most visitors do not notice it until you turn it on.'},
      {q:'Do you have a warm white?', a:'Yes, and it is what most owners run most nights: a 2700K warm white close to what good landscape lighting produces. The colours are there for when you want them.'},
      {q:'Will the channel fit my roofline?', a:'It is cut and fitted on site to your eaves, gables and returns, including barrel-tile rooflines and pool cages. Corners and peaks are planned on the drawing before the ladder goes up.'},
      {q:'How is it fixed to the house?', a:'The channel is fastened to the fascia, not clipped to a gutter, so it stays put through summer storms and does not interfere with drainage.'},
      {q:'Can it join the rest of the house?', a:'If LUMA did the lighting or automation, the roofline joins the same scenes: Evening turns it on with the lanai, Away turns it off with everything else, and a keypad by the door has a button for it.'},
      {q:'What is the warranty?', a:'Warranty terms depend on the product line you choose; we set them out in writing in the proposal, before anything is ordered.'},
    ]}
    ctaTitle='Tell us what your roofline should do'
    ctaBody='Send a photo of the front of the house. We will come back with a run plan, a channel colour, and an honest range before anything is ordered.'
  />;
}

/* ─── NETWORKING PAGE ─── */
function NetworkingPage({navigate}) {
  return <ServicePageShell
    navigate={navigate}
    formName="networking-inquiry"
    installGrid={{
      eyebrow:'What goes in',
      h2:'The parts you <em>never have to look at.</em>',
      lead:'Access points that disappear into the ceiling, switching and patch panels dressed so the next person can read them, and a rack that stays tidy years later.',
      items:[
        {key:'netAP',     cap:'Wi-Fi 6 / 7 access point'},
        {key:'netSwitch', cap:'Managed PoE switching'},
        {key:'netPatch',  cap:'Structured cabling'},
        {key:'netRack',   cap:'Clean rack'},
      ],
    }}
    hero={{
      eyebrow:'Networking',
      h1:'A network <em>your home is built on,</em> not bolted to.',
      lead:'Enterprise-grade Wi-Fi and structured cabling designed before drywall. Wired wherever wires can land, mesh only where it belongs — so every device works the day you move in.',
      image: PHOTOS.netRack,
      primaryLabel:'See a finished rack →', primaryAction:()=>navigate('work'),
      secondaryLabel:'Talk to us', secondaryAction:()=>navigate('contact'),
    }}
    valueProp={{
      eyebrow:'The wired backbone',
      h2:'Wires <em>where they should be,</em> wireless where they can\'t.',
      lead:'A modern Gulf Coast home runs 60–100+ connected devices. Mesh alone doesn\'t scale to that. We engineer a wired spine first, then layer wireless on top.',
      cards:[
        {title:'Cabling', icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M3.5 16.5C3.5 11 7 9 10 9s6.5 2 6.5 7.5"/><circle cx="10" cy="5" r="2.2"/></svg>,
         desc:'Cat6A or Cat7 to every TV, AP, camera, and workspace. Fiber backbone between floors. Every drop labeled at both ends.'},
        {title:'Wi-Fi 6/7', icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><path d="M2.5 8A12 12 0 0 1 17.5 8" strokeOpacity=".4"/><path d="M5 11a8 8 0 0 1 10 0" strokeOpacity=".7"/><path d="M7.5 14a4 4 0 0 1 5 0"/><circle cx="10" cy="16.5" r="0.9" fill="currentColor"/></svg>,
         desc:'Ubiquiti U7 Pro or U7 Pro Max access points, surveyed for coverage. 6 GHz where devices support it, 5 GHz fallback for the rest.'},
        {title:'Rack & gateway', icon:<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"><rect x="3" y="3" width="14" height="14" rx="1"/><line x1="3" y1="7" x2="17" y2="7"/><line x1="3" y1="11" x2="17" y2="11"/><line x1="3" y1="15" x2="17" y2="15"/><circle cx="14.5" cy="5" r="0.5" fill="currentColor"/></svg>,
         desc:'UniFi Dream Machine SE or Pro Max gateway. PoE switching, VLAN isolation for IoT, dual-WAN failover. Photographed and documented.'},
      ],
      split:{
        eyebrow:'Four signs',
        h2:'<em>Four signs</em> your network is the bottleneck.',
        image: PHOTOS.networkingRack,
        alt:'Network rack with structured cabling',
        rows:[
          {name:'Devices reconnect at random',     desc:'Mesh nodes hand off badly when they\'re overloaded. A wired backbone fixes it permanently.'},
          {name:'Streaming buffers in one room',   desc:'Almost always a coverage gap or an underpowered AP. A site survey finds it in an hour.'},
          {name:'Smart-home commands lag',         desc:'Lutron, cameras, and Sonos share a flat network with the kids\' Xbox. VLAN isolation removes the contention.'},
          {name:'Guest Wi-Fi slows the house',     desc:'A separate guest VLAN with rate limits keeps a teenager\'s download from killing the security cameras.'},
        ],
      },
    }}
    why={{
      h2:'A network <em>you forget exists.</em>',
      rows:[
        {n:'01', text:'Wired wherever wires can land. Mesh only where it belongs — never as a substitute for a Cat6A drop you should have run during framing.'},
        {n:'02', text:'Every drop is labeled at both ends. Patch panel photographed and filed with you, alongside a network map of every VLAN, AP, and reserved IP.'},
        {n:'03', text:'We ship the network 30 days before move-in so you arrive online — gateway provisioned, APs surveyed, every device pre-onboarded.'},
      ],
    }}
    cases={['case-spacious', 'case-urban']}
    credentials={['Ubiquiti UEWA','Ubiquiti UWA-Pro','Cat6A bonded subcontractor','Insured & bonded']}
    ctaCopy={{
      h2:'Start a <em>network conversation.</em>',
      lead:'Tell us about the home, the floor plan, and the timeline. We\'ll send a cabling plan within 48 hours.',
      placeholder:'Square footage, # of floors, current pain points, move-in date…',
      onSubmit:()=>navigate('contact'),
    }}
  />;
}

/* ─── CONTACT PAGE ─── */
/* ─── CONTACT ───
   The reference's /contact: hero, one paragraph, a single-column form with
   pill choices, then the location cards. The form posts to Netlify Forms;
   its hidden twin lives in contact.html (scripts/generate-seo-pages.py). */
let CONTACT_PRESET = null;  // a link that opens the form for a reason sets this first
const CF_INQUIRY = ['New project','Service request','Designer or builder'];
const CF_SYSTEMS = ['Lighting control','Shades','Home theater','Audio & video','Security cameras','Networking & Wi-Fi','Permanent lighting','Whole-home automation'];
const CF_CONTACT = ['Phone','Email','Text','No preference'];
const CF_HEARD = ['Google','Client referral','Builder referral','Designer or architect','Social media','Other'];

function FxChoice({name, value, type='radio', checked, onChange}){
  return (
    <label className={'fx-chip'+(checked?' on':'')}>
      <input type={type} name={name} value={value} checked={checked} onChange={onChange}/>
      <span>{value}</span>
    </label>
  );
}

function FxContactForm(){
  const nap = napInfo();
  const [inquiry, setInquiry] = useState(() => {
    const preset = CONTACT_PRESET; CONTACT_PRESET = null;
    if (preset) return preset;
    const q = new URLSearchParams(window.location.search).get('type');
    return q === 'service' ? 'Service request' : q === 'trade' ? 'Designer or builder' : 'New project';
  });
  const [systems, setSystems] = useState([]);
  const [how, setHow] = useState('');
  const [heard, setHeard] = useState('');
  const [status, setStatus] = useState('idle');
  const toggle = (s) => setSystems(xs => xs.includes(s) ? xs.filter(x => x !== s) : [...xs, s]);

  async function submit(e){
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    data.set('systems', systems.join(', '));
    data.set('source_page', window.location.pathname);
    setStatus('sending');
    try {
      const res = await fetch('/', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:new URLSearchParams(data).toString()});
      if (!res.ok) throw new Error('HTTP ' + res.status);
      setStatus('sent');
    } catch(err) { setStatus('error'); }
  }

  if (status === 'sent') return (
    <div className="fx-form-done" role="status">
      <h2 className="fx-d3">Thank you.</h2>
      <p className="fx-lede">Your request is with us and we will come back with next steps. If it cannot wait, call <a href={nap.telHref}>{nap.telephoneDisplay}</a>.</p>
    </div>
  );

  const field = (name, label, type='text', required=false, auto) => (
    <label className="fx-input">
      <span>{label}{required && <b aria-hidden="true"> *</b>}</span>
      <input name={name} type={type} required={required} autoComplete={auto}/>
    </label>
  );
  return (
    <form className="fx-form" name="contact" method="POST" onSubmit={submit}>
      <input type="hidden" name="form-name" value="contact"/>
      <p hidden><label>Leave this empty <input name="bot-field" tabIndex={-1} autoComplete="off"/></label></p>
      {field('first_name','First name','text',true,'given-name')}
      {field('last_name','Last name','text',true,'family-name')}
      {field('email','Email','email',true,'email')}
      {field('phone','Phone','tel',true,'tel')}
      {field('address','Street address','text',false,'street-address')}
      {field('city','City','text',false,'address-level2')}
      {field('zip','ZIP code','text',false,'postal-code')}
      <fieldset className="fx-chips">
        <legend>What is this about?</legend>
        {CF_INQUIRY.map(v => <FxChoice key={v} name="inquiry" value={v} checked={inquiry===v} onChange={()=>setInquiry(v)}/>)}
      </fieldset>
      <fieldset className="fx-chips">
        <legend>Which systems? <small>Choose any</small></legend>
        {CF_SYSTEMS.map(v => <FxChoice key={v} type="checkbox" value={v} checked={systems.includes(v)} onChange={()=>toggle(v)}/>)}
      </fieldset>
      <label className="fx-input">
        <span>How can we help?</span>
        <textarea name="message" rows={5} placeholder="Square footage, architect or builder, timeline, what you want the house to do"/>
      </label>
      <fieldset className="fx-chips">
        <legend>Best way to reach you</legend>
        {CF_CONTACT.map(v => <FxChoice key={v} name="preferred_contact" value={v} checked={how===v} onChange={()=>setHow(v)}/>)}
      </fieldset>
      <fieldset className="fx-chips">
        <legend>How did you hear about us?</legend>
        {CF_HEARD.map(v => <FxChoice key={v} name="heard_from" value={v} checked={heard===v} onChange={()=>setHeard(v)}/>)}
      </fieldset>
      <button type="submit" className="fx-btn" disabled={status==='sending'}>{status==='sending' ? 'Sending…' : 'Send request'}</button>
      {status === 'error' && <p className="fx-form-err" role="alert">That did not go through. Please call <a href={nap.telHref}>{nap.telephoneDisplay}</a> or write to <a href={nap.mailHref}>{nap.email}</a>.</p>}
    </form>
  );
}

function ContactPage({navigate}) {
  const nap = napInfo();
  const cities = geoData().cities || {};
  const byCounty = (county) => Object.keys(cities).filter(id => (cities[id].county || '').includes(county));
  const countyCard = (county, photo) => (
    <div className="fx-panel-card" key={county}>
      <span className="fx-panel-img"><img src={photo} alt={county + ' County'} loading="lazy" decoding="async"/></span>
      <span className="fx-panel-body">
        <h3>{county} County</h3>
        <i className="fx-panel-rule" aria-hidden="true"/>
        <p>{byCounty(county).map((id,i,a) => (
          <React.Fragment key={id}><NavLink page={cityPageId(id)} navigate={navigate} className="fx-inline">{cities[id].name}</NavLink>{i < a.length-1 ? ', ' : ''}</React.Fragment>
        ))}</p>
      </span>
    </div>
  );
  return (
    <div className="page">
      <FxInnerHero kicker="Contact us" h1="Start your project" image={PLACE_PHOTO('sarasota')} alt="Sarasota from the bay"/>

      <section className="fx-band--plain fx-py-md" style={{paddingBottom:32}}>
        <div className="fx-field">
          <div className="fx-intro-prose">
            <p><strong>New build, renovation, or a system you already live with.</strong> Tell us about the house and what you want it to do. If you would rather talk, call <a href={nap.telHref} className="fx-inline">{nap.telephoneDisplay}</a>, {nap.hours}.</p>
          </div>
        </div>
      </section>

      <section className="fx-band--plain" style={{paddingBottom:96}}>
        <FxContactForm/>
      </section>

      <section className="fx-band fx-py-lg">
        <div className="fx-wide">
          <div className="fx-heads" style={{marginBottom:40}}>
            <h2 className="fx-d3">Where we work</h2>
            <p className="fx-lede">One studio in Sarasota, serving Sarasota and Manatee Counties.</p>
          </div>
          <div className="fx-panels fx-panels--static fx-panels--three">
            {countyCard('Sarasota', PLACE_PHOTO('sarasota'))}
            {countyCard('Manatee', PLACE_PHOTO('bradenton'))}
            <div className="fx-panel-card">
              <span className="fx-panel-img"><img src={PHOTOS.handPhone} alt="Calling the studio" loading="lazy" decoding="async"/></span>
              <span className="fx-panel-body">
                <h3>Talk to the studio</h3>
                <i className="fx-panel-rule" aria-hidden="true"/>
                <p><a href={nap.telHref} className="fx-inline">{nap.telephoneDisplay}</a><br/><a href={nap.mailHref} className="fx-inline">{nap.email}</a><br/>{nap.hours}</p>
              </span>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

/* ─── FOOTER ─── */
function Footer({navigate}) {
  const nap = napInfo();
  const cities = geoData().cities || {};
  const groups = [
    {label:'Solutions', links:[
      ['lighting','Lighting'],['shading','Shading'],['theaters','Home theaters'],
      ['audio','Audio & video'],['security','Security'],['networking','Networking'],['automation','Automation'],['permanent-lighting','Permanent outdoor lighting'],
    ]},
    {label:'Studio', links:[
      ['work','Our work'],['about','About'],      ['journal','Journal'],
      ['journal-smart-home-sarasota','Smart home Sarasota'],
      ['luma-smart-home-sarasota','This LUMA, not the others'],
      ['designers','Designers & builders'],
      ['budget-calculator','Budget calculator'],['support','Customer support'],['smart-home-demo','3D demo'],['contact','Contact'],
    ]},
    {label:'Service areas', links:[
      ['service-areas','All service areas'],
      ...Object.keys(cities).map(id=>[cityPageId(id), cities[id].name]),
    ]},
  ];
  const go = navigate || ((p)=>{ window.location.href = pathFor(p); });
  return (
    <footer className="footer">
      <div className="footer-brand">
        <NavLink page="home" navigate={go} className="footer-logo">LUMA Smart Home</NavLink>
        <p className="footer-nap">
          <span className="footer-nap-name">LUMA Smart Home</span><br/>
          Sarasota, Florida<br/>
          <a href={nap.mapsUrl} target="_blank" rel="noopener noreferrer">{nap.mapsLabel}</a>
        </p>
        <p>Residential technology studio. Lighting, shades, audio, security, and Wi-Fi for Gulf Coast homes.</p>
        <p>
          <a href={nap.telHref}>{nap.telephoneDisplay}</a><br/>
          <a href={nap.mailHref}>{nap.email}</a><br/>
          <span>{nap.hours}</span>
        </p>
      </div>
      {groups.map(g=>(
        <nav key={g.label} className="footer-col" aria-label={g.label}>
          <strong>{g.label}</strong>
          {g.links.map(([page,label])=>(
            <NavLink key={page} page={page} navigate={go}>{label}</NavLink>
          ))}
        </nav>
      ))}
      <div className="footer-meta">
        <span>© 2026 LUMA Smart Home · Sarasota, FL</span>
        <span>Serving {nap.area}</span>
      </div>
    </footer>
  );
}

/* ─── BUDGET CALCULATOR PAGE ─── */
const BUDGET_TIERS = [
  {tier:'Foundation',  range:'$45k – $85k',   sqft:'2,500 – 4,000 sq ft',
   includes:['Lutron RadioRA 3 lighting','Structured cabling + Wi-Fi 6','4–6 cameras + on-prem NVR','One keypad zone, one app']},
  {tier:'Signature',   range:'$120k – $220k', sqft:'4,000 – 7,500 sq ft', featured:true,
   includes:['Lutron HomeWorks lighting + shades','Whole-home audio (8–12 zones)','12+ cameras, perimeter alarm','Crestron / Savant control','Theater or media room']},
  {tier:'Estate',      range:'$300k+',        sqft:'7,500+ sq ft / multi-building',
   includes:['Multi-residence Crestron','Outdoor audio + dock systems','24+ cameras, PTZ + analytics','Dedicated cinema room','Two-year on-call service']},
];

/* ─── DETAILED BUDGET WIZARD ─── */
/* Range estimator. Each option contributes [low, high] to a category bucket.
   Calibrated for Gulf Coast luxury market — slightly above the national HTA reference,
   reflects union labor + island access fees + post-hurricane site conditions.        */
const WIZARD_STEPS = [
  {id:'home',   label:'The home'},
  {id:'enter',  label:'Entertainment'},
  {id:'safety', label:'Security & Wi-Fi'},
  {id:'ctrl',   label:'Lighting & control'},
  {id:'recap',  label:'Your range'},
];

function pricePerSqft(sqft, perLow, perHigh){
  return [Math.round(sqft*perLow), Math.round(sqft*perHigh)];
}

function DetailedBudgetWizard(){
  const [step, setStep] = useState(0);
  const [a, setA] = useState({
    sqft: 5000,
    wiring: 'existing',
    musicRooms: '4-7',
    tvCount: '4-7',
    videoMatrix: 'no',
    theater: 'none',
    surround: 'enhanced',
    alarm: 'yes',
    cameras: '4-7',
    wifi: 'performance',
    lighting: 'main-ext',
    shades: 8,
    appUnify: 'single',
    hvac: 'yes',
    voice: 'yes',
  });
  const set = (k,v)=>setA(s=>({...s,[k]:v}));

  // ── pricing tables (Gulf Coast calibration) ──
  const wiringRange = {
    'existing':  ['Already wired',           [0,0]],
    'partial':   ['Some new runs needed',    pricePerSqft(a.sqft, 0.6, 1.6)],
    'old':       ['Old wiring · full rewire',pricePerSqft(a.sqft, 1.4, 3.6)],
    'newbuild':  ['New construction · all new',pricePerSqft(a.sqft, 1.6, 3.4)],
  };
  const musicRoomRange = {
    'none':  ['No whole-home audio',[0,0]],
    '1-3':   ['1–3 rooms',          [3500, 9500]],
    '4-7':   ['4–7 rooms',          [9500, 26000]],
    '8-14':  ['8–14 rooms',         [21000, 58000]],
    '15+':   ['15+ rooms · indoor + lanai',[42000, 130000]],
  };
  const tvRange = {
    'none':  ['No TVs to install',[0,0]],
    '1-3':   ['1–3 TVs',          [1800, 5500]],
    '4-7':   ['4–7 TVs',          [5500, 16000]],
    '8-14':  ['8–14 TVs',         [12000, 36000]],
    '15+':   ['15+ TVs',          [26000, 80000]],
  };
  const videoMatrix = {
    'no':  ['Each TV stays standalone',[0,0]],
    'yes': ['Centralized video matrix',[8500, 32000]],
  };
  const theaterRange = {
    'none':       ['No dedicated theater',[0,0]],
    'coastal':    ['Coastal · 4–6 seats', [11000, 26000]],
    'resident':   ['Resident · 6–8 seats',[27000, 56000]],
    'estate':     ['Estate · 8–12 seats', [58000, 130000]],
    'cinema':     ['Cinema · reference room',[140000, 290000]],
  };
  const surroundRange = {
    'none':      ['No surround room',[0,0]],
    'soundbar':  ['Soundbar + sub',  [900, 3200]],
    'enhanced':  ['Receiver-based 5.1 / 7.1',[3500, 11500]],
    'perform':   ['Atmos 9-spkr performance',[12000, 24000]],
    'reference': ['Atmos 11-spkr reference',[24000, 48000]],
  };
  const alarmRange = {
    'no':  ['Skip burglar alarm', [0,0]],
    'yes': ['On-prem alarm · no monthly',[1800, 5500]],
  };
  const camerasRange = {
    'none':  ['No cameras',     [0,0]],
    '1-3':   ['1–3 cameras',    [2400, 5200]],
    '4-7':   ['4–7 cameras',    [4800, 12500]],
    '8-14':  ['8–14 cameras',   [10500, 26000]],
    '15+':   ['15+ cameras · perimeter',[22000, 55000]],
  };
  const wifiRange = {
    'none':       ['Use existing router',[0,0]],
    'consumer':   ['Consumer mesh',     [800, 1700]],
    'performance':['Performance UniFi', [2600, 5400]],
    'enterprise': ['Enterprise · multi-AP',[6500, 24000]],
  };
  const lightingRange = {
    'none':     ['Conventional switches',[0,0]],
    'few':      ['A few rooms only',     [1400, 3200]],
    'main-ext': ['Main areas + exterior',[3800, 9500]],
    'whole':    ['Whole house + landscape',[12000, 38000]],
  };
  const shadesRange = (() => {
    const n = Math.max(0, Math.min(80, Number(a.shades)||0));
    return ['Motorized shades · '+n, [Math.round(n*900), Math.round(n*1900)]];
  })();
  const unifyRange = {
    'none':   ['No unified app',     [0,0]],
    'multi':  ['Multiple vendor apps',[0,0]],
    'single': ['Single LUMA app',    [6500, 16500]],
  };
  const hvacRange = {
    'no':  ['Standalone thermostats',[0,0]],
    'yes': ['HVAC integrated to app',[900, 2400]],
  };
  const voiceRange = {
    'no':  ['No voice control',[0,0]],
    'yes': ['Voice control layer',[600, 1900]],
  };

  const lines = [
    {cat:'Pre-wire & infrastructure', sub:wiringRange[a.wiring][0],  rng:wiringRange[a.wiring][1]},
    {cat:'Whole-home music',          sub:musicRoomRange[a.musicRooms][0], rng:musicRoomRange[a.musicRooms][1]},
    {cat:'Televisions',               sub:tvRange[a.tvCount][0],     rng:tvRange[a.tvCount][1]},
    {cat:'Video distribution',        sub:videoMatrix[a.videoMatrix][0], rng:videoMatrix[a.videoMatrix][1]},
    {cat:'Dedicated theater',         sub:theaterRange[a.theater][0],rng:theaterRange[a.theater][1]},
    {cat:'Media-room sound',          sub:surroundRange[a.surround][0],rng:surroundRange[a.surround][1]},
    {cat:'Alarm system',              sub:alarmRange[a.alarm][0],    rng:alarmRange[a.alarm][1]},
    {cat:'Cameras & NVR',             sub:camerasRange[a.cameras][0],rng:camerasRange[a.cameras][1]},
    {cat:'Network & Wi-Fi',           sub:wifiRange[a.wifi][0],      rng:wifiRange[a.wifi][1]},
    {cat:'Lighting control',          sub:lightingRange[a.lighting][0],rng:lightingRange[a.lighting][1]},
    {cat:'Motorized shading',         sub:shadesRange[0],            rng:shadesRange[1]},
    {cat:'Unified control app',       sub:unifyRange[a.appUnify][0], rng:unifyRange[a.appUnify][1]},
    {cat:'HVAC integration',          sub:hvacRange[a.hvac][0],      rng:hvacRange[a.hvac][1]},
    {cat:'Voice control',             sub:voiceRange[a.voice][0],    rng:voiceRange[a.voice][1]},
  ];
  const totalLow  = lines.reduce((s,l)=>s+l.rng[0], 0);
  const totalHigh = lines.reduce((s,l)=>s+l.rng[1], 0);
  // Add base design + project management overhead (15% of mid)
  const base = Math.round((totalLow+totalHigh)/2 * 0.15);
  const finalLow  = totalLow + base;
  const finalHigh = totalHigh + Math.round(base * 1.4);
  const fmt = n => n>=1000 ? '$'+Math.round(n/1000)+'k' : '$'+n;

  const Pill = ({k,v,label,group}) => (
    <button type="button" onClick={()=>set(group, k)}
      className={'bw-option'+(a[group]===k?' selected':'')}>{label||v}</button>
  );
  const Stack = ({k,group,title,sub}) => (
    <button type="button" onClick={()=>set(group, k)}
      className={'bw-option'+(a[group]===k?' selected':'')}><strong>{title}</strong><span>{sub}</span></button>
  );

  return (
    <section className="th-section--cream" id="detailed-wizard">
      <div className="th-section--cream-inner">
        <div className="sec-label">Detailed estimator</div>
        <h2 className="sec-title">Walk through it <em>like we would.</em></h2>
        <p className="sec-body">Twelve quick questions, organized the way we'd ask them on a property walk-through. The range adjusts as you answer. No email required to see the number.</p>

        <div className="bw-shell">
          {/* progress */}
          <div className="bw-step-label"><span>Step {Math.min(step+1,WIZARD_STEPS.length)} of {WIZARD_STEPS.length}</span><strong>{WIZARD_STEPS[step].label}</strong></div>
          <div className="bw-progress">
            {WIZARD_STEPS.map((s,i)=>(
              <span key={s.id} className={'bw-step-dot'+(i<step?' done':i===step?' active':'')}/>
            ))}
          </div>

          {/* STEP 0 — HOME */}
          {step===0 && <>
            <div className="bw-q">
              <div className="bw-q-label">How large is the residence?</div>
              <div className="bw-q-help">Heated/cooled square footage. Lanais and detached structures we'll cover separately on the proposal.</div>
              <div style={{display:'flex',alignItems:'center',gap:14,flexWrap:'wrap'}}>
                <input type="number" className="bw-input" value={a.sqft} step="100" min="1500" max="25000"
                  onChange={e=>set('sqft', Math.max(1500, Math.min(25000, +e.target.value||0)))} />
                <span style={{fontSize:13,color:'var(--mid)'}}>sq ft</span>
                <input type="range" min="1500" max="20000" step="250" value={a.sqft}
                  onChange={e=>set('sqft', +e.target.value)} style={{flex:1,minWidth:200,accentColor:'#C57238'}}/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">What's the wiring situation?</div>
              <div className="bw-q-help">Pre-wire is the single biggest swing factor. Honest input here keeps the range tight.</div>
              <div className="bw-option-stack" style={{gridTemplateColumns:'1fr 1fr'}}>
                <Stack k="existing" group="wiring" title="Already wired" sub="House has structured cabling and we just integrate."/>
                <Stack k="partial"  group="wiring" title="Some new runs" sub="Add a few drops to existing infrastructure."/>
                <Stack k="old"      group="wiring" title="Old wiring, full rewire" sub="Pull and replace through finished walls."/>
                <Stack k="newbuild" group="wiring" title="New construction" sub="Coordinated rough-in with the builder."/>
              </div>
            </div>
          </>}

          {/* STEP 1 — ENTERTAINMENT */}
          {step===1 && <>
            <div className="bw-q">
              <div className="bw-q-label">Whole-home music — how many rooms?</div>
              <div className="bw-q-help">Count interior rooms + outdoor zones (lanai, pool, dock).</div>
              <div className="bw-options">
                <Pill k="none" group="musicRooms" label="None"/>
                <Pill k="1-3" group="musicRooms" label="1–3"/>
                <Pill k="4-7" group="musicRooms" label="4–7"/>
                <Pill k="8-14" group="musicRooms" label="8–14"/>
                <Pill k="15+" group="musicRooms" label="15+"/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">How many televisions across the home?</div>
              <div className="bw-options">
                <Pill k="none" group="tvCount" label="None"/>
                <Pill k="1-3" group="tvCount" label="1–3"/>
                <Pill k="4-7" group="tvCount" label="4–7"/>
                <Pill k="8-14" group="tvCount" label="8–14"/>
                <Pill k="15+" group="tvCount" label="15+"/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">Centralize sources to one rack?</div>
              <div className="bw-q-help">Cable boxes, Apple TVs, and security feeds in one closet — viewable from any TV.</div>
              <div className="bw-options">
                <Pill k="yes" group="videoMatrix" label="Yes, video matrix"/>
                <Pill k="no" group="videoMatrix" label="No, keep separate"/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">Dedicated theater room?</div>
              <div className="bw-q-help">Hardware + calibration only — seating and architectural build-out priced separately.</div>
              <div className="bw-option-stack" style={{gridTemplateColumns:'1fr 1fr'}}>
                <Stack k="none"     group="theater" title="No theater" sub="Skip for now."/>
                <Stack k="coastal"  group="theater" title="Coastal · $11k–$26k" sub="4–6 seats, 100″–120″ screen, in-wall speakers."/>
                <Stack k="resident" group="theater" title="Resident · $27k–$56k" sub="6–8 seats, brighter projector, dedicated processor."/>
                <Stack k="estate"   group="theater" title="Estate · $58k–$130k" sub="8–12 seats, 12–15ft screen, theater-grade sound."/>
                <Stack k="cinema"   group="theater" title="Cinema · $140k–$290k" sub="Reference room: acoustics, riser, 4K laser."/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">Surround sound in a media room?</div>
              <div className="bw-options">
                <Pill k="none" group="surround" label="None"/>
                <Pill k="soundbar" group="surround" label="Soundbar + sub"/>
                <Pill k="enhanced" group="surround" label="5.1 / 7.1 receiver"/>
                <Pill k="perform" group="surround" label="9-spkr Atmos"/>
                <Pill k="reference" group="surround" label="11-spkr reference"/>
              </div>
            </div>
          </>}

          {/* STEP 2 — SAFETY */}
          {step===2 && <>
            <div className="bw-q">
              <div className="bw-q-label">Burglar alarm?</div>
              <div className="bw-q-help">We install on-prem (no monthly contract). Optional cellular monitoring later.</div>
              <div className="bw-options">
                <Pill k="yes" group="alarm" label="Yes"/>
                <Pill k="no"  group="alarm" label="No"/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">How many cameras?</div>
              <div className="bw-q-help">A typical Gulf Coast home runs 6–12: front door, drive, sides, lanai, pool, dock.</div>
              <div className="bw-options">
                <Pill k="none" group="cameras" label="None"/>
                <Pill k="1-3" group="cameras" label="1–3"/>
                <Pill k="4-7" group="cameras" label="4–7"/>
                <Pill k="8-14" group="cameras" label="8–14"/>
                <Pill k="15+" group="cameras" label="15+ · perimeter"/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">Wi-Fi & networking grade?</div>
              <div className="bw-q-help">Network is the foundation. Underspec'd Wi-Fi sinks every other system.</div>
              <div className="bw-option-stack" style={{gridTemplateColumns:'1fr 1fr'}}>
                <Stack k="none"        group="wifi" title="Use existing" sub="Keep your current router. Risky for whole-home automation."/>
                <Stack k="consumer"    group="wifi" title="Consumer mesh" sub="Eero / Orbi class · OK for under 3,500 sq ft."/>
                <Stack k="performance" group="wifi" title="Performance UniFi" sub="Pro AP + switching, our common spec."/>
                <Stack k="enterprise"  group="wifi" title="Enterprise" sub="Multi-AP, segmented VLANs, dual-WAN failover."/>
              </div>
            </div>
          </>}

          {/* STEP 3 — CONTROL */}
          {step===3 && <>
            <div className="bw-q">
              <div className="bw-q-label">Lighting control coverage?</div>
              <div className="bw-option-stack" style={{gridTemplateColumns:'1fr 1fr'}}>
                <Stack k="none"     group="lighting" title="Conventional switches" sub="Manual everything. We'll skip the layer."/>
                <Stack k="few"      group="lighting" title="A few rooms" sub="Living, primary, key exterior fixtures."/>
                <Stack k="main-ext" group="lighting" title="Main + exterior" sub="Most living areas, lanai, landscape lights."/>
                <Stack k="whole"    group="lighting" title="Whole house + landscape" sub="Every keypad and dimmer, including landscape DMX."/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">Motorized shades — how many windows?</div>
              <div className="bw-q-help">Round-number guess is fine. Lanai screens count if you'd like them automated.</div>
              <div style={{display:'flex',alignItems:'center',gap:14,flexWrap:'wrap'}}>
                <input type="number" className="bw-input" value={a.shades} min="0" max="80"
                  onChange={e=>set('shades', Math.max(0,Math.min(80, +e.target.value||0)))}/>
                <span style={{fontSize:13,color:'var(--mid)'}}>shades</span>
                <input type="range" min="0" max="40" step="1" value={a.shades}
                  onChange={e=>set('shades', +e.target.value)} style={{flex:1,minWidth:200,accentColor:'#C57238'}}/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">Single app or multiple apps?</div>
              <div className="bw-q-help">Single app means lighting, music, locks, cameras, climate — all unified. Costs more to integrate, but daily life is dramatically simpler.</div>
              <div className="bw-options">
                <Pill k="single" group="appUnify" label="Single unified app"/>
                <Pill k="multi"  group="appUnify" label="Multiple vendor apps"/>
                <Pill k="none"   group="appUnify" label="No app control"/>
              </div>
            </div>
            <div className="bw-q">
              <div className="bw-q-label">HVAC + voice control?</div>
              <div style={{display:'flex',gap:24,flexWrap:'wrap'}}>
                <div>
                  <div className="bw-q-help" style={{margin:0,marginBottom:8}}>Thermostats in the app</div>
                  <div className="bw-options">
                    <Pill k="yes" group="hvac" label="Yes"/>
                    <Pill k="no"  group="hvac" label="No"/>
                  </div>
                </div>
                <div>
                  <div className="bw-q-help" style={{margin:0,marginBottom:8}}>Voice (Alexa / Google / Apple)</div>
                  <div className="bw-options">
                    <Pill k="yes" group="voice" label="Yes"/>
                    <Pill k="no"  group="voice" label="No"/>
                  </div>
                </div>
              </div>
            </div>
          </>}

          {/* STEP 4 — RECAP */}
          {step===4 && <>
            <div className="bw-q">
              <div className="bw-q-label">Your estimated range</div>
              <div className="bw-q-help">Indicative only — design, hardware, installation, and one year of service all in. Final number depends on hardware tier, finish quality, site conditions, and integration depth. We'll send a real proposal within 48 hours of a property walk-through.</div>
            </div>
            <div className="bw-result">
              <div className="bw-result-row"><span>Category</span><span className="bw-rng">Low</span><span className="bw-rng">High</span></div>
              {lines.filter(l=>l.rng[1]>0).map(l=>(
                <div key={l.cat} className="bw-result-row">
                  <div className="bw-cat">{l.cat}<div className="bw-cat-sub">{l.sub}</div></div>
                  <div className="bw-rng">{fmt(l.rng[0])}</div>
                  <div className="bw-rng">{fmt(l.rng[1])}</div>
                </div>
              ))}
              <div className="bw-result-row">
                <div className="bw-cat">Design + project management<div className="bw-cat-sub">~15% of hardware + labor</div></div>
                <div className="bw-rng">{fmt(base)}</div>
                <div className="bw-rng">{fmt(Math.round(base*1.4))}</div>
              </div>
              <div className="bw-result-row total">
                <span>Total range</span>
                <div className="bw-rng">{fmt(finalLow)}</div>
                <div className="bw-rng">{fmt(finalHigh)}</div>
              </div>
            </div>
          </>}

          {/* nav */}
          <div className="bw-nav">
            <button type="button" className="btn-ghost" onClick={()=>setStep(s=>Math.max(0,s-1))} disabled={step===0} style={step===0?{opacity:.4,cursor:'default'}:{}}>← Back</button>
            <span className="bw-running">Running estimate <strong>{fmt(finalLow)} – {fmt(finalHigh)}</strong></span>
            {step<WIZARD_STEPS.length-1
              ? <button type="button" className="btn-solid" onClick={()=>setStep(s=>Math.min(WIZARD_STEPS.length-1, s+1))}>Continue →</button>
              : <button type="button" className="btn-solid" onClick={()=>{const el=document.querySelector('#detailed-wizard');if(el)el.scrollIntoView({behavior:'smooth'});setTimeout(()=>setStep(0),200);}}>Start over</button>}
          </div>
        </div>
      </div>
    </section>
  );
}

/* ==========================================================================
   INNER PAGES — the reference's About, Support and Work, piece for piece.
   The copy is the studio's own, carried over from the pages these replace;
   nothing is added that the studio has not said before.
   ========================================================================== */
const FX_ICON_PATHS = {
  ticket:  <><path d="M3 8a2 2 0 0 0 2-2h14a2 2 0 0 0 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 0-2 2H5a2 2 0 0 0-2-2v-2a2 2 0 0 0 0-4Z"/><path d="M14 6v12" strokeDasharray="2 2.5"/></>,
  plan:    <><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 14h3M8 17h6"/></>,
  phone:   <path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/>,
  open:    <><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 7.6-1.7"/></>,
  network: <><rect x="3" y="4" width="18" height="6" rx="1.5"/><rect x="3" y="14" width="18" height="6" rx="1.5"/><path d="M7 7h.01M7 17h.01M11 7h.01M11 17h.01"/></>,
  lines:   <path d="M9 6h12M9 12h12M9 18h12M4 6h.01M4 12h.01M4 18h.01"/>,
  plans:   <><path d="M4 20l3.5-1 11-11-2.5-2.5-11 11L4 20Z"/><path d="M14.5 7.5l2.5 2.5M3 3h7v4"/></>,
  clock:   <><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></>,
  sun:     <><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></>,
  people:  <><circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0M16 5a3 3 0 0 1 0 6M21 20a6 6 0 0 0-4-5.7"/></>,
  shield:  <><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3Z"/><path d="M9 12l2 2 4-4"/></>,
  gift:    <><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M5 12v9h14v-9M12 8v13M12 8H8.5a2.5 2.5 0 1 1 0-5C11 3 12 8 12 8Zm0 0h3.5a2.5 2.5 0 1 0 0-5C13 3 12 8 12 8Z"/></>,
};
function FxIcon({name}){
  return <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">{FX_ICON_PATHS[name]}</svg>;
}

/* their "elegant tabs": a centred row of plain labels over one panel */
function FxTabs({tabs}){
  const [on, setOn] = useState(0);
  return (
    <div className="fx-tabs">
      <div className="fx-tabs-bar" role="tablist">
        {tabs.map((t,i) => (
          <button key={t.label} type="button" role="tab" aria-selected={on===i}
            className={'fx-tab'+(on===i?' on':'')} onClick={()=>setOn(i)}>{t.label}</button>
        ))}
      </div>
      <div className="fx-tabs-panel" role="tabpanel">{tabs[on].body}</div>
    </div>
  );
}

/* the values panel from the service shell, on its own */
function FxValuesPanel({h2, lead, items}){
  return (
    <section className="fx-values fx-values--plain">
      <div className="fx-wide">
        <div className="fx-values-grid">
          <div className="fx-values-copy" style={{gap:16}}>
            <h2 className="fx-d3" style={{fontSize:'clamp(28px,2.4vw,32px)'}}>{h2}</h2>
            {lead && <div className="fx-lede"><p>{lead}</p></div>}
          </div>
          <div className="fx-values-list">
            {items.map(it => (
              <div key={it.title} className="fx-value">
                <span className="fx-tile" aria-hidden="true"><FxIcon name={it.icon}/></span>
                <span><strong>{it.title}</strong><p>{it.desc}</p></span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

/* photo cards, the reference's big-panels */
function FxPhotoPanels({h2, lead, items, band}){
  return (
    <section className={(band ? 'fx-band' : 'fx-band--plain') + ' fx-py-lg'}>
      <div className="fx-wide">
        {h2 && <div className="fx-heads" style={{marginBottom:40}}><h2 className="fx-d3">{h2}</h2>{lead && <p className="fx-lede">{lead}</p>}</div>}
        <div className={'fx-panels fx-panels--static' + (items.length === 3 ? ' fx-panels--three' : '')}>
          {items.map(c => (
            <div key={c.title} className="fx-panel-card">
              <span className="fx-panel-img"><img src={c.photo} alt={c.alt || c.title} loading="lazy" decoding="async"/></span>
              <span className="fx-panel-body">
                {c.kicker && <span className="fx-panel-kicker">{c.kicker}</span>}
                <h3>{c.title}</h3>
                <i className="fx-panel-rule" aria-hidden="true"/>
                <p>{c.body}</p>
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* their image-and-text block: a rounded teal card, photo left */
function FxImageText({photo, alt, h2, body, children}){
  return (
    <section className="fx-band--plain fx-py-lg">
      <div className="fx-wide">
        <div className="fx-imgtext">
          <img src={photo} alt={alt} loading="lazy" decoding="async"/>
          <div className="fx-imgtext-copy">
            <h2 className="fx-d3">{h2}</h2>
            <div className="fx-lede"><p>{body}</p></div>
            {children}
          </div>
        </div>
      </div>
    </section>
  );
}

function FxFaqBlock({items, h2='Frequently asked questions'}){
  return (
    <section className="fx-band--plain fx-py-lg">
      <div className="fx-field">
        <div className="fx-heads" style={{marginBottom:32}}><h2 className="fx-d3">{h2}</h2></div>
        <div className="fx-faq">
          {items.map((q,i) => (
            <details key={q.q} className="fx-faq-item" open={i===0}>
              <summary>{q.q}<i aria-hidden="true">+</i></summary>
              <p>{q.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ─── ABOUT ─── */
const ABOUT_PRINCIPLES = [
  {icon:'open',    title:'Open over proprietary',  desc:'Lutron, Ubiquiti, Somfy, Sonos. Professional platforms with documented APIs. No dealer lock: your home stays yours if you ever leave us.'},
  {icon:'network', title:'Network first',          desc:'Every project begins with the network. Wired backbone, segmented Wi-Fi, on-prem control. Everything else fails without it.'},
  {icon:'lines',   title:'Pricing in lines',       desc:'Every device, every labor hour. No bundled mysteries, no surprise change orders.'},
  {icon:'plans',   title:'Design with architects', desc:'We show up early in the build, not after drywall. Integration happens in plans, not in patches.'},
  {icon:'clock',   title:'Stay after turnover',    desc:'Twelve months of service bundled. Quarterly check-ins. Quiet system updates.'},
  {icon:'sun',     title:'Respect the hour',       desc:'Technology should disappear into the day. The best system is the one you stop noticing.'},
];

const ABOUT_PHASES = [
  {kicker:'Step 01', title:'Walk-through', photo:PHOTOS.heroDesigners, alt:'A finished living room',
   body:'60–90 minutes on site. We listen first, then sketch the system layers. Free, no obligation.'},
  {kicker:'Step 02', title:'Proposal', photo:PHOTOS.tradeFlatlay, alt:'Plans and finishes on a desk',
   body:'A line-item document within two business days. Every device priced, every hour counted, scope locked.'},
  {kicker:'Step 03', title:'Install', photo:PHOTOS.lumaVan, alt:'The LUMA van on a job site',
   body:'Coordinated with the builder, electrician, and AV trades. Daily clean-up, weekly progress photos.'},
  {kicker:'Step 04', title:'Service', photo:PHOTOS.handPhone, alt:'Adjusting the house from a phone',
   body:'Twelve months of priority service included. Same technicians, same phone number.'},
];

const ABOUT_FAQ = [
  {q:'What does LUMA Smart Home do?',
   a:'We design, install and look after lighting control, motorized shades, audio and video, home theaters, security cameras and networks in private homes.'},
  {q:'Where do you work?',
   a:'Sarasota and Manatee Counties: Sarasota, Bradenton, Lakewood Ranch, Venice, Siesta Key, Longboat Key, Anna Maria Island and Palmetto.'},
  {q:'When should we bring you in?',
   a:'As early as the plans. We would rather mark up drawings than patch finished walls, so the wiring goes in at rough-in, not after drywall.'},
  {q:'Who owns the system when it is done?',
   a:'You do. We build on open, documented platforms, so there is no dealer lock and the house stays yours if you ever change installers.'},
  {q:'What happens after the install?',
   a:'Service is part of the job: remote tuning, measured updates, and a technician who already knows the house. LUMA Care plans are on the Customer Support page.'},
];

function AboutPage({navigate}) {
  return (
    <div className="page">
      <FxInnerHero kicker="About us" h1="We build homes around the Gulf Coast hour." image={PHOTOS.heroAbout} alt="Sarasota marina"/>

      <section className="fx-band--plain fx-py-md">
        <div className="fx-field">
          <div className="fx-intro-prose">
            <p><strong>LUMA is a residential technology studio based in Sarasota, Florida.</strong> We integrate lighting, shading, security, audio, and networking into homes that feel effortless, and we stay engaged long after turnover, because that is when most integrators disappear.</p>
          </div>
        </div>
      </section>

      <section className="fx-band--plain" style={{paddingBottom:96}}>
        <div className="fx-wide">
          <FxTabs tabs={[
            {label:'What we believe', body:(
              <>
                <p className="fx-tabs-lead">Six principles we do not bend on, from the first walk-through to the last service call.</p>
                <div className="fx-iconrow">
                  {ABOUT_PRINCIPLES.map(p => (
                    <div key={p.title} className="fx-iconrow-item">
                      <span className="fx-tile" aria-hidden="true"><FxIcon name={p.icon}/></span>
                      <strong>{p.title}</strong>
                      <p>{p.desc}</p>
                    </div>
                  ))}
                </div>
              </>
            )},
            {label:'Our story', body:(
              <div className="fx-tabs-prose">
                <h3 className="fx-d3">A different kind of integrator</h3>
                <p>LUMA was founded on a simple observation: the Gulf Coast smart-home market is crowded with dealer-locked systems, opaque pricing, and integrators who vanish after turnover. Homeowners pay for premium gear and receive a black box they can't manage, can't modify, and can't get serviced without waiting weeks for a call back.</p>
                <p>We started LUMA to flip that model. Open platforms, so you own your system. Line-item proposals, so you know exactly what you're paying for. Service bundled into every project, and a studio that stays with your home for years, not weeks.</p>
              </div>
            )},
          ]}/>
        </div>
      </section>

      <FxCallout kicker="What we believe" h2="The best smart home is the one you stop noticing."
        body="The windows are already where they should be. The music is already at dinner volume. The sun is still doing the work."
        actions={false} navigate={navigate}/>

      <FxPhotoPanels h2="Four phases, one studio." lead="How a project runs, from the first visit to the years after." items={ABOUT_PHASES}/>

      <FxImageText photo={PHOTOS.tradeFlatlay} alt="Plans, finishes and a keypad on a designer's desk"
        h2="Working on a new build?"
        body="We work alongside interior designers, architects, and custom builders: marked-up plans, a rough-in package for the electrician, and one proposal your client can read.">
        <NavLink page="designers" navigate={navigate} className="fx-btn">Designers &amp; builders</NavLink>
      </FxImageText>

      <FxFaqBlock items={ABOUT_FAQ}/>

      <FxCta navigate={navigate}
        title="Let's meet at your property."
        body="First visit is free. 60–90 minutes on site, no obligation. You'll walk away knowing what a LUMA-tuned home could look like, whether we build it together or not."/>
    </div>
  );
}

/* ─── CUSTOMER SUPPORT (LUMA Care) ───
   The reference's /support and /support/247-support on one page: three
   ways in, how support works, the plans, a closing callout. */
const CARE_PLANS = [
  {tier:'Shoreline', price:75, tag:'For seasonal residences and lock-and-leave homes',
   bullets:[
     'Weekday remote diagnostics (Mon–Sat)',
     'Secure messaging and email within one business day',
     'Firmware and patch guidance for gear we installed',
     '10% off standard on-site service visits',
   ]},
  {tier:'Channel', price:119, tag:'For full-time Gulf Coast homes',
   bullets:[
     'Everything in Shoreline',
     'Priority queue: same team, faster call-backs',
     'Proactive log review when vendors ship updates',
     'Remote scene and keypad tweaks after you move in',
     '20% off standard on-site service visits',
   ]},
  {tier:'Open Gulf', price:189, tag:'For estates and homes where downtime is not an option',
   bullets:[
     'Everything in Channel',
     'Extended-hours phone line to the service desk',
     'Quarterly remote check on network, storage and backups',
     'One annual on-site visit (up to 90 min)',
     'Same-day on-site dispatch when available',
     '30% off standard on-site service visits',
   ]},
];

function ServiceSupportPage({navigate}) {
  const nap = napInfo();
  const service = () => { CONTACT_PRESET = 'Service request'; };
  const toPlans = (e) => { e.preventDefault(); const el = document.getElementById('plans'); if (el) el.scrollIntoView({behavior:'smooth'}); };
  return (
    <div className="page">
      <FxInnerHero kicker="Customer support" h1="Keep the house effortless, long after install." image={lu('/assets/video/luma-care-poster.jpg')} alt="A LUMA technician walking a homeowner through the control app"/>

      <section className="fx-band--plain fx-py-lg">
        <div className="fx-wide">
          <div className="fx-heads" style={{marginBottom:48}}>
            <h2 className="fx-d3">Support you can count on</h2>
            <p className="fx-lede">Smart homes age like boats: sun, salt, and software updates never stop. LUMA Care is ongoing stewardship for the systems we designed, by technicians who already know your rack, your scenes, and how your family uses the place.</p>
          </div>
          <div className="fx-icards">
            <NavLink page="contact" navigate={navigate} onNavigate={service} className="fx-icard">
              <span className="fx-icard-tile"><FxIcon name="ticket"/></span>
              <small>Submit a request</small><h3>Request service</h3>
              <p>Tell us what feels wrong: a scene, a shade, a camera, Wi-Fi in the guest wing. Photos and short videos help.</p>
            </NavLink>
            <a href="#plans" onClick={toPlans} className="fx-icard">
              <span className="fx-icard-tile"><FxIcon name="plan"/></span>
              <small>LUMA Care</small><h3>View service plans</h3>
              <p>Three monthly plans, from ${CARE_PLANS[0].price} a month. Month-to-month after the first 90 days.</p>
            </a>
            <a href={nap.telHref} className="fx-icard">
              <span className="fx-icard-tile"><FxIcon name="phone"/></span>
              <small>Service line</small><h3>{nap.telephoneDisplay}</h3>
              <p>{nap.hours}. Or write to {nap.email}.</p>
            </a>
          </div>
        </div>
      </section>

      <FxPhotoPanels band h2="How we support you"
        lead="Wi-Fi maps change, cameras need cleaning and re-aiming, shade limits shift, and vendors ship updates that deserve a measured rollout. When something drifts, we realign it."
        items={[
          {kicker:'Step 01', title:'You signal us', photo:PHOTOS.handPhone, alt:'Reporting an issue from a phone',
           body:'Call, email, or text the service line and describe what feels wrong. Photos and quick videos welcome.'},
          {kicker:'Step 02', title:'We diagnose', photo:PHOTOS.networkingRack, alt:'A documented equipment rack',
           body:'Remote first: we connect to the network you own, pull logs with your consent, and reproduce the issue. If it is hardware, we schedule a visit with parts on the truck.'},
          {kicker:'Step 03', title:'We close the loop', photo:PHOTOS.lumaVan, alt:'The LUMA van on a job site',
           body:'Fix, verify, and leave notes in your file so the next technician, five years from now, isn’t guessing.'},
        ]}/>

      <section className="fx-plans" id="plans">
        <div className="fx-wide">
          <div className="fx-heads" style={{marginBottom:48}}>
            <h2 className="fx-d3">LUMA Care plans</h2>
            <p className="fx-lede">Month-to-month after the first 90 days, cancel anytime. Prices are for single-family homes in Sarasota and Manatee Counties; estates over 12,000 sq ft are quoted individually.</p>
          </div>
          <div className="fx-plans-grid">
            {CARE_PLANS.map(p => (
              <div key={p.tier} className="fx-plan">
                <h3>{p.tier}</h3>
                <div className="fx-plan-price">${p.price}<span>/mo</span></div>
                <p className="fx-plan-tag">{p.tag}</p>
                <ul className="fx-checks">{p.bullets.map(b => <li key={b}>{b}</li>)}</ul>
                <NavLink page="contact" navigate={navigate} onNavigate={service} className="fx-plan-link">Start {p.tier} <i aria-hidden="true">→</i></NavLink>
              </div>
            ))}
          </div>
          <p className="fx-plans-note">Membership covers planning, remote labor, and coordination. Hardware, truck rolls, and parts are invoiced separately at the discounted rates above. LUMA Home Systems LLC, Sarasota: Florida licensed low-voltage contractor, insured for residential and light commercial work.</p>
        </div>
      </section>

      <FxCallout kicker="LUMA Care" h2="Need help today?"
        body="Tell us what's going wrong. If you're not sure which plan fits, we'll recommend one after a short call."
        label="Request service" onNavigate={service} navigate={navigate}/>
    </div>
  );
}

/* ─── WORK ───
   The reference's /work: a short navy band, the newest project as a raised
   card, the rest in a grid. Only LUMA_CASES. */
const WORK_ORDER = ['case-urban','case-family','case-spacious','case-modern','case-bighouse'];

function CasesPage({navigate}) {
  const [lead, ...rest] = WORK_ORDER;
  const L = LUMA_CASES[lead];
  return (
    <div className="page">
      <section className="fx-work-hero">
        <div className="fx-work-hero-inner">
          <h1 className="fx-d2">Our work</h1>
          <p>Five finished projects, from a Bird Key waterfront home to a 9,000+ sq ft Bonita Bay residence. Each one shows the systems we installed and the equipment list.</p>
        </div>
      </section>

      <section className="fx-work-feature-wrap">
        <div className="fx-work-feature">
          <NavLink page={lead} navigate={navigate} className="fx-work-feature-img"><img src={L.photo} alt={L.title} loading="eager" decoding="async"/></NavLink>
          <div className="fx-work-feature-copy">
            <span className="fx-panel-kicker">{L.place}</span>
            <h2 className="fx-d3">{L.title}</h2>
            <p className="fx-lede">{L.lede}</p>
            <NavLink page={lead} navigate={navigate} className="fx-more">View project <i aria-hidden="true">→</i></NavLink>
          </div>
        </div>
      </section>

      <section className="fx-work-list">
        <div className="fx-wide">
          <div className="fx-work-grid">
            {rest.map(id => { const c = LUMA_CASES[id]; return (
              <NavLink key={id} page={id} navigate={navigate} className="fx-work-item">
                <span className="fx-work-item-img"><img src={c.photo} alt={c.title} loading="lazy" decoding="async"/></span>
                <span className="fx-work-item-copy">
                  <small>{c.place}</small>
                  <h3>{c.title}</h3>
                  <p>{c.scope}</p>
                </span>
              </NavLink>
            );})}
          </div>
        </div>
      </section>
    </div>
  );
}

function BudgetCalculatorPage({navigate}) {
  const [sqft, setSqft] = React.useState(5000);
  const [picks, setPicks] = React.useState({lighting:true, shading:true, audio:false, theater:false, security:true, network:true, automation:false});
  const services = [
    {k:'lighting', label:'Lighting',          per:18},
    {k:'shading',  label:'Shading',           per:14},
    {k:'audio',    label:'Audio',             per:12},
    {k:'theater',  label:'Theater',           flat:55000},
    {k:'security', label:'Security',          per:10},
    {k:'network',  label:'Networking',        per:8},
    {k:'automation',label:'Automation layer', per:6},
  ];
  const est = services.reduce((sum,s)=>{
    if(!picks[s.k]) return sum;
    return sum + (s.flat || s.per*sqft);
  }, 15000);
  const fmt = n => '$'+Math.round(n/1000)+'k';
  return (
    <div className="page">
      {/* Hero — light split with modern FL home */}
      <section style={{
        display:'grid', gridTemplateColumns:'1fr 1.1fr',
        minHeight:'min(82vh,720px)', overflow:'hidden',
        background:'var(--cream)',
      }} className="lit-hero-wrap">
        {/* left — cream text panel */}
        <div style={{
          display:'flex', flexDirection:'column', justifyContent:'center',
          padding:'88px 64px 88px 80px', background:'var(--cream)',
        }} className="lit-hero-text">
          <div style={{fontSize:12,letterSpacing:'.16em',textTransform:'uppercase',color:'var(--accent)',fontWeight:600,marginBottom:20}}>Budget calculator · Gulf Coast</div>
          <h1 style={{
            fontFamily:'var(--serif)', fontSize:'clamp(38px,4.4vw,62px)',
            fontWeight:600, lineHeight:1.08, color:'var(--dark)',
            margin:'0 0 22px', textWrap:'balance',
          }}>Three tiers. <em style={{color:'var(--accent)',fontStyle:'italic'}}>One honest range.</em></h1>
          <p style={{fontSize:18,lineHeight:1.72,color:'var(--mid)',maxWidth:460,margin:'0 0 28px'}}>Smart-home budgets vary widely. These ranges reflect what we actually build for Gulf Coast homes — design, hardware, installation, and two-year service all in.</p>
          <ul style={{listStyle:'none',padding:0,margin:'0 0 32px',display:'flex',flexDirection:'column',gap:10}}>
            {['Whole-home packages from $85k – $450k+','Sarasota area installations since 2016','Proposal within 48 hrs of a site walk'].map(t=>(
              <li key={t} style={{display:'flex',alignItems:'flex-start',gap:10,fontSize:16,color:'var(--dark)',lineHeight:1.5}}>
                <span style={{color:'var(--accent)',flexShrink:0,marginTop:3,fontWeight:700}}>✓</span>{t}
              </li>
            ))}
          </ul>
          <div style={{display:'flex',gap:12,flexWrap:'wrap'}}>
            <button className="btn-solid" style={{fontSize:16,padding:'14px 28px'}} onClick={()=>navigate('contact')}>Get a tailored quote →</button>
          </div>
        </div>
        {/* right — modern FL home photo */}
        <div style={{position:'relative',overflow:'hidden',minHeight:480}}>
          <img loading="lazy" decoding="async" src={PHOTOS.heroModernHome} alt="Modern luxury home Gulf Coast" style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:'center 40%',display:'block'}}/>
          <div style={{position:'absolute',inset:0,background:'linear-gradient(270deg,transparent 55%,rgba(248,244,237,.18) 100%)'}}/>
        </div>
      </section>

      <section className="th-section">
        <div className="sec-label">Sample budgets</div>
        <h2 className="sec-title">Three tiers <em>of finished home.</em></h2>
        <div className="th-grid-3" style={{marginTop:44}}>
          {BUDGET_TIERS.map(t=>(
            <div key={t.tier} className="th-card" style={t.featured?{borderColor:'var(--accent)',background:'#fff'}:{}}>
              <div className="sec-label" style={{textAlign:'left',marginBottom:6}}>{t.tier}</div>
              <h3 style={{fontFamily:'var(--serif)',fontSize:30,fontWeight:600,margin:'4px 0 4px',color:'var(--accent)'}}>{t.range}</h3>
              <p style={{margin:'0 0 14px',fontSize:13,color:'var(--mid)'}}>{t.sqft}</p>
              <ul style={{listStyle:'none',padding:0,margin:0,display:'flex',flexDirection:'column',gap:8}}>
                {t.includes.map(x=><li key={x} style={{fontSize:14,lineHeight:1.5,color:'var(--dark)',paddingLeft:14,position:'relative'}}><span style={{position:'absolute',left:0,top:8,width:6,height:6,borderRadius:'50%',background:'var(--accent)'}}/>{x}</li>)}
              </ul>
            </div>
          ))}
        </div>
      </section>

      <section className="th-section--cream">
        <div className="th-section--cream-inner">
          <div className="sec-label">Quick estimator</div>
          <h2 className="sec-title">Roughly, <em>where do you land?</em></h2>
          <div style={{maxWidth:760,margin:'40px auto 0',background:'#fff',borderRadius:18,padding:'32px 36px',border:'1px solid rgba(0,0,0,.06)'}}>
            <label style={{display:'block',fontSize:13,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--mid)',marginBottom:10}}>Approx. square footage: <strong style={{color:'var(--accent)',fontSize:16,letterSpacing:0,textTransform:'none'}}>{sqft.toLocaleString()} sq ft</strong></label>
            <input type="range" min="2000" max="15000" step="250" value={sqft} onChange={e=>setSqft(+e.target.value)} style={{width:'100%',accentColor:'#C57238'}}/>
            <div style={{display:'flex',flexWrap:'wrap',gap:10,marginTop:24}}>
              {services.map(s=>(
                <button type="button" key={s.k} onClick={()=>setPicks({...picks,[s.k]:!picks[s.k]})}
                  style={{padding:'10px 16px',borderRadius:999,border:'1px solid '+(picks[s.k]?'var(--accent)':'rgba(0,0,0,.15)'),background:picks[s.k]?'var(--accent)':'#fff',color:picks[s.k]?'#fff':'var(--dark)',fontSize:13,cursor:'pointer',transition:'all .15s'}}>
                  {s.label}
                </button>
              ))}
            </div>
            <div style={{marginTop:32,paddingTop:24,borderTop:'1px solid rgba(0,0,0,.08)',display:'flex',justifyContent:'space-between',alignItems:'baseline'}}>
              <span style={{fontSize:13,letterSpacing:'.08em',textTransform:'uppercase',color:'var(--mid)'}}>Estimated range</span>
              <span style={{fontFamily:'var(--serif)',fontSize:36,fontWeight:600,color:'var(--accent)'}}>{fmt(est*0.85)} – {fmt(est*1.2)}</span>
            </div>
            <p style={{fontSize:12,color:'var(--mid)',margin:'12px 0 0',lineHeight:1.6}}>Indicative only. Final numbers depend on hardware tier, finish quality, site conditions, and integration depth. We'll send a real proposal within 48 hours of a property walk-through.</p>
          </div>
        </div>
      </section>

      {/* Detailed multi-step wizard */}
      <DetailedBudgetWizard/>

      <section className="th-section" style={{textAlign:'center',paddingTop:64,paddingBottom:88}}>
        <h2 className="sec-title">Ready for a <em>real number?</em></h2>
        <p className="sec-body">Tell us about the property and the systems that matter. We'll send a tailored proposal within two business days.</p>
        <div style={{marginTop:28,display:'flex',gap:12,justifyContent:'center',flexWrap:'wrap'}}>
          <button className="btn-solid" onClick={()=>navigate('contact')}>Start a conversation →</button>
          <button className="btn-ghost" onClick={()=>navigate('home')}>Back to home</button>
        </div>
      </section>
    </div>
  );
}

/* ─── CASE STUDIES ───
   The reference's single-project page: a tall photo hero with the place
   above the name, a centred lede and the systems list, a gallery band, the
   write-up, the wave CTA. Text and photos are the ones these pages always
   had. Most are portrait phone shots, so the band is a filmstrip of one
   height and each frame keeps its own shape instead of being cropped. */
const CASE_DETAIL = {
  'case-spacious': {
    lede:'A 7,400 sq ft modern home wired end-to-end for music, network, and effortless ownership: calm in the rooms, organized in the rack, easy on the family.',
    about:[
      'The brief was simple: music everywhere, no visible boxes, and a network the family could rely on year-round between Naples and the northeast. We delivered a single Sonos backbone covering every interior zone plus the lanai and pool deck.',
      'Behind the scenes: a documented UniFi network with full Wi-Fi 6 coverage, a managed WattBox so the rack reboots itself if anything hangs, and remote monitoring so we see issues before the homeowner does.',
    ],
    rooms:[
      {room:'Whole-home audio',   gear:'Sonos Amp · in-ceiling architectural speakers · 8 zones interior + lanai'},
      {room:'Network & remote',   gear:'UniFi Dream Machine · Wi-Fi 6 mesh · WattBox managed power · 24/7 monitoring'},
      {room:'Outdoor experience', gear:'Landscape audio along the pool deck · weatherproof keypads · app control'},
      {room:'Service-friendly',   gear:'Labelled rack · documented for any technician · open platform, no dealer lock-in'},
    ],
    photos:[
      {src:PHOTOS.caseSpSceneA, alt:'Living room with hidden audio'},
      {src:PHOTOS.caseSpSceneB, alt:'Open-plan kitchen and dining'},
      {src:PHOTOS.caseSpCeiling, alt:'Architectural in-ceiling speakers'},
    ],
  },
  'case-urban': {
    lede:'A waterfront urban residence built around music. Bowers & Wilkins from the media room to the pool deck, a 7.1.2 Atmos array tuned in-room, and a UniFi network that just works.',
    about:[
      'The owners are music people. The system was specified around Bowers & Wilkins from day one: in-walls in the great room, a tuned 7.1.2 Atmos array in the media room, and a discreet landscape system that carries the sound out to the pool without disturbing the neighbors.',
      'The network and rack are equally serious: a UniFi backbone with hardwired drops to every TV, access points sized for guests, and a WattBox that keeps the rack online without a service call.',
    ],
    rooms:[
      {room:'Media room',        gear:'Bowers & Wilkins 7.1.2 Dolby Atmos · in-room calibration · acoustic treatment'},
      {room:'Great room & home', gear:'B&W in-wall + in-ceiling speakers · multi-zone streaming · keypad scenes'},
      {room:'Pool & landscape',  gear:'B&W weatherproof landscape audio · zoned for the pool, lanai, and lawn'},
      {room:'Network & rack',    gear:'UniFi · Wi-Fi 6 · WattBox managed power · documented patch panel'},
    ],
    photos:[
      {src:PHOTOS.caseUrPool, alt:'Pool with discreet landscape audio'},
      {src:PHOTOS.caseUrInWall, alt:'B&W in-wall speaker'},
      {src:PHOTOS.caseUrSpeakerDetail, alt:'B&W speaker close-up'},
      {src:PHOTOS.caseUrRack, alt:'UniFi network rack'},
    ],
  },
  'case-family': {
    lede:'A 9,000+ sq ft family residence where the architecture is the story, and the lighting was designed to disappear into it. Hidden cove LEDs, layered scenes, and one keypad in every room.',
    about:[
      'This was a lighting-led project from the first walkthrough. We worked with the architect and designer to hide the fixtures inside the architecture itself: coves above the great room, linear runs under the wood paneling, and a layered scheme that lets a single keypad take the home from morning to evening to overnight.',
      'The result is a house that feels handcrafted in light. No lamp clutter, no glare. Each scene was tuned in person after dark, then handed over with a one-page guide the family actually uses.',
    ],
    rooms:[
      {room:'Great room',            gear:'Hidden cove LEDs above the vault · downlight wash · dim-to-warm scenes'},
      {room:'Architectural accents', gear:'Linear LED runs under wood paneling · niche accent light · staircase grazing'},
      {room:'Bath & spa',            gear:'Backlit shower niche · vanity scenes · after-hours mode'},
      {room:'Control & exterior',    gear:'Lutron RadioRA 3 · designer keypads in every room · landscape & uplight scenes'},
    ],
    photos:[
      {src:PHOTOS.caseHfGreatRoom, alt:'Great room with hidden cove lighting'},
      {src:PHOTOS.caseHfLedCove, alt:'Architectural cove LEDs'},
      {src:PHOTOS.caseHfLedDetail, alt:'Linear LED detail under wood'},
      {src:PHOTOS.caseHfShower, alt:'Backlit shower niche'},
    ],
  },
  'case-modern': {
    lede:'Five independent AV zones in a single hillside home (entertainment room, main living room, and three outdoor patios), unified under one control layer.',
    about:[
      'A modern hillside home designed around five distinct entertainment zones. The client wanted each area to feel complete on its own, and seamlessly connected when the whole house is in use.',
      'No exposed wiring, no visible hardware. Every zone was calibrated after install and fully documented for future expansion.',
    ],
    rooms:[
      {room:'Entertainment room', gear:'Denon AVR · Martin Logan architectural ceiling speakers · Sony TV · 5.1 surround'},
      {room:'Main living room',   gear:'Sony 85" display · Sonos Arc soundbar · flush-mount over linear fireplace'},
      {room:'Patios × 3',         gear:'Polk Audio outdoor speakers · WiiM amplifier per zone · independent source & volume'},
    ],
    photos:[
      {src:PHOTOS.projMrLiving, alt:'Living room with panoramic view'},
      {src:PHOTOS.projMrTv, alt:'Sony TV over the fireplace'},
      {src:PHOTOS.projMrAvRoom, alt:'AV entertainment room'},
      {src:PHOTOS.projMrPatio, alt:'Patio zone'},
    ],
  },
  'case-bighouse': {
    lede:'16 audio zones, 6 video zones, a full Dolby Atmos theater, and 80+ speakers, all running from a single URC processor and built for long-term client ownership.',
    about:[
      'A full-home integration designed in close collaboration with the client, built around a URC processor managing 16 audio zones and 6 video zones. Planned for long-term ownership: open architecture, fully documented.',
      'The dedicated theater has a 4K Epson laser projector, a 130" Severtson screen, and a 7.2.4 Dolby Atmos array powered by KEF speakers, calibrated to the room.',
    ],
    rooms:[
      {room:'Control backbone', gear:'URC processor · 16 audio zones · 6 video zones · open architecture'},
      {room:'Home theater',     gear:'Epson 4K laser · 130" Severtson screen · KEF 7.2.4 Dolby Atmos'},
      {room:'Whole-home audio', gear:'80+ KEF architectural ceiling speakers across all zones'},
      {room:'Security & automation', gear:'Perimeter cameras · motorized shades · whole-home automation'},
    ],
    photos:[
      {src:PHOTOS.projBmLiving, alt:'Finished living room'},
      {src:PHOTOS.projBmTv, alt:'TV on dark marble'},
      {src:PHOTOS.projBmPatio, alt:'Covered patio with pool'},
      {src:PHOTOS.projBmRack, alt:'URC equipment rack'},
      {src:PHOTOS.projBmKef, alt:'KEF speaker delivery'},
      {src:PHOTOS.projBmGameroom, alt:'Game room with ceiling speakers'},
      {src:PHOTOS.projBmControl, alt:'Control panel'},
    ],
  },
};

function FxGallery({photos}){
  const track = useRef(null);
  const step = (dir) => {
    const el = track.current; if (!el) return;
    const slide = el.querySelector('figure');
    el.scrollBy({left: dir * (slide ? slide.offsetWidth + 24 : el.clientWidth), behavior:'smooth'});
  };
  return (
    <section className="fx-gallery-band" aria-label="Project photos">
      <div className="fx-slides" ref={track}>
        {photos.map(p => (
          <figure key={p.src} className="fx-slide">
            <img src={p.src} alt={p.alt} loading="lazy" decoding="async"/>
          </figure>
        ))}
      </div>
      <div className="fx-slides-nav">
        <button type="button" aria-label="Previous photo" onClick={()=>step(-1)}>←</button>
        <button type="button" aria-label="Next photo" onClick={()=>step(1)}>→</button>
      </div>
    </section>
  );
}

function FxCasePage({id, navigate}){
  const c = LUMA_CASES[id], d = CASE_DETAIL[id];
  return (
    <div className="page">
      <section className="lit-hero-wrap fx-hero--case">
        <div>
          <div>{c.place}</div>
          <h1>{c.title}</h1>
        </div>
        <div><img src={c.photo} alt={c.title} loading="eager" fetchpriority="high" decoding="async"/></div>
      </section>

      <article className="fx-case-intro">
        <div className="fx-case-inner">
          <NavLink page="work" navigate={navigate} className="fx-post-back">← All work</NavLink>
          <p className="fx-case-lede">{d.lede}</p>
          <h3>Systems</h3>
          <div className="fx-case-systems">
            {d.rooms.map(r => (
              <div key={r.room}>
                <small>{r.room}</small>
                <ul className="fx-checks">{r.gear.split(' · ').map(g => <li key={g}>{g}</li>)}</ul>
              </div>
            ))}
          </div>
        </div>
      </article>

      <FxGallery photos={d.photos}/>

      <section className="fx-case-prose">
        <div className="fx-case-inner">
          <h3>About this project</h3>
          {d.about.map(p => <p key={p.slice(0,24)}>{p}</p>)}
        </div>
      </section>

      <FxCta navigate={navigate}
        title="Want a similar setup?"
        body="We'll scope your home in one visit and have a line-item proposal back within two business days."
        label="Start a project"/>
    </div>
  );
}

/* ─── SMART HOME DEMO ─── */
function SmartHomeDemoPage({navigate}) {
  const [hoverId, setHoverId] = React.useState(null);
  const [modalRoomId, setModalRoomId] = React.useState(null);
  const [isMobile, setIsMobile] = React.useState(false);

  React.useEffect(()=>{
    const mq = window.matchMedia('(max-width: 759px)');
    const sync = ()=>setIsMobile(mq.matches);
    sync();
    if (mq.addEventListener) mq.addEventListener('change', sync);
    else mq.addListener(sync);
    return ()=>{
      if (mq.removeEventListener) mq.removeEventListener('change', sync);
      else mq.removeListener(sync);
    };
  },[]);

  /* SVG dots scale with viewport — bigger and easier to tap on phones (60+ users) */
  const dotScale = isMobile ? 1.55 : 1.0;

  /* Each room: centroid (cx,cy) and a rough polygon (shape) tracing the room on
     the 3D dollhouse render. All coordinates are percent (0-100). The polygon
     forms a large, intuitive click target and a hover overlay that lights up
     the actual room footprint — not just a tiny dot. */
  /* Each room is mapped to a 4-point parallelogram polygon that traces the
     isometric footprint on the dollhouse. cx/cy = dot center (visual middle).
     cardPos = preferred hover-card placement (T/B/L/R) so cards stay inside
     the image and never float over the wrong room. */
  const ROOMS = [
    {
      id:'garage', name:'Garage', cx:19, cy:19,
      shape:'9,9 30,9 30,33 9,33', cardPos:'B',
      color:'#C57238', tag:'Security · Entry · EV',
      features:[
        {title:'Smart Door Entry',    body:'App or keypad unlock — arrival triggers a Welcome scene throughout the house.'},
        {title:'4K Security Cameras', body:'Cameras cover driveway and garage, stored on a local NVR — no cloud subscription.'},
        {title:'EV Charger Control',  body:'Level 2 charger scheduled to off-peak rates via the automation panel.'},
        {title:'Motion Lighting',     body:'Full brightness on entry, steps to 20% after 3 minutes of idle.'},
      ],
      packages:[
        {name:'Garage Foundation', tier:'Essential',  price:'from $2,800', desc:'Smart deadbolt, 2 outdoor 4K cameras to local NVR, motion-linked LED.'},
        {name:'Garage Signature',  tier:'Recommended', price:'from $6,400', desc:'Adds video doorbell, EV charger integration, app-controlled door operator, keypad with house scenes.'},
        {name:'Garage Curated',    tier:'Concierge',   price:'from $11,000', desc:'Includes full 4-camera perimeter, license-plate recognition, automation triggers for Welcome / Goodbye routines.'},
      ],
    },
    {
      id:'foyer', name:'Entry & Foyer', cx:38, cy:14,
      shape:'32,5 44,5 44,26 32,26', cardPos:'B',
      color:'#C57238', tag:'Keypad · Security · Lighting',
      features:[
        {title:'Welcome Scene',       body:'Arrival lights the foyer, disarms the alarm, and sets climate — all at once.'},
        {title:'Lutron Keypad Hub',   body:'A keypad at the front door controls every scene in the house.'},
        {title:'Video Doorbell',      body:'Rings to your TV and phone simultaneously — answer from the couch.'},
        {title:'Zone Alarm',          body:'Smart alarm with instant push alerts and optional central monitoring.'},
      ],
      packages:[
        {name:'Foyer Foundation', tier:'Essential',  price:'from $1,900', desc:'2 dimmed circuits, smart entry lock, doorbell camera, one Lutron Pico remote.'},
        {name:'Foyer Signature',  tier:'Recommended', price:'from $4,800', desc:'Adds 5-button Lutron Seetouch keypad with Welcome / Away / Goodnight scenes and entry-zone alarm.'},
        {name:'Foyer Curated',    tier:'Concierge',   price:'from $9,500', desc:'Includes Josh.ai voice, intercom-to-room, biometric lock, and full house-wide trigger orchestration.'},
      ],
    },
    {
      id:'office', name:'Home Office', cx:50, cy:15,
      shape:'44,5 57,5 57,27 44,27', cardPos:'B',
      color:'#C57238', tag:'Networking · Shading · Focus',
      features:[
        {title:'Dedicated Wi-Fi 6E',  body:'Separate access point — zero bandwidth contention with IoT or streaming.'},
        {title:'Motorized Blackout',  body:'Shades scheduled down at 9 AM to cut glare, up at 5 PM automatically.'},
        {title:'Focus Scene',         body:'4000K task lighting, do-not-disturb on phones, music paused in this zone.'},
        {title:'Display Matrix',      body:'Route any source — laptop, conferencing, Apple TV — to the monitor in one tap.'},
      ],
      packages:[
        {name:'Office Foundation', tier:'Essential',  price:'from $2,400', desc:'Wired Cat6A drops, dedicated Wi-Fi 6 AP, dimmable downlights on Focus scene.'},
        {name:'Office Signature',  tier:'Recommended', price:'from $5,800', desc:'Adds motorized blackout shades, conferencing mic + camera, single-touch keypad.'},
        {name:'Office Curated',    tier:'Concierge',   price:'from $12,000', desc:'Includes A/V matrix to 2 displays, acoustic treatment, KVM, and Wi-Fi 6E + segregated VLAN.'},
      ],
    },
    {
      id:'living', name:'Living Room', cx:34, cy:43,
      shape:'26,33 43,33 43,52 26,52', cardPos:'T',
      color:'#C57238', tag:'Lighting · Audio · Scenes',
      features:[
        {title:'Scene Control',       body:'Morning, Entertain, Movie, Goodnight — one keypad tap shifts every system at once.'},
        {title:'Lutron Dimming',      body:'Fine-grain dimmer control across cove lights, pendants, and table lamps on one mesh.'},
        {title:'In-Ceiling Audio',    body:'Sonos architectural speakers calibrated for the space — balanced and invisible.'},
        {title:'Motorized Shades',    body:'Gulf-facing glass auto-tinted at peak sun hours; clear again at golden hour.'},
      ],
      packages:[
        {name:'Living Foundation', tier:'Essential',  price:'from $6,500', desc:'6 Lutron dimmed zones, 4 in-ceiling speakers on one Sonos Amp, single keypad with 4 scenes.'},
        {name:'Living Signature',  tier:'Recommended', price:'from $14,000', desc:'Adds tunable cove lighting, motorized solar shades, 5.1 audio, larger keypad with full scene set.'},
        {name:'Living Curated',    tier:'Concierge',   price:'from $32,000', desc:'Includes Ketra tunable-white, 7.1.4 Atmos, automated drapery, art lighting, hidden TV reveal.'},
      ],
    },
    {
      id:'kitchen', name:'Kitchen & Dining', cx:51, cy:37,
      shape:'44,27 60,27 60,58 44,58', cardPos:'T',
      color:'#C57238', tag:'Lighting · Climate · Scenes',
      features:[
        {title:'Tunable White',       body:'Under-cabinet lighting follows your circadian rhythm — warm morning, crisp afternoon.'},
        {title:'Climate Zone',        body:'Kitchen on its own HVAC zone — pre-cool before guests arrive at 6 PM.'},
        {title:'Entertain Scene',     body:'Dims pendants, activates under-cabinet fill, sets music to 30% background level.'},
        {title:'Exhaust Automation',  body:'Range hood activates when cooking sensors detect heat — no manual switch needed.'},
      ],
      packages:[
        {name:'Kitchen Foundation', tier:'Essential',  price:'from $4,800', desc:'5 dimmed zones, under-cabinet LED, ceiling speakers tied to Living, single Pico scene.'},
        {name:'Kitchen Signature',  tier:'Recommended', price:'from $11,500', desc:'Adds tunable white under-cabinet, dedicated HVAC zone, full keypad with Cook / Entertain / Dim scenes.'},
        {name:'Kitchen Curated',    tier:'Concierge',   price:'from $24,000', desc:'Includes Ketra accent layer, hidden in-cabinet TV, motorized window treatment, and smart range hood automation.'},
      ],
    },
    {
      id:'master', name:'Master Suite + Bath', cx:18, cy:61,
      shape:'8,49 31,49 31,95 8,95', cardPos:'T',
      color:'#C57238', tag:'Shading · Climate · Audio · Spa',
      features:[
        {title:'Sunrise Wake Routine', body:'Shades rise slowly with dawn or a set schedule — no alarm sound required.'},
        {title:'Goodnight Keypad',    body:'One tap: shades down, lights off, thermostat to sleep temperature.'},
        {title:'En-Suite Spa Scene',  body:'Mirror lighting, heated floors, exhaust fan, and music — all from one keypad.'},
        {title:'Sleep Zone Climate',  body:'Master kept 2–3° cooler than common areas for optimal rest.'},
      ],
      packages:[
        {name:'Master Foundation', tier:'Essential',  price:'from $5,200', desc:'4 dimmed zones in bedroom, 2 in bath, bedside Pico, single motorized roller shade, dedicated thermostat.'},
        {name:'Master Signature',  tier:'Recommended', price:'from $12,500', desc:'Adds 5-button keypad both bedsides, dual blackout + sheer shades, in-ceiling audio in both rooms, mirror lighting, Sleep / Wake routines.'},
        {name:'Master Curated',    tier:'Concierge',   price:'from $26,000', desc:'Includes dawn-simulation lighting, in-wall LCR speakers, motorized drapery, heated floors, full spa scene control.'},
      ],
    },
    {
      id:'theater', name:'Home Theater', cx:45, cy:75,
      shape:'33,59 59,59 59,93 33,93', cardPos:'T',
      color:'#C57238', tag:'Theater · Atmos · Control',
      features:[
        {title:'4K Laser Projection',  body:'JVC or Sony 4K laser projector on a 120″ acoustically transparent screen.'},
        {title:'Dolby Atmos 7.2.4',   body:'Full speaker layout with acoustic treatment designed into the room.'},
        {title:'Motorized Blackout',  body:'Room-darkening shades drop and lights dim when Movie mode activates.'},
        {title:'Single Touch Panel',  body:'Crestron TSW controls projector, AVR, streaming, and lighting from one screen.'},
      ],
      packages:[
        {name:'Theater Foundation', tier:'Essential',  price:'from $14,000', desc:'4K HDR display, 5.1 in-wall speakers, AVR, single Harmony / Pico-style remote, basic dimming.'},
        {name:'Theater Signature',  tier:'Recommended', price:'from $38,000', desc:'Adds 4K laser projector + 110″ screen, 7.1.4 Atmos, Crestron control, motorized masking, acoustic treatment.'},
        {name:'Theater Curated',    tier:'Concierge',   price:'from $95,000', desc:'Includes reference 4K dual laser, calibrated 9.2.6 Atmos, riser seating, isolated breaker, professional acoustic design.'},
      ],
    },
    {
      id:'lanai', name:'Covered Lanai', cx:74, cy:27,
      shape:'61,11 89,11 89,49 61,49', cardPos:'B',
      color:'#2D5E5A', tag:'Outdoor AV · Lighting · Shade',
      features:[
        {title:'Weather-Rated Audio', body:'Sonance Marine in-ceiling speakers tuned for outdoor acoustics.'},
        {title:'SunBrite Outdoor TV', body:'Outdoor-rated 4K display — built for Florida heat and humidity.'},
        {title:'Wind-Linked Screen',  body:'Motorized privacy screen drops automatically when Gulf gusts exceed 15 mph.'},
        {title:'Landscape Lighting',  body:'Soffit and landscape on scene control — Entertain, Dine, or Party modes.'},
      ],
      packages:[
        {name:'Lanai Foundation', tier:'Essential',  price:'from $5,800', desc:'2 weather-rated speakers on Sonos Amp, soffit lighting on dusk-to-dawn, ceiling fan automation.'},
        {name:'Lanai Signature',  tier:'Recommended', price:'from $13,500', desc:'Adds SunBrite outdoor 4K TV, 4-speaker setup with sub, motorized roll-down screens.'},
        {name:'Lanai Curated',    tier:'Concierge',   price:'from $28,000', desc:'Includes outdoor cinema, landscape lighting on Ketra, automated drop-screens, outdoor-rated keypads & Wi-Fi mesh.'},
      ],
    },
    {
      id:'pool', name:'Pool & Spa', cx:79, cy:70,
      shape:'64,50 93,50 93,93 64,93', cardPos:'T',
      color:'#2D5E5A', tag:'Pool Control · LED · Heat',
      features:[
        {title:'Pool Automation',     body:'Pentair or Jandy integration — temperature, jets, and filtration from any device.'},
        {title:'LED Color Sync',      body:'Pool and spa lighting changes with scenes — teal for Entertain, warm for Relax.'},
        {title:'Spa Pre-Heat',        body:'Schedule the spa to heat by 6 PM Friday — automated, no manual switches.'},
        {title:'Safety Sensors',      body:'Water level and temperature alerts pushed to your phone instantly.'},
      ],
      packages:[
        {name:'Pool Foundation', tier:'Essential',  price:'from $3,200', desc:'Pool automation gateway (Pentair / Jandy), app control of pump, heater, single LED color light.'},
        {name:'Pool Signature',  tier:'Recommended', price:'from $7,800', desc:'Adds Control4-integrated keypad for pool / spa scenes, multicolor LED, scheduled spa heat-up.'},
        {name:'Pool Curated',    tier:'Concierge',   price:'from $16,000', desc:'Includes water-feature automation, underwater speakers, water-level sensors, full landscape scene tie-in.'},
      ],
    },
  ];

  const hovered = hoverId ? ROOMS.find(r => r.id === hoverId) : null;
  const modal = modalRoomId ? ROOMS.find(r => r.id === modalRoomId) : null;

  /* Close modal on Escape */
  React.useEffect(()=>{
    if (!modal) return;
    const onKey = e => { if (e.key === 'Escape') setModalRoomId(null); };
    window.addEventListener('keydown', onKey);
    /* lock body scroll while modal open */
    const prev = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      window.removeEventListener('keydown', onKey);
      document.body.style.overflow = prev;
    };
  }, [modal]);

  /* Compute zoom-in crop for the picture-in-picture image.
     Strategy: 350% size + position so the chosen room's centroid lands at 50/50
     of the visible viewport. Clamp position to keep image edges from showing. */
  const ZOOM = 350; // % of container width
  const cropPos = modal
    ? (() => {
        // For background-size N% on element width W, the image draws at N% of W.
        // background-position: P% means image-pct P aligns with container-pct P.
        // To place modal.cx,modal.cy at 50%,50% of container:
        //   we want the room point to be at center → set position so the room sits in middle.
        //   formula: pos_pct = cx (since at pos=cx the image-cx aligns to container-cx,
        //   but we want it at 50%). Convert with: P = cx · imageSize / (imageSize - containerSize) etc.
        // Simpler: position percentage = (cx - 50)·(N/(N-100)) + 50, clamped 0–100.
        const k = ZOOM / (ZOOM - 100);
        const px = Math.max(0, Math.min(100, (modal.cx - 50) * k + 50));
        const py = Math.max(0, Math.min(100, (modal.cy - 50) * k + 50));
        return `${px}% ${py}%`;
      })()
    : 'center';

  return (
    <div className="page">

      {/* ── Hero ── */}
      <section className="demo-hero" style={{
        background:'transparent', color:'var(--dark)',
        textAlign:'center',
      }}>
        <div style={{fontSize:11,letterSpacing:'.18em',textTransform:'uppercase',color:'var(--accent)',fontWeight:600,marginBottom:18,fontFamily:'var(--sans)'}}>Interactive 3D Demo</div>
        <h1 className="demo-hero-title" style={{fontFamily:'var(--serif)',fontWeight:600,lineHeight:1.1,maxWidth:780,margin:'0 auto 20px'}}>
          See every system <em style={{color:'var(--accent)',fontStyle:'italic'}}>in place.</em>
        </h1>
        <p className="demo-hero-body" style={{lineHeight:1.7,color:'var(--mid)',maxWidth:600,margin:'0 auto'}}>
          Tap any glowing zone (or hover on desktop) to preview the smart systems inside. Open the full picture-in-picture view with packages and pricing.
        </p>
      </section>

      {/* ── 3D Dollhouse Plan ── */}
      <section className="demo-plan-section" style={{background:'transparent'}}>
        <div className="demo-wrap">
          <div className="demo-plan-wrap">
            <div className="demo-plan-stage">
              <img loading="lazy" decoding="async" className="demo-plan-img" src="/assets/smart-home-demo/dollhouse-premium.jpg" alt="Premium 3D cutaway view of a LUMA smart home — every system in place"/>

              <svg className="demo-plan-svg" viewBox="0 0 100 100" preserveAspectRatio="none">
                <defs>
                  <filter id="glow-hot" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur stdDeviation="0.9" result="blur"/>
                    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
                  </filter>
                </defs>

                {ROOMS.map(room => {
                  const isHover = room.id === hoverId;
                  return (
                    <g key={room.id} style={{cursor:'pointer'}}
                      onClick={()=>setModalRoomId(room.id)}
                      onMouseEnter={()=>setHoverId(room.id)}
                      onMouseLeave={()=>setHoverId(null)}
                    >
                      {/* Transparent hit polygon — covers the whole zone for hover/click */}
                      <polygon
                        points={room.shape}
                        fill="rgba(255,255,255,0.001)"
                      />

                      {/* Triple pulse rings — always running so zones never look dead */}
                      <circle cx={room.cx} cy={room.cy} r={2.5*dotScale} fill="none" stroke={room.color} strokeWidth="0.55" opacity="0.95" vectorEffect="non-scaling-stroke" pointerEvents="none">
                        <animate attributeName="r"       from={2.5*dotScale} to={8*dotScale} dur="2.4s" repeatCount="indefinite"/>
                        <animate attributeName="opacity" from="0.95" to="0" dur="2.4s" repeatCount="indefinite"/>
                      </circle>
                      <circle cx={room.cx} cy={room.cy} r={2.5*dotScale} fill="none" stroke={room.color} strokeWidth="0.55" opacity="0.95" vectorEffect="non-scaling-stroke" pointerEvents="none">
                        <animate attributeName="r"       from={2.5*dotScale} to={8*dotScale} dur="2.4s" begin="0.8s" repeatCount="indefinite"/>
                        <animate attributeName="opacity" from="0.95" to="0" dur="2.4s" begin="0.8s" repeatCount="indefinite"/>
                      </circle>
                      <circle cx={room.cx} cy={room.cy} r={2.5*dotScale} fill="none" stroke={room.color} strokeWidth="0.55" opacity="0.95" vectorEffect="non-scaling-stroke" pointerEvents="none">
                        <animate attributeName="r"       from={2.5*dotScale} to={8*dotScale} dur="2.4s" begin="1.6s" repeatCount="indefinite"/>
                        <animate attributeName="opacity" from="0.95" to="0" dur="2.4s" begin="1.6s" repeatCount="indefinite"/>
                      </circle>

                      {/* MAIN DOT — large white circle with colored stroke */}
                      <circle
                        cx={room.cx} cy={room.cy}
                        r={(isHover ? 3.0 : 2.4) * dotScale}
                        fill="#FCFAF6"
                        stroke={room.color}
                        strokeWidth={isHover ? 0.8 : 0.55}
                        vectorEffect="non-scaling-stroke"
                        filter="url(#glow-hot)"
                        style={{transition:'all .2s'}}
                        pointerEvents="none"
                      />
                      <circle
                        cx={room.cx} cy={room.cy}
                        r={(isHover ? 1.55 : 1.15) * dotScale}
                        fill={room.color}
                        style={{transition:'all .2s'}}
                        pointerEvents="none"
                      />
                      <circle
                        cx={room.cx} cy={room.cy}
                        r={0.45 * dotScale}
                        fill="#FCFAF6"
                        opacity={isHover ? 1 : 0.7}
                        pointerEvents="none"
                      />
                    </g>
                  );
                })}
              </svg>

              {/* HOVER CARD — anchored per-room with cardPos (T/B/L/R) so it
                  appears right next to the zone and never floats over the wrong room. */}
              {ROOMS.map(room => {
                const isHover = room.id === hoverId;
                const pos = room.cardPos || 'T';
                // Pre-baked transform offsets — point-relative
                const transforms = {
                  T: 'translate(-50%, calc(-100% - 18px))',
                  B: 'translate(-50%, calc(0% + 18px))',
                  L: 'translate(calc(-100% - 18px), -50%)',
                  R: 'translate(calc(0% + 18px), -50%)',
                };
                return (
                  <div
                    key={room.id+'_hover'}
                    className={`demo-hover-card ${isHover ? 'show' : ''}`}
                    style={{
                      left:`${room.cx}%`,
                      top:`${room.cy}%`,
                      transform: transforms[pos],
                      borderColor: room.color,
                      boxShadow:`0 20px 50px rgba(0,0,0,.6),0 0 0 6px ${room.color}22`,
                    }}
                  >
                    <div className="demo-hover-title">{room.name}</div>
                    <div className="demo-hover-tag" style={{color:room.color}}>{room.tag}</div>
                    <ul className="demo-hover-list">
                      {room.features.slice(0,4).map(f=>(
                        <li key={f.title}>{f.title}</li>
                      ))}
                    </ul>
                    <div className="demo-hover-cta" style={{color:room.color,borderTopColor:`${room.color}40`}}>
                      Click to open detail view <span style={{fontSize:14}}>→</span>
                    </div>
                  </div>
                );
              })}
            </div>
            <div className="demo-plan-hint">
              <span className="demo-plan-hint-pulse"/>
              <span>Tap any room to see what we install · Hover for a quick preview</span>
            </div>
          </div>
        </div>
      </section>

      {/* ── Picture-in-picture MODAL ── */}
      {modal && (
        <div className="demo-modal-backdrop" onClick={()=>setModalRoomId(null)}>
          <div className="demo-modal" onClick={e=>e.stopPropagation()}>
            <button className="demo-modal-close" onClick={()=>setModalRoomId(null)} aria-label="Close">×</button>

            {/* Picture-in-picture — zoomed crop of the dollhouse focused on this room.
                Spotlight ring at 50/50 reinforces which zone the modal represents. */}
            <div className="demo-modal-image" style={{
              backgroundPosition: cropPos,
              backgroundSize: `${ZOOM}%`,
            }}>
              <div className="demo-modal-spot" style={{
                top: '50%', left: '50%',
                borderColor: modal.color,
              }}/>
              <div className="demo-modal-image-tag" style={{borderColor:`${modal.color}66`,color:modal.color}}>{modal.tag}</div>
            </div>

            <div className="demo-modal-body">
              <div className="demo-modal-eyebrow" style={{color:modal.color}}>Smart systems · this zone</div>
              <h3 className="demo-modal-title">{modal.name}</h3>
              <p className="demo-modal-sub">What we install in this space — and at what level.</p>

              <div className="demo-modal-section-label">What's included</div>
              <div className="demo-feats">
                {modal.features.map((f,i)=>(
                  <div key={f.title} className="demo-feat">
                    <div className="demo-feat-num" style={{color:modal.color}}>{String(i+1).padStart(2,'0')}</div>
                    <div>
                      <div className="demo-feat-title">{f.title}</div>
                      <div className="demo-feat-body">{f.body}</div>
                    </div>
                  </div>
                ))}
              </div>

              <div className="demo-packages">
                <div className="demo-modal-section-label">Choose a package</div>
                <div className="demo-package-list">
                  {modal.packages.map((p,i)=>(
                    <div
                      key={p.name}
                      className={`demo-package ${i===1 ? 'demo-package--accent' : ''}`}
                      onClick={()=>navigate('contact')}
                    >
                      <div className="demo-package-head">
                        <div>
                          <div className="demo-package-name">{p.name}</div>
                          <div className="demo-package-tier" style={{color: i===1 ? modal.color : undefined}}>{p.tier}</div>
                        </div>
                        <div className="demo-package-price" style={{color:modal.color}}>{p.price}</div>
                      </div>
                      <div className="demo-package-desc">{p.desc}</div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="demo-modal-cta">
                <button className="btn-solid" style={{fontSize:14,padding:'12px 22px'}} onClick={()=>{setModalRoomId(null);navigate('contact');}}>Plan this zone →</button>
                <button className="btn-ghost" style={{fontSize:14,padding:'11px 22px'}} onClick={()=>setModalRoomId(null)}>Back to home plan</button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ── Bottom CTA ── */}
      <section className="th-section" style={{textAlign:'center'}}>
        <div className="sec-label">Ready to automate?</div>
        <h2 className="sec-title">Your home, <em>fully orchestrated.</em></h2>
        <p className="sec-body" style={{maxWidth:520,margin:'0 auto 32px'}}>Every system in this floor plan is available for your Sarasota or Gulf Coast home. We scope, design, and install — all under one roof.</p>
        <div style={{display:'flex',gap:12,justifyContent:'center',flexWrap:'wrap'}}>
          <button className="btn-solid" style={{fontSize:16,padding:'14px 28px'}} onClick={()=>navigate('contact')}>Start your project →</button>
          <button className="btn-ghost" style={{fontSize:16,padding:'13px 24px'}} onClick={()=>navigate('work')}>See completed homes</button>
        </div>
      </section>

    </div>
  );
}

/* ─── GEO / JOURNAL / BRAND ─── */
function Crumbs({items, navigate}){
  return (
    <nav className="geo-crumbs" aria-label="Breadcrumb">
      {items.map((it,i)=>(
        <span key={it.page || it.label}>
          {i>0 && <span className="geo-crumbs-sep">/</span>}
          {it.page
            ? <NavLink page={it.page} navigate={navigate}>{it.label}</NavLink>
            : <span>{it.label}</span>}
        </span>
      ))}
    </nav>
  );
}

function GeoHero({eyebrow, h1, lede, image, alt, navigate, primary, secondary}){
  return (
    <section className="lit-hero-wrap geo-hero">
      <div className="lit-hero-text geo-hero-text">
        {eyebrow && <div className="geo-eyebrow">{eyebrow}</div>}
        <h1>{h1}</h1>
        <p>{lede ? <LinkedText text={lede} navigate={navigate}/> : lede}</p>
        <div className="geo-hero-actions">
          <NavLink page={(primary && primary.page) || 'contact'} navigate={navigate} className="btn-solid">{(primary && primary.label) || 'Book a consultation →'}</NavLink>
          {secondary && <NavLink page={secondary.page} navigate={navigate} className="btn-ghost">{secondary.label}</NavLink>}
        </div>
      </div>
      <div className="geo-hero-photo">
        <img loading="lazy" decoding="async" src={image} alt={alt || h1}/>
      </div>
    </section>
  );
}

/* ── Location pages, on the reference's /locations pattern ──────────────
   hub:  inner hero → centred paragraph → a card per place → map → callout
   city: inner hero → copy + a real photo of the place → (a finished project
         in that city, when there is one) → systems → areas we serve → map →
         callout. Place photos are real and geotagged: see
         assets/photos/places/CREDITS.md. Nothing here describes a job that
         is not in LUMA_CASES. */
const PLACE_PHOTO = (id) => lu('/assets/photos/places/' + id + '.jpg');
/* the kind of house each place page describes (generated, graded); the
   place itself stays a real geotagged photo in the hero */
const PLACE_HOME = (id) => lu('/assets/photos/homes/' + id + '.jpg');
const CITY_CASES = { sarasota: 'case-urban' };

function FxInnerHero({kicker, h1, image, alt}){
  return (
    <section className="lit-hero-wrap">
      <div className="lit-hero-text">
        <div>{kicker}</div>
        <h1 style={{fontFamily:'var(--serif)',color:'#FCFAF6',margin:0}}>{h1}</h1>
      </div>
      <div style={{position:'relative',overflow:'hidden'}}>
        <img loading="eager" fetchpriority="high" decoding="async" src={image} alt={alt || ''} style={{width:'100%',height:'100%',objectFit:'cover',display:'block'}}/>
      </div>
    </section>
  );
}

function FxCallout({kicker, h2, body, navigate, actions=true, label, onNavigate}){
  return (
    <section className="fx-callout">
      <div className="fx-callout-inner">
        {kicker && <p className="fx-callout-kicker">{kicker}</p>}
        <h2 className="fx-d3">{h2}</h2>
        {body && <div className="fx-lede"><p>{body}</p></div>}
        {actions && <FxActions navigate={navigate} tone="dark" label={label} onNavigate={onNavigate}/>}
      </div>
    </section>
  );
}

function FxMap({query, title}){
  return (
    <section className="fx-map">
      <iframe title={title || ('Map of ' + query)} loading="lazy" referrerPolicy="no-referrer-when-downgrade"
        src={'https://www.google.com/maps?q=' + encodeURIComponent(query) + '&z=11&output=embed'}/>
    </section>
  );
}

/* Service pages: the reference's "Areas we serve" — one centred line of places */
function GeoStrip({serviceId, navigate}){
  const g = geoData();
  const cities = g.cities || {};
  const svc = (g.services && g.services[serviceId]) || {};
  const ids = Object.keys(cities);
  if (!ids.length) return null;
  return (
    <section className="fx-areas">
      <div className="fx-field">
        <h3 className="fx-d3">{(svc.nav || 'This system')} across Sarasota &amp; Manatee</h3>
        <p className="fx-lede">
          {ids.map((id,i)=>(
            <React.Fragment key={id}>
              <NavLink page={servicePageForCity(id, serviceId)} navigate={navigate} className="fx-inline">{cities[id].name}</NavLink>{i < ids.length-1 ? ', ' : '. '}
            </React.Fragment>
          ))}
          <NavLink page="service-areas" navigate={navigate} className="fx-more">All service areas <i aria-hidden="true">→</i></NavLink>
        </p>
      </div>
    </section>
  );
}

function ServiceAreasHub({navigate}){
  const g = geoData();
  const cities = g.cities || {};
  const nap = napInfo();
  return (
    <div className="page">
      <FxInnerHero kicker="Service areas" h1="Serving Sarasota & Manatee Counties" image={PLACE_PHOTO('sarasota')} alt="Sarasota bayfront"/>
      <section className="fx-band--plain fx-py-md">
        <div className="fx-field">
          <div className="fx-intro-prose">
            <p>{(g.hub && g.hub.lede) || 'Two counties, one studio in Sarasota.'} Wherever the house is, it gets the same drawings, the same crew and the same aftercare, and you reach us on <a href={nap.telHref} className="fx-inline">{nap.telephoneDisplay}</a>.</p>
          </div>
        </div>
      </section>
      <section className="fx-band--plain" style={{paddingBottom:96}}>
        <div className="fx-wide">
          <div className="fx-panels fx-panels--static fx-panels--places">
            {Object.keys(cities).map(id => { const c = cities[id]; return (
              <NavLink key={id} page={cityPageId(id)} navigate={navigate} className="fx-panel-card">
                <span className="fx-panel-img"><img src={PLACE_HOME(id)} alt={'A typical ' + c.name + ' house'} loading="lazy" decoding="async"/></span>
                <span className="fx-panel-body">
                  <small className="fx-panel-kicker">{c.county}</small>
                  <h3>{c.name}</h3>
                  <i className="fx-panel-rule" aria-hidden="true"/>
                  <p>{c.tagline}</p>
                  <span className="fx-panel-more">Learn more <i aria-hidden="true">→</i></span>
                </span>
              </NavLink>
            );})}
          </div>
        </div>
      </section>
      <FxMap query="Sarasota County and Manatee County, Florida" title="Sarasota and Manatee Counties"/>
      <FxCallout navigate={navigate} kicker="Sarasota studio" h2="Ready for a walkthrough?"
        body="Tell us where the house is and what it should do. We come out, walk it with you, and send a line-item proposal."/>
    </div>
  );
}

function CityHubPage({cityId, navigate}){
  const g = geoData();
  const city = (g.cities && g.cities[cityId]) || null;
  const services = g.services || {};
  if (!city) return <ServiceAreasHub navigate={navigate}/>;
  const caseId = CITY_CASES[cityId];
  const kase = caseId && LUMA_CASES[caseId];
  const gallery = cityId === 'sarasota' ? [PHOTOS.caseUrHero, PHOTOS.caseUrPool, PHOTOS.caseUrInWall, PHOTOS.caseUrRack] : null;
  return (
    <div className="page">
      <FxInnerHero kicker={city.county} h1={city.h1} image={PLACE_PHOTO(cityId)} alt={city.name}/>
      <section className="fx-py-md">
        <div className="fx-wide">
          <div className="fx-row">
            <div className="fx-row-copy">
              <div className="fx-lede">
                <p><strong style={{color:'var(--dark)'}}><LinkedText text={city.lede} navigate={navigate}/></strong></p>
                {(city.paragraphs||[]).map((p,i)=><p key={i}><LinkedText text={p} navigate={navigate}/></p>)}
              </div>
            </div>
            <div className="fx-row-media">
              <img src={PLACE_HOME(cityId)} alt={'A typical ' + city.name + ' house'} loading="lazy" decoding="async"/>
            </div>
          </div>
        </div>
      </section>

      {kase && (
        <section className="fx-band fx-py-lg">
          <div className="fx-wide">
            <div className="fx-heads" style={{marginBottom:40}}>
              <h2 className="fx-d3">Finished in {city.name}: {kase.title}</h2>
              <p className="fx-lede">{kase.place}. {kase.lede}</p>
            </div>
            <div className="fx-gallery">
              {gallery.map((src,i)=><img key={i} src={src} alt={kase.title} loading="lazy" decoding="async"/>)}
            </div>
            <p style={{textAlign:'center',marginTop:32}}>
              <NavLink page={caseId} navigate={navigate} className="fx-more">Read the case study <i aria-hidden="true">→</i></NavLink>
            </p>
          </div>
        </section>
      )}

      <section className="fx-areas">
        <div className="fx-field">
          <h3 className="fx-d3">What we install in {city.name}</h3>
          <p className="fx-lede">
            {Object.keys(services).map((sid,i,arr)=>(
              <React.Fragment key={sid}>
                <NavLink page={servicePageForCity(cityId, sid)} navigate={navigate} className="fx-inline">{services[sid].name}</NavLink>{i < arr.length-1 ? ', ' : '.'}
              </React.Fragment>
            ))}
          </p>
        </div>
      </section>

      {city.neighborhoods && city.neighborhoods.length > 0 && (
        <section className="fx-areas fx-areas--tight">
          <div className="fx-field">
            <h3 className="fx-d3">Areas we serve</h3>
            <p className="fx-lede">{city.neighborhoods.join(', ')}, and the rest of {city.county}.</p>
          </div>
        </section>
      )}

      <FxMap query={city.name + ', Florida'} title={'Map of ' + city.name}/>
      <FxCallout navigate={navigate} kicker={'Serving ' + city.name} h2="Ready for a walkthrough?"
        body={'Tell us about the ' + city.name + ' house. We come out, walk it with you, and send a line-item proposal.'}/>
    </div>
  );
}

function CityServicePage({cityId, serviceId, navigate}){
  const g = geoData();
  const city = (g.cities && g.cities[cityId]) || {};
  const svc = (g.services && g.services[serviceId]) || {};
  const row = (g.cityServices && g.cityServices[cityId+'/'+serviceId]) || null;
  if (!row) return <CityHubPage cityId={cityId} navigate={navigate}/>;
  const photo = lu(svc.og || '/assets/photos/lighting-scene.jpg');
  return (
    <div className="page">
      <FxInnerHero kicker={city.name + ' · ' + svc.nav} h1={row.h1} image={PLACE_PHOTO(cityId)} alt={city.name}/>
      <section className="fx-py-md">
        <div className="fx-wide">
          <div className="fx-row">
            <div className="fx-row-copy">
              <div className="fx-lede">
                <p><strong style={{color:'var(--dark)'}}><LinkedText text={row.lede} navigate={navigate}/></strong></p>
                {(row.paragraphs||[]).map((p,i)=><p key={i}><LinkedText text={p} navigate={navigate}/></p>)}
              </div>
              {row.bullets && <ul className="fx-points fx-points--list">{row.bullets.map(b=><li key={b}>{b}</li>)}</ul>}
              <p style={{marginTop:24}}>
                <NavLink page={serviceId} navigate={navigate} className="fx-more">{svc.nav} overview <i aria-hidden="true">→</i></NavLink>
                <span style={{margin:'0 14px',color:'var(--cream3)'}}>·</span>
                <NavLink page={cityPageId(cityId)} navigate={navigate} className="fx-more">Everything in {city.name} <i aria-hidden="true">→</i></NavLink>
              </p>
            </div>
            <div className="fx-row-media"><img src={photo} alt={svc.name} loading="lazy" decoding="async"/></div>
          </div>
        </div>
      </section>
      <FxMap query={city.name + ', Florida'} title={'Map of ' + city.name}/>
      <FxCallout navigate={navigate} kicker={city.name + ' · ' + svc.nav} h2="Ready for a walkthrough?"
        body={'Tell us about the house and what the ' + (svc.nav || 'system').toLowerCase() + ' should do. We come out, walk it with you, and send a line-item proposal.'}/>
    </div>
  );
}

/* ── Journal, on the reference's /blog pattern: a plain title block, then a
   three-column grid of cards (photo, category, title, dek, "Read more").
   The article page: category and date line, headline, dek, lead photo,
   prose at 20px. Newest first. ── */
const fmtDate = (iso) => { try { return new Date(iso + 'T12:00:00').toLocaleDateString('en-US', {month:'long', day:'numeric', year:'numeric'}); } catch(e) { return iso; } };

function JournalIndex({navigate}){
  const g = geoData();
  const order = g.articleOrder || [];
  const articles = g.articles || {};
  const hub = g.journalHub || {};
  return (
    <div className="page">
      <section className="fx-blog-head">
        <div className="fx-field">
          <h1 className="fx-d2">{hub.h1 || 'Notes from the studio'}</h1>
          <p className="fx-lede">{hub.lede}</p>
        </div>
      </section>
      <section className="fx-blog-list">
        <div className="fx-field">
          <div className="fx-blog-grid">
            {order.map(id => { const a = articles[id]; if (!a) return null; return (
              <article key={id} className="fx-blog-card">
                <NavLink page={id} navigate={navigate} className="fx-blog-img" tabIndex={-1} aria-hidden="true">
                  <img src={lu(a.og || '/assets/photos/gulf-sunset.jpg')} alt="" loading="lazy" decoding="async"/>
                </NavLink>
                <div className="fx-blog-body">
                  <div className="fx-blog-meta"><span>{a.category}</span><time dateTime={a.date}>{fmtDate(a.date)}</time></div>
                  <h2><NavLink page={id} navigate={navigate}>{a.h1}</NavLink></h2>
                  <p>{a.dek}</p>
                  <NavLink page={id} navigate={navigate} className="fx-panel-more">Read more <i aria-hidden="true">→</i></NavLink>
                </div>
              </article>
            );})}
          </div>
        </div>
      </section>
      <FxCta navigate={navigate}/>
    </div>
  );
}

function JournalArticle({articleId, navigate}){
  const g = geoData();
  const a = (g.articles && g.articles[articleId]) || null;
  if (!a) return <JournalIndex navigate={navigate}/>;
  const order = (g.articleOrder || []).filter(id => id !== articleId).slice(0, 3);
  return (
    <div className="page">
      <article className="fx-post">
        <div className="fx-post-inner">
          <NavLink page="journal" navigate={navigate} className="fx-more fx-post-back"><i aria-hidden="true" style={{transform:'none'}}>←</i> All notes</NavLink>
          <div className="fx-blog-meta"><span>{a.category}</span><time dateTime={a.date}>{fmtDate(a.date)}</time></div>
          <h1 className="fx-d2">{a.h1}</h1>
          <p className="fx-post-dek">{a.dek}</p>
        </div>
        <div className="fx-post-photo"><img src={lu(a.og || '/assets/photos/gulf-sunset.jpg')} alt={a.h1} loading="eager" decoding="async"/></div>
        <div className="fx-post-inner fx-post-prose">
          {(a.blocks||[]).map((b,i)=>{
            if (b.type==='h2') return <h2 key={i}>{b.text}</h2>;
            if (b.type==='ul') return <ul key={i}>{b.items.map(it=><li key={it}><LinkedText text={it} navigate={navigate}/></li>)}</ul>;
            return <p key={i}><LinkedText text={b.text} navigate={navigate}/></p>;
          })}
        </div>
      </article>
      {order.length > 0 && (
        <section className="fx-band fx-py-lg">
          <div className="fx-field">
            <div className="fx-heads" style={{marginBottom:40}}><h2 className="fx-d3">More from the journal</h2></div>
            <div className="fx-blog-grid">
              {order.map(id => { const b = (g.articles||{})[id]; if (!b) return null; return (
                <article key={id} className="fx-blog-card">
                  <NavLink page={id} navigate={navigate} className="fx-blog-img" tabIndex={-1} aria-hidden="true"><img src={lu(b.og)} alt="" loading="lazy" decoding="async"/></NavLink>
                  <div className="fx-blog-body">
                    <div className="fx-blog-meta"><span>{b.category}</span><time dateTime={b.date}>{fmtDate(b.date)}</time></div>
                    <h2><NavLink page={id} navigate={navigate}>{b.h1}</NavLink></h2>
                    <NavLink page={id} navigate={navigate} className="fx-panel-more">Read more <i aria-hidden="true">→</i></NavLink>
                  </div>
                </article>
              );})}
            </div>
          </div>
        </section>
      )}
      <FxCta navigate={navigate}/>
    </div>
  );
}

function BrandPage({navigate}){
  const nap = napInfo();
  const faqs = [
    {q:'Is LUMA Smart Home the same as luma.com?', a:'No. luma.com is an events and invitation platform. We do not run event software. We design lighting, shades, audio, security, and Wi-Fi for Gulf Coast homes.'},
    {q:'Is this Luma AI or Luma Labs?', a:'No. Luma AI (lumalabs.ai) builds generative video and 3D tools. If you wanted Dream Machine, that is a different company.'},
    {q:'Do you make Snap One Luma cameras?', a:'No. Snap One sells a camera line named Luma through security dealers. When this studio specs cameras, we use on-premise UniFi Protect — your footage on your property.'},
  ];
  return (
    <div className="page">
      <GeoHero
        eyebrow="Entity · Sarasota, Florida"
        h1="LUMA Smart Home — the Sarasota studio."
        lede="Residential technology. Not the events app, not the video model, not the camera SKU that shares a word."
        image={PHOTOS.heroAbout}
        alt="Sarasota marina"
        navigate={navigate}
        primary={{page:'contact', label:'Start a project →'}}
        secondary={{page:'journal-not-luma-com', label:'Read the explainer'}}
      />
      <section className="th-section">
        <Crumbs items={[{page:'home', label:'Home'},{label:'LUMA Smart Home Sarasota'}]} navigate={navigate}/>
        <div className="geo-prose">
          <p>LUMA Smart Home (lumasmarthome.com) is a residential technology studio based in Sarasota, Florida. We specify and install Lutron lighting, motorized shades, whole-home audio, UniFi cameras and Wi-Fi, and automation for houses in Sarasota and Manatee Counties. See <NavLink page="service-areas" navigate={navigate} className="inline-link">where we work</NavLink> and <NavLink page="about" navigate={navigate} className="inline-link">about the studio</NavLink>.</p>
          <p>Legal name: LUMA Home Systems LLC. The public name on this site and on Google should stay LUMA Smart Home — Sarasota, with the trades in the description so a search for lighting or smart home does not land you on an events platform.</p>
        </div>
        <address className="geo-nap">
          <strong>LUMA Smart Home</strong>
          <span>Sarasota, Florida</span>
          <a href={nap.telHref}>{nap.telephoneDisplay}</a>
          <a href={nap.mailHref}>{nap.email}</a>
          <span>{nap.hours}</span>
          <a href={nap.mapsUrl} target="_blank" rel="noopener noreferrer">{nap.mapsLabel}</a>
        </address>
        <h2 className="geo-subhead">If a search sent you to the wrong LUMA</h2>
        <div className="geo-faq">
          {faqs.map(f=>(
            <div key={f.q} className="geo-faq-item">
              <h3>{f.q}</h3>
              <p>{f.a}</p>
            </div>
          ))}
        </div>
        <div className="geo-next">
          <NavLink page="service-areas" navigate={navigate} className="btn-solid">Where we work</NavLink>
          <NavLink page="about" navigate={navigate} className="btn-ghost">About the studio</NavLink>
        </div>
      </section>
    </div>
  );
}

/* ─── APP ─── */
function readPageFromUrl(){
  const seo = window.LUMA_SEO || {routes:{}};
  const aliases = window.LUMA_SEO_ALIASES || {};
  const path = normalizePath(window.location.pathname);
  const routes = seo.routes || {};
  for (const id of Object.keys(routes)) {
    if (normalizePath(routes[id].path) === path) return id;
  }
  const slug = path.replace(/^\//, '');
  if (isKnownPage(slug)) return slug;
  if (aliases[slug] && isKnownPage(aliases[slug])) return aliases[slug];
  try {
    const q = new URLSearchParams(window.location.search||'').get('p');
    if (q && isKnownPage(q)) return q;
    if (q && aliases[q] && isKnownPage(aliases[q])) return aliases[q];
  } catch(e) {}
  const h = (window.location.hash||'').replace(/^#\/?/,'').split(/[?#]/)[0];
  if (h && isKnownPage(h)) return h;
  if (h && aliases[h] && isKnownPage(aliases[h])) return aliases[h];
  if (window.__LUMA_PAGE && isKnownPage(window.__LUMA_PAGE)) return window.__LUMA_PAGE;
  return 'home';
}

function App() {
  const [page, setPage] = useState(readPageFromUrl);

  useEffect(()=>{
    const sync = ()=> setPage(readPageFromUrl());
    window.addEventListener('popstate', sync);
    window.addEventListener('hashchange', sync);
    return ()=>{
      window.removeEventListener('popstate', sync);
      window.removeEventListener('hashchange', sync);
    };
  }, []);

  useEffect(()=>{ applySeo(page); }, [page]);

  function navigate(p){
    setPage(p);
    applySeo(p);
    try {
      const next = pathFor(p);
      const current = normalizePath(window.location.pathname);
      if (current !== normalizePath(next) || window.location.search || window.location.hash) {
        window.history.pushState({page:p}, '', next);
      }
    } catch(e) {
      window.location.hash = p==='home' ? '' : '/' + p;
    }
    window.scrollTo({top:0,behavior:'smooth'});
  }

  const pages = {
    home:      <HomePage navigate={navigate}/>,
    shading:   <ShadingPage navigate={navigate}/>,
    theaters:  <TheatersPage navigate={navigate}/>,
    automation:<AutomationPage navigate={navigate}/>,
    audio:     <AudioPage navigate={navigate}/>,
    security:  <SecurityPage navigate={navigate}/>,
    networking:<NetworkingPage navigate={navigate}/>,
    'permanent-lighting':<PermanentLightingPage navigate={navigate}/>,
    lighting:  <LightingPage navigate={navigate}/>,
    designers: <DesignersPage navigate={navigate}/>,
    contact:   <ContactPage navigate={navigate}/>,
    'budget-calculator': <BudgetCalculatorPage navigate={navigate}/>,
    work:      <CasesPage navigate={navigate}/>,
    'case-spacious': <FxCasePage id="case-spacious" navigate={navigate}/>,
    'case-urban':    <FxCasePage id="case-urban" navigate={navigate}/>,
    'case-family':   <FxCasePage id="case-family" navigate={navigate}/>,
    'case-modern':   <FxCasePage id="case-modern" navigate={navigate}/>,
    'case-bighouse': <FxCasePage id="case-bighouse" navigate={navigate}/>,
    about:     <AboutPage navigate={navigate}/>,
    support:   <ServiceSupportPage navigate={navigate}/>,
    'smart-home-demo': <SmartHomeDemoPage navigate={navigate}/>,
  };
  const route = (window.LUMA_SEO && window.LUMA_SEO.routes && window.LUMA_SEO.routes[page]) || {};
  const kind = route.kind;
  let view = pages[page];
  if (!view) {
    if (kind === 'areas-hub') view = <ServiceAreasHub navigate={navigate}/>;
    else if (kind === 'city') view = <CityHubPage cityId={route.city} navigate={navigate}/>;
    else if (kind === 'city-service') view = <CityServicePage cityId={route.city} serviceId={route.service} navigate={navigate}/>;
    else if (kind === 'journal-hub') view = <JournalIndex navigate={navigate}/>;
    else if (kind === 'article') view = <JournalArticle articleId={page} navigate={navigate}/>;
    else if (kind === 'brand') view = <BrandPage navigate={navigate}/>;
    else view = <HomePage navigate={navigate}/>;
  }
  const serviceIds = ['lighting','shading','theaters','audio','security','networking','automation'];
  return (
    <div>
      <Nav navigate={navigate}/>
      {view}
      {serviceIds.includes(page) && <GeoStrip serviceId={page} navigate={navigate}/>}
      {page !== 'home' && <RelatedLinks page={page} navigate={navigate}/>}
      <Footer navigate={navigate}/>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App/>);
