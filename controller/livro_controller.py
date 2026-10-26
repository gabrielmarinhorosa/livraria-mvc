"""CONTROLLER: recebe as ações do usuário, chama o Model e escolhe a View."""
from flask import Blueprint, redirect, render_template, request, url_for

from model.livro import LivroModel

livro_bp = Blueprint("livros", __name__)
model = LivroModel()


@livro_bp.get("/")
def index():
    return render_template(
        "index.html",
        livros=model.listar(),
        erro=request.args.get("erro"),
    )


@livro_bp.post("/livros")
def adicionar():
    try:
        model.adicionar(
            request.form.get("titulo", "").strip(),
            request.form.get("autor", "").strip(),
            request.form.get("preco", ""),
        )
    except ValueError as e:
        return redirect(url_for("livros.index", erro=str(e)))
    return redirect(url_for("livros.index"))
