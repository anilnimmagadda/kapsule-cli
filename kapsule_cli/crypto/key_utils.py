# kapsule_cli/crypto/key_utils.py

from pathlib import Path

# Establish base and keys directory
BASE_DIR = Path(__file__).resolve().parent
KEYS_DIR = BASE_DIR / "keys"
KEYS_DIR.mkdir(exist_ok=True)  # Ensure keys directory exists

# Define paths for key and shared secret files
PRIVATE_KEY_PATH = KEYS_DIR / "private_key.bin"
PUBLIC_KEY_PATH = KEYS_DIR / "public_key.bin"
SHARED_SECRET_PATH = KEYS_DIR / "shared_secret.bin"

def save_key(path, key_bytes):
    """
    Save binary key data to the specified file path.

    Args:
        path (Path): Destination file path.
        key_bytes (bytes): Key data to save.
    """
    try:
        print(f"[DEBUG] Writing to: {path}")
        print(f"[DEBUG] Type of path: {type(path)}")
        with open(str(path), "wb") as f:
            f.write(key_bytes)
    except Exception as e:
        print(f"[ERROR] Failed to save key to {path}: {e}")
        raise

def load_key(path):
    """
    Load binary key data from the specified file path.

    Args:
        path (Path): File path to load key from.

    Returns:
        bytes: Loaded key data.
    """
    if not path.exists():
        raise FileNotFoundError(f"Key not found: {path}")
    with open(path, "rb") as f:
        return f.read()

def save_shared_secret(secret: bytes):
    """
    Persist the shared secret derived from KEM.

    Args:
        secret (bytes): Shared secret to store.
    """
    with open(SHARED_SECRET_PATH, "wb") as f:
        f.write(secret)

def load_shared_secret() -> bytes:
    """
    Retrieve the shared secret used during decryption.

    Returns:
        bytes: Shared secret data.
    """
    with open(SHARED_SECRET_PATH, "rb") as f:
        return f.read()
