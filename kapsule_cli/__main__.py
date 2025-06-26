import typer
from kapsule_cli.encrypt.file import encrypt_app
from kapsule_cli.decrypt.file import decrypt_app

app = typer.Typer()
app.add_typer(encrypt_app, name="encrypt")
app.add_typer(decrypt_app, name="decrypt")

if __name__ == "__main__":
    app()

