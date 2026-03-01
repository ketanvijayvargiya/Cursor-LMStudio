import requests
import json
import sys

def verify_lm_studio(base_url):
    """Verifies if the LM Studio local server is running and accessible."""
    if not base_url.endswith('/v1'):
        base_url = base_url.rstrip('/') + '/v1'

    models_url = f"{base_url}/models"

    print(f"Checking connection to: {models_url}...")
    try:
        response = requests.get(models_url, timeout=5)
        if response.status_code == 200:
            models = response.json()
            print("✅ Success! Connected to LM Studio.")
            print(f"Available models: {len(models.get('data', []))}")
            for model in models.get('data', []):
                print(f" - {model['id']}")
            return True
        else:
            print(f"❌ Failed. Server returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Could not connect to the server. Is LM Studio running?")
        print(f"Detail: {e}")
        return False

def main():
    print("--- LM Studio API Verification Tool ---")
    url = input("Enter your LM Studio Base URL [default: http://localhost:1234/v1]: ").strip()
    if not url:
        url = "http://localhost:1234/v1"

    success = verify_lm_studio(url)

    if success:
        print("\nYour setup is ready for Cursor integration!")
    else:
        print("\nPlease check your LM Studio settings and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
