import socket
import psutil

def get_network_info():
    # Get the hostname
    hostname = socket.gethostname()
    
    # Get the local IP address
    local_ip = socket.gethostbyname(hostname)
    
    # Get the external IP address (using a simple public API)
    external_ip = psutil.net_if_addrs()
    
    print("Network Information:")
    print(f"Hostname: {hostname}")
    print(f"Local IP Address: {local_ip}")
    print("External IP Address Information:")
    print(external_ip)

if __name__ == "__main__":
    get_network_info()
