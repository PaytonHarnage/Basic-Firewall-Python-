import logging

# Set up logging to track blocked or allowed traffic
logging.basicConfig(filename="firewall.log", level=logging.INFO)

# Define a list of allowed and blocked IPs
allowed_ips = ['192.168.1.100', '192.168.1.101']
blocked_ips = ['192.168.1.102', '192.168.1.103']

# Define ports to block
blocked_ports = [80, 443]  # Block HTTP and HTTPS ports

# Function to check if the traffic should be allowed
def check_traffic(ip, port):
    """Check if the incoming traffic is allowed based on IP and port."""
    # Check if the IP is in the blocked list
    if ip in blocked_ips:
        logging.warning(f"Blocked IP: {ip}")
        return False
    # If IP is not in allowed list, treat it as allowed by default
    if ip not in allowed_ips:
        logging.info(f"Allowed IP: {ip}")
    
    # Check if the port is blocked
    if port in blocked_ports:
        logging.warning(f"Blocked Port: {port}")
        return False
    
    return True

# Function to simulate receiving traffic and applying firewall rules
def receive_traffic():
    """Simulate receiving network traffic and apply firewall rules."""
    while True:
        # Simulate receiving traffic by asking user for IP and port
        ip = input("Enter source IP address: ")
        port = int(input("Enter source port number: "))
        
        # Check if the traffic should be allowed
        if check_traffic(ip, port):
            print(f"Traffic from {ip} on port {port} allowed.")
        else:
            print(f"Traffic from {ip} on port {port} blocked.")
        
        # Ask if the user wants to continue testing
        continue_flag = input("Continue? (y/n): ")
        if continue_flag.lower() != 'y':
            break

# Main function to run the firewall
def main():
    """Main function to run the firewall simulation."""
    print("Simple Python Firewall\n")
    receive_traffic()

if __name__ == "__main__":
    main()
