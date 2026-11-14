# MakeHumanLady_walkin.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Light  [LIGHT]  pos=(4.08, -22.73, 5.90) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00) parent=CMU compliant skeleton
physics: STATIC mass=1.0

### Camera  [CAMERA]  pos=(7.36, -6.93, 4.96) rot_deg=(63.56, 0.00, 46.69) size=(0.00, 0.00, 0.00)
camera: lens=50.0 type=PERSP ortho_scale=7.31
physics: STATIC mass=1.0

### CMU compliant skeleton  [ARMATURE]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(5.32, 7.84, 14.38)
physics: STATIC mass=1.0
- prop facing (BOOL) = False
- SENSOR KEYBOARD "W" -> [And, FLIP]: use_pulse_true_level=True, use_tap=True, controllers=(bpy.data.objects['CMU compliant skeleton']...OrController, bpy.data.objects['CMU compliant skeleton']...OrController), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "S" -> [FLIP, And]: use_tap=True, controllers=(bpy.data.objects['CMU compliant skeleton']...OrController, bpy.data.objects['CMU compliant skeleton']...OrController), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR PROPERTY "Property" -> [And.001]: use_tap=True, controllers=(bpy.data.objects['CMU compliant skeleton']...AndController,), evaluation_type=PROPCHANGED, property=facing
- CONTROLLER LOGIC_OR "And" -> [Action]
- CONTROLLER LOGIC_OR "FLIP" -> [Property]
- CONTROLLER LOGIC_AND "And.001" -> [Motion]
- ACTUATOR ACTION "Action": play_mode=PLAY, action=obj:CMU walkslow, use_continue_last_frame=True, frame_end=120.0, use_force=True, blend_mode=BLEND
- ACTUATOR PROPERTY "Property": mode=TOGGLE, property=facing
- ACTUATOR MOTION "Motion": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=3.142, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 3.142), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True

### female_sportsuit01Mesh  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(4.58, 11.69, 4.76) parent=CMU compliant skeleton
mesh "female_sportsuit01": 1797 verts 1718 faces colour=#FFFFFF
physics: STATIC mass=1.0

### shoes06Mesh  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(3.47, 2.74, 3.50) parent=CMU compliant skeleton
mesh "shoes06": 1492 verts 1426 faces colour=#FFFFFF
physics: STATIC mass=1.0

### makehumanladycmu.meshMesh  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(5.92, 7.06, 6.92) parent=CMU compliant skeleton
mesh "makehumanladycmu.mesh": 9368 verts 9262 faces colour=#D29F80
physics: STATIC mass=1.0

### short03Mesh  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(1.70, 1.81, 2.03) parent=CMU compliant skeleton
mesh "short03": 1011 verts 961 faces colour=#FFFFFF
physics: STATIC mass=1.0

### high-polyMesh  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, -0.00, 0.00) size=(0.86, 0.34, 0.38) parent=CMU compliant skeleton
mesh "high-poly": 1064 verts 1020 faces colour=#FFFFFF
physics: STATIC mass=1.0

### Plane  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(86.95, 86.95, 0.00)
mesh "Plane": 4 verts 1 faces
physics: STATIC mass=1.0

## text blocks
### Text  (11 lines)
```
W & S to toggle Model direction

Model made in MakeHuman
Animations from
Carnegie Mellon University
BVH MOCAP library
http://mocap.cs.cmu.edu/resources.php

A good target for 
In Placer Addon correction
https://fatihpehlevan.gumroad.com/l/InPlacer
```