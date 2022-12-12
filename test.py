import subprocess
import time
import unittest
import re
import requests

from app import main


class BotTests(unittest.TestCase):

    def test_get_data(self):
        pattern = re.compile("[-, +]?[0-9]+(.[0-9]+)?")

        url_1 = 'https://www.meteoservice.ru/weather/overview/moskva'
        data_1 = main.get_data(url_1)
        response = requests.get(url_1)
        self.assertEqual(response.status_code, 200)

        url_2 = 'https://www.meteoservice.ru/weather/overview/sankt-peterburg'
        data_2 = main.get_data(url_2)
        response = requests.get(url_1)
        self.assertEqual(response.status_code, 200)

        self.assertIsNotNone(pattern.fullmatch(data_1))
        self.assertIsNotNone(pattern.fullmatch(data_2))

    def test_get_advice(self):
        url_1 = 'https://www.meteoservice.ru/weather/overview/moskva'
        advice_1 = main.get_advice(url_1)
        response = requests.get(url_1)
        self.assertEqual(response.status_code, 200)

        url_2 = 'https://www.meteoservice.ru/weather/overview/sankt-peterburg'
        advice_2 = main.get_advice(url_2)
        response = requests.get(url_1)
        self.assertEqual(response.status_code, 200)

        self.assertEqual('Тепло! Можно походить без шапочки ;)', advice_1)
        self.assertEqual('Думаю, сегодня точно стоит надеть шапку', advice_2)


if __name__ == '__main__':
    p = subprocess.Popen(["python", "./app/main.py"])
    time.sleep(3)
    unittest.main()
    p.terminate()
