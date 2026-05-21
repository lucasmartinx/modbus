from clientemodbus import ClienteMODBUS
from interface_usuario import InterfaceUsuario

if __name__ == '__main__':
    # 1. Cria o cliente
    c = ClienteMODBUS('localhost', 5020)

    # 2. Passa o cliente para a interface
    menu = InterfaceUsuario(c)

    # 3. Inicia o menu
    menu.atendimento()