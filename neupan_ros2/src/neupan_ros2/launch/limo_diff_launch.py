import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # 1. 定义 RViz 配置文件路径
    rviz_cfg = PathJoinSubstitution(
        [FindPackageShare("neupan_ros2"), "rviz", "neupan.rviz"]
    )

    # 2. 定义核心配置文件路径
    config = os.path.join(
        get_package_share_directory('neupan_ros2'),
        'config',
        'limo_diff.yaml'
    )

    print(f"Using configuration file: {config}")

    return launch.LaunchDescription([
        
        # 【关键新增】发布 map -> odom 的静态变换 (0,0,0)
        # 解决 Gazebo 仿真没有 map 坐标系导致无法规划的问题
        launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_map_odom',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
            output='screen',
            parameters=[{'use_sim_time': True}]
        ),

        # 3. 启动 NeuPAN 核心节点
        launch_ros.actions.Node(
            package='neupan_ros2',
            executable='neupan_node',
            name='neupan_node',
            output="screen",
            emulate_tty=True,
            parameters=[
                config, 
                {'use_sim_time': True}  # 必须开启仿真时间同步
            ],
            remappings=[
                ('/neupan_cmd_vel', '/cmd_vel'),
                ('/scan', '/scan')
            ]
        ),
        
        # 4. 启动 RViz
        launch_ros.actions.Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            arguments=["-d", rviz_cfg],
            parameters=[{'use_sim_time': True}]
        ),
    ])