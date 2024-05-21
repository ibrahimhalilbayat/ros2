from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    launch_description = LaunchDescription()
    location_names = ["Rivendell", "Moria", "Mordor", "Minastirith", "Isengard"]
    news_nodes = []

    for location in location_names:
        news_nodes.append(Node(
            package="python_package",
            executable="news_of_middle_earth_node",
            name= "news_from_" + location.lower(),
            parameters=[
                {"location_name": location,
                 "publish_freq": 2.0}          
            ]
        ))


    palantir_node = Node(
        package="python_package",
        executable="palantir_node",
        name="palantir"
    )

    for node in news_nodes:
        launch_description.add_action(node)
    launch_description.add_action(palantir_node)

    return launch_description
