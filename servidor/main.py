from servidormodbus import ServidorMODBUS

# Mudando para 5020 para bater com o cliente
s = ServidorMODBUS('localhost', 5020)
s.run()