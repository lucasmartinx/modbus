from time import sleep
from clientemodbus import ClienteMODBUS
class InterfaceUsuario:
    """
    Classe para lidar com a interação do usuário via console
    """
    def __init__(self, cliente):
        self.cliente = cliente

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        # Abre a conexão usando o método do cliente
        self.cliente.conectar()
        try:
            atendimento = True
            while atendimento:
                sel = input("Opções: (1- Leitura | 2- Escrita | 3- Configuração | 4- Sair | 5- Float | 6- Bits): ")

                if sel == '1':
                    tipo = input("""Qual tipo de dado deseja ler? (1- Holding Register | 2- Coil | 3- Input Register | 4- Discrete Input): """)
                    addr = input("Digite o endereço da tabela MODBUS: ")
                    nvezes = input("Digite o número de vezes que deseja ler: ")
                    for i in range(0, int(nvezes)):
                        print(f"Leitura {i+1}: {self.cliente.lerDado(int(tipo), int(addr))}")
                        sleep(self.cliente._scan_time)

                elif sel == '2':
                    tipo = input("""Qual tipo de dado deseja escrever? (1- Holding Register | 2- Coil): """)
                    addr = input("Digite o endereço da tabela MODBUS: ")
                    valor = input("Digite o valor que deseja escrever: ")
                    ok = self.cliente.escreveDado(int(tipo), int(addr), int(valor))
                    print("Escrita realizada." if ok else "Falha na escrita.")

                elif sel == '3':
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self.cliente._scan_time = float(scant)

                elif sel == '4':
                    atendimento = False

                elif sel == '5':
                    acao = input("1- Ler Float ou 2- Escrever Float? ")
                    addr = int(input("Endereco inicial: "))
                    
                    if acao == '1':
                        print("Float lido:", self.cliente.lerFloat(addr))
                        
                    if acao == '2':
                        val = float(input("Digite o Float (ex: 3.14): "))
                        self.cliente.escreveFloat(addr, val)
                        print("Float escrito!")

                elif sel == '6':
                    acao = input("1- Ler os 16 bits ou 2- Mudar 1 bit? ")
                    addr = int(input("Endereco (Holding Reg): "))
                    
                    if acao == '1':
                        print("Bits:", self.cliente.lerBitsRegistrador(addr))
                        
                    if acao == '2':
                        bit_idx = int(input("Qual bit (0-15)? "))
                        estado = int(input("Novo estado (1 para ligar, 0 para desligar)? "))
                        self.cliente.escreveBitRegistrador(addr, bit_idx, estado)
                        print("Bit alterado!")

                else:
                    print("Seleção inválida")
        except Exception as e:
            print('Erro no atendimento: ', e.args)
        finally:
            # Fecha a conexão ao sair
            self.cliente.fechar()

if __name__ == "__main__":
    # Instancia o cliente MODBUS
    meu_cliente = ClienteMODBUS(server_ip='127.0.0.1', porta=5020)
    
    # Instancia a interface passando o cliente como parâmetro
    minha_interface = InterfaceUsuario(meu_cliente)
    
    # Inicia o loop do menu
    minha_interface.atendimento()