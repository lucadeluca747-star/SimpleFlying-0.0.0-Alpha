from ursina import *
import math
import time



app = Ursina(title='cuber game', icon='textures/ursina.ico', fullscreen = True, developer_mode = False)

sky = Sky(texture='publicsky.jfif', rotation=(0, 0, 0), scale=350)

ground = Entity(
    model='plane',
    scale=250,
    texture='grass', 
    texture_scale=(250, 250),
    collider='box'
    
)


cube = Entity(
    model='planee.obj',
    texture='plane_roughness.jpg',
    scale=0.3,
    position=(0, 1, 0),
    
)

textures = ('plane_roughness.jpg', 'internal_ground_ao_texture.jpeg', 'plane_albedo.png', 'plane_normal.jpg')

print(cube.collider)
cube.collider = 'mesh'
cube.collision = True

cube.collider = cube.model  

cam = EditorCamera()
cam.look_at(cube)
cam.rotation_x = 15
cam.rotation_y = 180
cam.parent = cube
cam.movement_speed = 0
cam.ignore_input = True
cam.position = (0, 10, 20)

horizon = Entity(
parent=camera.ui,
model='quad',
texture='basehorizon.png',
scale=.2,

)   
horizon.x = 0.75
horizon.y = -0.3
a = 0
cooldown = 0
def update():
    global a
    if held_keys['a']:
        cube.position += cube.left * 0.1
    if held_keys['d']:
        cube.position += cube.right * 0.1
    if held_keys['w']:
        cube.position -= cube.forward * 1

    if held_keys['s']:
        cube.position += cube.forward * 1
    global cooldown
    if held_keys['e']:
        cube.rotation_y += 0.8
        cube.rotation_z -= 0.9
    if held_keys['q']:
        cube.rotation_y -= 0.8
        cube.rotation_z += 0.9
    if held_keys['m']:
        cube.rotation_x += 1
    if held_keys['n']:
        cube.rotation_x -= 1

    if held_keys['f']:
        cube.position = (0, 0, 0.5)
        horizon.texture = load_texture('basehorizon.png')
    cooldown -= time.dt
    if held_keys['t'] and cooldown <= 0:
        
        cube.texture = load_texture(textures[a])
        a += 1
        if a >= int(len(textures )):
            a = 0
        cooldown = .2

    if cube.rotation_z > 0:
        cube.rotation_z -= 0.35
    elif cube.rotation_z < 0:
        cube.rotation_z += 0.35
    else:
        pass
    if cube.rotation_x > 0:
        cube.rotation_x -= 0.15
    elif cube.rotation_x < 0:
        cube.rotation_x += 0.15
    else:
        pass
    
    collisioneaereo = ground.intersects()
    if collisioneaereo.hit:
        cube.y +=1
    else:
        cube.position = cube.position
        cube.y = cube.y
    if held_keys['w']:
        horizon.texture=load_texture('horizonflat.png')
    elif held_keys['m'] and held_keys['q'] or held_keys['w'] and held_keys['q']:
            horizon.texture=load_texture('upleft.png')
    elif held_keys['m'] and held_keys['e'] or held_keys['w'] and held_keys['e']:
        horizon.texture=load_texture('upright.png')
    elif held_keys['m'] and held_keys['w'] or held_keys['m']:
        horizon.texture=load_texture('uphorizon.png')
    elif held_keys['n'] and held_keys['w'] or held_keys['n']:
        horizon.texture=load_texture('downhorizon.png')
    elif held_keys['n'] and held_keys['e']:
        horizon.texture=load_texture('downright.png')
    elif held_keys['n'] and held_keys['q']:
        horizon.texture=load_texture('downleft.png')
    elif held_keys['e'] and held_keys['w'] or held_keys['e']:
        horizon.texture=load_texture('righthorizon.png')
    elif held_keys['q'] and held_keys['w'] or held_keys['q']:
        horizon.texture=load_texture('lefthorizon.png')
    
    else:
        horizon.texture = load_texture('basehorizon.png')

app.run()