import socket, os
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import urllib,sys
import re

try:
    def main_web_port_scan():
        target = input("Enter your target website url: ")
        starting_range = int(input("Enter starting range of ports: "))
        ending_range = int(input("Enter ending range of ports: "))


        if not target:
            print("\n You didn't provide any input!")
            sys.exit(1)
        
        if not starting_range or not ending_range:
            print("\n You didn't provide ranges.")
            sys.exit(1)

        if starting_range <= 0 or ending_range > 65535:
            print("\n Invalid Ranges!")
            sys.exit(1) 


        if target.startswith("http://"):
            target = target.replace("http://", "", 1)
        elif target.startswith("https://"):
            target = target.replace("https://", "", 1)

        queue = Queue()
        open_ports = []

        # Port Scan Logic Starts from Here

        def port_scan(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except socket.gaierror:
                print("\n Unable to connect to the target!")
                sys.exit(1)
            except socket.error:
                print("\n Unable to connect to the target!")
                sys.exit(1)
            
        def fill_queue(port_list):
            for port in port_list:
                queue.put(port)

        def worker():
            while not queue.empty():
                port = queue.get()
                port_scan(port)
        
        port_list = range(starting_range, ending_range+1)
        fill_queue(port_list)

        with ThreadPoolExecutor(max_workers=100) as executor:
            for _ in range(queue.qsize()):
                executor.submit(worker)
        if open_ports:
            pass
        else:
            return False
        
        for port in open_ports:
            print(port, end=" ")
except Exception as e:
    print("\n An Error Occurred!")
    sys.exit(1)