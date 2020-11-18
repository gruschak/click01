# http://api.openweathermap.org/data/2.5/weather?q=London&appid=fed9597b3ac268198e76e038dc48c748
"""
Getting started with a 'click' package
"""
import requests
import click

SAMPLE_API_KEY = 'fed9597b3ac268198e76e038dc48c748'


@click.group()
def cli():
    pass


def current_weather(location, api_key):
    url = 'http://api.openweathermap.org/data/2.5/weather'

    if not api_key:
        api_key = SAMPLE_API_KEY

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    if response.ok:
        temperature = round(response.json()['main']['temp'] - 273.15, 1)
        return response.json()['weather'][0]['description'] + ", t=" + str(temperature)


@cli.command(name='weather')
@click.argument('city', required=True, type=str)
@click.option('--api-key', '-a',  help='API key for the OpenWeatherMap API')
def weather(city, api_key):
    weather_report = current_weather(city, api_key)
    print(f"The weather in {city} right now: ")
    click.secho(f"{weather_report}", fg="yellow")


@cli.command(name='pwd')
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.password_option()
def pwd(verbose, name, password):
    """This is an example script to learn Click."""
    if verbose:
        click.echo(f"We are in the verbose mode.")
    click.echo(f"Hello World")
    for n in name:
        click.echo(f'Bye {n}')
    click.echo(f'We received {password} as password.')


if __name__ == "__main__":
    cli()
