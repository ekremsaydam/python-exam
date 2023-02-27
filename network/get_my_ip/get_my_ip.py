"""Get My ip."""
import socket


def get_ip_address():
    """Get my ip."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    print("\tLocal IP :", local_ip)


get_ip_address()
