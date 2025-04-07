# 🔐 BruteLogin
Here’s a simple Python script for brute-forcing form-based login pages. For educational purposes and authorized security testing only.

## ⚠️ Legal disclaimer!
Don't be a lammer running this script randomly.
This was made for LEARNING PURPOSES ONLY.
Unauthorized use = ILLEGAL AF (CFAA, GDPR, etc.)

## 🚀 Functions:
- Sends POST requests with different passwords from a wordlist.
- Progress bar implemented using tqdm.
- Detects successful login by checking for a success keyword in the HTML response.
- Reads credentials and form fields directly from user input via CLI.

## 🛠️ Requirements:
Python 3.x

Required libraries:
  requests
  tqdm

You can install the required libraries with:
pip install requests tqdm

## 📥 Instalation:
Clone this repository:
git clone https://github.com/MatheusLAmazonas/brute-login
cd brute-login

## 📦 How to use:
python bruteforce_login.py

Exemplo de uso:
Enter the login URL: https://exemplo.com/login
Enter the username field name: user
Enter the password field name: pass
Enter the username to test: admin
Enter the path to the wordlist: wordlist.txt
Enter a keyword that indicates a successful login: Welcome!

## 📁 Wordlist Structure Guide:
The wordlist should be a .txt file with one password per line. Example:

123456
admin
password123
qwerty
...

## ✅ Sucess:
[✓] Password found: password123

## ❌ Failure:
[×] No valid password found in the wordlist.

