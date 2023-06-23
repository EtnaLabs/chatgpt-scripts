import os
import subprocess

import click
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

YELLOW = "yellow"
GREEN = "green"
BLACK = "black"
RED = "red"
BLUE = "blue"
MAGENTA = "magenta"
CYAN = "cyan"
WHITE = "white"
BRIGHT_BLACK = "bright_black"
BRIGHT_RED = "bright_red"
BRIGHT_GREEN = "bright_green"
BRIGHT_YELLOW = "bright_yellow"
BRIGHT_BLUE = "bright_blue"
BRIGHT_MAGENTA = "bright_magenta"
BRIGHT_CYAN = "bright_cyan"
BRIGHT_WHITE = "bright_white"

COMMAND = CYAN
PROMPT = BRIGHT_BLACK


@click.command()
@click.argument("question", default="")
def cli(question: str):
    if not question:
        question = click.prompt("Type your question")

    """Sai is a command line tool to use ChatGPT to ask questions about your project."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a command line tool. "
                "If the answer of my question can be a command, "
                "answer only the command and nothing else",
            },
            {"role": "user", "content": question},
        ],
        max_tokens=50,
        temperature=0.3,
    )

    res = response["choices"][0]["message"]["content"]
    if res[0] == "```" and res[-1] == "```":
        res = res[3:-3]
    elif res[0] == "`" and res[-1] == "`":
        res = res[1:-1]

    click.secho("Execute Command: ", fg=PROMPT, nl=False)
    click.secho(res, fg=COMMAND, nl=False)
    execute = click.prompt("", default="Y/n", prompt_suffix="")

    if execute == "y" or execute == "Y" or execute == "yes" or execute == "Yes":
        subprocess.run(res, shell=True)

    else:
        click.secho("Command not executed.", fg=RED)


def main():
    cli()


if __name__ == "__main__":
    main()
