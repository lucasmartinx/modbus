//Deve demonstrar a escrita e leitura de um valor float utilizando Holding Registers.



from clientemodbus import ClienteMODBUS
from time import sleep

# Cria o cliente apontando para o seu servidor
cliente = ClienteMODBUS('localhost', 5020)

print("--- TESTE DE FLOAT (32 bits) ---")
cliente.conectar()

endereco = 10  # Escolha um endereço inicial da sua tabela
valor_para_escrever = 3.1415

# Escreve o Float
print(f"Escrevendo o valor {valor_para_escrever} no endereço {endereco}...")
sucesso = cliente.escreveFloat(endereco, valor_para_escrever)

if sucesso:
    sleep(0.5) # Pausa rápida para o servidor processar
    # Lê o Float de volta
    valor_lido = cliente.lerFloat(endereco)
    print(f"Leitura concluída! Valor lido: {valor_lido}")
else:
    print("Falha ao tentar escrever o Float.")

cliente.fechar()