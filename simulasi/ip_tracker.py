import requests

def lacak_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print(f"🌐 Lokasi IP: {data['query']}")
        print(f"Negara     : {data['country']}")
        print(f"Kota       : {data['city']}")
        print(f"ISP        : {data['isp']}")
    except:
        print("❌ Gagal melacak IP.")

if __name__ == "__main__":
    ip = input("Masukkan IP yang ingin dilacak: ").strip()
    lacak_ip(ip)
