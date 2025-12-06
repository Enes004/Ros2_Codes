#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node): #Inheritance

    def __init__(self): #constructor

        super().__init__("phyton_test") #parent class constructor
        self.get_logger().info("Selam world")
        self.counter = 0 # Object of MyNode class , Encapsulation
        self.create_timer(0.5 , self.timer_callback)#0,5 saniyede bir fonksiyonu çağır

    def timer_callback(self): # Object Method
        self.counter += 1
        self.get_logger().info(f"aleyküm selam world , {self.counter}")

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
    