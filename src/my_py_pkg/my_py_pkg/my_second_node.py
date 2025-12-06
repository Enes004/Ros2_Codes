import rclpy
from rclpy.node import Node

class MyNode2(Node):
    def __init__(self):
        super().__init__("remember_node")
        self.counter = 0
        self.get_logger().info("Hello Ros")
        self.create_timer(1,self.timer_callback)
    
    def timer_callback(self):
        self.counter +=1
        self.get_logger().info("aleyküm esselam duydum seni")
       

def main(args=None):
    rclpy.init(args=args)
    MyNodeObject = MyNode2()
    rclpy.spin(MyNodeObject)
    rclpy.shutdown()

if __name__ == "__main__":
    main()