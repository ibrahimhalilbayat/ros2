from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    le_launch_description = LaunchDescription()

    isengard_node = Node(
        package="python_package",
        executable="isengard_node",
        parameters=[
            {"publishing_frequency": 2.0}
        ]
    )

    minas_tirith_node = Node(
        package="python_package",
        executable="minas_tirith_node",
        parameters=[
            {"publishing_frequency": 2.0}
        ]
    )

    mordor_node = Node(
        package="python_package",
        executable="mordor_node",
        parameters=[
            {"publishing_frequency": 2.0}
        ]
    )

    moria_node = Node(
        package="python_package",
        executable="moria_node",
        parameters=[
            {"publishing_frequency": 2.0}
        ]
    )

    riven_dell_node = Node(
        package="python_package",
        executable="riven_dell_node",
        parameters=[
            {"publishing_frequency": 2.0}
        ]
    )

    palantir_node = Node(
        package="python_package",
        executable="palantir_node"
    )

    le_launch_description.add_action(isengard_node)
    le_launch_description.add_action(mordor_node)
    le_launch_description.add_action(riven_dell_node)
    le_launch_description.add_action(moria_node)
    le_launch_description.add_action(minas_tirith_node)
    le_launch_description.add_action(palantir_node)

    return le_launch_description
