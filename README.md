# 🔐 BruteLogin
Here’s a simple Python script for brute-forcing form-based login pages.<br> 
For educational purposes and authorized security testing only.<br>

## ⚠️ Legal disclaimer!
Don't be a lammer running this script randomly.<br>
This was made for LEARNING PURPOSES ONLY.<br>
Unauthorized use = ILLEGAL AF (CFAA, GDPR, etc.)<br>

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
Clone this repository:<br>
git clone https://github.com/MatheusLAmazonas/brute-login<br>
cd brute-login<br>

## 📦 How to use:
python bruteforce_login.py

Exemplo de uso:<br>
Enter the login URL: https://exemplo.com/login<br>
Enter the username field name: user<br>
Enter the password field name: pass<br>
Enter the username to test: admin<br>
Enter the path to the wordlist: wordlist.txt<br>
Enter a keyword that indicates a successful login: Welcome!<br>

## 📁 Wordlist Structure Guide:
The wordlist should be a .txt file with one password per line. Example:<br>

123456<br>
admin<br>
password123<br>
qwerty<br>
...<br>

## ✅ Sucess:
[✓] Password found: password123

## ❌ Failure:
[×] No valid password found in the wordlist.

