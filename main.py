from flask import Flask, send_file, abort
import os

app = Flask(__name__)

# Caminho para a pasta onde os arquivos PDF estão armazenados no seu PC
PDF_FOLDER = 'C:/Users/Arthurzinho/Documents/'

@app.route('/download/<filename>')
def download_file(filename):
    # Gera o caminho completo do arquivo
    file_path = os.path.join(PDF_FOLDER, filename)
    
    # Verifica se o arquivo existe
    if os.path.exists(file_path):
        # Envia o arquivo como resposta
        return send_file(file_path, as_attachment=True)
    else:
        # Retorna erro 404 se o arquivo não for encontrado
        abort(404)

if __name__ == '__main__':
    # Executa o servidor Flask localmente
    app.run()
