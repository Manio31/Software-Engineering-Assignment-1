
import secrets

def generate_api_key():
    return secrets.token_urlsafe(32)

if __name__ == "__main__":
    for i in range(1, 4):
        print(f"Consumer {i}: {generate_api_key()}")
