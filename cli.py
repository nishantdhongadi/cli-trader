import click
from trading import login, buy_crypto, sell_crypto, check_balance       # TODO: write trading.py :p


@click.group()

def cli():
    pass


@cli.command()
@click.option('--username', prompt=True, help='Your Robinhood username')
@click.option('--password', prompt=True, hide_input=True, help='Your Robinhood password')

def login_cmd(username, password):
    
    """ Login to Robinhood """
    
    if login(username, password):
        click.echo('Login successful')
    else:
        click.echo('Login failed')


@cli.command()
@click.option('--symbol', prompt='Crypto Symbol', help='The symbol of the cryptocurrency')
@click.option('--amount', prompt='Amount to buy', type=float, help='The amount of cryptocurrency to buy')

def buy(symbol, amount):
   
    """ Buy cryptocurrency """
    
    result = buy_crypto(symbol, amount)
    click.echo(result)


@cli.command()
@click.option('--symbol', prompt='Crypto Symbol', help='The symbol of the cryptocurrency')
@click.option('--amount', prompt='Amount to sell', type=float, help='The amount of cryptocurrency to sell')

def sell(symbol, amount):
    
    """ Sell cryptocurrency """
    
    result = sell_crypto(symbol, amount)
    click.echo(result)


@cli.command()

def balance():
    
    """ Check account balance """
    
    result = check_balance()
    click.echo(result)


if __name__ == '__main__':
    cli()
