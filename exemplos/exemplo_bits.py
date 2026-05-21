//Deve demonstrar a leitura dos 16 bits de um registrador e a alteração de um bit específico.



from clientemodbus import ClienteMODBUS
from time import sleep

# Cria o cliente apontando para o seu servidor
cliente = ClienteMODBUS('localhost', 5020)

print("--- TESTE DE MANIPULAÇÃO DE BITS ---")
cliente.conectar()

endereco = 20  # Endereço do Holding Register que vamos usar
bit_alvo = 3   # Vamos alterar o bit 3 (lembrando que vai de 0 a 15)
estado = 1     # 1 para ligar, 0 para desligar

# Escreve o Bit
print(f"Ligando o bit {bit_alvo} do registrador {endereco}...")
sucesso = cliente.escreveBitRegistrador(endereco, bit_alvo, estado)

if sucesso:
    sleep(0.5) # Pausa rápida
    # Lê todos os 16 bits do registrador para ver como ficou
    bits_lidos = cliente.lerBitsRegistrador(endereco)
    print(f"Leitura dos 16 bits (do 0 ao 15): {bits_lidos}")
else:
    print("Falha ao tentar alterar o bit.")

cliente.fechar()