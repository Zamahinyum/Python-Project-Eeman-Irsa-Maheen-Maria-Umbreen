# ============================
# main.py
# Entry point of the program
# ============================
import bpy
import sys
import os

# Add current script directory to Python path
script_dir = os.path.dirname(bpy.data.filepath)
if script_dir not in sys.path:
    sys.path.append(script_dir)

from scene_generator import SceneGenerator

def main():
    print("=== PROCEDURAL GALAXY GENERATOR ===")

    scene = SceneGenerator()
    scene.clear_scene()
    scene.generate_scene()
    scene.setup_lighting()
    scene.setup_camera()

    bpy.context.scene.frame_end = 500
    print("✓ Scene generated successfully")

if __name__ == "__main__":
    main()
