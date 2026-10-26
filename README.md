# Livraria — Arquitetura MVC (Exercício 7.2)

MVP da livraria organizado em **Model–View–Controller**, com front-end funcional (listar e cadastrar livros).

## Estrutura

```
livraria-mvc/
├── app.py                         # ponto de entrada (cria o Flask e registra o controller)
├── model/
│   └── livro.py                   # MODEL: entidade Livro + regras e dados
├── controller/
│   └── livro_controller.py        # CONTROLLER: recebe a requisição, chama o model, escolhe a view
└── view/
    └── templates/index.html       # VIEW: página HTML que exibe os dados
```

## Fluxo

1. O usuário envia o formulário (**View**).
2. O **Controller** recebe o `POST /livros` e chama `LivroModel.adicionar()`.
3. O **Model** valida e guarda o livro.
4. O **Controller** redireciona e renderiza a **View** com a lista atualizada.

O Model não conhece Flask nem HTML; a View não tem regra de negócio.

## Como rodar

```bash
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:5000
