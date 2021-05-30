from mock_example.app.dice import roll_dice
import requests


def guess_number(num: int):
    result = roll_dice()
    if result == num:
        return 'you won'
    else:
        return 'you lost'


def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()["origin"]


if __name__ == '__main__':
    print(get_ip())
