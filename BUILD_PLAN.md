# Build Plan

A 3D split-screen racing game where 2 players play on 1 keyboard.

Each step below is one request to Claude Code. Do them in order. Finish and play-test a step before starting the next one. Each step should end with a commit.

## Design decisions (from the design doc)

- First to finish 3 laps wins. Laps per track is a setting, so some tracks can have more or fewer.
- Driving is fast and slippery.
- Off the road: speed drops to 60% of normal.
- Race starts with a 3-2-1 countdown.
- Lap counter at the top of the screen.
- Winner sees FIRST PLACE! Loser sees SECOND PLACE.
- When cars hit each other, they ricochet.
- Red drives with WASD, Blue drives with the arrow keys.

## Track 1 (from the drawing)

Counterclockwise, start line on the left straight.

| Feature | Where | Rule |
|---|---|---|
| Start/finish line | Left straight | Lap counts when you cross it going the right way |
| Speed pad | Bottom-left, after the start | Boost |
| Speed pad | Top straight | Boost |
| Jump | Top, before the speed pad | Car leaves the ground for a moment |
| Half-pipe wall | Inside of the bottom-middle turn | Car can ride up the wall like a half pipe |
| Mud | Bottom-right inner section | Slows to 60% speed |
| Mud | Right side, after the corner | Slows to 60% speed |
| Deer crossing | Right side | Deer crosses the road whenever you turn the corner |
| Loop-de-loop | Right straight | Car goes around a vertical loop |
| Scenery | Buildings (left), rocks (top-left and right), dumpster (bottom) | Decoration, off the road |

## Build order

### Step 1: The track
Ask: "Build the track from my drawing (attached photo). Flat road, grass around it, a start/finish line on the left straight, cars go counterclockwise. No features yet."

Done when: both cars can drive a full lap on a road shaped like the drawing.

### Step 2: The race rules
Ask: "Add a 3-2-1 countdown before the race starts, a lap counter at the top of each screen, 3 laps to win (make the number of laps a setting), and end screens that say FIRST PLACE! for the winner and SECOND PLACE for the other player."

Done when: a full race runs from countdown to end screen.

### Step 3: Driving feel
Ask: "Make the driving fast and slippery. When a car is off the road, drop its speed to 60% of normal. When the two cars hit each other, make them ricochet."

Then open the code and find the numbers for top speed, acceleration, turning, and grip. Change them yourself until it feels right. Write down what each number does in the process log.

Done when: both players agree it feels fast and slippery, and bumping is fun.

### Step 4: Speed pads and mud
Ask: "Add zones on the road that change the car's speed: speed pads that boost you, and mud that slows you to 60%. Put them where they are on my drawing."

Speed pads and mud are the same kind of thing (a zone that changes speed) with different numbers. Try changing the boost amount yourself.

Done when: driving over a pad boosts you and driving through mud slows you.

### Step 5: Jump
Ask: "Add a jump ramp on the top straight. The car leaves the ground, flies for a moment, and lands."

Done when: the jump looks right from the chase camera and the car lands on the road.

### Step 6: Half-pipe wall
Ask: "Add a curved wall on the inside of the bottom-middle turn that the car can ride up like a half pipe and come back down."

Done when: you can ride the wall through the turn without falling off the track.

### Step 7: Deer crossing
Ask: "On the right side of the track, make a deer run across the road whenever a car comes around the corner. If a car hits the deer, the car slows down."

Done when: the deer appears at the right moment and can be dodged.

### Step 8: Loop-de-loop (stretch goal)
Ask: "Add a loop-de-loop on the right straight. The car drives up and around a vertical loop and the camera follows."

This is the hardest feature on the page. It is fine if it comes last or does not make it in. The game is complete without it.

### Step 9: Scenery and polish
Ask for the buildings, rocks, and dumpster from the drawing. Then: a title screen with the game's name, engine sound, skid sound when off road, best-lap time.

## After every step

1. Play-test with both players.
2. Add bugs and ideas to the list.
3. Commit with a message that says what changed.
4. Write a process log entry: what you asked for, what worked, what you changed yourself.

## Stretch ideas (only after Step 9)

- A second track with a different number of laps
- Nitro button (name idea: Overdrive)
- Time trial mode against your own best lap
- Online play against another computer
