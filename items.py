
# items.py

# Importing the global shop multiplier from config
from config import SHOP_COST_MULTIPLIER

def apply_cost_multiplier(item_list):
    """Apply a global cost multiplier to items."""
    for item in item_list:
        item['cost'] = int(item['cost'] * SHOP_COST_MULTIPLIER)
    return item_list

defense_upgrades = apply_cost_multiplier([
    {"name": "Firewall Upgrade", "defense": 5, "cost": 20},
    {"name": "Antivirus Suite", "defense": 3, "cost": 15},
    {"name": "Intrusion Detection System", "defense": 8, "cost": 50},
    {"name": "Encrypted Hard Drive", "defense": 6, "cost": 30},
    {"name": "Advanced Firewall", "defense": 8, "cost": 40},
    {"name": "Biometric Scanner", "defense": 10, "cost": 50},
    {"name": "Intrusion Prevention System", "defense": 12, "cost": 60},
    {"name": "Hardened Kernel", "defense": 9, "cost": 45},
    {"name": "Secure VPN", "defense": 7, "cost": 35},
    {"name": "Two-Factor Authenticator", "defense": 5, "cost": 25},
    {"name": "SSL Certificate", "defense": 4, "cost": 20},
    {"name": "Patch Management System", "defense": 11, "cost": 55},
    {"name": "Data Loss Prevention", "defense": 13, "cost": 65},
    {"name": "Endpoint Protection", "defense": 14, "cost": 70},
    {"name": "Advanced Encryption", "defense": 15, "cost": 80},
    {"name": "Zero Trust Architecture", "defense": 16, "cost": 85},
    {"name": "Behavioral Analytics", "defense": 10, "cost": 50},
    {"name": "Physical Security Token", "defense": 6, "cost": 32},
    {"name": "Network Segmentation", "defense": 8, "cost": 38},
    {"name": "Intrusion Detection System Pro", "defense": 18, "cost": 90},
    {"name": "Air-Gapped Backup", "defense": 20, "cost": 100},
    {"name": "Anti-Malware Suite", "defense": 12, "cost": 60},
    {"name": "Incident Response Team", "defense": 19, "cost": 95}
])

offense_tools = apply_cost_multiplier([
    {"name": "Basic Exploit Kit", "attack": 5, "cost": 25},
    {"name": "Penetration Testing Toolkit", "attack": 10, "cost": 50},
    {"name": "Zero-Day Exploit", "attack": 15, "cost": 75},
    {"name": "Packet Injector", "attack": 7, "cost": 30},
    {"name": "Brute Force Script", "attack": 9, "cost": 40},
    {"name": "Sniffer Tool", "attack": 12, "cost": 50},
    {"name": "Exploit Chain", "attack": 14, "cost": 60},
    {"name": "Phishing Toolkit", "attack": 10, "cost": 45},
    {"name": "Privilege Escalation Kit", "attack": 15, "cost": 70},
    {"name": "Social Engineering Suite", "attack": 8, "cost": 35},
    {"name": "Denial-of-Service Module", "attack": 11, "cost": 55},
    {"name": "Keylogger Installer", "attack": 9, "cost": 38},
    {"name": "Remote Access Tool", "attack": 13, "cost": 65},
    {"name": "Backdoor Creator", "attack": 16, "cost": 75},
    {"name": "Zero-Day Finder", "attack": 18, "cost": 85},
    {"name": "SQL Injector Pro", "attack": 14, "cost": 60},
    {"name": "DNS Spoofer", "attack": 10, "cost": 50},
    {"name": "Man-in-the-Middle Proxy", "attack": 12, "cost": 55},
    {"name": "Web Shell Deployer", "attack": 15, "cost": 70},
    {"name": "Rootkit Builder", "attack": 17, "cost": 80},
    {"name": "Credential Harvester", "attack": 11, "cost": 48},
    {"name": "Worm Propagator", "attack": 19, "cost": 90},
    {"name": "Botnet Command Tool", "attack": 20, "cost": 100}
])

threats = [
    {"name": "Rogue Botnet", "hp": 30, "attack": 5, "money": 10, "xp": 10},
    {"name": "Phishing Scam", "hp": 50, "attack": 8, "money": 20, "xp": 20},
    {"name": "Advanced Persistent Threat", "hp": 80, "attack": 12, "money": 30, "xp": 30},
    {"name": "Ransomware Attack", "hp": 100, "attack": 15, "money": 40, "xp": 40},
    {"name": "Malware Injection", "hp": 60, "attack": 10, "money": 25, "xp": 25},
    {"name": "Keylogger Breach", "hp": 70, "attack": 9, "money": 35, "xp": 30},
    {"name": "DNS Spoof", "hp": 90, "attack": 13, "money": 45, "xp": 35},
    {"name": "Trojan Horse", "hp": 120, "attack": 17, "money": 50, "xp": 50},
    {"name": "Worm Invasion", "hp": 110, "attack": 18, "money": 55, "xp": 60},
    {"name": "Spyware Breach", "hp": 95, "attack": 14, "money": 38, "xp": 45},
    {"name": "Adware Storm", "hp": 80, "attack": 11, "money": 30, "xp": 35},
    {"name": "Rootkit Strike", "hp": 130, "attack": 20, "money": 60, "xp": 70},
    {"name": "SQL Injection", "hp": 100, "attack": 16, "money": 42, "xp": 50},
    {"name": "Brute Force Assault", "hp": 120, "attack": 19, "money": 58, "xp": 65},
    {"name": "XSS Barrage", "hp": 85, "attack": 12, "money": 33, "xp": 40},
    {"name": "Man-in-the-Middle", "hp": 115, "attack": 17, "money": 50, "xp": 55},
    {"name": "DDoS Swarm", "hp": 140, "attack": 22, "money": 70, "xp": 80},
    {"name": "Packet Sniffer", "hp": 90, "attack": 13, "money": 36, "xp": 43}
]
