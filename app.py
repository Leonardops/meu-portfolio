from flask import Flask, render_template

app = Flask(__name__)

projetos = [
    {
        "titulo": "Portfolio pessoal",
        "descricao": "Site desenvolvido com flask, html e css.",
        "link": "#"
    },
    {
        "titulo": "Sistema em Python",
        "descricao": "Projeto para praticar lógica e estrutura.",
        "link": "#"
    },
    {
        "titulo": "Projeto Futuro",
        "descricao": "Em breve mais projetos aqui 👀",
        "link": "#"
    }
]

@app.route("/")
def home():
    return render_template("index.html", projetos=projetos)

if __name__ == "__main__":
    app.run(debug=True)

