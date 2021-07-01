import click


@click.group()
@click.version_option('0.1.0', prog_name='chrono')
def main():
    """
    Submit your weekly challenges solutions using chrono.
    """
    pass


@main.command('submit', help='Submit your solution')
@click.argument('filename', nargs=1)
def submit(filename: str) -> None:
    ext = filename.split('.')[-1].strip()

    if ext == "py":
        lang = 'python'
    elif ext == "js":
        lang = 'javascript'
    else:
        click.echo('Invalid File Format')
        return

    try:
        with open(filename, 'r') as f:
            code = f.read()
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
