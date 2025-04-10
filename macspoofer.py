#!/usr/bin/env python3

import subprocess
import argparse
import re
import random
import os
import sys
import time

# Banner
def show_banner():
    banner = r"""
  ____  _____      _      _       
 |  _ \| ____|    | |    (_)      
 | |_) | |__   ___| |_ __ _ _ __  
 |  _ <|  __| / __| __/ _` | '_ \ 
 | |_) | |____\__ \ || (_| | | | |
 |____/|______|___/\__\__,_|_| |_|

       MAC Spoofer - by Rawat_Shiva
              Codename: BErlin
    """
    print("\033[96m" + banner + "\033[0m")  # Cyan color banner


# Function to generate a random MAC address
def generate_random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0x00, 0xFF) for _ in range(5))

# Function to get current MAC address
def get_current_mac(interface):
    try:
        result = subprocess.check_output(["ip", "link", "show", interface], text=True)
        mac_address = re.search(r"link/ether (\S+)", result)
        return mac_address.group(1) if mac_address else None
    except subprocess.CalledProcessError:
        print(f"[!] Could not find interface {interface}")
        sys.exit(1)

# Function to change MAC address
def change_mac(interface, new_mac):
    try:
        subprocess.call(["ip", "link", "set", interface, "down"])
        subprocess.call(["ip", "link", "set", interface, "address", new_mac])
        subprocess.call(["ip", "link", "set", interface, "up"])
        print(f"[+] MAC address for {interface} changed to {new_mac}")
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

# Function to store and restore original MAC
def restore_mac(interface, original_mac):
    if not original_mac:
        print("[!] No original MAC address saved.")
        sys.exit(1)
    change_mac(interface, original_mac)
    print(f"[+] MAC address for {interface} restored to {original_mac}")

def is_root():
    return os.geteuid() == 0

# Main
if __name__ == "__main__":
    if not is_root():
        print("[!] Please run as root (sudo).")
        sys.exit(1)

    show_banner()

    parser = argparse.ArgumentParser(description="MAC Address Spoofing Tool for Kali Linux - by Rawat_Shiva")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g. eth0, wlan0)")
    parser.add_argument("-m", "--mac", help="New MAC address to assign")
    parser.add_argument("-r", "--random", action="store_true", help="Generate a random MAC address")
    parser.add_argument("--restore", action="store_true", help="Restore original MAC address")

    args = parser.parse_args()

    current_mac = get_current_mac(args.interface)
    if current_mac is None:
        print("[!] Could not read current MAC address.")
        sys.exit(1)

    if args.restore:
        restore_mac(args.interface, current_mac)
    else:
        if args.random:
            new_mac = generate_random_mac()
        elif args.mac:
            new_mac = args.mac
        else:
            print("[!] You must specify --mac or --random or --restore.")
            sys.exit(1)

        change_mac(args.interface, new_mac)
