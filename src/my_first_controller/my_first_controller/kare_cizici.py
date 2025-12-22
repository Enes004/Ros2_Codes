import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from my_robot_interfaces.msg import Telemetry



class Kare_Cizici(Node):
    def __init__(self):
        super().__init__('kare_cizici_node')
        self.get_logger().info("Node basladi")

        # Velocity publisher controls the motion via /turtle1/cmd_vel topic
        self.velocity_publisher = self.create_publisher(Twist,'/turtle1/cmd_vel',10)

        # Hız yayıncısının altına ekleyebilirsin
        self.telemetry_publisher = self.create_publisher(Telemetry, '/robot_telemetry', 10)
        
        # Turtledan gelen mesajları alıp bu mesajları işlediğimiz yer
        self.location_listener = self.create_subscription(Pose , '/turtle1/pose', self.location_callback,10)

        # Bizim kendimizin sabit bir ritim kullanarak yapacağımız işler için bir timer oluşturduk
        self.timer = self.create_timer(0.1 , self.kare_cizen_dongu)


        #variables that store data
        self.baslangic_x = None
        self.baslangic_y = None
        self.baslangic_theta = None
        self.anlik_konum = None
        self.state = "ILERI_GIT"




        #Kaplumbagadan gelen veriyi msg ile aldık , terminale dümenden basalım şimdilik
        # Bak kardeşim, ben şimdi başka işlerle uğraşacağım.
        # Ama /turtle1/pose kanalından bir mesaj (pizza) gelirse, benim şu konum_guncelle numaramı ara (Call me back!)
        # Bir mesaj gelirse çalışır

    def location_callback(self,msg):
        self.anlik_konum = msg         # msg includes (x,y,theta)

        if (self.baslangic_x == None):
            self.baslangic_x = msg.x
            self.baslangic_y = msg.y
            self.get_logger().info(f"Baslangic Noktasi -> x: {msg.x} , y: {msg.y}")


    def kare_cizen_dongu(self):
        if self.anlik_konum is None:
            return
        
        mesafe = math.sqrt(
            (self.anlik_konum.x - self.baslangic_x)**2 
                              +
            (self.anlik_konum.y - self.baslangic_y)**2 ) 

        hareket_komutu= Twist()

        if self.state == "ILERI_GIT":
            if mesafe<2.0:
                hareket_komutu.linear.x = 1.0
                self.get_logger().info(f"Gidiliyor... Mesafe: {mesafe:.2f}")
            
            else:
                hareket_komutu.linear.x = 0.0
                self.state = "DONUS_YAP"
                self.baslangic_theta = self.anlik_konum.theta 
                self.get_logger().info("Hedefe ulaşildi, durdum!")

        elif self.state == "DONUS_YAP":
            fark = self.anlik_konum.theta - self.baslangic_theta
            
            # 2. Açı zıplamasını (wrapping) düzelt
            # Bu iki satır açıyı her zaman en kısa yoldan hesaplar
            if fark > math.pi: fark -= 2 * math.pi
            if fark < -math.pi: fark += 2 * math.pi
            
            donus_miktari = abs(fark)

            # 3. 1.57 yerine tam değer kullan: math.pi / 2
            if donus_miktari < (math.pi / 2.0):
                # Hedefe yaklaştıkça hızı düşürürsek (P kontrol) daha hassas durur
                # Şimdilik sabit 0.1 kalsın ama yavaş olması iyidir
                hareket_komutu.angular.z = 0.2 
            else:
                # DURUŞ
                hareket_komutu.angular.z = 0.0
                self.velocity_publisher.publish(hareket_komutu) # Hemen dur komutu gönder
                
                self.state = "ILERI_GIT"
                self.baslangic_x = self.anlik_konum.x
                self.baslangic_y = self.anlik_konum.y
                self.get_logger().info("90 derece tamam! Yeni kenar.")

        self.velocity_publisher.publish(hareket_komutu)

        # 2. Telemetriyi yayınla (Rapor)
        t_msg = Telemetry()
        t_msg.x = self.anlik_konum.x
        t_msg.y = self.anlik_konum.y
        t_msg.theta = self.anlik_konum.theta
        t_msg.durum = self.state 
        
        self.telemetry_publisher.publish(t_msg)


        
def main(args=None):
    rclpy.init(args=args)

    mynode = Kare_Cizici()

    rclpy.spin(mynode)
    rclpy.shutdown()

if __name__ == '__main__':
    main()