# Geração de Embeddings com Ollama e Python

## 1. Descrição


O programa recebe um texto em português, solicita ao modelo de embeddings que gere sua representação numérica e exibe a quantidade de dimensões e os valores do vetor gerado.

## 2. Tecnologias utilizadas

- Python 3
- Ollama
- Modelo `nomic-embed-text`
- Biblioteca Python `ollama`
- Windows e PowerShell

## 3. Pré-requisitos

Antes de executar o projeto, é necessário ter:

- Python instalado no computador.
- Ollama instalado e em execução.
- A biblioteca Python `ollama` instalada.
- O modelo `nomic-embed-text` baixado.

Download do Ollama para Windows:

https://ollama.com/download/windows

## 4. Instalação e configuração

### Passo 1 — Instalar e verificar o Ollama

Baixe o instalador pelo site oficial e conclua a instalação.

Abra um novo terminal PowerShell e execute:

```powershell
ollama --version
```

Se o comando apresentar a versão do Ollama, a instalação está acessível pelo terminal.

#### Se o comando `ollama` não for reconhecido

Esse erro pode ocorrer quando o Ollama não está instalado ou quando seu executável não está configurado no PATH do Windows.

Verifique se o executável existe no seguinte caminho:

```powershell
Test-Path "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"
```

Se o resultado for `True`, utilize o caminho completo para baixar o modelo:

```powershell
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" pull nomic-embed-text
```

Para listar os modelos instalados:

```powershell
& "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" list
```

Se o resultado for `False`, verifique se o executável está em outro local:

```powershell
where.exe ollama
```

Se o executável não for encontrado, instale ou repare a instalação do Ollama pelo site oficial.

### Passo 2 — Baixar o modelo de embeddings

Se o comando `ollama` estiver funcionando, execute:

```powershell
ollama pull nomic-embed-text
```

Esse comando baixa o modelo necessário para gerar os embeddings.

Para confirmar que o modelo está disponível:

```powershell
ollama list
```

O modelo `nomic-embed-text` deverá aparecer na lista.

## 5. Verificar se o Ollama está em execução

O Ollama disponibiliza uma API local, normalmente no endereço `http://localhost:11434`.

### Método 1 — Pelo navegador

Abra o Chrome, Edge ou outro navegador e acesse:

http://localhost:11434

Se o Ollama estiver em execução, normalmente será exibida a mensagem:

```text
Ollama is running
```

Essa mensagem confirma que o serviço está respondendo no endereço local.

### Método 2 — Pelo PowerShell

Execute o seguinte comando para consultar os modelos disponíveis:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

Se o serviço estiver funcionando, será retornada uma resposta com informações sobre os modelos instalados.

### Método 3 — Testar a geração de embeddings

Para confirmar que o modelo consegue gerar embeddings, execute no PowerShell:

```powershell
$body = @{
    model = "nomic-embed-text"
    input = "Teste de geração de embeddings"
} | ConvertTo-Json

Invoke-RestMethod `
    -Uri "http://localhost:11434/api/embed" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```

Se o teste for bem-sucedido, a resposta conterá a propriedade `embeddings`, com uma lista de valores numéricos.

Se o modelo não estiver instalado, baixe-o conforme as instruções da seção 4.

#### Possíveis erros

- **Conexão recusada:** verifique se o aplicativo Ollama está aberto e em execução.
- **Modelo não encontrado:** execute `ollama pull nomic-embed-text`.
- **Comando `ollama` não reconhecido:** consulte o procedimento alternativo da seção 4.
- **Erro na API:** confira o endereço, o nome do modelo e a resposta retornada pelo PowerShell.

## 6. Instalar as dependências Python

Na pasta do projeto, execute:

```powershell
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém a biblioteca necessária para a comunicação com o Ollama.

## 7. Executar o projeto

Na pasta em que estão os arquivos do projeto, execute:

```powershell
python main.py
```

O programa define um texto em português, envia a solicitação ao modelo `nomic-embed-text` e apresenta o embedding retornado.

O Ollama deve estar em execução localmente antes de iniciar o programa.

## 8. Funcionamento do programa

O arquivo `main.py` realiza as seguintes etapas:

1. Define um texto de entrada em português.
2. Seleciona o modelo `nomic-embed-text`.
3. Envia o texto ao Ollama por meio da biblioteca Python.
4. Recebe o embedding gerado pelo modelo.
5. Armazena o vetor numérico em uma variável Python.
6. Exibe a quantidade de dimensões, os dez primeiros valores e o vetor completo.

A chamada principal utilizada para gerar os embeddings é:

```python
resposta = ollama.embed(
    model="nomic-embed-text",
    input=texto
)
```

O vetor é obtido com:

```python
embedding = resposta["embeddings"][0]
```

## 9. Resultado esperado

Ao executar o programa, serão exibidos:

- O texto original.
- O nome do modelo utilizado.
- A quantidade de dimensões do embedding.
- Os dez primeiros valores do vetor.
- O vetor completo.
- Uma mensagem confirmando a geração dos embeddings.

O modelo `nomic-embed-text` normalmente gera vetores com 768 dimensões.

Os valores numéricos são calculados pelo modelo durante a execução e dependem do texto processado.

## 10. Evidência em vídeo

O vídeo de demonstração deverá apresentar visualmente:

1. O código Python no arquivo `main.py`.
2. A confirmação de que o modelo está instalado.
3. A verificação de que o Ollama está respondendo localmente.
4. A exibição do número de dimensões e dos valores do embedding.
5. A mensagem de sucesso ao final da execução.

**Link do vídeo:** a inserir após a gravação e publicação.

## 11. Estrutura do projeto

```text
unidade_3/
├── main.py
├── requirements.txt
└── README.md
```
