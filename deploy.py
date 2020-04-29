from flask import Flask, request
import requests
import threading
import time

app = Flask(__name__)

volume = 0

@app.route('/tanque_EtOH', methods=['POST'])
def tanque_EtOH():
    data = request.get_json()
    var = data.get('volume', None)
    
    
    
    global volume
    
    volume += var * 0.99 
    
    resposta = {
        'volume': volume
    }
    
    return resposta




@app.route('/tanque_EtOH', methods=['GET'])
def getVolume():
    global volume
    resposta = {
        'EtOH': volume
    }
    return resposta

class EtOH(threading.Thread): # 
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            global volume
            request = {
                'EtOH': volume
            }
            response = requests.post('URL-thomas', json = request, headers = {"Content-Type": "application/json"}).json()
            
            time.sleep(3)
            volume = response['EtOH'] * 0.99 # ver com o tomas o EtOH
            request = {
                'EtOH': volume
            }
            requests.post('URL-Simões', json = request, headers = {"Content-Type": "application/json"}) # mandar pro simões
            volume = 0



if __name__ == '__main__':
    app.run()
    