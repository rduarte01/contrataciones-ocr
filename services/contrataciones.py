from utils import *
from config import TOKEN
import requests

class Contrataciones_services:

    def get_data(self, module="contracts", id="LC-12006-19-170106"): 
        url = f"{HOST}/{module}/{id}"
        payload={}
        headers = {
            'Authorization': f'{TOKEN}',
            'Cookie': 'BIGipServer~produccion~BeOpendataV3=2496440512.55165.0000'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    def downloadFile(self, url, fileName):
        with open(f"{FILES_DIR}/{fileName}", "wb") as file:
            response = requests.get(url)
            file.write(response.content)
        print('downloadFile completed')
