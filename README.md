# Aplicação Cliente-Servidor Modbus TCP

Este repositório contém o desenvolvimento de uma aplicação cliente-servidor Modbus TCP escrita em Python, utilizando a biblioteca `pymodbus`. 

O projeto foi construído seguindo boas práticas de programação, mantendo uma **separação clara de responsabilidades** (a lógica de comunicação Modbus é totalmente isolada da interface do usuário) e implementando operações avançadas, como manipulação de números de ponto flutuante (floats) e bits individuais.

## 🚀 Funcionalidades

- **Servidor Modbus TCP:** Disponibiliza uma área de memória de *Holding Registers* para testes locais.
- **Cliente Modbus TCP:** Classe dedicada exclusivamente à comunicação, conversão e manipulação de dados.
- **Operações com Float (32 bits):** Empacotamento e desempacotamento de valores `float` ocupando 2 *Holding Registers* consecutivos.
- **Leitura de Bits:** Mapeamento de um *Holding Register* para visualizar o estado individual de seus 16 bits.
- **Escrita de Bit Individual:** Utiliza a técnica de *Read-Modify-Write* (máscaras binárias) para ligar ou desligar um único bit sem afetar os outros 15.
- **Interface Interativa (CLI):** Um menu de linha de comando isolado para o usuário realizar testes.

## 📂 Estrutura do Repositório

```text
meu_projeto_modbus/
│
├── README.md                  # Documentação do projeto
├── requirements.txt           # Dependências do Python
├── .gitignore                 # Arquivos ignorados pelo Git
│
├── servidor/
│   └── servidor_modbus.py     # Script para iniciar o servidor local
│
├── cliente/
│   ├── __init__.py            # Torna o diretório um pacote importável
│   ├── cliente_modbus.py      # Lógica de comunicação Modbus isolada
│   └── interface_usuario.py   # Menu interativo (CLI)
│
└── exemplos/
    ├── exemplo_float.py       # Script demonstrando a operação com Floats
    └── exemplo_bits.py        # Script demonstrando a operação com Bits individuais
# modbus