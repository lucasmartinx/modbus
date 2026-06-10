# kivy-modbus

# Interface Cliente Modbus TCP (Kivy)

Este projeto consiste em uma interface gráfica (GUI) desenvolvida em Python utilizando o framework **Kivy**. O objetivo da aplicação é fornecer um painel de controle simples e intuitivo para conectar e interagir com um servidor Modbus TCP.

## 🛠️ Recursos da Interface

A tela da aplicação possui suporte para os seguintes recursos (front-end):
* **Conexão:** Campos para inserção de IP e Porta, com botão de conectar.
* **Endereçamento:** Campo para definir o endereço Modbus (Holding Registers, Coils, etc.) alvo da operação.
* **Escrita de Dados:** Campo para inserir o novo valor e botão de confirmação para envio ao servidor.
* **Leitura de Dados:** Exibição do valor atual lido do dispositivo conectado.

*Nota: A interface atual é o esqueleto (front-end) da aplicação. A lógica de back-end com as bibliotecas Modbus precisa ser acoplada aos métodos do Kivy.*

## 📁 Estrutura de Arquivos

* `main.py`: Arquivo principal em Python contendo a lógica de inicialização da aplicação, configurações da janela e a classe do widget base (`MyWidget`).
* `basic.kv`: Arquivo de Kivy Language (KV) contendo toda a estrutura visual, layout, cores, botões e campos de texto da interface.
* `requirements.txt`: Arquivo com as dependências necessárias para rodar o projeto.

## ⚙️ Pré-requisitos e Instalação

Para rodar este projeto, você precisará do **Python** instalado em sua máquina.

1. Clone ou baixe este repositório para o seu computador.
2. Abra o terminal na pasta do projeto.
3. (Opcional, mas recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
