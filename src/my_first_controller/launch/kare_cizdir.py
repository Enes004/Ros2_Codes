from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Kaplumbağa Simülasyonunu Başlat
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # 2. Senin Yazdığın Kare Çizici Kodunu Başlat
        Node(
            package='my_first_controller',
            executable='kare_cizici_exe', # Buraya dikkat, setup.py'daki ismi yazacağız
            name='controller'
        )
    ])