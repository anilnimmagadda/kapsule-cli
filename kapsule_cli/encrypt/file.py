import typer
from kapsule_cli.crypto.crypto import encrypt_file

encrypt_app = typer.Typer()

@encrypt_app.command("file")
def encrypt_command(input_path: str, output_path: str = "encrypted.bin"):
    encrypt_file(input_path, output_path)