from flask import Flask, request
import requests
import threading
import time

app = Flask(__name__)

volume = 0

@app.route('/', methods=['POST'])
def tanque_EtOH():
    data = request.get_json()
    var = data.get('etoh', None)
    
    
    
    global volume
    
    volume += var * 0.99 
    
    response = {
        'status_code': 200
    }
    time.sleep(3)
    
    print("Volume recebido:", volume)
    return response 




@app.route('/', methods=['GET']) # O GET  mostra na tela
def getVolume():
    global volume
    
    response = {
        'etoh': volume
    }
    return response

class EtOH(threading.Thread): # 
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            global volume
            request = {
                "origem": "etoh",
                "etoh": volume
            }
            #time.sleep(5)
            requests.post('https://destrotrampo.herokuapp.com/naoh-etoh', json = request, headers = {"Content-Type": "application/json"})# manda pro simões, ele tem que fazer um post só pra receber o etoh
            print("Volume para o tanque:",volume)
            volume = 0
            



#if __name__ == '__main__':
#    app.run()

def create_app():
    global app
    tanque = EtOH()
    tanque.start()
    return app