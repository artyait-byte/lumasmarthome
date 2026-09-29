# Photography references, by zone

How the leaders in each category actually shoot the thing, so our generated
frames look like their galleries and not like renders. Use these notes to
write prompts; never feed their images into the generator.

## Every frame
Real-estate editorial, full-frame 24mm at f/8, available light, natural
white balance, fine grain, slight vignette, small imperfections (a magazine on
the sofa, a car in the drive, a chair not quite square). Never HDR glow, never
perfect symmetry, never over-saturated. Run every output through
`scripts/photo_grade.sh` before it goes in `assets/photos/`.

Prompt suffix that produced the good frames:
> Candid editorial real-estate photograph shot on a full-frame camera with a
> 24mm lens at f/8, available light only, natural white balance, slight lens
> vignetting, fine film grain, small real-world imperfections, not a render,
> not CGI, no HDR glow. No people, no text, no logos, no watermark.

## Permanent lighting — JellyFish, Trimlight, Gemstone
Night or late dusk, from the street or the driveway, whole roofline in frame.
The LEDs read as **discrete dots with a soft bloom**, not a continuous line;
the track itself is invisible in the soffit shadow. Colours are bold
(red/green, purple, teal) or warm white; sky near-black or a deep dusk
gradient. Handheld feel, a little grain. Trimlight also does the dusk
close-up: the eave line against an orange sky. Ours: `permanent-holiday.jpg`
(dots, street view), `permanent-dusk.jpg` (warm-white line at dusk).

## Lighting control — Lutron
Warm interiors at evening, layered light (cove + downlight + lamp), 2700K.
Keypad shown small and real: a rectangular plate with a few engraved buttons
beside a doorway, brushed nickel or matte white. Never a glowing glass square.

## Shades — Lutron, Hunter Douglas
Midday, glare being tamed: linen roller shades half-down over bright water,
sunlight diffused across pale furniture. Fabric texture visible.

## Audio — Sonance
Bright daylight outdoor living: lanai, pool, long sofa, wide lens. Speakers
are barely visible in the ceiling; the photo is about the place, not the gear.

## Home theater — CEDIA award galleries
Under-exposed and moody, from the back row, fabric walls, recliners slightly
askew, a dim bar, star ceiling faint. Screen shows a paused frame, not black.

## Cameras — Ubiquiti Protect
Exterior at dusk from the driveway; the camera is a small dome under the
soffit at a corner, easy to miss. Landscape uplighting, lit entry.

## Networking — Ubiquiti, Access Networks
Domestic scale only: a rack in a wood-trimmed closet with a doorway in frame,
never a data-centre aisle. Patch cables dressed, labels readable.

## Automation — Control4, Josh.ai
A lived-in room at golden hour with one keypad in shot and shades mid-travel;
the system is implied by the state of the room, not by a screen.

## Show the house doing something
A beautiful room reads as an interior-design site. What sells a smart home is
the act of control or its result, visible in the frame:
- **State pairs / sets from one camera** — the same room at 07:00, 14:30,
  19:30, 22:45, generated from one base frame with `--image-references`, so
  only light and shades change. Used by the scene switcher (`FxScenes`).
- **Hands, not faces** — a fingertip on a keypad, a phone driving shades that
  are visibly mid-travel, a tap on an in-wall panel, a remote as the screen
  lights. Hands show intent; faces are where generated people look fake.
- Keep button labels and screen UI illegible in prompts; real words come out
  garbled.

## Service areas — the house each page describes
`assets/photos/homes/{city}.jpg` are generated (Seedream 5 Pro, graded with
`scripts/photo_grade.sh`) from the page's own text: Bird Key glass and lanai,
West Bradenton CBS ranch on the river, Lakewood Ranch new construction,
Venice Island 1920s Italian Renaissance, Siesta gulf-front with solar screens,
Longboat bay-side elevated modern, Anna Maria cottage on pilings, Palmetto
river-front bungalow. The place heroes stay real geotagged photos
(`assets/photos/places/CREDITS.md`).
