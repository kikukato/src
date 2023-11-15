import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class SerialCommandPublisher(Node):
    def __init__(self):
        super().__init__('serial_command_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.serial_port = '/dev/ttyACM0'  # Ajusta el puerto serial según tu configuración
        self.serial_baudrate = 9600
        self.serial_timeout = 1

        try:
            self.ser = serial.Serial(self.serial_port, self.serial_baudrate, timeout=self.serial_timeout)
            self.get_logger().info(f'Serial port {self.serial_port} opened successfully.')
        except serial.SerialException as e:
            self.get_logger().error(f'Error opening serial port: {e}')
            rclpy.shutdown()

        self.timer = self.create_timer(0.1, self.publish_command)

    def publish_command(self):
        try:
            if self.ser.in_waiting > 0:
                received_data = self.ser.readline().decode('utf-8').rstrip()
                self.get_logger().info(f'Received command: {received_data}')

                twist_msg = Twist()

                if received_data == 'w':
                    twist_msg.linear.x = 0.1  # Ajusta la velocidad lineal hacia adelante según tus necesidades
                elif received_data == 'x':
                    twist_msg.linear.x = -0.1  # Ajusta la velocidad lineal hacia atrás según tus necesidades
                elif received_data == 'a':
                    twist_msg.angular.z = 0.5  # Ajusta la velocidad angular hacia la izquierda según tus necesidades
                elif received_data == 'd':
                    twist_msg.angular.z = -0.5  # Ajusta la velocidad angular hacia la derecha según tus necesidades
                elif received_data == 's':
                    twist_msg.angular.z = 0.0  # Ajusta la velocidad angular hacia la derecha según tus necesidades
                    twist_msg.linear.x = 0.0    

                self.publisher_.publish(twist_msg)

        except serial.SerialException as e:
            self.get_logger().error(f'Serial communication error: {e}')

def main(args=None):
    rclpy.init(args=args)

    serial_command_publisher = SerialCommandPublisher()

    rclpy.spin(serial_command_publisher)

    serial_command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()