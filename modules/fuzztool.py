import requests
import sys

class Fuzz:
    
    
    def __init__(self):
        pass


    def run(link, wordlist):
        try:
            truth_path = list()
            f = open(wordlist, 'r')
            words = f.readlines()
            
            for i in words:
                
                linka = f'https://{link}/{i}'
                print(linka)
                response = requests.get(linka)
                if response.status_code == 200: truth_path.append(link)
                
            if len(truth_path) < 0:
                return truth_path
            else:
                return ValueError

        except Exception as e:
            print(f'Fancy Except: {e}')
