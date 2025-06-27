import typer
from .signer import verify_file

verify_app = typer.Typer()

@verify_app.command("file")
def verify_file_command(input_file: str, sig_path: str = "signature.bin"):
    """Command to verify the digital signature of a file."""
    verify_file(input_file, sig_path)
