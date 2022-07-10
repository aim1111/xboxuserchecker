from wsgiref import headers
import requests
import random
import dhooks
from dhooks import Webhook, Embed
from requests import session
import threading
from threading import Thread
session = requests.session()
import queue
from queue import Queue
usernames = queue.Queue()
huk = input('Webhook: ')
ppp = input('Proxies file: ')
uuu = input('Users file: ')
hook = Webhook(huk)
P = []
for line in open(uuu, 'r'):
            usernames.put(line.strip())
for i in open(ppp, 'r').read().splitlines():
	
	        P.append(i)
def check():
    while usernames.qsize() != 0:
                Proxy = random.choice(P)
                Proxy.strip()
                user = usernames.get()
                prox = {
						'http': f'http://{Proxy}',
						'https': f'http://{Proxy}'
					}
                headers = {
                    'authority': 'xboxgamertag.com',
                    'method': 'GET',
                    'path': '/search/ashfdvdshvfs',
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'cookie': 'ga=GA1.2.1809765661.1644872577; _gid=GA1.2.1669764856.1644872577; __gads=ID=8ee93ddee1c391ac-22be2957e8cf0063:T=1644872578:RT=1644872578:S=ALNI_MZVzC6amSvHBhz847fK-nKVm3w2Mg; __cf_bm=_3VMP9NFhT0g.BKaddVlR7nGbvjiJKQjochViKLZ430-1644872589-0-AUoydDf2WZGd9qzS2jpm+FM1UO3DrcDF0df96+AkCUOY59Ao9d+P+2mzrLHf+nU0w0KEB8vkhmmheNjVnrmSxf43t74bCNa8XmdTWKpMwT7ePJHZpDoYSTcanYgD32Sdig==; _gat_gtag_UA_16948229_1=1',
                    'referer': 'https://xboxgamertag.com/',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                    }
                url = f"https://xboxgamertag.com/search/{user}"

                r = session.get(url, headers=headers, proxies=prox)

                if r.status_code == 404:
                    hook.send(f'{user} is available on xbox!')
                else:
                    print(f'{r.status_code} : {user}')
threading.Thread(target=check).start()

