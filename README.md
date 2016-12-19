# CurrencyConverterBot
[![License](https://img.shields.io/:license-mit-blue.svg)](https://astrocb.mit-license.org)

## About

CurrencyConverterBot is a [Reddit](https://reddit.com/) bot that can convert between a number of currencies. Built using [PRAW](http://praw.readthedocs.io/en/stable/) and Python 3.

## Usage
To trigger [the bot](https://reddit.com/user/ConvertCurrency), leave a comment in the following format:

```
/u/ConvertCurrency {numerical amount} {current currency} (to) {desired currency}
```

For example,

```
/u/ConvertCurrency 100 USD to GBP
```

Acceptable currency formats can be found [here](https://pypi.python.org/pypi/CurrencyConverter/0.5).

## Configuration

If you'd like to fork/clone this bot, there are a few things you'll have to set up. First of all, it depends on the [CurrencyConverter Python package](https://pypi.python.org/pypi/CurrencyConverter/0.5), which can be downloaded directly from their website or with pip.

Next, you'll need a configuration file with the necessary data required for accessing read/write features of the API.

You can create a Reddit account for your bot, or simply use your existing account. Once you have the username/password for the account you'd like the bot to post under, create a file in the root directory called `credentials.py`.

It should contain 3 variables: `USERNAME`, `PASSWORD`, and `USERAGENT`, an identifier required to access the Reddit API. This can be anything you like, but make sure it's unique. It's also a good idea to include a version in the user agent so that it can be easily changed if it gets blocked for some reason (not that you would spam the Reddit API or anything...).

Example `credentials.py` file:

```py
USERNAME="mybot123"
PASSWORD="mypass123"
USERAGENT="MyBot 1.0.0"
```

Then, just run `bot.py` through a Python 3 interpreter and you're good to go.

## Blacklist
I've included a blacklist to prevent the bot from posting in certain subs and responding to certain users.

The files are pretty self-explanatory; each line of `sub_blacklist.txt` and `user_blacklist.txt` represent an individual blacklisted sub and user respectively. Add to the blacklist as necessary by simply adding lines to these files. The bot will recompile its blacklist database each time you run it, and it will not post in blacklisted subs or respond to blacklisted users.

The code could also be easily modified to use a whitelist if that's more of what you're looking for.
