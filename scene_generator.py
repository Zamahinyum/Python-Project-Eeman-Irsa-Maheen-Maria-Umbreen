# =====================================
# scene_generator.py
# Manages scene, camera, lighting
# =====================================

import bpy
import math
from object_generator import ObjectGenerator
from animator import Animator

class SceneGenerator:
    """Controls overall scene assembly"""

    def __init__(self):
        self.objects = ObjectGenerator()

    def clear_scene(self):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()

    def setup_lighting(self):
        # Create world if it doesn't exist
        if bpy.context.scene.world is None:
            world = bpy.data.worlds.new("World")
            bpy.context.scene.world = world
        
        world = bpy.context.scene.world
        
        # Enable nodes if not already enabled
        if not world.use_nodes:
            world.use_nodes = True
        
        # Get or create background node
        nodes = world.node_tree.nodes
        if "Background" in nodes:
            bg = nodes["Background"]
        else:
            bg = nodes.new(type="ShaderNodeBackground")
        
        bg.inputs[0].default_value = (0.005, 0.005, 0.015, 1)
        bg.inputs[1].default_value = 0.05

        bpy.ops.object.light_add(type='POINT', location=(0, 0, 0))
        bpy.context.object.data.energy = 2000

    def setup_camera(self):
        bpy.ops.object.camera_add(location=(0, -35, 15))
        cam = bpy.context.object
        bpy.context.scene.camera = cam

        Animator.animate_camera_orbit(cam, 35, 15, 500)

    def generate_scene(self):
        self.objects.create_sun()

        planets = [
            ("Mercury", 4, 0.4, (0.8, 0.6, 0.4), 150),
            ("Venus", 6, 0.7, (1, 0.85, 0.5), 200),
            ("Earth", 8, 0.8, (0.1, 0.4, 0.95), 250),
            ("Mars", 10, 0.6, (0.95, 0.35, 0.2), 300),
        ]

        for p in planets:
            planet = self.objects.create_planet(*p)
            if p[0] == "Earth":
                self.objects.create_moon(planet, 1.5, 0.2, 100)

        self.objects.create_asteroid_belt(12, 14, 80)