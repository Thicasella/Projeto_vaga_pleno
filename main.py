import operator

# Lista de veículos
veiculos = [
    {"modelo": "Carro 1", "descricao": "Descrição breve do Carro 1.", "preco": 25000, "imagem": "car1.jpg"},
    {"modelo": "Carro 2", "descricao": "Descrição breve do Carro 2.", "preco": 30000, "imagem": "car2.jpg"},
    {"modelo": "Carro 3", "descricao": "Descrição breve do Carro 3.", "preco": 20000, "imagem": "car3.jpg"}
]

# Ordenar veículos por preço
veiculos_ordenados = sorted(veiculos, key=operator.itemgetter('preco'))

# Adicionar mais um veículo
veiculos_ordenados.append({"modelo": "Carro 4", "descricao": "Descrição breve do Carro 4.", "preco": 35000, "imagem": "car4.jpg"})

# Gerar HTML dinâmico
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Catalogo de Vendas de Carros</title>
</head>
<body>

    <header>
        <h1>Catalogo de Vendas de Carros</h1>
    </header>

    <section class="car-list">
"""

for carro in veiculos_ordenados:
    html_content += f"""
        <div class="car">
            <img src="{carro['imagem']}" alt="{carro['modelo']}">
            <h2>{carro['modelo']}</h2>
            <p>{carro['descricao']}</p>
            <p>Preço: ${carro['preco']}</p>
            <button>Ver Detalhes</button>
        </div>
"""

html_content += """
    </section>

    <footer>
        <p>&copy; 2024 Catálogo de Vendas de Carros</p>
    </footer>

</body>
</html>
"""

# Escrever HTML em um arquivo
with open('index.html', 'w') as file:
    file.write(html_content)
