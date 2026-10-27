# Progress Log

One entry per work session. For each step: what I asked for, what worked, what went wrong, and what I changed myself.

## Oct 25, 2026 — Steps 1, 2 and 3

### What I asked for

- Step 1: Build the track from my drawing. Flat road, grass, start line on the left straight. (Finished the night before, pushed today.)
- Step 2: 3-2-1 countdown, lap counter on each screen, laps as a setting, FIRST PLACE! / SECOND PLACE end screens.
- Step 3: Fast and slippery driving, grass slows you down, cars ricochet. Later I asked for a bump to the back half of a car to make it swerve.

### What worked

- The track is a list of points down the middle of the road, traced from my drawing. Press M for an overhead map to compare it to the paper.
- The game has four states: idle, countdown, racing, finished.
- Cars now have a direction they point and a separate direction they move, so they drift. One block of numbers called DRIVE controls the feel.

### What went wrong and how we fixed it

- We decided cars go UP the left straight (clockwise), not counterclockwise like the plan said, because that matches the arrow on my drawing.
- It was easy to cheat by driving across the grass in the middle. Fix: the lap is now 16 checkpoints that only count on the road, and the screen says GO BACK TO THE TRACK or WRONG WAY.
- Grass wasn't slow enough. Fix: grass now caps you at half speed and drags you down hard.

### Numbers I changed myself

- ACCEL 45 -> 60 (faster launch)
- DRAG 0.7 -> 0.75 (coasts a little longer)
- BOUNCE 0.9 -> 2.9 -> 2.0 -> 1.5 (2.9 was total pinball, 1.5 is fun but not crazy)
- Tried width 24 for the road, went back to 14

### What each number does

| Number | What it does |
|---|---|
| TOP_SPEED | fastest on the road |
| ACCEL | how quick the launch is |
| TURN | how sharp it steers |
| GRIP | how fast a slide stops (1 = rails, 0 = ice) |
| DRAG | speed you keep after coasting one second |
| OFFROAD and GRASS_DRAG | how slow and sticky the grass is |
| BOUNCE | how hard cars bounce off each other (above 1 adds energy) |
| SPIN | how much a hit to the back half makes a car swerve |

### New things I learned

- `git add` puts files in the box, `git commit` seals it, `git push` sends it to GitHub.
- The game is live at https://shiffnergames.github.io/accelerate/ and updates every time I push.
- Press F12 and type `ACCEL.DRIVE.GRIP = 0.7` to try a number without reloading.

Next: Step 4, speed pads and mud.
