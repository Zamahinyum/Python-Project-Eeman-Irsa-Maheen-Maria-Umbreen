# =====================================
# object_generator.py
# Creates ALL procedural objects
# =====================================

import bpy
import random
import math
from animator import Animator

class ObjectGenerator:
    """Class responsible for creating objects and materials"""

    def __init__(self):
        self.materials = []

    # ---------- MATERIALS ----------
    def create_material(self, name, color, emission=0, metallic=0, roughness=0.5):
        """Create material using Principled BSDF"""
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True

        nodes = mat.node_tree.nodes
        nodes.clear()

        bsdf = nodes.new("ShaderNodeBsdfPrincipled")
        output = nodes.new("ShaderNodeOutputMaterial")

        bsdf.inputs["Base Color"].default_value = (*color, 1)
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness

        if "Emission Color" in bsdf.inputs:
            bsdf.inputs["Emission Color"].default_value = (*color, 1)
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = emission

        mat.node_tree.links.new(bsdf.outputs[0], output.inputs[0])
        self.materials.append(mat)
        return mat

    def apply_material(self, obj, mat):
        if obj.data.materials:
            obj.data.materials[0] = mat
        else:
            obj.data.materials.append(mat)

    # ---------- OBJECTS ----------
    def create_sun(self):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=2.5)
        sun = bpy.context.object
        sun.name = "Sun"

        mat = self.create_material("SunMat", (1, 0.9, 0.3), emission=50)
        self.apply_material(sun, mat)

        Animator.animate_rotation(sun, 'Z', 1, 250)
        return sun

    def create_planet(self, name, distance, size, color, speed):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=(distance, 0, 0))
        planet = bpy.context.object
        planet.name = name

        mat = self.create_material(f"{name}_Mat", color, metallic=0.3)
        self.apply_material(planet, mat)

        Animator.animate_orbit(planet, distance, speed)
        Animator.animate_rotation(planet, 'Z', 1, 120)
        return planet

    def create_moon(self, planet, distance, size, speed):
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=size,
            location=(planet.location.x + distance, 0, 0)
        )
        moon = bpy.context.object
        moon.name = f"{planet.name}_Moon"

        mat = self.create_material("MoonMat", (0.8, 0.8, 0.85))
        self.apply_material(moon, mat)

        Animator.animate_orbit_around_point(
            moon, planet.location, distance, speed
        )

    def create_asteroid_belt(self, inner, outer, count=80):
        for i in range(count):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(inner, outer)

            bpy.ops.mesh.primitive_ico_sphere_add(
                radius=random.uniform(0.05, 0.15),
                location=(
                    radius * math.cos(angle),
                    radius * math.sin(angle),
                    random.uniform(-0.5, 0.5)
                ),
                subdivisions=1
            )

            asteroid = bpy.context.object
            asteroid.name = f"Asteroid_{i}"

            mat = self.create_material(
                f"AstMat_{i}",
                (random.uniform(0.4, 0.6), random.uniform(0.3, 0.5), random.uniform(0.3, 0.45)),
                roughness=0.8
            )
            self.apply_material(asteroid, mat)

            Animator.animate_orbit(asteroid, radius, random.uniform(500, 800))
