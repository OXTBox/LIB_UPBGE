# dump_blend.py - run inside UPBGE headless:
#   blender.exe --background FILE.blend --python dump_blend.py -- OUT.md
# Writes a text spec of a Blender Game Engine file: scenes, objects (type, position,
# rotation, size, colour, mesh size), game properties, logic bricks (sensors, controllers,
# actuators with their settings and links) and the text blocks (embedded scripts).
# Images are never opened or described. (Claude, 2026-11-13, for LIB_UPBGE)
import bpy, sys, math

out = sys.argv[sys.argv.index('--') + 1] if '--' in sys.argv else None
L = []
def w(s=''): L.append(s)

SKIP = {'rna_type', 'name', 'type', 'show_expanded', 'pin', 'active', 'states', 'is_unlinked'}

def brick(b):
    parts = []
    for p in b.bl_rna.properties:
        k = p.identifier
        if k in SKIP: continue
        try: v = getattr(b, k)
        except Exception: continue
        if v is None or v == '' : continue
        if hasattr(v, 'name') and not isinstance(v, str): v = 'obj:' + v.name
        elif hasattr(v, '__len__') and not isinstance(v, str):
            try: v = tuple(round(x, 3) if isinstance(x, float) else x for x in v)
            except Exception: continue
        elif isinstance(v, float): v = round(v, 3)
        if v in (False, 0, 0.0) : continue
        parts.append(f'{k}={v}')
    return ', '.join(parts)

def r3(v): return '(' + ', '.join(f'{x:.2f}' for x in v) + ')'

w(f'# {bpy.data.filepath.split(chr(92))[-1].split("/")[-1]}')
w()
for sc in bpy.data.scenes:
    w(f'## scene "{sc.name}"  camera={sc.camera.name if sc.camera else "-"}')
    try:
        gs = sc.game_settings
        w(f'game: fps={gs.fps} physics={gs.physics_engine} gravity={round(gs.physics_gravity,2)}')
    except Exception: pass
    w()
    for ob in sc.objects:
        line = f'### {ob.name}  [{ob.type}]  pos={r3(ob.location)} rot_deg={r3([math.degrees(a) for a in ob.rotation_euler])} size={r3(ob.dimensions)}'
        if ob.parent: line += f' parent={ob.parent.name}'
        if not ob.visible_get(): line += ' (hidden)'
        w(line)
        if ob.type == 'MESH' and ob.data:
            me = ob.data
            col = ''
            if ob.active_material:
                c = ob.active_material.diffuse_color
                col = f' colour=#{int(c[0]*255):02X}{int(c[1]*255):02X}{int(c[2]*255):02X}'
            w(f'mesh "{me.name}": {len(me.vertices)} verts {len(me.polygons)} faces{col}')
        if ob.type == 'FONT':
            w(f'text: "{ob.data.body}"')
        if ob.type == 'CAMERA':
            w(f'camera: lens={round(ob.data.lens,1)} type={ob.data.type} ortho_scale={round(ob.data.ortho_scale,2)}')
        try:
            g = ob.game
            w(f'physics: {g.physics_type} mass={round(g.mass,2)}')
            for p in g.properties:
                w(f'- prop {p.name} ({p.type}) = {p.value}')
            for s in g.sensors:
                links = ', '.join(c.name for c in s.controllers)
                w(f'- SENSOR {s.type} "{s.name}" -> [{links}]: {brick(s)}')
            for c in g.controllers:
                extra = ''
                if c.type == 'PYTHON':
                    extra = f' script={c.text.name if c.text else c.module}'
                if c.type == 'EXPRESSION':
                    extra = f' expr={c.expression}'
                links = ', '.join(a.name for a in c.actuators)
                w(f'- CONTROLLER {c.type} "{c.name}"{extra} -> [{links}]')
            for a in g.actuators:
                w(f'- ACTUATOR {a.type} "{a.name}": {brick(a)}')
        except Exception as e:
            w(f'(no game logic: {e})')
        # logic nodes / components, if any
        try:
            for comp in ob.game.components:
                w(f'- COMPONENT {comp.name} module={comp.module}')
        except Exception: pass
        w()
w('## text blocks')
for t in bpy.data.texts:
    w(f'### {t.name}  ({len(t.lines)} lines)')
    w('```')
    w(t.as_string()[:6000])
    w('```')
text = '\n'.join(L)
if out:
    open(out, 'w', encoding='utf-8').write(text)
else:
    print(text)
