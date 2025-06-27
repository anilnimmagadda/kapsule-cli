# kapsule_cli/crypto/test_keys.py

from oqs import KeyEncapsulation
from .key_utils import save_key, load_key, PRIVATE_KEY_PATH, PUBLIC_KEY_PATH

def test_key_persistence():
    """
    Test function to validate key generation, saving, and loading.

    Steps:
    1. Generate a Kyber512 keypair using liboqs.
    2. Save the private and public keys to disk.
    3. Load the keys back from disk.
    4. Print confirmation and key sizes.
    """

    # Generate keypair using Kyber512
    with KeyEncapsulation("Kyber512") as kem:
        public_key = kem.generate_keypair()
        private_key = kem.export_secret_key()

        # Persist both keys to disk
        save_key(PRIVATE_KEY_PATH, private_key)
        save_key(PUBLIC_KEY_PATH, public_key)

        print("✅ Keys saved.")

    # Reload keys from disk
    loaded_private = load_key(PRIVATE_KEY_PATH)
    loaded_public = load_key(PUBLIC_KEY_PATH)

    # Display confirmation and lengths
    print(f"🔑 Private key loaded: {len(loaded_private)} bytes")
    print(f"🔐 Public key loaded: {len(loaded_public)} bytes")

# Execute test if run as script
if __name__ == "__main__":
    test_key_persistence()
