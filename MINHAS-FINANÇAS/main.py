from utilitarios import(
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total
)

# Categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_viagens = cadastrar_categoria('Viagens')
categoria_lazer = cadastrar_categoria('Lazer')

# Transações
cadastrar_transacao(
    descricao = 'Salário jan/24',
    valor = 2000,
    categoria = categoria_receitas
)

cadastrar_transacao(
    descricao = 'Ressarcimento',
    valor = 500,
    categoria = categoria_receitas
)

cadastrar_transacao(
    descricao = 'Água',
    valor = -100,
    categoria = categoria_contas
)

total = saldo_total()
print(f'Saldo total: {total}')
