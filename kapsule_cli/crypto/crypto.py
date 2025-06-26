from oqs import KeyEncapsulation
from pathlib import Path
from .key_utils import load_key, save_key, save_shared_secret, load_shared_secret, PRIVATE_KEY_PATH, PUBLIC_KEY_PATH

def encrypt_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        plaintext = f.read()

    with KeyEncapsulation("Kyber512") as kem:
        public_key = kem.generate_keypair()
        private_key = kem.export_secret_key()
        public_bytes = public_key  # Already bytes in liboqs

        save_key(PRIVATE_KEY_PATH, private_key)
        save_key(PUBLIC_KEY_PATH, public_bytes)

        ciphertext, shared_secret = kem.encap_secret(public_key)
        save_shared_secret(shared_secret)
        encrypted = bytes([b ^ shared_secret[i % len(shared_secret)] for i, b in enumerate(plaintext)])

    with open(output_path, 'wb') as f:
        f.write(ciphertext + b"::" + encrypted)

    print(f"✅ Encrypted {input_path} → {output_path}")

def decrypt_file(input_path, output_path):
    with open(input_path, 'rb') as f:
        data = f.read()

    if b"::" not in data:
        raise ValueError("Invalid file format. Expecting ciphertext::encrypted")

    _, encrypted = data.split(b"::", 1)

    shared_secret = load_shared_secret()

    decrypted = bytes([b ^ shared_secret[i % len(shared_secret)] for i, b in enumerate(encrypted)])

    with open(output_path, 'wb') as f:
        f.write(decrypted)

    print(f"✅ Decrypted {input_path} → {output_path}")
