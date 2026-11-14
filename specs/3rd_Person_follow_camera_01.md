# 3rd_Person_follow_camera_01.blend

## scene "Scene"  camera=Camera
game: fps=60 physics=BULLET gravity=9.8

### Maze  [MESH]  pos=(0.00, 0.00, -1.65) rot_deg=(0.00, 0.00, 0.00) size=(192.87, 192.87, 3.56)
mesh "Plane.001": 2379 verts 4596 faces colour=#444444
physics: STATIC mass=1.0

### Sphere  [MESH]  pos=(1.85, -22.62, 1.25) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Sphere": 482 verts 512 faces
physics: NO_COLLISION mass=1.0
- SENSOR ALWAYS "Always" -> [And]: use_pulse_true_level=True, controllers=(bpy.data.objects['Sphere']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Steering]
- ACTUATOR STEERING "Steering": mode=SEEK, velocity=5.0, acceleration=2.0, turn_speed=720.0, distance=10.0, target=obj:Follow_Target, facing_axis=NEG_X, lock_z_velocity=True

### Empty  [EMPTY]  pos=(-6.49, -7.25, 7.39) rot_deg=(0.00, -0.00, 0.00) size=(0.00, 0.00, 0.00) parent=Sphere
physics: NO_COLLISION mass=1.0
- SENSOR ALWAYS "Always" -> [And]: use_pulse_true_level=True, controllers=(bpy.data.objects['Empty']...AndController,)
- CONTROLLER LOGIC_AND "And" -> [Edit Object]
- ACTUATOR EDIT_OBJECT "Edit Object": mode=TRACKTO, dynamic_operation=RESTOREDYN, up_axis=UPAXISZ, track_axis=TRACKAXISY, object=obj:Camera_Target, track_object=obj:Camera_Target, linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_replace_display_mesh=True, use_3d_tracking=True

### Camera  [CAMERA]  pos=(-1.57, -12.53, 5.66) rot_deg=(90.00, -0.00, 0.00) size=(0.00, 0.00, 0.00) parent=Empty
camera: lens=35.0 type=PERSP ortho_scale=7.31
physics: NO_COLLISION mass=1.0

### Lamp.002  [LIGHT]  pos=(7.78, 4.31, 6.73) rot_deg=(180.00, -0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### Lamp.001  [LIGHT]  pos=(7.78, 4.31, 6.73) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### Plane  [MESH]  pos=(0.00, 0.00, 0.00) rot_deg=(0.00, 0.00, 0.00) size=(192.87, 192.87, 0.00)
mesh "Plane": 4 verts 1 faces colour=#CCCCCC
physics: STATIC mass=1.0

### Player  [MESH]  pos=(2.00, 0.00, 1.00) rot_deg=(0.00, 0.00, 0.00) size=(2.00, 2.00, 2.00)
mesh "Cube": 8 verts 6 faces colour=#1933CC
physics: CHARACTER mass=1.0
- SENSOR KEYBOARD "W" -> [W]: controllers=(bpy.data.objects['Player']...AndController,), key=W, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "S" -> [S]: controllers=(bpy.data.objects['Player']...AndController,), key=S, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "A" -> [A]: controllers=(bpy.data.objects['Player']...AndController,), key=A, modifier_key_1=NONE, modifier_key_2=NONE
- SENSOR KEYBOARD "D" -> [D]: controllers=(bpy.data.objects['Player']...AndController,), key=D, modifier_key_1=NONE, modifier_key_2=NONE
- CONTROLLER LOGIC_AND "W" -> [Forward]
- CONTROLLER LOGIC_AND "S" -> [Backward]
- CONTROLLER LOGIC_AND "A" -> [Motion.002]
- CONTROLLER LOGIC_AND "D" -> [Motion.003]
- ACTUATOR MOTION "Forward": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=0.1, offset_location=(0.0, 0.1, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Backward": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_max_y=-0.1, offset_location=(0.0, -0.1, 0.0), offset_rotation=(0.0, 0.0, 0.0), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Motion.002": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=0.017, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, 0.017), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- ACTUATOR MOTION "Motion.003": mode=OBJECT_NORMAL, servo_mode=SERVO_LINEAR, force_min_z=-0.017, offset_location=(0.0, 0.0, 0.0), offset_rotation=(0.0, 0.0, -0.017), force=(0.0, 0.0, 0.0), torque=(0.0, 0.0, 0.0), linear_velocity=(0.0, 0.0, 0.0), angular_velocity=(0.0, 0.0, 0.0), use_local_location=True, use_local_rotation=True, use_local_force=True, use_local_torque=True, use_servo_limit_x=True, use_servo_limit_y=True, use_servo_limit_z=True
- COMPONENT Component module=module

### Lamp  [LIGHT]  pos=(10.31, 3.41, 14.65) rot_deg=(37.26, 3.16, 106.94) size=(0.00, 0.00, 0.00)
physics: NO_COLLISION mass=1.0

### Camera_Target  [EMPTY]  pos=(1.97, 1.80, 2.72) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00) parent=Player
physics: NO_COLLISION mass=1.0

### Follow_Target  [EMPTY]  pos=(1.97, -4.52, 0.60) rot_deg=(0.00, 0.00, 0.00) size=(0.00, 0.00, 0.00) parent=Player
physics: NO_COLLISION mass=1.0

## text blocks
### info  (1 lines)
```
                        'w a s d for control'
```
### module.py  (25 lines)
```
import bge
from collections import OrderedDict

if not hasattr(bge, "__component__"):
    # Put shared definitions here executed only in game engine.
    # e.g:
    # scene = bge.logic.getCurrentScene()
    pass

class Component(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def start(self, args):
        # Put your initialization code here, args stores the values from the UI.
        # self.object is the owner object of this component.
        pass

    def update(self):
        # Put your code executed every logic step here.
        # self.object is the owner object of this component.
        pass

```