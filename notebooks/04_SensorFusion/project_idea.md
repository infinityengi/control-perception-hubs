## Sensor Fusion for Precise Navigation

**1. Notebook:** *EKF/UKF for 2D robot with IMU+GPS*

* Tools: Python, `filterpy` or custom implementation, Matplotlib
* What to do: simulate IMU/GNSS measurements, implement EKF and UKF, compare errors, visualize covariance ellipses.

**2. Project:** *Tightly-coupled GNSS+IMU (simple dataset)*

* Tools: Python, GTSAM (if available), or factor graph library
* Add a Jupyter notebook that walks from raw data → preprocessing → factor graph optimization → results.

**Repo helpers:** `filterpy`, GTSAM bindings, `robot_localization` ROS package.
