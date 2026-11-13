# Look and Feel: Neon Night

This is the chosen look for Accelerate. It replaces the daytime demo look (blue sky, green grass, block cars). Build it one step at a time, the same way as BUILD_PLAN.md.

## Reference images

- `design/neon-night.png` shows the game view: night city, glowing curbs, both cars from behind.
- `design/car1.png` shows Car 1 from the side.
- The `.svg` versions of both are the same drawings as code, with every color in them.

The images are 2D mockups. Match the mood, colors and shapes. Do not try to match them pixel for pixel.

## Rules that must not break

- The driving feel stays the same. Do not change any `DRIVE` or `JUMP` numbers, and keep each car's collision size the same as now.
- The game must still build into the single offline HTML file. No files loaded from the internet at run time. Build the cars from Three.js shapes in code.
- It has to run smoothly on a school Chromebook in split screen. Anything expensive (bloom, extra lights, shadows) needs an on/off setting.
- Speed pads, mud, the jump ramp, the map on M, the countdown, lap counter and place screens all keep working.

## The theme

Put all of these in one `THEME` block next to `DRIVE`, with a comment on each line, and add it to `window.ACCEL` so the values can be changed from the console.

| Part | Color | Notes |
|---|---|---|
| Sky | `#0b0f2a` | Flat dark navy. Fog is the same color. |
| Stars | `#ffffff` | Small dots, scattered, not many |
| Ground | `#101536` | Replaces the grass |
| Ground grid lines | `#ff2bd6` | Thin, faint (about 30% strength) |
| Road | `#1c2033` | |
| Center line | `#19e6ff` | Dashed, glowing |
| Curbs | `#19e6ff` and `#ff2bd6` | Alternating blocks, both glowing |
| Buildings | `#1a2152` and `#141a3d` | Two shades, mixed |
| Window lights | `#ffd84d`, `#19e6ff`, `#ff2bd6` | A few lit windows per building |
| Tail lights | `#ff2040` | Glowing |
| Headlights | `#fff3b0` | |

### Scenery

- Remove the pine trees. Put simple box buildings of different heights around the outside of the track, far enough back that they never block the road.
- Each building gets a few small lit windows. Most windows stay dark.
- Speed pads and mud need new colors that read clearly at night. Suggestion: speed pads glow bright cyan, mud is a dull brown-purple with no glow.

### Lighting

- Low, cool ambient light so unlit things look dark blue, not black.
- Glowing things (curbs, center line, windows, tail lights, underglow) use emissive materials so they stay bright in the dark.
- Each car has a soft pool of colored light on the road under it (underglow) in its own color.
- Headlights that light the road ahead are a nice extra. Add them only if the Chromebook stays smooth.
- Bloom (the glow halo effect) is optional. Add it behind a setting, `THEME.BLOOM`, that can be switched off.

### The HUD

- Font: Orbitron, weight 900, with letter spacing. It must be embedded for the offline build, or fall back to a bold system font.
- Lap counter: a cyan (`#19e6ff`) box with dark navy (`#0b0f2a`) text and slightly rounded corners.
- WRONG WAY and GO BACK TO THE TRACK: magenta (`#ff2bd6`) box with dark navy text.
- Countdown and FIRST PLACE! / SECOND PLACE screens use the same font, cyan and magenta on dark navy.

## The cars

Put the cars in a `CARS` list so more can be added later. Each entry holds the car's name, body colors, glow color and which shape it uses. Player 1 and player 2 each point at one entry.

### Car 1: neon orange sports coupe

An original low-poly design. See `design/car1.png`.

Shape:

- Low, wedge-shaped body. Long hood that slopes down to the nose, cabin set toward the back, short rear deck.
- Fastback cabin: the roof slopes down smoothly into the rear deck.
- Narrow and low. About 4 long (same as now), 1.6 wide, 1.1 tall.
- Flat faces with visible edges. Each face is a slightly different shade so the shape reads without smooth shading.
- Raised rear wing: a flat blade on two short supports, with a small cyan plate on each end.
- Dark side skirt along the bottom between the wheels.
- Six-sided wheel rims.
- From behind: a wide red tail light bar across the back, a dark panel low in the bumper, and two small round exhausts.
- No number on the car.

Colors:

| Part | Color |
|---|---|
| Body, main | `#ff6a00` |
| Body, top faces (lighter) | `#ff8f3d` |
| Body, shaded faces | `#c24e00` |
| Side skirt and wing supports | `#8f3a00` |
| Wing blade | `#c24e00` |
| Wing end plates | `#19e6ff` |
| Glass | `#0b0f2a` |
| Side stripe, upper | `#19e6ff` |
| Side stripe, lower (thinner) | `#ff2bd6` |
| Headlights | `#fff3b0` |
| Tail lights | `#ff2040` |
| Tires | `#151829` |
| Rims | `#c9d3ff` |
| Underglow | `#ff6a00` |

The two stripes run along the lower door between the front and rear wheels.

### Car 2: neon green

The same shape as Car 1 for now, in green. It will get its own shape later.

| Part | Color |
|---|---|
| Body, main | `#39ff14` |
| Body, top faces (lighter) | `#7dff66` |
| Body, shaded faces | `#1fa80a` |
| Side skirt and wing | `#0f5c05` |
| Underglow | `#39ff14` |

Everything else matches Car 1.

## Build steps

Each step is one request. Play-test, commit and write the progress log after each one.

1. **Theme block.** Add `THEME` with the sky, fog, ground, road and light colors, and switch the scene to night. Nothing else changes yet.
2. **Glowing track.** Recolor the curbs to alternating cyan and magenta, add the dashed cyan center line, and make both glow. Recolor the speed pads and mud.
3. **City.** Remove the trees. Add the buildings with lit windows and the stars.
4. **Car 1.** Add the `CARS` list and build the orange coupe from `design/car1.png`. Player 1 drives it.
5. **Car 2.** Add the green version for player 2.
6. **Car lights.** Underglow for both cars, glowing tail lights, then headlights if it stays smooth.
7. **HUD.** Restyle the lap counter, warnings, countdown and place screens.
8. **Bloom test.** Add bloom behind `THEME.BLOOM`. Test on the Chromebook from the offline file. Keep it on only if the game stays smooth.

After step 3 and again after step 8, rebuild the offline file and test it on the Chromebook.
