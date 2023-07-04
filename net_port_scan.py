import socket, os
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import urllib,sys
import re
import subprocess

try:
    def main_net_port_scan(target_ip, start, end):
        target = target_ip
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
                sys.exit(1)
            except socket.error:
                sys.exit(1)
            
        def fill_queue(port_list):
            for port in port_list:
                queue.put(port)

        def worker():
            while not queue.empty():
                port = queue.get()
                port_scan(port)
            
        port_list = range(start, end+1)
        fill_queue(port_list)

        with ThreadPoolExecutor(max_workers=100) as executor:
            for _ in range(queue.qsize()):
                executor.submit(worker)
        if open_ports:
            pass
        else:
            return False
        
        for ports in open_ports:
            print(ports, end=" ")
except Exception as e:
    pass
    sys.exit(1)