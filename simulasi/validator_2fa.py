import pyotp
import getpass
import re

def cek_kekuatan_password(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*()]", password)):
        return True
    return False

def simulasi_2fa():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    print(f"Kode Rahasia 2FA Anda (simpan di Authenticator): {secret}")
    kode = input("Masukkan kode 2FA dari aplikasi Anda: ").strip()
    if totp.verify(kode):
        print("✅ Kode 2FA valid!")
    else:
        print("❌ Kode 2FA salah atau kedaluwarsa.")

if __name__ == "__main__":
    print("=== VALIDATOR PASSWORD & 2FA ===")
    passwd = getpass.getpass("Buat password baru: ")
    if cek_kekuatan_password(passwd):
        print("✅ Password kuat.")
        simulasi_2fa()
    else:
        print("❌ Password lemah. Gunakan kombinasi huruf besar, kecil, angka, dan simbol.")
