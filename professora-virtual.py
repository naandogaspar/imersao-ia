# Importando a biblioteca
import google.generativeai as genai

# Configurando a chave api_key
api_key = "SECRET_KEY"
genai.configure(api_key=api_key)

# Instrucoes e configuracao
system_instruction = "Voce esta no brasil e uma professora do ensino fundamental que vai interagir com criancas de 5 a 15 anos, voce ensina as seguintes materias, portugues gramatica, matematica, geografia e historia do brasil, voce deve falar e responder de forma divertida e so pode reponder sobre questoes das materias que voce ensina, qualquer outro assunto que nao seja relacionado a isso voce deve informar que seu objetivo e ajudar o aluno a estudar, o aluno pode pedir para que voce faca algumas perguntas, nesse caso sempre que fizer uma pergunta termine com a frase 'qual e a resposta?'"

generation_config = {
    'candidate_count': 1,
    'temperature': 0.5
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
]

# Definindo variaveis para receber o nome do usuario e nome do modelo
usuario = ""
model_name = "gemini-1.5-pro-latest"

# Criando o modelo
model = genai.GenerativeModel(model_name=model_name, system_instruction=system_instruction, generation_config=generation_config,safety_settings=safety_settings)

# Criando o chat
chat = model.start_chat(history=[])

# Inicializacao do chat
prompt = input("\nOla, seja muito bem vindo!\n\nEu sou a T.IA sua professora virtual, eu vou te auxilar nas materias de portugues, matematica, historia e geografia e tambem posso te fazer perguntas para testar o seu conhecimento.\n\nPra gente iniciar primeiro me fale o seu nome:\n\n")
usuario = chat.send_message(prompt)

prompt = input("\nLegal, e como eu posso te ajudar hoje?:\n")

while prompt != "sair":
  response = chat.send_message(prompt)
  print("T.IA: ",response.text,"\n")
  prompt = input("")