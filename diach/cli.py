import click
import time
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command('ts')
@click.option('-n', '--now', is_flag=True, help='Return actual timestamp')
@click.option('-r', '--revert', help='Convert timestamp to date')
@click.option('-c', '--convert')
def ts_cmd(now, convert, revert):
    if now:
        get_now()
    elif revert:
        try:
            result = convert_to_dt(revert)
            click.echo(result)
        except ValueError as v:
            click.echo("I Can't convert {} to datetime".format(revert))


def get_now():
    click.echo(time.time())

def convert_to_dt(value, format='%Y-%m-%d %H:%M:%S'):
    return datetime.utcfromtimestamp(float(value)).strftime(format)


cli.add_command(ts_cmd)
if __name__ == '__main__':
    cli()

