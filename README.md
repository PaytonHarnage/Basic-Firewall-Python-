# Basic-Firewall-Python-
This project implements a basic Python-based firewall that filters incoming network traffic based on IP addresses and port numbers. The firewall checks traffic against a set of predefined rules to determine whether to allow or block it. It logs all traffic actions (allowed or blocked) and provides a simple command-line interface for testing purposes

# Key Features
* IP-Based Filtering: Blocks or allows traffic from specific IP Addresses.
* Port-Based Filtering: Blocks traffic on predefined ports (e.g., HTTP, HTTPS).
* Logging: Logs all allowed and blocked traffic for review
* Simple CLI: Allows users to input source IP addresses and ports to simulate incoming traffic

# How it works
1. The firewall script checks incoming traffic against a list of allowed and blocked IP Addresses.
2. It checks the incoming port against a list of blocked ports (e.g., HTTP/HTTPS ports).
3. Based on the rules, the traffic is either allowed or blocked, and actions are logged to a fire (firewall.log).
4. The user is prompted to input an IP and port for simulated traffic, allowing for testing of different scenarios.

# Usage: 
1. Clone or download this repository
2. Run the main.py script in your terminal
3. Input IP addresses and ports for simulated traffic
4. View logged traffic actions in the firewall.log file

# Technologies Used: 
* Python for script development
* Socket Programming (simulated for traffic handling)
* Logging for tracking traffic events
