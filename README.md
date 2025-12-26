neupan
neupan部署仿真实验

克隆代码
```bash
gitclone https://github.com/HeisenberrrRg/neupan.git
```

创建虚拟环境（ Prerequisite- Python >= 3.10）
```bash
cd neupan
python3 -m venv neupan_venv
```

进入虚拟环境
```bash
source neupan_venv/bin/activate
```

在虚拟环境中安装colcon build工具，安装PyTorch CUDA 12.1 的版本 (常用)，安装numpy < 2.0
```bash
pip install -U pip
pip install colcon-common-extensions
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip3 install "numpy<2.0" scipy matplotlib pyyaml
```

安装NeuPAN
```bash
cd ..
cd NeuPAN
pip install -e .
```

安装ir-sim
```bash
pip install ir-sim
```

neupan_ros2部分安装
```bash
cd ..
cd neupan_ros2
```

安装neupan_ros2的依赖
```bash
#（脚本安装）
chmod +x setup.sh
./setup.sh

#（手动安装）
sudo apt update
sudo apt install -y \
    ros-humble-tf2-tools \
    ros-humble-tf2-ros \
    ros-humble-nav-msgs \
    ros-humble-sensor-msgs \
    ros-humble-geometry-msgs \
    ros-humble-visualization-msgs \
    libeigen3-dev \
    libyaml-cpp-dev
```
    
build neupan_ros2 功能包
```bash
# Use build script
chmod +x build.sh
./build.sh

# Or build manually
colcon build --symlink-install
source install/setup.bash
```

跑仿真neupan_ros2仿真示例
Run Demo

**Simulation with NeuPAN:**
```bash
source install/setup.bash
ros2 launch neupan_ros2 sim_diff_launch.py sim_env_config:=scenario_corridor.yaml
```

**Alternative scenarios:** See [ddr_minimal_sim scenarios](src/ddr_minimal_sim/README.md#pre-configured-scenarios) for complete list (corridor, maze, narrow_passage, u_trap, polygon_random, empty)

### Usage Scenarios

#### Scenario 1: Real Robot Deployment (Limo)

Deploy NeuPAN on physical Limo robot:

```bash
# Make sure Limo drivers are running
ros2 launch neupan_ros2 limo_diff_launch.py
```

#### Scenario 2: Complete Simulation

Full system with simulator + NeuPAN planner:

```bash
ros2 launch neupan_ros2 sim_diff_launch.py

ros2 launch neupan_ros2 sim_diff_launch.py sim_env_config:=scenario_maze.yaml
```




