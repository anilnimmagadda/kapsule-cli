import typer

# Import command groups from various modules
from kapsule_cli.encrypt.file import encrypt_app
from kapsule_cli.decrypt.file import decrypt_app
from kapsule_cli.signing.sign_app import sign_app
from kapsule_cli.signing.verify_app import verify_app

# Create the main Typer app
app = typer.Typer(help="Kapsule CLI: Post-quantum file encryption and signing toolkit")

# Register subcommands under their respective namespaces
app.add_typer(encrypt_app, name="encrypt", help="Encrypt files using Kyber512")
app.add_typer(decrypt_app, name="decrypt", help="Decrypt files using stored shared secret")
app.add_typer(sign_app, name="sign", help="Sign files using Dilithium2")
app.add_typer(verify_app, name="verify", help="Verify signatures using stored public key")

# Entry point
if __name__ == "__main__":
    app()


