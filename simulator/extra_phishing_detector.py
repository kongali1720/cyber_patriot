# phishing_detector.py
import requests
from urllib.parse import urlparse

def analyze_url(url):
    try:
        # Cek karakteristik phishing
        if '@' in url or 'bit.ly' in url:
            return "⚠️ HIGH RISK: Possible phishing URL"
            
        # Analisis SSL
        if not url.startswith('https'):
            return "⚠️ WARNING: No SSL encryption"
            
        return "✅ URL appears safe"
    except:
        return "❌ Error analyzing URL"
