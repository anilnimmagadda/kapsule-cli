from oqs import KeyEncapsulation
from pathlib import Path

# Utility functions and constants for key persistence
from .key_utils import (
    load_key,
    save_key,
    save_shared_secret,
    load_shared_secret,
    PRIVATE_KEY_PATH,
    PUBLIC_KEY_PATH
)

def encrypt_file(input_path, output_path):
    """
    Encrypts a file using Kyber512 KEM and XOR symmetric encryption with a shared secret.

    Args:
        input_path (str): Path to the plaintext input file.
        output_path (str): Path to save the encrypted file.
    """
    with open(input_path, 'rb') as f:
        plaintext = f.read()

    # Initialize Kyber512 and generate public/private key pair
    with KeyEncapsulation("Kyber512") as kem:
        public_key = kem.generate_keypair()
        private_key = kem.export_secret_key()

        # Save key material for reuse (MVP scope only)
        save_key(PRIVATE_KEY_PATH, private_key)
        save_key(PUBLIC_KEY_PATH, public_key)

        # Derive shared secret and encrypt via XOR
        ciphertext, shared_secret = kem.encap_secret(public_key)
        save_shared_secret(shared_secret)

        encrypted = bytes([
            b ^ shared_secret[i % len(shared_secret)]
            for i, b in enumerate(plaintext)
        ])

    # Save the ciphertext and XOR-encrypted payload
    with open(output_path, 'wb') as f:
        f.write(ciphertext + b"::" + encrypted)

    print(f"✅ Encrypted {input_path} → {output_path}")

def decrypt_file(input_path, output_path):
    """
    Decrypts a file using the stored shared secret (from prior encapsulation).

    Args:
        input_path (str): Path to the encrypted file.
        output_path (str): Path to save the decrypted plaintext file.
    """
    with open(input_path, 'rb') as f:
        data = f.read()

    if b"::" not in data:
        raise ValueError("Invalid file format. Expecting ciphertext::encrypted")

    # In MVP, ciphertext is unused post shared-secret generation
    _, encrypted = data.split(b"::", 1)

    # Retrieve persisted shared secret from prior run
    shared_secret = load_shared_secret()

    decrypted = bytes([
        b ^ shared_secret[i % len(shared_secret)]
        for i, b in enumerate(encrypted)
    ])

    with open(output_path, 'wb') as f:
        f.write(decrypted)

    print(f"✅ Decrypted {input_path} → {output_path}")
