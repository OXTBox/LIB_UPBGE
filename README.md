# LIB_UPBGE

Small Blender Game Engine templates (Blender-Game-Engine-Templates, Apache 2.0, kept local in
`templates/`), taken apart into **text specs** so the same demos can be made in **Vibecode3D**
and **xt3d**. The owner: "UPBGE are examples we should produce, we have a bunch of them already."

- `specs/<template>.md`: every scene and object (type, position, rotation, size, colour, mesh
  size), game properties, logic bricks (sensors, controllers, actuators, their settings and
  links) and the embedded Python. Made by `tools/dump_blend.py` with UPBGE 0.50 headless:
  `C:\LIB_BIN\upbge-0.50\blender.exe --background X.blend --python dump_blend.py -- X.md`
  (UPBGE has to run from a Windows drive; it lives in `C:\LIB_BIN\upbge-0.50`). No image is
  opened or described.

## The templates and our games

| Template | What it is | Ours already | To make |
|---|---|---|---|
| pong | two paddles (W/S, arrows), ball, score walls | VectorPong3D, BatDuel | - |
| breakout_like | paddle, ball, 60-odd bricks | WallBreaker, JaiAlaiBlock | - |
| Rotation_Shooter | spin and shoot, spawned "Cubeeroids" | VectorBlobApocalypse | - |
| CUBE_INVADERS | invader rows of cubes | SkyRaiders (closest) | an exact Cube Invaders |
| SideScroll_Shooter | side-scrolling shooter | - | **new** |
| Dodge_Tunnel | cubes fly at you down a tunnel from 4 spawners; dodge in x/y | RockField (closest) | **new** |
| TrenchRun_Torus_IV | ride the trench of a torus, pillboxes fire, camera on the player | - | **new** |
| Simple_Player_Maze (+ _Waypoints) | player in a maze; patrols on waypoints | DotMaze, PromptAndGlazeMaze | waypoint patrols as a demo |
| Pits_Vines_Ladders | platformer: pits, vines, ladders | VineRun, ShaftDescent | ladders |
| 3rd_Person_follow_camera | third-person character, following camera | Amazing Couple | - |
| FPS+Enemies+WallRun | first person, enemies, wall running | Hunter, uDead | wall run |
| MakeHumanLady_walkin | a walking character | LIB_MOCAP walk clips | - |
| Mouse_Tracker_01 / _Grid / _RTS | a marker follows the mouse; grid cells light; RTS: click places a GoRing, the unit steers to it (seek, slows in a buffer ring) | GeneticAnomaly / uDead clicks | **new**: the RTS click-to-go demo |
| Sigils_01 / _02 | a sigil plane, UV scrolling, Space cycles colour | - | **new** (and LIB_DEE's sigils) |
| TextScroll2 | a title and a text crawl moving away | Sequencer Type / Term | a crawl clip |
| TextReader_filepath / _textBlock | read text from a file / a text block into the game | Sequencer, LIB_GENERICA | - |
| path_to_scripts | utility: where the scripts are | - | - |
