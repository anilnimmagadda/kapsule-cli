# Kapsule CLI – Post-Quantum Encryption for Developers

Kapsule is a command-line encryption tool built using post-quantum cryptography (PQC) standards selected by NIST.

It’s fast, minimal, and built for the CLI-first developer. No fluff. Just real encryption.

---

## Motivation: "Harvest Now, Decrypt Later"

Quantum computers may still be years away — but the threat is already here.

Sensitive data intercepted today can be stored and decrypted tomorrow using quantum attacks. This is known as:

HNDL: Harvest Now, Decrypt Later

Kapsule was built to counter this — by giving developers a simple way to start encrypting with post-quantum standards right now.

---

## Features

- Kyber512 encryption (PQC, NIST finalist)
- Dilithium2 signing (PQC, NIST finalist)
- Keypair persistence (shared secrets & public keys)
- Fully local, no third-party dependencies
- Built with liboqs-python

---

## Usage

### Encrypt a file

```bash
kapsule-cli encrypt message.txt
# → creates encrypted.bin
```

### Decrypt the file

```bash
kapsule-cli decrypt encrypted.bin
# → creates decrypted.txt
```

### Sign a file

```bash
kapsule-cli sign message.txt
# → creates signature.bin
```

### Verify the signature

```bash
kapsule-cli verify message.txt
# → outputs “Signature is valid.”
```

---

## Key Management (MVP Scope)

| Function     | How It Works                        |
|--------------|-------------------------------------|
| Encryption   | Uses a Kyber512 keypair             |
| Shared Secret | Stored and reused across sessions  |
| Signing      | Public key is saved + reused        |
| Private Key  | Not yet used in signing (planned)   |

We persist only the minimum needed to demonstrate real-world PQC flows — while keeping it educational and open for review.

---

## Stack

- Python 3.10+
- liboqs
- typer (CLI framework)

---

## Coming Soon

- Hybrid encryption modes (symmetric + PQC)
- Test suite (signing, tampering cases)
- Exportable key formats (PEM, etc.)
- Optional GPG-style trust model
- Simple API server mode (opt-in)

---

## Who's This For?

Developers, researchers, security teams, and anyone who:

- Knows the quantum shift is coming
- Wants to future-proof sensitive data
- Believes encryption shouldn’t expire

---

## Let’s Connect

Follow the project:
- GitHub
- Discuss HNDL in forums like Quantum World Association
- Contact : https://www.linkedin.com/in/anilnimmagadda/

---

## License

Open-source and community-first.
MIT License.