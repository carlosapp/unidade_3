import ollama


def gerar_embedding(texto, modelo="nomic-embed-text"):
    """Gera o embedding de um texto usando o Ollama local."""
    resposta = ollama.embed(
        model=modelo,
        input=texto
    )

    return resposta["embeddings"][0]


def main():
    texto = "O original não pode ser desoriginalizado."
    modelo = "nomic-embed-text"

    print("=== GERADOR DE EMBEDDINGS COM O OLLAMA ===")
    print(f"\nTexto original: {texto}")
    print(f"Modelo: {modelo}")

    try:
        embedding = gerar_embedding(texto, modelo)

        print(f"\nQuantidade de dimensões: {len(embedding)}")
        print("\nPrimeiros 10 valores:")
        print(embedding[:10])

        print("\nEmbedding completo:")
        print(embedding)

        print("\nEmbeddings gerados com sucesso!")

    except Exception as erro:
        print("\nErro ao gerar embeddings.")
        print(f"Detalhes: {erro}")
        print(
            "Verifique se o Ollama está em execução "
            "e se o modelo foi baixado."
        )


if __name__ == "__main__":
    main()
