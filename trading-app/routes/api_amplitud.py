from flask import Blueprint, request, jsonify
import requests
import os
import time 
from dotenv import load_dotenv
load_dotenv()


amplitud_bp = Blueprint('amplitud', __name__, url_prefix='/amplitud')

def amplitud():

    api_url = os.getenv("API_AMPLITUD")
    
    try:
        response = requests.get(api_url, stream=True)
        print(response.status_code) 

        response.raise_for_status()  
        
        if response.status_code == 200:
            print("Procesando datos en streaming...")
            for chunk in response.iter_content(chunk_size=1024):  
                if chunk:  
                    print(chunk.decode("utf-8")) 
               
            
    
    except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500


@amplitud_bp.route('/datos', methods=['GET'])
def ver_datos():
    amplitud()
    return jsonify({"msg": "Datos de amplitud procesados"}), 200

