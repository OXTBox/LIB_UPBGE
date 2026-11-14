# Pits_Vines_Ladders.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=10.71

### GroundPond  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 80.00, 2.00) (hidden)
mesh "Cube.006": 76 verts 152 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['GroundPond']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### GroundBottom  [MESH]  pos=(0.00, 0.00, -27.64) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 111.51, 2.00)
mesh "Cube.011": 8 verts 6 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False

### GroundLeftHole  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 80.00, 2.00) (hidden)
mesh "Cube.016": 20 verts 12 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False
- prop Lefthole (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['GroundLeftHole']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftWall_LeftHole  [MESH]  pos=(0.00, -36.14, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundLeftHole (hidden)
mesh "Cube.023": 8 verts 6 faces
physics: STATIC mass=1.0
- prop LeftWall (BOOL) = False
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['LeftWall_LeftHole']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['LeftWall_LeftHole']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, LeftWall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundLeftHole, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "LeftWall": to_property=TopGroundSpawner, subject=LeftWall, body_type=TEXT, body_message=LeftWall1, body_property=LeftWall1
- ACTUATOR MESSAGE "Message.001": to_property=RightPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### RightWall_LeftHole  [MESH]  pos=(0.00, 35.30, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundLeftHole (hidden)
mesh "Cube.022": 8 verts 6 faces
physics: STATIC mass=1.0
- prop RightWall (FLOAT) = 0.0
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWall_LeftHole']...AndController,), property=Player
- SENSOR DELAY "Delay" -> [And.001]: controllers=(bpy.data.objects['RightWall_LeftHole']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, Rightwall, Spawn]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundLeftHole, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Rightwall": to_property=TopGroundSpawner, subject=RightWall, body_type=TEXT, body_message=RightWall, body_property=RightWall
- ACTUATOR MESSAGE "Spawn": to_property=LeftPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### GroundRightHole  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 80.00, 2.00) (hidden)
mesh "Cube.017": 20 verts 12 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False
- prop RightHole (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['GroundRightHole']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [END]
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftWall_RightHole  [MESH]  pos=(0.00, -36.14, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundRightHole (hidden)
mesh "Cube.025": 8 verts 6 faces
physics: STATIC mass=1.0
- prop LeftWall (BOOL) = False
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['LeftWall_RightHole']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['LeftWall_RightHole']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, LeftWall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundRightHole, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "LeftWall": to_property=TopGroundSpawner, subject=LeftWall, body_type=TEXT, body_message=LeftWall1, body_property=LeftWall1
- ACTUATOR MESSAGE "Message.001": to_property=RightPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### RightWall_RightHole  [MESH]  pos=(0.00, 35.30, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundRightHole (hidden)
mesh "Cube.024": 8 verts 6 faces
physics: STATIC mass=1.0
- prop RightWall (FLOAT) = 0.0
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWall_RightHole']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['RightWall_RightHole']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, Rightwall, Spawn]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundRightHole, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Rightwall": to_property=TopGroundSpawner, subject=RightWall, body_type=TEXT, body_message=RightWall, body_property=RightWall
- ACTUATOR MESSAGE "Spawn": to_property=LeftPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### GroundTwoHoles  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 80.00, 2.00) (hidden)
mesh "Cube.018": 32 verts 18 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False
- prop TwoHoles (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['GroundTwoHoles']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftWall_TwoHoles  [MESH]  pos=(0.00, -36.14, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundTwoHoles (hidden)
mesh "Cube.027": 8 verts 6 faces
physics: STATIC mass=1.0
- prop LeftWall (BOOL) = False
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['LeftWall_TwoHoles']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['LeftWall_TwoHoles']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, LeftWall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundTwoHoles, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "LeftWall": to_property=TopGroundSpawner, subject=LeftWall, body_type=TEXT, body_message=LeftWall1, body_property=LeftWall1
- ACTUATOR MESSAGE "Message.001": to_property=RightPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### RightWall_TwoHoles  [MESH]  pos=(0.00, 35.30, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00) parent=GroundTwoHoles (hidden)
mesh "Cube.026": 8 verts 6 faces
physics: STATIC mass=1.0
- prop RightWall (FLOAT) = 0.0
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWall_TwoHoles']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['RightWall_TwoHoles']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, RightWall, spawn]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundTwoHoles, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "RightWall": to_property=TopGroundSpawner, subject=RightWall, body_type=TEXT, body_message=RightWall, body_property=RightWall
- ACTUATOR MESSAGE "spawn": to_property=LeftPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### GroundSolid  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 80.00, 2.00) (hidden)
mesh "Cube.003": 8 verts 6 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['GroundSolid']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftWall_GroundSolid  [MESH]  pos=(0.00, -36.14, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundSolid (hidden)
mesh "Cube.020": 8 verts 6 faces
physics: STATIC mass=1.0
- prop LeftWall (BOOL) = False
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['LeftWall_GroundSolid']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['LeftWall_GroundSolid']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, LeftWall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundSolid, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "LeftWall": to_property=TopGroundSpawner, subject=LeftWall, body_type=TEXT, body_message=LeftWall, body_property=LeftWall
- ACTUATOR MESSAGE "Message.001": to_property=RightPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### RightWall_GroundSolid  [MESH]  pos=(0.00, 35.30, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundSolid (hidden)
mesh "Cube.021": 8 verts 6 faces
physics: STATIC mass=1.0
- prop RightWall (FLOAT) = 0.0
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWall_GroundSolid']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['RightWall_GroundSolid']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, Rightwall, Spawn]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundSolid, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Rightwall": to_property=TopGroundSpawner, subject=RightWall, body_type=TEXT, body_message=RightWall, body_property=RightWall
- ACTUATOR MESSAGE "Spawn": to_property=LeftPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### LeftWallBottom  [MESH]  pos=(0.00, -43.32, -15.54) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundBottom
mesh "Cube.010": 8 verts 6 faces
physics: STATIC mass=1.0
- prop LeftWallDown (BOOL) = False
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['LeftWallBottom']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['LeftWallBottom']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, LeftWall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=RoomDespawnALL, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "LeftWall": to_property=TopGroundSpawner, subject=LeftWall, body_type=TEXT, body_message=LeftWall1, body_property=LeftWall1
- ACTUATOR MESSAGE "Message.001": to_property=RightPlayerSpawnBottom, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### RightWallBottom  [MESH]  pos=(0.00, 41.45, -15.54) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundBottom
mesh "Cube.008": 8 verts 6 faces
physics: STATIC mass=1.0
- prop RightWallDown (FLOAT) = 0.0
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWallBottom']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['RightWallBottom']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, Rightwall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=RoomDespawnALL, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Rightwall": to_property=TopGroundSpawner, subject=RightWall, body_type=TEXT, body_message=RightWall, body_property=RightWall
- ACTUATOR MESSAGE "Message.001": to_property=LeftPlayerSpawnBottom, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### GroundPond_Vine  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 80.00, 2.00) (hidden)
mesh "Cube.015": 76 verts 152 faces
physics: STATIC mass=1.0
- prop Ground (BOOL) = False
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['GroundPond_Vine']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftWall_Pond  [MESH]  pos=(0.00, -36.14, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundPond_Vine (hidden)
mesh "Cube.029": 8 verts 6 faces
physics: STATIC mass=1.0
- prop LeftWall (BOOL) = False
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['LeftWall_Pond']...AndController,), property=Player
- SENSOR DELAY "0" -> [And.001]: controllers=(bpy.data.objects['LeftWall_Pond']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, LeftWall, Message.001]
- CONTROLLER LOGIC_AND "And.001" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundPond_Vine, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "LeftWall": to_property=TopGroundSpawner, subject=LeftWall, body_type=TEXT, body_message=LeftWall1, body_property=LeftWall1
- ACTUATOR MESSAGE "Message.001": to_property=RightPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### RightWall_Pond  [MESH]  pos=(0.00, 35.30, 8.68) rot_deg=(0.00, 0.00, 0.00) size=(20.00, 2.00, 24.00) parent=GroundPond_Vine (hidden)
mesh "Cube.030": 8 verts 6 faces
physics: STATIC mass=1.0
- prop RightWall (FLOAT) = 0.0
- prop Wall (BOOL) = True
- SENSOR COLLISION "Collision" -> [And]: controllers=(bpy.data.objects['RightWall_Pond']...AndController,), property=Player
- SENSOR DELAY "Delay" -> [Or]: controllers=(bpy.data.objects['RightWall_Pond']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Message, RightWall, Spawn]
- CONTROLLER LOGIC_AND "Or" -> [Visibility]
- ACTUATOR MESSAGE "Message": to_property=GroundPond_Vine, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "RightWall": to_property=TopGroundSpawner, subject=RightWall, body_type=TEXT, body_message=RightWall, body_property=RightWall
- ACTUATOR MESSAGE "Spawn": to_property=LeftPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn
- ACTUATOR VISIBILITY "Visibility": 

### HoleMaker1  [MESH]  pos=(0.00, -17.00, -2.22) rot_deg=(0.00, 0.00, 0.00) size=(8.00, 8.00, 7.09) (hidden)
mesh "Cube.002": 8 verts 6 faces
physics: NO_COLLISION mass=1.0

### PondMaker  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(14.51, 25.95, 8.72) (hidden)
mesh "Cylinder": 64 verts 34 faces
physics: NO_COLLISION mass=1.0

### HoleMake2  [MESH]  pos=(0.00, 17.00, -2.22) rot_deg=(0.00, 0.00, 0.00) size=(8.00, 8.00, 7.09) (hidden)
mesh "Cube.019": 8 verts 6 faces
physics: NO_COLLISION mass=1.0

### Player  [MESH]  pos=(0.00, -28.67, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00) (hidden)
mesh "Cube.009": 8 verts 6 faces colour=#CCCCCC
physics: CHARACTER mass=1.0
- prop Jump (BOOL) = False
- prop Hooked (BOOL) = False
- prop Climb (BOOL) = False
- prop Player (BOOL) = True
- prop VineVis (BOOL) = False
- SENSOR KEYBOARD "LEFT" -> [LEFT]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "RIGHT" -> [RIGHT]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "JUMP" -> [JUMP, UNHOOK]: controllers=(bpy.data.objects['Player']...AndController, bpy.data.objects['Player']...AndController), key=SPACE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "JUMPT" -> [JUMPT]: controllers=(bpy.data.objects['Player']...AndController,), evaluation_type=PROPEQUAL, property=Jump, value=TRUE, value_min=TRUE
- SENSOR COLLISION "Ground" -> [JUMPF]: controllers=(bpy.data.objects['Player']...AndController,), property=Ground
- SENSOR COLLISION "HOOK" -> [HOOK.001]: controllers=(bpy.data.objects['Player']...AndController,), property=VINE
- SENSOR PROPERTY "VINET" -> [HOOK]: controllers=(bpy.data.objects['Player']...AndController,), evaluation_type=PROPEQUAL, property=VineVis, value=TRUE, value_min=TRUE
- SENSOR PROPERTY "HookedT" -> [HOOK, UNHOOK]: controllers=(bpy.data.objects['Player']...AndController, bpy.data.objects['Player']...AndController), evaluation_type=PROPEQUAL, property=Hooked, value=TRUE, value_min=TRUE
- SENSOR KEYBOARD "UP" -> [UP]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "DOWN" -> [DOWN]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "CLIMB" -> [DOWN, UP]: controllers=(bpy.data.objects['Player']...AndController, bpy.data.objects['Player']...AndController), evaluation_type=PROPEQUAL, property=Climb, value=TRUE, value_min=TRUE
- SENSOR NEAR "Ladder" -> [CLIMB]: controllers=(bpy.data.objects['Player']...AndController,), property=Ladder, distance=3.0, reset_distance=3.5
- SENSOR NEAR "Near" -> [CLIMBF]: invert=True, controllers=(bpy.data.objects['Player']...AndController,), property=Ladder, distance=3.0, reset_distance=3.5
- SENSOR COLLISION "EXIT" -> [EXIT]: controllers=(bpy.data.objects['Player']...AndController,), property=Wall
- SENSOR MESSAGE "Vine" -> [And]: controllers=(bpy.data.objects['Player']...AndController,), subject=Vine
- SENSOR MESSAGE "NoVine" -> [And.001]: controllers=(bpy.data.objects['Player']...AndController,), subject=NoVine
- CONTROLLER LOGIC_AND "LEFT" -> [LEFT]
- CONTROLLER LOGIC_AND "RIGHT" -> [RIGHT]
- CONTROLLER LOGIC_AND "JUMP" -> [JUMPT]
- CONTROLLER LOGIC_AND "JUMPT" -> [JUMP]
- CONTROLLER LOGIC_AND "JUMPF" -> [JUMPF, ResetROT]
- CONTROLLER LOGIC_AND "HOOK.001" -> [HOOK]
- CONTROLLER LOGIC_AND "HOOK" -> [VineHook, NoPhys, JUMPF]
- CONTROLLER LOGIC_AND "UNHOOK" -> [UNHOOK, UnParent, JUMPT.001, HookedFalse]
- CONTROLLER LOGIC_AND "UP" -> [UP, NoPhysics]
- CONTROLLER LOGIC_AND "DOWN" -> [DOWN]
- CONTROLLER LOGIC_AND "CLIMB" -> [CLIMBT]
- CONTROLLER LOGIC_AND "CLIMBF" -> [PHYSICS, CLIMBF]
- CONTROLLER LOGIC_AND "EXIT" -> [END]
- CONTROLLER LOGIC_AND "And" -> [VINE]
- CONTROLLER LOGIC_AND "And.001" -> [NoVINE]
- ACTUATOR MOTION "LEFT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.2, offset_location=(0.0, -0.2, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "RIGHT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.2, offset_location=(0.0, 0.2, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "JUMPT": mode=ASSIGN, property=Jump, value=TRUE, object_property=TRUE
- ACTUATOR MOTION "JUMP": mode=OBJECT_CHARACTER, servo_mode=SERVO_LINEAR, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_servo_limit_y=True, use_servo_limit_z=True, use_character_jump=True
- ACTUATOR PROPERTY "JUMPF": mode=ASSIGN, property=Jump, value=FALSE, object_property=FALSE
- ACTUATOR ACTION "ResetROT": play_mode=PLAY, action=obj:ResetRotation, blend_mode=BLEND
- ACTUATOR PROPERTY "HOOK": mode=ASSIGN, property=Hooked, value=TRUE, object_property=TRUE
- ACTUATOR PARENT "VineHook": mode=SETPARENT, object=obj:VineHook
- ACTUATOR EDIT_OBJECT "NoPhys": mode=DYNAMICS, dynamic_operation=SUSPENDPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "UNHOOK": mode=DYNAMICS, dynamic_operation=RESTOREPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR PARENT "UnParent": mode=REMOVEPARENT, use_compound=True, use_ghost=True
- ACTUATOR PROPERTY "HookedFalse": mode=ASSIGN, property=Hooked, value=FALSE, object_property=FALSE
- ACTUATOR PROPERTY "JUMPT.001": mode=ASSIGN, property=Jump, value=TRUE, object_property=TRUE
- ACTUATOR EDIT_OBJECT "NoPhysics": mode=DYNAMICS, dynamic_operation=SUSPENDPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MOTION "UP": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=0.3, offset_location=(0.0, 0.0, 0.3), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "DOWN": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_z=-0.3, offset_location=(0.0, 0.0, -0.3), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR PROPERTY "CLIMBT": mode=ASSIGN, property=Climb, value=TRUE, object_property=TRUE
- ACTUATOR EDIT_OBJECT "PHYSICS": mode=DYNAMICS, dynamic_operation=RESTOREPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR PROPERTY "CLIMBF": mode=ASSIGN, property=Climb, value=FALSE, object_property=FALSE
- ACTUATOR EDIT_OBJECT "END": mode=ENDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR PROPERTY "VINE": mode=ASSIGN, property=VineVis, value=TRUE, object_property=TRUE
- ACTUATOR PROPERTY "NoVINE": mode=ASSIGN, property=VineVis, value=FALSE, object_property=FALSE

### PointTop  [LIGHT]  pos=(0.00, 0.00, 11.06) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### PointBottom  [LIGHT]  pos=(0.00, 0.00, -14.68) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### CameraToggle  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Lights (BOOL) = False
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['CameraToggle']...AndController,), subject=On
- SENSOR MESSAGE "Message.001" -> [And.001]: controllers=(bpy.data.objects['CameraToggle']...AndController,), subject=Off
- CONTROLLER LOGIC_AND "And" -> [Motion]
- CONTROLLER LOGIC_AND "And.001" -> [Motion.001]
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_y=-3.142, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, -3.142, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Motion.001": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_y=3.142, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 3.142, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Camera  [CAMERA]  pos=(47.67, 0.21, 27.20) rot_deg=(54.46, 0.00, 90.00) size=(0.00, 0.00, 0.00)
camera: lens=29.0 type=PERSP ortho_scale=7.31
physics: NO_COLLISION mass=1.0
- SENSOR DELAY "Always" -> []: controllers=()
- CONTROLLER LOGIC_AND "And" -> []
- ACTUATOR SCENE "Edit Object": mode=CAMERA

### VINESWING  [MESH]  pos=(0.00, 0.00, 21.47) rot_deg=(-82.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube.007": 8 verts 6 faces
physics: NO_COLLISION mass=1.0
- prop ROT (BOOL) = False
- prop Visible (BOOL) = False
- prop Hooked (BOOL) = False
- SENSOR DELAY "Delay" -> [And]: controllers=(bpy.data.objects['VINESWING']...AndController,), delay=160, use_repeat=True
- SENSOR PROPERTY "RIGHt" -> [And.001]: controllers=(bpy.data.objects['VINESWING']...AndController,), evaluation_type=PROPEQUAL, property=ROT, value=FALSE, value_min=FALSE
- SENSOR PROPERTY "LEFT" -> [And.002]: controllers=(bpy.data.objects['VINESWING']...AndController,), evaluation_type=PROPEQUAL, property=ROT, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "And" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [RIGHT]
- CONTROLLER LOGIC_AND "And.002" -> [LEFT]
- ACTUATOR PROPERTY "Property": mode=TOGGLE, property=ROT
- ACTUATOR MOTION "RIGHT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_x=0.017, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.017, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "LEFT": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_x=-0.017, offset_location=(0.0, 0.0, 0.0), offset_rotation=(-0.017, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### Vine  [MESH]  pos=(0.00, 0.00, 12.79) rot_deg=(0.00, 0.00, 0.00) size=(0.40, 0.40, 25.02) parent=VINESWING
mesh "Cube.001": 8 verts 6 faces colour=#CCCCCC
physics: RIGID_BODY mass=1.0
- prop VINE (BOOL) = True
- prop Visible (BOOL) = False
- SENSOR MESSAGE "Show" -> [Show]: controllers=(bpy.data.objects['Vine']...AndController,), subject=Show
- SENSOR PROPERTY "VisibleT" -> [Visible]: controllers=(bpy.data.objects['Vine']...AndController,), evaluation_type=PROPEQUAL, property=Visible, value=TRUE, value_min=TRUE
- SENSOR MESSAGE "Hide" -> [And.003]: controllers=(bpy.data.objects['Vine']...AndController,), subject=Hide
- SENSOR PROPERTY "VisibleF" -> [Hide]: controllers=(bpy.data.objects['Vine']...AndController,), evaluation_type=PROPEQUAL, property=Visible, value=FALSE, value_min=FALSE
- CONTROLLER LOGIC_AND "Show" -> [Show]
- CONTROLLER LOGIC_AND "Visible" -> [Visibility, PHYS]
- CONTROLLER LOGIC_AND "And.003" -> [Hide]
- CONTROLLER LOGIC_AND "Hide" -> [Visibility.001, NoPHYS]
- ACTUATOR PROPERTY "Show": mode=ASSIGN, property=Visible, value=True, object_property=True
- ACTUATOR VISIBILITY "Visibility": use_visible=True, apply_to_children=True
- ACTUATOR EDIT_OBJECT "PHYS": mode=DYNAMICS, dynamic_operation=RESTOREPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR PROPERTY "Hide": mode=ASSIGN, property=Visible, value=FALSE, object_property=FALSE
- ACTUATOR VISIBILITY "Visibility.001": apply_to_children=True
- ACTUATOR EDIT_OBJECT "NoPHYS": mode=DYNAMICS, dynamic_operation=SUSPENDPHY, up_axis=UPAXISZ, track_axis=TRACKAXISY, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### VineHook  [EMPTY]  pos=(0.00, 0.00, -1.18) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00) parent=VINESWING
physics: NO_COLLISION mass=1.0
- prop VINE (FLOAT) = 0.0

### TopGroundSpawner  [MESH]  pos=(0.00, 0.00, -3.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 0.00)
mesh "Circle": 32 verts 0 faces
physics: STATIC mass=1.0
- prop Room (INT) = 0
- prop count (INT) = 0
- SENSOR MESSAGE "LeftWall" -> [And]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), subject=LeftWall
- SENSOR MESSAGE "RightWall" -> [And.009]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), subject=RightWall
- SENSOR PROPERTY "Room<0" -> [And.001]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPLESSTHAN, property=Room, value=0, value_min=0
- SENSOR PROPERTY "Room>4" -> [And.002]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPGREATERTHAN, property=Room, value=4, value_min=4
- SENSOR PROPERTY "Room0" -> [And.003]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=0, value_min=0
- SENSOR PROPERTY "Room4" -> [And.004]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=4, value_min=4
- SENSOR PROPERTY "Room1" -> [And.005]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=1, value_min=1
- SENSOR PROPERTY "Room2" -> [And.006]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=2, value_min=2
- SENSOR PROPERTY "Room3" -> [And.007]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=3, value_min=3
- SENSOR PROPERTY "CHANGED" -> [LADDERS, Lights]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController, bpy.data.objects['TopGroundSpawner']...AndController), evaluation_type=PROPCHANGED, property=Room
- SENSOR DELAY "5" -> [Lights]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), delay=5
- SENSOR PROPERTY "Not2" -> [Not2]: controllers=(bpy.data.objects['TopGroundSpawner']...AndController,), evaluation_type=PROPNEQUAL, property=Room, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [Room-1, CamOff]
- CONTROLLER LOGIC_AND "And.009" -> [Room+1, CamOff]
- CONTROLLER LOGIC_AND "And.001" -> [4]
- CONTROLLER LOGIC_AND "And.002" -> [0]
- CONTROLLER LOGIC_AND "And.003" -> [Room0]
- CONTROLLER LOGIC_AND "And.004" -> [Room4]
- CONTROLLER LOGIC_AND "And.005" -> [Room1]
- CONTROLLER LOGIC_AND "And.006" -> [Room2, VINE, Vine]
- CONTROLLER LOGIC_AND "And.007" -> [Room3]
- CONTROLLER LOGIC_AND "LADDERS" -> [LADDERS]
- CONTROLLER LOGIC_AND "Lights" -> [CamON]
- CONTROLLER LOGIC_AND "Not2" -> [HideVine, NoVine]
- ACTUATOR PROPERTY "Room-1": mode=ADD, property=Room, value=-1, object_property=-1
- ACTUATOR PROPERTY "Room+1": mode=ADD, property=Room, value=1, object_property=1
- ACTUATOR MESSAGE "CamOff": to_property=CameraToggle, subject=Off, body_type=TEXT, body_message=Off, body_property=Off
- ACTUATOR PROPERTY "4": mode=ASSIGN, property=Room, value=4, object_property=4
- ACTUATOR PROPERTY "0": mode=ASSIGN, property=Room, value=0, object_property=0
- ACTUATOR EDIT_OBJECT "Room0": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:GroundSolid, track_object=obj:GroundSolid, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "Room4": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:GroundTwoHoles, track_object=obj:GroundTwoHoles, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "Room1": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:GroundLeftHole, track_object=obj:GroundLeftHole, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR EDIT_OBJECT "Room2": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:GroundPond_Vine, track_object=obj:GroundPond_Vine, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MESSAGE "VINE": to_property=Vine, subject=Show, body_type=TEXT, body_message=Show, body_property=Show
- ACTUATOR MESSAGE "Vine": to_property=Player, subject=Vine, body_type=TEXT, body_message=Vine, body_property=Vine
- ACTUATOR EDIT_OBJECT "Room3": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:GroundRightHole, track_object=obj:GroundRightHole, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MESSAGE "LADDERS": to_property=LadderCheck, subject=Room, body_type=TEXT, body_message=Room, body_property=Room
- ACTUATOR MESSAGE "CamON": to_property=CameraToggle, subject=On, body_type=TEXT, body_message=On, body_property=On
- ACTUATOR MESSAGE "HideVine": to_property=Vine, subject=Hide, body_type=TEXT, body_message=Hide, body_property=Hide
- ACTUATOR MESSAGE "NoVine": to_property=Player, subject=NoVine, body_type=TEXT, body_message=NoVine, body_property=NoVine

### LeftPlayerSpawn  [EMPTY]  pos=(0.00, -29.32, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Spawn (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['LeftPlayerSpawn']...AndController,), subject=Spawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Player, track_object=obj:Player, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LeftPlayerSpawnBottom  [EMPTY]  pos=(0.00, -38.51, -23.92) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Spawn (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['LeftPlayerSpawnBottom']...AndController,), subject=Spawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Player, track_object=obj:Player, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### RightPlayerSpawn  [EMPTY]  pos=(0.00, 28.24, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Spawn (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['RightPlayerSpawn']...AndController,), subject=Spawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Player, track_object=obj:Player, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### RightPlayerSpawnBottom  [EMPTY]  pos=(0.00, 36.01, -23.92) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Spawn (FLOAT) = 0.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['RightPlayerSpawnBottom']...AndController,), subject=Spawn
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Player, track_object=obj:Player, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LadderCheck  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- prop Room (INT) = 0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['LadderCheck']...AndController,), subject=Room
- SENSOR PROPERTY "1" -> [1]: controllers=(bpy.data.objects['LadderCheck']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=1, value_min=1
- SENSOR PROPERTY "3" -> [3]: use_pulse_true_level=True, controllers=(bpy.data.objects['LadderCheck']...AndController,), evaluation_type=PROPEQUAL, value=3, value_min=3
- SENSOR PROPERTY "4" -> [4]: controllers=(bpy.data.objects['LadderCheck']...AndController,), evaluation_type=PROPEQUAL, property=Room, value=4, value_min=4
- SENSOR PROPERTY "0" -> [And.001]: controllers=(bpy.data.objects['LadderCheck']...OrController,), evaluation_type=PROPEQUAL, property=Room, value=0, value_min=0
- SENSOR PROPERTY "2" -> [And.001]: controllers=(bpy.data.objects['LadderCheck']...OrController,), evaluation_type=PROPEQUAL, property=Room, value=2, value_min=2
- CONTROLLER LOGIC_AND "And" -> [COPY]
- CONTROLLER LOGIC_AND "1" -> [Left]
- CONTROLLER LOGIC_AND "3" -> [RIght, HideL]
- CONTROLLER LOGIC_AND "4" -> [Left, RIght]
- CONTROLLER LOGIC_OR "And.001" -> [HideL, HideR]
- ACTUATOR PROPERTY "COPY": mode=COPY, property=Room, value=Room, object=obj:TopGroundSpawner, object_property=Room
- ACTUATOR MESSAGE "Left": to_property=LadderLeft, subject=Ladder, body_type=TEXT, body_message=Ladder, body_property=Ladder
- ACTUATOR MESSAGE "RIght": to_property=LadderRight, subject=Ladder, body_type=TEXT, body_message=Ladder, body_property=Ladder
- ACTUATOR MESSAGE "HideL": to_property=LadderLeft, subject=Hide, body_type=TEXT, body_message=Hide, body_property=Hide
- ACTUATOR MESSAGE "HideR": to_property=LadderRight, subject=Hide, body_type=TEXT, body_message=Hide, body_property=Hide

### RoomDespawnALL  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- SENSOR MESSAGE "Message" -> [And]: controllers=(bpy.data.objects['RoomDespawnALL']...AndController,), subject=Despawn
- CONTROLLER LOGIC_AND "And" -> [Message, Message.001, Message.002, Message.003, Message.004]
- ACTUATOR MESSAGE "Message": to_property=GroundLeftHole, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Message.001": to_property=GroundPond_Vine, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Message.002": to_property=GroundRightHole, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Message.003": to_property=GroundTwoHoles, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn
- ACTUATOR MESSAGE "Message.004": to_property=GroundSolid, subject=Despawn, body_type=TEXT, body_message=Despawn, body_property=Despawn

### LadderLeft  [MESH]  pos=(-2.41, -18.15, -14.73) rot_deg=(0.00, 0.00, 0.00) size=(0.59, 4.51, 25.12)
mesh "Cube.004": 80 verts 44 faces
physics: STATIC mass=1.0
- prop Ladder (INT) = 0
- SENSOR KEYBOARD "Keyboard" -> [And.001]: controllers=(bpy.data.objects['LadderLeft']...OrController,), key=X, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR MESSAGE "Ladder" -> [And.001]: controllers=(bpy.data.objects['LadderLeft']...OrController,), subject=Ladder
- SENSOR PROPERTY "Ladder1" -> [Ladder]: controllers=(bpy.data.objects['LadderLeft']...AndController,), evaluation_type=PROPEQUAL, property=Ladder, value=1, value_min=1
- SENSOR MESSAGE "HIDE" -> [HIDE]: controllers=(bpy.data.objects['LadderLeft']...AndController,), subject=Hide
- SENSOR PROPERTY "Ladder0" -> [And]: controllers=(bpy.data.objects['LadderLeft']...AndController,), evaluation_type=PROPEQUAL, property=Ladder, value=0, value_min=0
- CONTROLLER LOGIC_OR "And.001" -> [Random]
- CONTROLLER LOGIC_AND "Ladder" -> [Ladder1]
- CONTROLLER LOGIC_AND "HIDE" -> [HIDE]
- CONTROLLER LOGIC_AND "And" -> [Visibility]
- ACTUATOR RANDOM "Random": seed=7699, property=Ladder, distribution=INT_UNIFORM, chance=0.1, int_max=1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR VISIBILITY "Ladder1": use_visible=True
- ACTUATOR PROPERTY "HIDE": mode=ASSIGN, property=Ladder, value=0, object_property=0
- ACTUATOR VISIBILITY "Visibility": 

### LadderRight  [MESH]  pos=(-2.42, 17.25, -15.24) rot_deg=(0.00, 0.00, 0.00) size=(0.59, 4.51, 25.12)
mesh "Cube.005": 80 verts 44 faces
physics: STATIC mass=1.0
- prop Ladder (INT) = 0
- SENSOR KEYBOARD "Keyboard" -> [And.001]: controllers=(bpy.data.objects['LadderRight']...OrController,), key=X, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR MESSAGE "Ladder" -> [And.001]: controllers=(bpy.data.objects['LadderRight']...OrController,), subject=Ladder
- SENSOR PROPERTY "Ladder1" -> [Ladder]: controllers=(bpy.data.objects['LadderRight']...AndController,), evaluation_type=PROPEQUAL, property=Ladder, value=1, value_min=1
- SENSOR MESSAGE "HIDE" -> [HIDE]: controllers=(bpy.data.objects['LadderRight']...AndController,), subject=Hide
- SENSOR PROPERTY "Ladder0" -> [And]: controllers=(bpy.data.objects['LadderRight']...AndController,), evaluation_type=PROPEQUAL, property=Ladder, value=0, value_min=0
- CONTROLLER LOGIC_OR "And.001" -> [Random]
- CONTROLLER LOGIC_AND "Ladder" -> [Ladder1]
- CONTROLLER LOGIC_AND "HIDE" -> [HIDE]
- CONTROLLER LOGIC_AND "And" -> [Visibility]
- ACTUATOR RANDOM "Random": seed=11127, property=Ladder, distribution=INT_UNIFORM, chance=0.1, int_max=1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR VISIBILITY "Ladder1": use_visible=True
- ACTUATOR PROPERTY "HIDE": mode=ASSIGN, property=Ladder, value=0, object_property=0
- ACTUATOR VISIBILITY "Visibility": 

### Ladder  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.59, 4.51, 25.12) (hidden)
mesh "Cube.012": 80 verts 44 faces
physics: STATIC mass=1.0
- prop Ladder (BOOL) = True

### LadderSpawner1  [EMPTY]  pos=(-1.89, -17.00, -14.49) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00) (hidden)
physics: NO_COLLISION mass=1.0
- prop Spawn (BOOL) = False
- SENSOR MESSAGE "Message" -> [And.001]: controllers=(bpy.data.objects['LadderSpawner1']...AndController,), subject=Spawn
- SENSOR KEYBOARD "Keyboard" -> [Ladder]: controllers=(bpy.data.objects['LadderSpawner1']...OrController,), key=TWO, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "SpawnT" -> [Ladder]: controllers=(bpy.data.objects['LadderSpawner1']...OrController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "And.001" -> [Random]
- CONTROLLER LOGIC_OR "Ladder" -> [Ladder]
- ACTUATOR RANDOM "Random": seed=1856, property=Spawn, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "Ladder": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Ladder, track_object=obj:Ladder, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### LadderSpawner2  [EMPTY]  pos=(-2.02, 17.00, -14.49) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00) (hidden)
physics: NO_COLLISION mass=1.0
- prop Spawn (BOOL) = False
- SENSOR MESSAGE "Message" -> [And.001]: controllers=(bpy.data.objects['LadderSpawner2']...AndController,), subject=Spawn
- SENSOR KEYBOARD "Keyboard" -> [And]: controllers=(bpy.data.objects['LadderSpawner2']...OrController,), key=TWO, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "Property" -> [And]: controllers=(bpy.data.objects['LadderSpawner2']...OrController,), evaluation_type=PROPEQUAL, property=Spawn, value=TRUE, value_min=TRUE
- CONTROLLER LOGIC_AND "And.001" -> [Random]
- CONTROLLER LOGIC_OR "And" -> [Edit Object]
- ACTUATOR RANDOM "Random": seed=1112, property=Spawn, distribution=BOOL_UNIFORM, chance=0.1, int_mean=0.1, float_value=0.1, float_min=0.1, float_mean=0.1, half_life_time=0.1
- ACTUATOR EDIT_OBJECT "Edit Object": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Ladder, track_object=obj:Ladder, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True

### INIT  [EMPTY]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0
- SENSOR KEYBOARD "1" -> [And]: controllers=(bpy.data.objects['INIT']...AndController,), key=ONE, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR DELAY "Delay" -> [PlayerSpawn]: use_tap=True, controllers=(bpy.data.objects['INIT']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Pond]
- CONTROLLER LOGIC_AND "PlayerSpawn" -> [PlayerSpawn]
- ACTUATOR EDIT_OBJECT "Pond": mode=ADDOBJECT, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:GroundPond_Vine, track_object=obj:GroundPond_Vine, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True
- ACTUATOR MESSAGE "PlayerSpawn": to_property=LeftPlayerSpawn, subject=Spawn, body_type=TEXT, body_message=Spawn, body_property=Spawn

## text blocks
### Text  (6 lines)
```
A  & D To move 
W & S to climb ladders
Space to jump

P key to start game

```