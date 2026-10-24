# 3RRR Planar Closed-Chain Robot

MuJoCo model of a 3RRR planar closed-chain robot. `3RRR_Planar.xml` defines the robot and its close loop constraints. Run `python scene.py` to open the model in the MuJoCo viewer. I will add Inverse kinematics (IK) simulation for this model soon.

## Previews

| CAD model | MuJoCo model |
|---|---|
| ![3RRR CAD model](<Images&GIFs/3RRR_CAD.gif>) | ![3RRR MuJoCo model](<Images&GIFs/3RRR_XML.gif>) |

## Repository contents

```text
.
├── .gitignore
├── 3RRR_Planar.xml
├── README.md
├── scene.py
├── angle_.png
├── meshes/
│   ├── actA.STL, actB.STL, actC.STL
│   ├── unactA.STL, unactB.STL, unactC.STL
│   ├── base.STL
│   └── endEffA.STL
├── STEP/
│   └── Assembly_RigidOrigin (Assembly).step
└── Images&GIFs/
    ├── 3RRR CAD 2026-10-20 22-14-11.mp4
    ├── 3RRR_CAD.gif
    ├── 3RRR_XML.gif
    ├── Assembly_RigidOrigin v1.jpg
    └── XML model video 2026-10-21 19-01-16.mp4
```

`STEP/` contains the CAD model; 

`Images&GIFs/` contains project images, GIFs, and videos.

The STL meshes XML references are in `meshes/`.