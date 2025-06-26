# kapsule_cli/crypto/key_utils.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
KEYS_DIR = BASE_DIR / "keys"
KEYS_DIR.mkdir(exist_ok=True)

PRIVATE_KEY_PATH = KEYS_DIR / "private_key.bin"
PUBLIC_KEY_PATH = KEYS_DIR / "public_key.bin"
SHARED_SECRET_PATH = KEYS_DIR / "shared_secret.bin"

def save_key(path, key_bytes):
    try:
        print(f"[DEBUG] Writing to: {path}")
        print(f"[DEBUG] Type of path: {type(path)}")
        with open(str(path), "wb") as f:
            f.write(key_bytes)
    except Exception as e:
        print(f"[ERROR] Failed to save key to {path}: {e}")
        raise

def load_key(path):
    if not path.exists():
        raise FileNotFoundError(f"Key not found: {path}")
    with open(path, "rb") as f:
        return f.read()
    
def save_shared_secret(secret: bytes):
    with open(SHARED_SECRET_PATH, "wb") as f:
        f.write(secret)

def load_shared_secret() -> bytes:
    with open(SHARED_SECRET_PATH, "rb") as f:
        return f.read()
