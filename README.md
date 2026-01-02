PYTHON PROJECT
Submitted by:
Eman Fatima 537512
Irsa liaqat 537745
Maheen farid 53364
Maria kousar 538067
Umbreen Tariq 500321


#Procedural Galaxy Scene Generator (Blender)

A modular **procedural galaxy scene generator** written in **Blender Python (bpy)**.
This project automatically creates a cinematic, animated solar-system-style scene with:

* A glowing sun
* Multiple orbiting planets
* A moon orbiting Earth
* An asteroid belt
* Animated camera orbit
* Cinematic lighting and space background

The project is structured cleanly into multiple Python files for **readability, scalability, and learning best practices**.

---

## Project Structure

```
ProceduralScene/
├── main.py              # Entry point (run this in Blender)
├── object_generator.py   # Object creation logic
├── scene_generator.py   # setup scene creation logic
├── animator.py          # All animation utilities
└── README.md            # Documentation
```

## Scene Contents

### Sun

* Large UV sphere at the origin
* Strong emission-based material
* Slow rotation animation

### Planets

| Name    | Features                                     |
| ------- | -------------------------------------------- |
| Mercury | Small, fast orbit                            |
| Venus   | Warm color palette                           |
| Earth   | Blue material + moon                         |
| Mars    | Red/orange tones                             |
| Jupiter | Large gas-giant scale                        |
| Saturn  | Large pale planet |

Each planet:

* Orbits the sun
* Rotates on its axis
* Uses a principled BSDF material

### Moon

* Orbits Earth
* Independent orbit animation

### Asteroid Belt

* Randomized positions
* Random sizes and colors
* Individual orbit animations

### Camera

* Cinematic orbit around the scene
* Always tracks the center

### Lighting

* Dark blue space background
* Central point light to enhance glow

