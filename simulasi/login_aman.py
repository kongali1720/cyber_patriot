import hashlib

users = {
    "tniadmin": hashlib.sha256("merahputih123".encode()).hexdigest(),
    "polriadmin": hashlib.sha256("tribrata789".encode()).hexdigest(),
}

def login(username, password):
    hashed_input = hashlib.sha256(password.encode()).hexdigest()
    if users.get(username) == hashed_input:
        print("✅ Login berhasil. Selamat datang, Patriot Siber!")
    else:
        print("❌ Login gagal. Username atau password salah.")

if __name__ == "__main__":
    print("=== LOGIN AMAN ===")
    uname = input("Username: ").strip()
    pwd = input("Password: ").strip()
    login(uname, pwd)
