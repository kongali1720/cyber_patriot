# password_checker.py
import re

def check_password(password):
    score = 0
    
    # Length check
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    
    # Complexity checks
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1
    
    # Rating
    if score >= 5: return "💪 SUPER STRONG"
    if score >= 3: return "👍 GOOD"
    return "❌ WEAK - Needs improvement"
