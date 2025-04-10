# mac-spoofer07
# 🛠️ BErlin - MAC Address Spoofing Tool

**BErlin** is a lightweight, Python-based MAC address spoofer built for Kali Linux.  
Change your MAC address to a custom one, randomize it for privacy, or restore the original with ease.

> 🔒 Made by **Rawat_Shiva** for ethical hacking and cybersecurity learning.

✅ How to Use:

# Clone and run ( give the permission )
chmod +x mac_spoofer.py

# Spoof with custom MAC 
sudo ./mac_spoofer.py -i eth0 -m 00:11:22:33:44:55

# Spoof with random MAC
sudo ./mac_spoofer.py -i wlan0 --random

# Restore (same session)
sudo ./mac_spoofer.py -i wlan0 --restore
