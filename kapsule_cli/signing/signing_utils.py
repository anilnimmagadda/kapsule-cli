from pathlib import Path

# Define the directory for signing keys
SIGN_KEYS_DIR = Path("signing_keys")
SIGN_KEYS_DIR.mkdir(exist_ok=True)

# Set file paths
PRIVATE_SIGN_KEY_PATH = SIGN_KEYS_DIR / "signing_private.key"
PUBLIC_SIGN_KEY_PATH = SIGN_KEYS_DIR / "signing_public.key"

def save_key(path: Path, key_data: bytes):
    """Save binary key data to file."""
    with open(path, "wb") as f:
        f.write(key_data)

def load_key(path: Path) -> bytes:
    """Load binary key data from file."""
    with open(path, "rb") as f:
        return f.read()