# ============================
# animator.py
# Handles ALL animation logic
# ============================

import math

class Animator:
    """Class responsible for animating objects and camera"""

    @staticmethod
    def animate_rotation(obj, axis='Z', start_frame=1, end_frame=100):
        """Animate object rotation around a given axis"""
        axis_index = {'X': 0, 'Y': 1, 'Z': 2}[axis]

        obj.rotation_euler[axis_index] = 0
        obj.keyframe_insert(data_path="rotation_euler", frame=start_frame)

        obj.rotation_euler[axis_index] = math.radians(360)
        obj.keyframe_insert(data_path="rotation_euler", frame=end_frame)

    @staticmethod
    def animate_orbit(obj, radius, duration):
        """Animate circular orbit around world origin"""
        steps = 20

        for i in range(steps + 1):
            frame = int((i / steps) * duration) + 1
            angle = (i / steps) * 2 * math.pi

            obj.location.x = radius * math.cos(angle)
            obj.location.y = radius * math.sin(angle)

            obj.keyframe_insert(data_path="location", frame=frame)

    @staticmethod
    def animate_orbit_around_point(obj, center, radius, duration):
        """Animate orbit around a specific point"""
        steps = 20

        for i in range(steps + 1):
            frame = int((i / steps) * duration) + 1
            angle = (i / steps) * 2 * math.pi

            obj.location.x = center.x + radius * math.cos(angle)
            obj.location.y = center.y + radius * math.sin(angle)

            obj.keyframe_insert(data_path="location", frame=frame)

    @staticmethod
    def animate_camera_orbit(camera, radius, height, duration):
        """Animate cinematic camera orbiting the scene"""
        steps = 30

        for i in range(steps + 1):
            frame = int((i / steps) * duration) + 1
            angle = (i / steps) * 2 * math.pi

            camera.location = (
                radius * math.cos(angle),
                radius * math.sin(angle),
                height
            )

            direction = -camera.location.normalized()
            camera.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()

            camera.keyframe_insert(data_path="location", frame=frame)
            camera.keyframe_insert(data_path="rotation_euler", frame=frame)
