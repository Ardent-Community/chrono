import click
@click.group()
@click.version_option('0.2.3', prog_name='chrono')
def main():
    '''Submit your weekly challenges solutions'''
    pass

@main.command('submit', help='Submit your solution')
@click.argument('filename', nargs=1)
def submit(filename):
    ext = filename.split('.')
    ext =repr(ext[-1])
    if ext == "'py'":
        lang = 'python'
    elif ext == "'js'":
        lang = 'javascript'
    else:
        click.echo('Invalid File Format')
        exit()

    try:
        with open(filename, 'r') as f:
            code = f.read()
    except Exception as e:
        pass



if __name__ == "__main__":
    main()
