#!/usr/bin/python3
import nmap

nscan = nmap.PortScanner()
p_start = 20
p_end = 700

# ASCII Art Banner
banner = r"""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ███╗   ██╗ ██████╗ ███████╗████████╗██████╗ ██╗██████╗ ███████╗  ║
║   ████╗  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗██║██╔══██╗██╔════╝  ║
║   ██╔██╗ ██║██║   ██║███████╗   ██║   ██████╔╝██║██████╔╝█████╗    ║
║   ██║╚██╗██║██║   ██║╚════██║   ██║   ██╔══██╗██║██╔═══╝ ██╔══╝    ║
║   ██║ ╚████║╚██████╔╝███████║   ██║   ██║  ██║██║██║     ███████╗  ║
║   ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝  ║
║                                                                    ║
║                  ███████╗ ██████╗ █████╗ ███╗   ██╗                ║
║                  ██╔════╝██╔════╝██╔══██╗████╗  ██║                ║
║                  ███████╗██║     ███████║██╔██╗ ██║                ║
║                  ╚════██║██║     ██╔══██║██║╚██╗██║                ║
║                  ███████║╚██████╗██║  ██║██║ ╚████║                ║
║                  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝                ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝

           ░▒▓ No Stripes? No Problem! ▓▒░
        
              /|       |\
             / |       | \              "Blending into networks
            |  |-------|  |              since [REDACTED]"
             \ |  ___  | /
              \| |   | |/               A Stealthy Nmap Automation Tool
                 |   |                  
              ___|   |___               by NostripesZebra
             |___________|
             
═══════════════════════════════════════════════════════════════════
"""

print(banner)

ip_addr = input("\n🎯 Please enter the IP address you want to scan: ")
print(f"📍 Target locked: {ip_addr}")
type(ip_addr)

resp = input("""\n🔍 Please Enter Scan Type:
                1) SYN ACK Scan (Stealth)
                2) UDP Scan
                3) Comprehensive Scan (Ports 20-700)
                
    Your choice: """)

print(f"\n⚡ Initiating scan type: {resp}")
print("═" * 67)

if resp == '1':
    print(f"📡 Nmap Version: {nscan.nmap_version()}")
    print("🔎 Running SYN ACK Scan on ports 1-1024...")
    nscan.scan(ip_addr, '1-1024', '-v -sS')
    print(f"\n📊 Scan Info: {nscan.scaninfo()}")
    print(f"🌐 IP Status: {nscan[ip_addr].state()}")
    print(f"📋 Protocols: {nscan[ip_addr].all_protocols()}")
    print(f"🔓 Open Ports: {nscan[ip_addr]['tcp'].keys()}")
    
elif resp == '2':
    print(f"📡 Nmap Version: {nscan.nmap_version()}")
    print("🔎 Running UDP Scan on ports 1-1024...")
    nscan.scan(ip_addr, '1-1024', '-v -sU')
    print(f"\n📊 Scan Info: {nscan.scaninfo()}")
    print(f"🌐 IP Status: {nscan[ip_addr].state()}")
    print(f"📋 Protocols: {nscan[ip_addr].all_protocols()}")
    print(f"🔓 Open Ports: {nscan[ip_addr]['udp'].keys()}")
    
elif resp == '3':
    print(f"📡 Nmap Version: {nscan.nmap_version()}")
    print("🔎 Running Comprehensive Scan (This may take a while)...")
    nscan.scan(ip_addr, '20-700', '-v -sS -sC -sV -A -O')
    print(f"\n📊 Scan Info: {nscan.scaninfo()}")
    print(f"🌐 IP Status: {nscan[ip_addr].state()}")
    print(f"📋 Protocols: {nscan[ip_addr].all_protocols()}")
    print(f"\n🔍 Detailed Port Analysis (Ports {p_start}-{p_end}):")
    print("─" * 67)
    for i in range(p_start, p_end+1):
        res = nscan.scan(ip_addr, str(i))
        res = res['scan'][ip_addr]['tcp'][i]['state']
        status_icon = "🟢" if res == "open" else "🔴"
        print(f'{status_icon} Port {i:4d} is {res}')
    
else:
    print("❌ Invalid input! Please run the script again and choose 1, 2, or 3.")

print("\n" + "═" * 67)
print("✅ Scan Complete! Stay invisible. 🦓")
print("═" * 67)
