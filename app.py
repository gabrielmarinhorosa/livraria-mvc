from flask import Flask

from controller.livro_controller import livro_bp

app = Flask(__name__, template_folder="view/templates")
app.register_blueprint(livro_bp)

if __name__ == "__main__":
    app.run(debug=True)
