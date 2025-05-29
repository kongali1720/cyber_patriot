import re

def is_phishing(url):
    suspicious_patterns = [
        r"free[-_.]?gift", r"login[-_.]?secure", r"update[-_.]?account", r"bank[-_.]?verify",
        r"bit\.ly", r"tinyurl\.com", r"@.*@", r"https?://\d+\.\d+\.\d+\.\d+"
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return True
    return False

if __name__ == "__main__":
    url = input("Masukkan URL untuk dicek: ").strip()
    if is_phishing(url):
        print("⚠️ TERDETEKSI: URL mencurigakan! Hati-hati.")
    else:
        print("✅ URL terlihat aman.")
