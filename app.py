from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Carregar o arquivo Excel
    file_path = 'data/lucas.xlsx'
    df = pd.read_excel(file_path)

    # Converter o DataFrame para uma lista de dicionários para passar ao HTML
    data = df.to_dict(orient='records')

    # Renderizar o template e passar os dados para a página
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)