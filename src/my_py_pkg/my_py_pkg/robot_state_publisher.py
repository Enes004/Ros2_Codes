import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotStatePublisher(Node):
    def __init__(self):
        super().__init__b("Robot_State_Publisher")
        self.robot_name = "Rover-001"
        self.publisher = self.create_publisher(String,"state_publisher_topic",10) #Created publisher
        self.timer = self.create_timer(0.5,self.publish_state)
        self.get_logger().info("Robot state publisher has been started")

    def publish_state(self):
        msg = String()
        msg.data = f"Hello , this is{self.robot_name} from Mars"
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node=RobotStatePublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()