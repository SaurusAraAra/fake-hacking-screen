import os
import time
import random

green = "\033[1;32m"
reset = "\033[0m"

os.system("clear")

banner = f"""{green}
███████╗ █████╗ ██╗  ██╗███████╗
██╔════╝██╔══██╗██║ ██╔╝██╔════╝
█████╗  ███████║█████╔╝ █████╗
██╔══╝  ██╔══██║██╔═██╗ ██╔══╝
██║     ██║  ██║██║  ██╗███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

FAKE HACKING SCREEN
{reset}
"""
print(banner)

targets = [
    "192.168.0.1",
    "192.168.1.1",
    "10.0.0.1",
    "127.0.0.1",
    "185.23.44.10"
]

steps = [
    "Bypassing firewall...",
    "Scanning open ports...",
    "Injecting payload...",
    "Decrypting database...",
    "Downloading credentials...",
    "Escalating privileges...",
    "Accessing root system..."
]

for i in range(50):
    ip = random.choice(targets)
    step = random.choice(steps)
    percent = random.randint(1,100)

    print(f"{green}[+] Target {ip} -> {step} {percent}%{reset}")
    time.sleep(random.uniform(0.05,0.2))

print(f"\n{green}[✓] ACCESS GRANTED{reset}")
print(f"{green}[✓] SYSTEM CONTROLLED{reset}")
