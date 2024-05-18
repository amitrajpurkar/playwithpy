from typing import Optional

import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def hello(name: Annotated[Optional[str], typer.Argument()] = None):
    if name is None:
        print("Hello World!")
    else:
        print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

if __name__ == "__main__":
    app()