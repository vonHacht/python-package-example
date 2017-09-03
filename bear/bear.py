import re
import requests

class bear:

    def __init__(self):
        self.str = "Class bear"

    def test_regex(self):
        regex = re.compile("Class")
        return regex.match(self.str).group(0)

    def test_requests(self):
        res = requests.get("https://www.google.com").content
        return res