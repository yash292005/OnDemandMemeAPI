import os

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from urlextract import URLExtract
extractor = URLExtract()
app = Flask(__name__)


@app.route('/<string:n>')

def userInp(n):
        url = 'https://www.google.com/search?q='+n+'memes&client=ubuntu&hs=OtH&channel=fs&sxsrf' \
                                                    '=ALeKk037FzJv8xFoWodOwL0cqcmLsx7Xbg:1613376671993&source=lnms' \
                                                    '&tbm=isch&sa=X&ved' \
                                                    '=2ahUKEwjC1rC7uOvuAhXc63MBHYMnAOEQ_AUoAXoECBEQAw&biw=1920&bih=904 '
        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }
        r = requests.get(url=url, headers=headers)
        print(r)
        soup = BeautifulSoup(r.text, 'html.parser')
        x = [soup.findAll("img")]
        example_text = str(x)
        urls = extractor.find_urls(example_text)
        result = {
            "Message": "hii welcome to YASH VARDHAN'S meme paradise",
            "Search_String": n,
            "output": urls
        }
        return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(port=port)
