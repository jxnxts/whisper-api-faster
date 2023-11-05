# Whisper API (Speech to Text)

A Whisper API é uma avançada interface de programação de aplicações (API) de conversão de fala em texto com tecnologia OpenAI. Esta API utiliza uma combinação de técnica de transformadores de linguagem e modelos de rede neural para oferecer capacidades de transcrição altamente precisas e eficientes. Ela foi treinada em várias horas de áudio multilíngue e fornece uma transcrição de fala citável, fácil de ler e gramaticalmente precisa. 

A API está disponível em diferentes tamanhos, cada um com suas próprias características. Portanto, pode-se escolher o modelo que melhor se adapta às necessidades do projeto.

## Modelos disponíveis:

| Model Size | Parameters | English-only | Multilingual |
| --- | --- | --- | --- |
| tiny | 39 M | ✓ | ✓ |
| base | 74 M | ✓ | ✓ |
| small | 244 M | ✓ | ✓ |
| medium | 769 M | ✓ | ✓ |
| large | 1550 M | x | ✓ |
| large-v2 | 1550 M | x | ✓ |

## Configuração em localhost:

### Criação do Ambiente Virtual:

1. Primeiro, instale o módulo virtualenv usando pip (`pip install virtualenv` para Windows ou `pip3 install virtualenv` para Mac/Linux).
2. No diretório do seu projeto, crie o ambiente virtual: `virtualenv venv`.

### Ativação do Ambiente Virtual:

- Para ativar o ambiente virtual, use o comando `. \venv\Scripts\activate` para windows ou `source venv/bin/activate` para Mac/Linux.
  
### Rodar a Aplicação:

1. Agora, você pode instalar qualquer pacote necessário para a sua aplicação usando pip (pip install nome_do_pacote). Esses pacotes serão instalados apenas dentro do seu ambiente virtual.
2. Execute seu script Python como normalmente faria: `python nome_do_script.py` (Windows) ou `python3 nome_do_script.py` (Mac/Linux).

## Configuração do Docker:

### Docker Compose:

Aqui está um exemplo de arquivo docker-compose.yml que pode ser usado para criar o serviço FastAPI.

```yaml
version: '3.9'
services:
  fastapi:
    build: 
      context: .
    image: fastapi:latest
    ports:
      - target: 9005
        published: 9005
    volumes:
      - type: bind
        source: .
        target: /app 
```

### Dockerfile:

Aqui está um exemplo de Dockerfile usado para criar a imagem FastAPI.

```Dockerfile
FROM python:3.11
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","9005"]
```
### Variáveis de Ambiente:

Algumas variáveis que você pode configurar para o serviço FastAPI. 

```bash
KMP_DUPLICATE_LIB_OK=TRUE
MODEL=large-v2
DEVICE=cpu
COMPUTETYPE=int8
VADFILTER=true
VALI_TOTAL = "CRIE UM TOKEN VALIDO"
```

Lembre-se de substituir o `CRIAR UM TOKEN VALIDO` pelo seu token.