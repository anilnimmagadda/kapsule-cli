from oqs import KeyEncapsulation
from .key_utils import save_key, load_key, PRIVATE_KEY_PATH, PUBLIC_KEY_PATH

def test_key_persistence():
    # Generate keypair
    with KeyEncapsulation("Kyber512") as kem:
        public_key = kem.generate_keypair()
        private_key = kem.export_secret_key()

        # Save keys
        save_key(PRIVATE_KEY_PATH, private_key)
        save_key(PUBLIC_KEY_PATH, public_key)

        print("✅ Keys saved.")

    # Load keys
    loaded_private = load_key(PRIVATE_KEY_PATH)
    loaded_public = load_key(PUBLIC_KEY_PATH)

    print(f"🔑 Private key loaded: {len(loaded_private)} bytes")
    print(f"🔐 Public key loaded: {len(loaded_public)} bytes")

if __name__ == "__main__":
    test_key_persistence()
