
This is the evolving roadmap for *Kapsule CLI*.

MVP goals are to demonstrate a usable, secure, post-quantum encryption workflow from the command line — with clean UX, educational structure, and cryptographic integrity.

---

### ✅ Current Features
- Kyber512 encryption (liboqs)
- Dilithium2 signing
- Key persistence (shared secrets & pubkeys)
- Typer-based CLI with subcommands
- Inline documentation

---

### 🧭 Near-Term Goals (MVP Scope)

| Feature              | Status   |
|----------------------|----------|
| Hybrid encryption    | ⏳ Planned     |
| JS SDK (encrypt only)| ⏳ Planned     |
| PEM key export       | ⏳ Planned     |
| CLI help improvements| ✅ Done        |
| Dev Docs site        | 🔜 In Progress |

---

### 🧱 Architecture Goals
- Modular: Each crypto function in its own folder
- Extendable: Add new algorithms or hybrid flows
- Transparent: Save/load keys intentionally

---

### 🌍 Vision
Build the *most developer-friendly PQC toolkit* — to help teams future-proof today’s data.

If you're interested in contributing to any section of this roadmap — let's talk!