import typer
from .signer import sign_file

sign_app = typer.Typer()

@sign_app.command("file")
def sign_file_command(input_file: str, sig_path: str = "signature.bin"):
    """Signs a file using post-quantum digital signature (Dilithium2)."""
    sign_file(input_file, sig_path)
