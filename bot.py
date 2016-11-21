import praw
import re
import time
from blacklist import *
from currency_converter import CurrencyConverter

try:
    from credentials import * # Python file containing USERNAME, PASSWORD, and USERAGENT config variables
except ImportError:
    print("Credentials file not available. You need to include a credentials.py file in the root directory. See README.")

PARSER = re.compile(r"\/?u\/ConvertCurrency (\d+(?:\.\d+\d)?)(?:\s?)(\w\w\w)(?:\s?)(?:to)? (\w\w\w)", re.I)
c = CurrencyConverter()

def get_data(message):
    matches = PARSER.findall(message.body)
    return (matches if matches else [])

def convert(amt, c1, c2):
    try:
        return c.convert(amt, c1, c2)
    except ValueError:
        return None

def get_message(conversions):
    m = ""
    for con in conversions:
        m += "{} {} is {} {}".format(con["original_amt"], con["original_cur"], con["new_amt"], con["new_cur"])
        if con != conversions[-1]:
            m += "\n\n"
    return m

def parse(message):
    conversions = []
    data = get_data(message)
    for d in data:
        amount = d[0]
        cur1 = d[1]
        cur2 = d[2]
        converted = convert(amount, cur1, cur2)
        if converted:
            conversions.append({
                "original_amt": amount,
                "original_cur": cur1,
                "new_amt": "{0:.2f}".format(converted), # Round off at 2 decimal places
                "new_cur": cur2
            })
        else:
            return "Currency not found"
    if len(conversions) > 0:
        return get_message(conversions)
    return None

def main():
    r = praw.Reddit(USERAGENT)
    r.login(USERNAME, PASSWORD, disable_warning=True)
    for comment in praw.helpers.comment_stream(r, 'all'):
        resp = parse(comment)
        if resp and not (str(comment.author) in BLACKLISTED_USERS or str(comment.submission.subreddit) in BLACKLISTED_SUBS):
            try:
                print(resp)
                comment.reply(resp)
            except praw.errors.RateLimitExceeded as error:
                # Rate limit error
                print("Sleeping for {} seconds".format(error.sleep_time))
                time.sleep(error.sleep_time) # Delay to prevent ratelimiting
            except ConnectionError as error:
                print("HTTP connection error: ", error)
            except ConnectionResetError as error:
                print("Connection reset: ", error)
            except Exception as other_error:
                print(other_error)
main()
