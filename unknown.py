def password_strength_score(password):
    """Return a score based on how many criteria are met."""
    score = 0
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()" for c in password): score += 1
    return score

# Then require a minimum score (e.g., at least 4 out of 5)
while True:
    pwd = input("Create a password: ")
    score = password_strength_score(pwd)
    if score >= 4:
        print("✅ Good password!")
        break
    else:
        print(f"❌ Weak (score {score}/5). Needs at least 4 criteria.")
        print("   - Length ≥ 12")
        print("   - Uppercase, lowercase, digit, special character")