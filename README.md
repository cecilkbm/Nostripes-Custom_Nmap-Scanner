# 🛰️ Custom Nmap Automation Tool (Python)
A Python-based command-line Nmap automation tool that simplifies common network scanning workflows by wrapping Nmap functionality into an interactive script.

This project was built to explore network reconnaissance, port scanning techniques, and basic security automation, while gaining hands-on experience using Nmap programmatically through Python.

---
## Technologies
  - Python 3
  - Nmap
  - python-nmap library
  - Linux / Unix-based environments
  - CLI-based interaction
#
## Features
  - Interactive scan type selection
  - User-supplied target IP address
  - Automated execution of common Nmap scan profiles
  - Supports multiple scan modes:
    - SYN ACK scan
    - UDP scan
    - Comprehensive service & OS detection scan
  - Displays scan metadata, host state, protocols, and open ports
  - Custom port range scanning (ports 20–700)
#
## 🧠 The Process
The goal of this project was to move beyond running Nmap manually and instead automate reconnaissance workflows using Python.

By leveraging the python-nmap module, I built a simple interface that:
  - Accepts user input
  - Executes predefined Nmap scan flags
  - Parses and displays structured scan results

This project helped bridge the gap between manual security tooling and scripted automation, which is a key skill in SOC, security engineering, and red team workflows.
#
## Lessons Learned
  - How Nmap scan types differ (SYN, UDP, comprehensive scans)
  - Programmatic control of external security tools
  - Parsing and navigating structured scan results
  - Automating repetitive reconnaissance tasks
  - The importance of validating user input and scan scope
  
It also reinforced that automation amplifies both capability and responsibility when running security tools.
#
## Scan Modes Explained
### 1️⃣ SYN ACK Scan
  - Uses TCP SYN scanning
  - Fast and stealthy
  - Common for identifying open TCP ports
### Flags used:
    -sS -v
### 2️⃣ UDP Scan
  - Identifies open UDP services
  - Slower but essential for full visibility
### Flags used:
    -sU -v
### 3️⃣ Comprehensive Scan (Ports 20–700)
  - Service and version detection
  - Default scripts enabled
  - OS detection and aggressive scanning
### Flags used:
    -sS -sC -sV -A -O -v
#
## ▶️ Running the Tool
### Prerequisites
  - Nmap installed on the system
  - Python 3
  - python3-nmap library

        pip install python3-nmap
### Run
    python3 Nmapscanner.py
#
## ⚠️ Usage Warning
This tool should only be used on systems you own or have explicit permission to scan.
Unauthorized scanning may be illegal and unethical.
#
## 📷 Preview
<img width="600" height="600" alt="NM1" src="https://github.com/user-attachments/assets/0c6c6d7e-c187-4161-b25d-8830cdfc709e" />
 
#
