# Kapsule CLI – Release v0.3.7

🔐 *Kapsule CLI* is now live with its first public release under version *v0.3.7* — combining post-quantum cryptographic primitives with a lightweight, developer-friendly CLI experience.

---

## 🚀 What's Included

### ✅ Core Features
- *Kyber512 Encryption*
  - Quantum-safe file encryption using NIST finalist algorithm.
  - Shared secret stored for session-resilient decryption.

- *Dilithium2 Signing*
  - Post-quantum digital signature for verifying file integrity.
  - Public key saved for multi-session verification.

### 🧠 Architecture Highlights
- Clean CLI commands:
  - encrypt, decrypt, sign, verify
- Modular Python code with typer
- Fully local, zero network dependency
- Inline documentation and structured folder layout
- Persisted key/secret storage using local filesystem

---

## 📁 File Structure

kapsule_cli/
├── encrypt/
├── decrypt/
├── signing/
├── crypto/
├── keys/ (auto-created)
└── main.py

---

## 🔧 Dev Notes

- Built with Python 3.10+ and liboqs
- Designed to be minimal, inspectable, and easily extensible
- MIT License

---

## 💡 What's Next

- Hybrid encryption mode (symmetric + PQ)
- JS SDK (Week 3 goal)
- API server wrapper
- Dev Docs portal (Week 4)
- Contributor PR process with protected main branch

---

## 🛡 Why v0.3.7?

Inspired by the elegance of numbers and the fun of cryptographic patterns:
- *0* — zero-trust mindset
- *3* — three pillars (encrypt, sign, verify)
- *7* — for quantum-safe aspirations

---

## 🧩 Contributors & Community

This project is just getting started — if you believe in encryption that lasts, join us. Check out [CONTRIBUTING.md](CONTRIBUTING.md) and [ROADMAP.md](ROADMAP.md) to get involved.

---

🌐 GitHub: [github.com/anil-kapsule/kapsule-cli](https://github.com/anilnimmagadda)  
📬 Contact: [linkedin.com/in/anilnimmagadda](https://www.linkedin.com/in/anilnimmagadda/)