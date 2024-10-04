from scapy.all import *

def packet_callback(packet):
   
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")
        
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"TCP Packet: Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")
        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"UDP Packet: Source Port: {udp_layer.sport}, Destination Port: {udp_layer.dport}")
        elif packet.haslayer(ICMP):
            print("ICMP Packet")
        else:
            print(f"Other Protocol: {packet.summary()}")

        
        if packet.haslayer(Raw):
            payload = packet.getlayer(Raw).load
            print(f"Payload: {payload}")
        print("-" * 50)

def start_sniffer(interface=None):
    print("Starting packet capture...")
    if interface:
        sniff(iface=interface, prn=packet_callback, store=0)
    else:
        sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
   
    interface = None  
    start_sniffer(interface)
