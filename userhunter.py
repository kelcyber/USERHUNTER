#!/usr/bin/env python3

import argparse
import time

BANNER = """
      ╔════════════════════════════════════════════╗
      ║      𝐔𝐬𝐞𝐫𝐇𝐮𝐧𝐭𝐞𝐫 - 𝐁𝐲 𝐊𝐞𝐥𝐜𝐲𝐛𝐞𝐫           ║
      ║      ╔════════════════════════════════╗     ║
      ║      ║    ⛧ Username & OSINT Tool    ║     ║
      ╚════════════════════════════════════════════╝
"""

print(BANNER)

def search_username(username):
    print(f"[+] Searching for username: {username}")
    time.sleep(1)
    print(f"[+] Found results for {username} on 10+ platforms (placeholder)")

def phone_lookup(phone):
    print(f"[+] Looking up phone number: {phone}")
    time.sleep(1)
    print("[+] Phone information (placeholder)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UserHunter - Username & OSINT Tool")
    parser.add_argument('--username', help='Username to search')
    parser.add_argument('--phone', help='Phone number to lookup')
    args = parser.parse_args()

    if args.username:
        search_username(args.username)
    if args.phone:
        phone_lookup(args.phone)
