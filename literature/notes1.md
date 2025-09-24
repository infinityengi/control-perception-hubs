# Foundations & Resources — Control, Navigation & ML  
**Curated for beginners who want a solid theoretical foundation + hands-on projects.**  
This README collects review papers, tutorials, university/course-style materials and open-source repositories for five topic areas frequently researched at the Institute for Automatic Control (IRT / Institut für Regelungstechnik) — RWTH Aachen and by the broader controls & robotics community.

> File purpose: save as `README.md` (or any `.md`) in a GitHub repo. Links point to papers, toolboxes, datasets and example repos (English-first).  
> Last checked (by assistant): September 2025.

---

## Quick index
- [Model-based predictive control (MPC)](#model-based-predictive-control-mpc)  
- [Robust control methods](#robust-control-methods)  
- [Digitally networked control systems (NCS)](#digitally-networked-control-systems-ncs)  
- [Sensor fusion for precise & robust navigation](#sensor-fusion-for-precise--robust-navigation)  
- [Machine learning in perception & control](#machine-learning-in-perception--control-engineering)  
- [Practical toolchain & datasets](#practical-toolchain--datasets)  
- [Getting started — suggested learning path](#getting-started---suggested-learning-path)  
- [IRT-specific pages & projects (RWTH Aachen)](#irt-specific-pages--projects-rwth-aachen)  
- [Full references & links (quick list)](#full-references--links-quick-list)

---

## Model-based predictive control (MPC)

**Short overview**  
MPC solves an optimization problem online at each control step using a dynamic model to predict future outputs. Strengths: multi-variable handling and explicit constraints. Common in process control, robotics (locomotion), vehicles and energy systems.

**Recommended review / tutorial (beginner → advanced)**

1. **Mayne, Rawlings, Rao & Scokaert (2000)** — *Constrained model predictive control: Stability and optimality* (Automatica) — Classic, foundational review of MPC theory and stability for constrained MPC. (Technical, but essential).  
   https://www.sciencedirect.com/science/article/pii/S0005109899002149  
   DOI: `10.1016/S0005-1098(99)00214-9`  
   (Also often available from university pages / ResearchGate.)

2. **Mayne (2014)** — *Model predictive control: Recent developments and future promise* — high-level survey of modern directions in MPC. (Good overview.)  
   https://www.sciencedirect.com/science/article/abs/pii/S0005109814005160

3. **Schwenzer et al. (2021)** — *Review on MPC (engineering applications)* — contemporary engineering-focused survey, useful for seeing wide application areas.  
   https://link.springer.com/article/10.1007/s00170-021-07682-3

**Hands-on toolboxes & repos (Python/C++/MATLAB)**

- **do-mpc** — Python nonlinear MPC + MHE toolbox (CasADi + IPOPT/OSQP friendly). Great examples and beginner docs. (Python)  
  https://www.do-mpc.com/ · https://github.com/do-mpc/do-mpc

- **pyMPC** — simple linear MPC Python examples; good for learning QP-based MPC. (Python)  
  https://github.com/forgi86/pyMPC

- **CasADi** — automatic differentiation & optimal control framework used heavily for NMPC (Python/C++). (C++ core, Python interface)  
  https://web.casadi.org/ · https://github.com/casadi/casadi

- **OSQP** — fast QP solver commonly used for MPC (Python/C).  
  https://osqp.org/ · https://github.com/osqp/osqp

**Suggested beginner exercises**
- Implement a simple linear MPC for a double-integrator using `pyMPC` or `do-mpc`.  
- Replace the QP solver with OSQP and profile solve times.  
- Reproduce figures from Mayne (2000) showing constraints and receding horizon behavior.

---

## Robust control methods

**Short overview**  
Robust control ensures stability and performance despite model uncertainty and disturbances. Common tools: H∞ synthesis, μ-synthesis (D-K), sliding-mode control, gain-scheduling and structured uncertainty modeling.

**High-quality references & tutorials**

1. **Zhou, Doyle & Glover** — *Robust and Optimal Control* (book) — classic text (deep theoretical coverage). (Book — advanced)  
   (Search via library / publisher; commonly cited textbook.)

2. **MathWorks – Robust Control Toolbox** — official documentation & tutorials (practical, MATLAB). Contains `hinfsyn`, `hinfnorm`, μ-synthesis demos. (Beginner → intermediate, MATLAB)  
   https://www.mathworks.com/help/robust/

3. **Petersen & Tempo (survey)** — survey articles on robust/stochastic control methods (look up in control journals). (Technical)

4. **H∞ / µ tutorials** — MATLAB video series & examples (MathWorks) — useful hands-on demos.  
   https://www.mathworks.com/videos/series/understanding-model-predictive-control.html (MPC playlist)  
   H∞/µ videos: https://www.mathworks.com/help/robust/

**Open-source tools (Python-centric)**

- **python-control** — core control analysis & some advanced routines (Python). Good for state-space, LQR, root-locus, bode, and some H∞ examples.  
  https://python-control.readthedocs.io/ · https://github.com/python-control/python-control

- **hinf/µ toolkits** — many µ/H∞ examples remain MATLAB heavy; for research, Python + SLYcot + control package provide building blocks.

**Suggested beginner exercises**
- Use the Python `control` library to design an LQR and compare closed-loop robustness vs. H∞ (using MATLAB examples if available).  
- Reproduce a basic H∞ design (MathWorks tutorial) to see the effect of modeling uncertainty.

---

## Digitally networked control systems (NCS)

**Short overview**  
NCS closes feedback loops over communication networks. Key challenges: variable delays, packet drops, quantization, scheduling, and security. Techniques: sampled-data design, event-triggered control, delay compensation, co-design of control & communication.

**Surveys & tutorials**

1. **Hespanha, Naghshtabrizi & Xu (2007)** — *A survey of recent results in networked control systems* — a widely cited survey of theory & methods. (Accessible PDF)  
   https://web.ece.ucsb.edu/~hespanha/published/ncs_v15p.pdf

2. **Zhang et al. (2020)** — *Networked Control Systems: A Survey of Trends and Techniques* — contemporary survey summarizing sampled-data, quantization, event-triggered and security aspects. (IEEE/CAA J. Autom. Sinica)  
   https://ieeexplore.ieee.org/document/8985252

3. **TrueTime** — MATLAB/Simulink toolbox for co-simulating controller execution and network effects (excellent for hands-on NCS experiments).  
   https://www.control.lth.se/truetime/ · GitHub mirror: https://github.com/sfischme/truetime

**Practical tools & platforms**
- **ROS (Robot Operating System)** — widely used middleware for distributed robot control (good for prototyping networked control across nodes).  
  https://www.ros.org/

- **MQTT / DDS / OPC UA** — industrial communication middleware for NCS (useful for practical applications).

**Suggested beginner exercises**
- Simulate a simple control loop (PID on a plant) in TrueTime with different network delays and task scheduling; observe stability/performance changes.  
- Implement a ROS-based distributed controller where sensors publish data over topics and a controller node subscribes; add artificial latency and measure closed-loop response.

---

## Sensor fusion for precise & robust navigation

**Short overview**  
Sensor fusion combines complementary sensors (GNSS, IMU, camera, LiDAR, radar, UWB) to give more accurate, robust pose/scene estimates. Common algorithms: Kalman Filter (KF/EKF/UKF), particle filters, factor-graph SLAM, Graph-based smoothing (e.g. GTSAM).

**Key review papers & tutorials**

1. **Khaleghi et al. (2013)** — *Multisensor data fusion: A review of the state-of-the-art* — comprehensive survey across architectures and algorithms. (Good theoretical + reference list.)  
   https://www.sciencedirect.com/science/article/pii/S1566253511000558

2. **Burri et al. (EuRoC dataset paper)** — provides background and datasets for visual-inertial fusion (useful for hands-on experiments).  
   EuRoC MAV dataset: https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets

3. **Practical Kalman filter tutorial** — *Welch & Bishop* (classic practical Kalman filter tutorial) — excellent beginner resource.  
   (Search "An Introduction to the Kalman Filter Welch Bishop" — available as PDF widely online.)

4. **Factor graph & GTSAM** — GTSAM library & docs for smoothing & mapping (C++/Python).  
   https://gtsam.org/

**Open-source packages & repos**

- **filterpy** — Python implementations of KF/EKF/UKF/particle filters (tutorials + code). (Python)  
  https://github.com/rlabbe/filterpy · https://filterpy.readthedocs.io/

- **robot_localization (ROS)** — ROS package for fusing IMU, odometry, GPS using EKF/UKF; excellent for real robot prototyping. (C++/ROS/Python interfaces)  
  https://github.com/cra-ros-pkg/robot_localization

- **ORB-SLAM2 / ORB-SLAM3** — visual SLAM systems (C++), useful for camera-based localization pipelines.  
  https://github.com/raulmur/ORB_SLAM2

- **Google Cartographer** — SLAM (C++), real-time LiDAR/IMU fusion for mapping & localization.  
  https://github.com/googlecartographer/cartographer

**Datasets**
- **KITTI** — multi-sensor driving dataset (camera, LiDAR, GPS/IMU).  
  https://www.cvlibs.net/datasets/kitti/

- **EuRoC (visual-inertial)** — synchronized stereo + IMU + ground truth — ideal for VIO/visual-inertial fusion experiments.  
  https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets

**Suggested beginner exercises**
- Run `robot_localization` in ROS with a recorded bag (e.g., EuRoC), compare filter tuning (process/noise covariance).  
- Implement a simple EKF for a 2D robot fusing odometry + GPS using `filterpy`.  
- Try ORB-SLAM2 on EuRoC sequences to understand visual-only localization limitations.

---

## Machine-learning approaches in perception systems & control engineering

**Short overview**  
ML (especially deep learning) dominates modern perception (object detection, segmentation, depth, sensor interpretation). In control, ML methods (supervised, system ID, RL, learning-based MPC) are increasingly used. For safety-critical systems, hybrid approaches (ML + control-theoretic guarantees) are active research.

**Survey papers & tutorials (good starting points)**

1. **Grigorescu et al. (2020)** — *A Survey of Deep Learning Techniques for Autonomous Driving* — covers perception architectures, RL, end-to-end systems and challenges (data, safety). Good beginner → intermediate survey.  
   https://arxiv.org/abs/1910.07738 · Journal: J. Field Robotics (2020)

2. **Wang et al. (2021/2022)** — surveys on ML for robotics/control (look up "A Survey on Machine Learning-Based Control" & "Learning-based MPC survey"). Useful for ML + control crossovers. Example: Learning-Based MPC survey:  
   https://www.mdpi.com/2076-3417/12/4/1995

3. **Kiumarsi et al. (2018)** — *Optimal and autonomous control using reinforcement learning: a survey* — RL in optimal control contexts. (Good intro to RL-for-control).  
   PubMed: https://pubmed.ncbi.nlm.nih.gov/29771662/

**Practical frameworks & repos (Python/C++)**

- **PyTorch** — flexible deep learning framework (Python)  
  https://pytorch.org/

- **TensorFlow** & **TensorFlow Object Detection API** — many pretrained detectors and examples. (Python)  
  https://github.com/tensorflow/models/tree/master/research/object_detection

- **Stable-Baselines3** — RL algorithms implemented for research/learning experiments (Python).  
  https://github.com/DLR-RM/stable-baselines3

- **OpenAI Gym / Gymnasium** — RL environments to prototype controllers and agents.  
  https://www.gymlibrary.dev/

- **OpenCV** — essential computer vision library (C++/Python) with many tutorials for perception basics.  
  https://opencv.org/

**Suggested beginner exercises**
- Train a YOLO/ResNet-based object detector on a small subset of KITTI using PyTorch or TensorFlow OD API.  
- Use Stable-Baselines3 on a gym environment (CartPole → continuous-control envs) to learn policy-gradient / actor-critic basics.  
- Implement a simple learning-based MPC: use a neural network for residual dynamics and integrate with `do-mpc` or a custom NMPC loop.

---

## Practical toolchain & datasets (quick list)

**Control & MPC**
- `do-mpc` (Python) — https://www.do-mpc.com/ · https://github.com/do-mpc/do-mpc  
- `pyMPC` (Python) — https://github.com/forgi86/pyMPC  
- `CasADi` (C++ core, Python API) — https://web.casadi.org/  
- `OSQP` solver — https://osqp.org/ · https://github.com/osqp/osqp  
- `python-control` — https://python-control.readthedocs.io/ · https://github.com/python-control/python-control

**Robust control**
- MathWorks Robust Control Toolbox & tutorials — https://www.mathworks.com/help/robust/

**NCS & real-time simulation**
- TrueTime (MATLAB/Simulink) — https://www.control.lth.se/truetime/ · GitHub mirror: https://github.com/sfischme/truetime

**Sensor fusion & SLAM**
- `filterpy` (KF/UKF examples) — https://github.com/rlabbe/filterpy  
- `robot_localization` (ROS) — https://github.com/cra-ros-pkg/robot_localization  
- `ORB-SLAM2` — https://github.com/raulmur/ORB_SLAM2  
- `GTSAM` (factor graphs) — https://gtsam.org/

**ML & Perception**
- PyTorch — https://pytorch.org/  
- TensorFlow Object Detection API — https://github.com/tensorflow/models/tree/master/research/object_detection  
- Stable-Baselines3 (RL) — https://github.com/DLR-RM/stable-baselines3  
- OpenCV — https://opencv.org/

**Datasets**
- KITTI — https://www.cvlibs.net/datasets/kitti/  
- EuRoC MAV — https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets

---

## IRT-specific (RWTH Aachen) pages & projects (direct links)
- IRT (Institut für Regelungstechnik) — institute main page:  
  https://www.irt.rwth-aachen.de/cms/irt/~iunj/das-institut/

- IRT — **autoFerry** project (full autonomy for an overactuated ferry):  
  https://www.irt.rwth-aachen.de/cms/irt/forschung/forschungsprojekte-dyn-liste-/a-c/~bfuekb/autoferry/?lidx=1

- IRT — **AKOON** project (Automated & Coordinated Navigation of Inland Ferries):  
  https://www.irt.rwth-aachen.de/cms/irt/forschung/forschungsprojekte-dyn-liste-/a-c/~cnzsr/akoon/?lidx=1

- IRT — **Fyts** (bicycle simulator for rehabilitation / haptic training):  
  https://www.irt.rwth-aachen.de/cms/irt/forschung/forschungsprojekte-dyn-liste-/d-f/~beyyrg/fyts/?lidx=1

> If you plan to reference IRT publications specifically, use the institute page (team & publications) to find the latest papers and PhD/Master theses by group members (e.g., Prof. Heike Vallery's biomedical robotics work).

---

## Getting started — suggested learning path (6–12 weeks)

**Weeks 1–2: Control foundations**
- Study a short control course: state-space, LQR, Kalman filter. Use `python-control` tutorials and `filterpy` for practical filters.
- Read: Welch & Bishop Kalman tutorial (practical).

**Weeks 3–4: MPC basics**
- Read Mayne (2000) or the Rawlings/MPC book chapter; watch MathWorks "Understanding MPC" videos.  
- Hands-on: implement a linear MPC in `pyMPC` or `do-mpc` for a 2-DOF plant; solve via OSQP.

**Weeks 5–6: Robust control & NCS**
- Read a short H∞ tutorial (MathWorks), try an H∞ design example if you have MATLAB; otherwise study robust control chapters from a standard text.  
- Explore NCS basics via Hespanha (2007) survey. Run a TrueTime demo with delay/packet loss.

**Weeks 7–10: Sensor fusion & perception**
- Take the KHaleghi multisensor survey (2013) and a practical VIO walkthrough (EuRoC).  
- Hands-on: run ORB-SLAM2 on EuRoC; implement EKF fusion (IMU+GPS) in `filterpy`.

**Weeks 10+: ML & control integration**
- Read Grigorescu (2020) for perception surveys, and Kiumarsi (2018) / Zhang (2022) for ML-in-control surveys.  
- Train a small object detector (YOLO/TensorFlow OD API) on KITTI subset and/or learn an RL policy in Gym for a continuous control task (Stable-Baselines3).

---

## Notes on citing & further reading
- For foundational MPC theory: Mayne et al., *Automatica* (2000).  
- For modern, engineering-focused MPC: Schwenzer et al. (2021).  
- For sensor fusion theory: Khaleghi et al. (2013).  
- For ML in perception: Grigorescu et al. (2020).  
- For RL-for-control: Kiumarsi et al. (2018).

---

## Full references & links (quick list)

**IRT / RWTH (institute pages & projects)**  
- IRT — Institute page: https://www.irt.rwth-aachen.de/cms/irt/~iunj/das-institut/  
- autoFerry (IRT): https://www.irt.rwth-aachen.de/cms/irt/forschung/forschungsprojekte-dyn-liste-/a-c/~bfuekb/autoferry/?lidx=1  
- AKOON (IRT): https://www.irt.rwth-aachen.de/cms/irt/forschung/forschungsprojekte-dyn-liste-/a-c/~cnzsr/akoon/?lidx=1  
- Fyts (IRT): https://www.irt.rwth-aachen.de/cms/irt/forschung/forschungsprojekte-dyn-liste-/d-f/~beyyrg/fyts/?lidx=1

**MPC & solvers**
- Mayne D.Q., Rawlings J.B., Rao C.V., Scokaert P.O.M., *Constrained model predictive control: Stability and optimality* (Automatica, 2000): https://www.sciencedirect.com/science/article/pii/S0005109899002149  
- Mayne (2014) — *Model predictive control: Recent developments and future promise*: https://www.sciencedirect.com/science/article/abs/pii/S0005109814005160  
- Schwenzer et al. (2021) — Review: https://link.springer.com/article/10.1007/s00170-021-07682-3  
- do-mpc: https://www.do-mpc.com/ · https://github.com/do-mpc/do-mpc  
- pyMPC: https://github.com/forgi86/pyMPC  
- CasADi: https://web.casadi.org/ · https://github.com/casadi/casadi  
- OSQP: https://osqp.org/ · https://github.com/osqp/osqp

**Robust control**
- MathWorks Robust Control Toolbox (tutorials & functions): https://www.mathworks.com/help/robust/  
- python-control (Python toolbox): https://python-control.readthedocs.io/ · https://github.com/python-control/python-control

**Networked Control Systems**
- Hespanha J.P., Naghshtabrizi P., Xu Y., *A survey of recent results in networked control systems* (PDF): https://web.ece.ucsb.edu/~hespanha/published/ncs_v15p.pdf  
- Zhang et al. (2020) — *Networked Control Systems: A Survey of Trends and Techniques*: https://ieeexplore.ieee.org/document/8985252  
- TrueTime (real-time NCS simulator): https://www.control.lth.se/truetime/ · https://github.com/sfischme/truetime

**Sensor fusion & SLAM**
- Khaleghi B., Khamis A., et al. (2013) — *Multisensor data fusion: A review of the state-of-the-art*: https://www.sciencedirect.com/science/article/pii/S1566253511000558  
- filterpy (KF library + tutorials): https://github.com/rlabbe/filterpy · https://filterpy.readthedocs.io/  
- robot_localization (ROS package): https://github.com/cra-ros-pkg/robot_localization  
- GTSAM (factor graphs): https://gtsam.org/  
- ORB-SLAM2: https://github.com/raulmur/ORB_SLAM2

**Machine learning & perception**
- Grigorescu S., Trasnea B., Cocias T., Macesanu G. (2020) — *A Survey of Deep Learning Techniques for Autonomous Driving* (arXiv / J. Field Robotics): https://arxiv.org/abs/1910.07738  
- Learning-based MPC survey (2022): https://www.mdpi.com/2076-3417/12/4/1995  
- PubMed / Kiumarsi RL survey (2018): https://pubmed.ncbi.nlm.nih.gov/29771662/  
- PyTorch: https://pytorch.org/  
- TensorFlow Object Detection API: https://github.com/tensorflow/models/tree/master/research/object_detection  
- Stable-Baselines3 (RL): https://github.com/DLR-RM/stable-baselines3  
- OpenCV: https://opencv.org/

**Datasets**
- KITTI Vision Benchmark Suite: https://www.cvlibs.net/datasets/kitti/  
- EuRoC MAV dataset: https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets

---

## License & contribution
This README is a curated collection of publicly available resources (papers, toolboxes, datasets). If you add this file to a GitHub repo, consider adding an MIT/CC license file if you want to allow reuse.

