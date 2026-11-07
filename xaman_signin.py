import os
import time
import qrcode
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Xaman API Credentials
XAMM_API_KEY = os.getenv("XAMM_API_KEY")
XAMM_API_SECRET = os.getenv("XAMM_API_SECRET")

# Xaman API Endpoints
XAMM_API_URL = "https://xumm.app/api/v1/platform/payload"


def initiate_xaman_signin():
    """Initiates a sign-in payload with Xaman API and returns payload details."""
    headers = {
        "X-API-Key": XAMM_API_KEY,
        "X-API-Secret": XAMM_API_SECRET,
        "Content-Type": "application/json",
    }

    # Payload requesting a simple sign-in (no transaction)
    payload = {"txjson": {"TransactionType": "SignIn"}}

    try:
        response = requests.post(XAMM_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error initiating Xaman sign-in: {e}")
        return None


def generate_qr_code(url):
    """Generates and displays a QR code in the terminal for the given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    print("\n🔍 Scan this QR code with your Xaman app to sign in:\n")
    qr.print_ascii()  # Prints QR code directly in the terminal


def check_payload_status(payload_uuid):
    """Polls the Xaman API to check if the user has signed the payload."""
    headers = {
        "X-API-Key": XAMM_API_KEY,
        "X-API-Secret": XAMM_API_SECRET,
        "Content-Type": "application/json",
    }

    status_url = f"{XAMM_API_URL}/{payload_uuid}"

    print("\n⏳ Waiting for you to sign in via the Xaman app...")

    while True:
        try:
            response = requests.get(status_url, headers=headers)
            response.raise_for_status()
            data = response.json()

            # Check if the payload has been resolved (signed or expired)
            if data.get("meta", {}).get("resolved"):
                if data.get("meta", {}).get("signed"):
                    user_address = data.get("response", {}).get("account")
                    print(f"\n✅ Sign-in successful!")
                    print(f"👤 User XRP Address: {user_address}")
                    return user_address
                else:
                    print("\n❌ Sign-in request was rejected or expired.")
                    return None

            # Wait 3 seconds before polling again
            time.sleep(3)

        except requests.exceptions.RequestException as e:
            print(f"❌ Error checking payload status: {e}")
            return None


def main():
    if not XAMM_API_KEY or not XAMM_API_SECRET:
        print(
            "❌ Error: XAMM_API_KEY or XAMM_API_SECRET is missing in your .env file."
        )
        return

    print("🚀 Starting Xaman Sign-In Flow...")

    # Step 1: Initiate Payload
    payload_data = initiate_xaman_signin()
    if not payload_data:
        return

    payload_uuid = payload_data.get("uuid")
    qr_url = payload_data.get("next", {}).get("always")

    # Step 2: Generate QR Code
    generate_qr_code(qr_url)

    # Step 3: Poll for Status
    user_address = check_payload_status(payload_uuid)

    if user_address:
        print(
            "\n🎉 You are now authenticated with the Harmonic Text Mirror ecosystem."
        )


if __name__ == "__main__":
    main()
