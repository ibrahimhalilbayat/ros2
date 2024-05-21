from setuptools import setup

package_name = 'python_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='frodo',
    maintainer_email='frodo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "python_node = python_package.first_node:main",
            "python_publisher = python_package.first_python_publisher:main",
            "python_subscriber = python_package.first_python_subscriber:main",
            "hw1_node = python_package.hw1:main",
            "hw2_node = python_package.hw2:main",
            "example_server_node = python_package.example_server:main",
            "example_client_node = python_package.example_client:main",
            "health_node = python_package.health_publisher:main",
            "battery_node = python_package.led_client:main",
            "led_node = python_package.led_server:main",
            "isengard_node = python_package.news_from_isengard:main",
            "minas_tirith_node = python_package.news_from_minas_tirith:main",
            "mordor_node = python_package.news_from_mordor:main",
            "moria_node = python_package.news_from_moria:main",
            "rivendell_node = python_package.news_from_rivendell:main",
            "palantir_node = python_package.palantir:main",
            "news_of_middle_earth_node = python_package.news_of_middle_earth:main"
                            ],
    },
)
