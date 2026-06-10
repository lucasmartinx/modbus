import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.clock import Clock
from kivy.lang import Builder
from clientemodbus import ClienteMODBUS

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

# Integração da interface gráfica diretamente no código Python
Builder.load_string('''
<MyWidget>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    
    BoxLayout:
        size_hint_y: None
        height: 40
        spacing: 5

        Label:
            text: 'IP:'
            size_hint_x: 0.3
            
        TextInput:
            id: txt_ip
            text: '127.0.0.1'
            multiline: False
            
        Label:
            text: 'Porta:'
            size_hint_x: 0.3
            
        TextInput:
            id: txt_porta
            text: '502'
            multiline: False
            
        Button:
            id: btn_conectar
            text: 'Conectar'
            background_color: [0, 0, 1, 1]
            on_press: root.toggle_conexao()

    BoxLayout:
        size_hint_y: None
        height: 40
        spacing: 5
    
        Label:
            text: 'Endereço:'
            size_hint_x: 0.3
            
        TextInput:
            id: endereco_ip
            text: '1000'
            multiline: False

    BoxLayout:
        size_hint_y: None
        height: 40
        spacing: 5
        
        Label:
            text: 'Novo valor:'
            size_hint_x: 0.3
            
        TextInput:
            id: novo_valor
            text: '0'
            multiline: False
       
        Button:
            id: enviar
            text: 'Confirmar'
            background_color: [0, 1, 0, 1]
            on_press: root.escrever_dados()
          
    BoxLayout:
        size_hint_y: None
        height: 40
        spacing: 5
        
        Label:
            id: lbl_valor_atual
            text: 'Valor atual: ---'

    BoxLayout:
        size_hint_y: None
        height: 40
        spacing: 5
      
        Switch: 
            id: leitura_recorrente
            active: False
            size_hint_x: 0.3
            on_active: root.tratar_recorrente(self, self.active)
            
        Label:
            text: 'Leitura recorrente'
            text_size: self.size
            halign: 'left'
            valign: 'center'

    Widget:
''')

class MyWidget(BoxLayout):
    def __init__(self, cliente_inicial, **kwargs):
        super().__init__(**kwargs)
        self.conectado = False
        self.evento_leitura = None
        self.cliente = cliente_inicial

    def toggle_conexao(self):
        if not self.conectado:
            ip = self.ids.txt_ip.text
            porta = int(self.ids.txt_porta.text)
            
            self.cliente = ClienteMODBUS(server_ip=ip, porta=porta)
            self.cliente.conectar()
            
            self.conectado = True
            self.ids.btn_conectar.text = 'Desconectar'
            self.ids.btn_conectar.background_color = [1, 0, 0, 1]
        else:
            if self.cliente:
                self.cliente.fechar()
            
            self.conectado = False
            self.ids.btn_conectar.text = 'Conectar'
            self.ids.btn_conectar.background_color = [0, 0, 1, 1]
            self.ids.leitura_recorrente.active = False

    def ler_dados(self, *args):
        try:
            endereco = int(self.ids.endereco_ip.text)
            # Lê Holding Register (tipo 1)
            valor = self.cliente.lerDado(1, endereco)
            self.ids.lbl_valor_atual.text = f'Valor atual: {valor}'
        except Exception:
            self.ids.lbl_valor_atual.text = 'Valor atual: Erro na leitura'

    def escrever_dados(self):
        try:
            endereco = int(self.ids.endereco_ip.text)
            valor = int(self.ids.novo_valor.text)
            # Escreve Holding Register (tipo 1)
            self.cliente.escreveDado(1, endereco, valor)
        except Exception:
            pass

    def tratar_recorrente(self, checkbox, is_active):
        if is_active:
            self.evento_leitura = Clock.schedule_interval(self.ler_dados, 1.0)
        else:
            if self.evento_leitura:
                self.evento_leitura.cancel()

class BasicApp(App):
    def __init__(self, cliente, **kwargs):
        super().__init__(**kwargs)
        self.cliente = cliente

    def build(self):
        return MyWidget(cliente_inicial=self.cliente)

class InterfaceUsuario:
    def __init__(self, cliente):
        self.cliente = cliente

    def atendimento(self):
        Config.set('graphics', 'resizable', True)
        app = BasicApp(self.cliente)
        app.run()

if __name__ == "__main__":
    meu_cliente = ClienteMODBUS(server_ip='127.0.0.1', porta=5020)
    minha_interface = InterfaceUsuario(meu_cliente)
    minha_interface.atendimento()