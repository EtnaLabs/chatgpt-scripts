import os

import click
import openai

YOU = "yellow"
CHATGPT = "green"
IMPORTANT = "cyan"

openai.api_key = os.environ["OPENAI_API_KEY"]


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
                "content": (
                    "You are a command line tool. "
                    "If the answer of my question can be a command, answer only the command and nothing else",  # noqa: E501
                ),
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

    click.secho(res, fg=CHATGPT)


def main():
    cli()


if __name__ == "__main__":
    main()
