import typer
from kapsule_cli.crypto.crypto import decrypt_file

decrypt_app = typer.Typer()

@decrypt_app.command("file")
def decrypt_command(input_path: str, output_path: str = "decrypted.txt"):
    decrypt_file(input_path, output_path)
