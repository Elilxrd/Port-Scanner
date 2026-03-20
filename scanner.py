
import socket # For creating a socket to connect to the target IP and check if the port is open or not
import threading # For multithreading to allow my port scanner to run faster

start_port = int(input("Starting port: "))
end_port = int(input("Ending port: "))

target = input("Enter target IP: ")
target = socket.gethostbyname(target)

def scan_port(port): # This function will be used to scan a single port and check if it is open or not
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if s.connect_ex((target, port)) ==0:
         print(f"[+]Port {port} is OPEN")

    s.close()

for port in range(start_port, end_port): # This loop will iterate through the specified range of ports and create a thread for each port to scan it concurrently
     thread = threading.Thread(target=scan_port, args=(port,))
     thread.start()
