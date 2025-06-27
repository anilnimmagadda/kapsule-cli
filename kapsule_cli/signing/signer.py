from oqs import Signature
from pathlib import Path
from .signing_utils import load_key, save_key, PRIVATE_SIGN_KEY_PATH, PUBLIC_SIGN_KEY_PATH

# Define the key storage directory
KEYS_DIR = Path(__file__).parent / "keys"
PRIVATE_KEY_PATH = KEYS_DIR / "sign_private_key.bin"
PUBLIC_KEY_PATH = KEYS_DIR / "sign_public_key.bin"
KEYS_DIR.mkdir(parents=True, exist_ok=True)

def generate_and_store_keys():
    """(Unused) Generates and saves keypair. Useful for external key management."""
    with Signature("Dilithium2") as sig:
        public_key = sig.generate_keypair()
        private_key = sig.export_secret_key()
        PUBLIC_KEY_PATH.write_bytes(public_key)
        PRIVATE_KEY_PATH.write_bytes(private_key)

def sign_file(input_path: str, sig_path: str):
    """Signs a file and saves the public key used for future verification."""
    with open(input_path, "rb") as f:
        message = f.read()

    with Signature("Dilithium2") as sig:
        public_key = sig.generate_keypair()
        signature = sig.sign(message)

    with open(sig_path, "wb") as f:
        f.write(signature)

    save_key(PUBLIC_SIGN_KEY_PATH, public_key)
    print(f"✅ Signed {input_path} → {sig_path}")

def verify_file(input_path: str, sig_path: str):
    """Verifies a file's signature using the previously saved public key."""
    with open(input_path, "rb") as f:
        message = f.read()

    with open(sig_path, "rb") as f:
        signature = f.read()

    public_key = load_key(PUBLIC_SIGN_KEY_PATH)

    with Signature("Dilithium2") as sig:
        is_valid = sig.verify(message, signature, public_key)

    if is_valid:
        print("✅ Signature is valid.")
    else:
        print("❌ Signature is invalid.")