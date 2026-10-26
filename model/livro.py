"""MODEL: dados e regras da livraria. Não sabe nada de HTTP nem de HTML."""
from dataclasses import dataclass


@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    preco: float


class LivroModel:
    def __init__(self):
        self._livros = [
            Livro(1, "Dom Casmurro", "Machado de Assis", 29.90),
            Livro(2, "O Cortiço", "Aluísio Azevedo", 24.50),
        ]

    def listar(self):
        return list(self._livros)

    def adicionar(self, titulo, autor, preco):
        if not titulo or not autor:
            raise ValueError("Título e autor são obrigatórios.")
        try:
            preco = float(preco)
        except (TypeError, ValueError):
            raise ValueError("Preço inválido.")
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")

        novo_id = max((l.id for l in self._livros), default=0) + 1
        livro = Livro(novo_id, titulo, autor, preco)
        self._livros.append(livro)
        return livro
