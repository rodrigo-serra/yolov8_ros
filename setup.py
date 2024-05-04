from setuptools import setup

package_name = 'yolov8_ros'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rodrigo Franco Serra',
    maintainer_email='rodrigo.serra@tecnico.ulisboa.pt',
    description='YOLOv8 for ROS 1',
    license='GPL-3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'yolov8_node = yolov8_ros.yolov8_node:main',
                'debug_node = yolov8_ros.debug_node:main',
                'tracking_node = yolov8_ros.tracking_node:main',
                'detect_3d_node = yolov8_ros.detect_3d_node:main',
        ],
    },
)
