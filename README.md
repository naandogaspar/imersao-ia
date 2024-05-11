# Seja bem vindo ao T.IA, carinhosamente chamado de Tia!
## Uma professora virtual que auxilia no ensino focado para crianças e jovens.

# Objetivo:
O objetivo desse projeto é ser uma ferramenta para auxilar o ensino infantil das nossas crianças, sabemos que para os pais esse é um grande desafio, até por muitas das vezes por lembrar do conteúdo ensinado.

É recomendado que o uso da criança sempre que possivel seja acompanhado de um adulto, a ideia não é ser um substitudo do responsavel e nem do professor, a ideia é trazer mais tecnologia, fonte de conhecimento e deixar o estudo mais divertido para nossos pequenos.

# Tecnologias:
- Python
- Google Generative AI
- Google Colab

# Melhorias:
- Categorizar os conteúdos das matéria de acordo com o ano letivo da criança

# Execução:
- Para executar esse projeto na sua máquina você precisa ter o Python instalado em seu ambiente
- Você precisará instalar a biblioteca do generativeai, usando o código:
  ```pip install -q -U google-generativeai```
- Você vai precisar de uma ```API KEY``` que pode ser gerada gratuitamente no Google AI Studio: https://aistudio.google.com/app/apikey e com essa chave substituir o valor ```SECRET_KEY``` na linha 5 do código:
  ```Python# Configurando a chave api_key
  api_key = "SECRET_KEY"
  genai.configure(api_key=api_key)```
- Apos baixar o arquivo principal, através do CMD / Prompt basta acessar o diretorio que o arquivo está localizado e executar o comando:
  ```python professora-virtual.py```
