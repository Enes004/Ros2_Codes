import rclpy
from rclpy.node import Node

# MyNode sınıfı, ROS2'nin "Node" sınıfından miras (inheritance) alır.
# Yani: "Sen artık sıradan bir Python sınıfı değil, bir ROS Robot Düğümüsün" diyoruz.
class MyNode(Node):

    def __init__(self):
        # 1. Önce miras aldığımız Node sınıfını başlatıyoruz.
        # 'ilk_dugum' -> Bu düğümün ROS ağındaki adı (kimliği) olacak.
        super().__init__('ilk_dugum') 

        # 2. Terminale log (mesaj) basmak için print() yerine bunu kullanırız.
        # Çünkü bu loglar ROS sistemine tarih/saat etiketiyle kaydedilir.
        self.get_logger().info('ROS2 Dünyasına Hoş Geldin Enes!')

        # 3. Bir zamanlayıcı (Timer) kuruyoruz.
        # 1.0 -> Kaç saniyede bir çalışsın? (1.0 saniye)
        # self.timer_callback -> Süre dolunca hangi fonksiyonu çalıştırsın?
        self.create_timer(1.0, self.timer_callback)

    # Zamanlayıcı her tetiklendiğinde burası çalışır (Sözel döngü gibi düşün)
    def timer_callback(self):
        self.get_logger().info('Merhaba! Kodun başarıyla çalışıyor.')

def main(args=None):
    # 1. ROS2 iletişim sistemini başlatır (Motoru çalıştır).
    rclpy.init(args=args)

    # 2. Yukarıda yazdığımız sınıftan bir nesne (robot beyni) oluşturuyoruz.
    node = MyNode()

    # 3. BURASI ÇOK ÖNEMLİ: rclpy.spin()
    # Bu komut "Programı kapatma, açık tut ve gelecek olayları (timer, sensör verisi vs.) bekle" der.
    # Eğer bunu yazmazsan program "node = MyNode()" satırından sonra hemen kapanır.
    # Sonsuz döngü (while True) gibi çalışır ama işlemciyi yormaz.
    rclpy.spin(node)

    # 4. Program kapatılınca (Ctrl+C yapılınca) temizlik yapar ve ROS'u kapatır.
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    #main