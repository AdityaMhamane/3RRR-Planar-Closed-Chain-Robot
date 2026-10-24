import mujoco
import mujoco.viewer

def main():
    # 1. Load model and create data context
    model_path = "3RRR_Planar.xml"
    model = mujoco.MjModel.from_xml_path(model_path)
    data = mujoco.MjData(model)

    # Pre-step simulation once to populate initial kinematic state
    mujoco.mj_step(model, data)

    with mujoco.viewer.launch_passive(model, data) as viewer:
            # Configure viewer camera
            viewer.cam.lookat[:] = model.stat.center
            viewer.cam.distance = max(2.0 * model.stat.extent, 1.0)
            viewer.cam.azimuth = 135
            viewer.cam.elevation = -25
    
            step_count = 0
            while viewer.is_running():
                mujoco.mj_step(model, data)
                viewer.sync()

if __name__ == "__main__":
    main()