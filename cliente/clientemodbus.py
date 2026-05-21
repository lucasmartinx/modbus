from pymodbus.client import ModbusTcpClient

class ClienteMODBUS():
    """
    Classe Cliente MODBUS usando pymodbus
    """
    def __init__(self, server_ip, porta, scan_time=1):
        """
        Construtor
        """
        # Cria o cliente TCP
        self._cliente = ModbusTcpClient(host=server_ip, port=porta)
        self._scan_time = scan_time

    def conectar(self):
        """Abre a conexão com o servidor MODBUS"""
        self._cliente.connect()

    def fechar(self):
        """Fecha a conexão com o servidor MODBUS"""
        self._cliente.close()

    def lerDado(self, tipo, addr):
        """
        Método para leitura de um dado da Tabela MODBUS
        Retorna o valor lido ou None em caso de falha.
        """
        # Holding Register (função 03)
        if tipo == 1:
            resp = self._cliente.read_holding_registers(address=addr, count=1, device_id=1)
            if resp and not resp.isError():
                return resp.registers[0]
            return None

        # Coil (função 01)
        if tipo == 2:
            resp = self._cliente.read_coils(address=addr, count=1, device_id=1)
            if resp and not resp.isError():
                return resp.bits[0]
            return None

        # Input Register (função 04)
        if tipo == 3:
            resp = self._cliente.read_input_registers(address=addr, count=1, device_id=1)
            if resp and not resp.isError():
                return resp.registers[0]
            return None

        # Discrete Input (função 02)
        if tipo == 4:
            resp = self._cliente.read_discrete_inputs(address=addr, count=1, device_id=1)
            if resp and not resp.isError():
                return resp.bits[0]
            return None

        # Tipo inválido
        return None

    def escreveDado(self, tipo, addr, valor):
        """
        Método para a escrita de dados na Tabela MODBUS
        Retorna True em caso de sucesso, False em caso de falha.
        """
        # Holding Register (função 06 - single)
        if tipo == 1:
            resp = self._cliente.write_register(address=addr, value=valor, device_id=1)
            return bool(resp and not resp.isError())

        # Coil (função 05 - single)
        if tipo == 2:
            # Em coils, valor esperado é 0/1 (False/True)
            resp = self._cliente.write_coil(address=addr, value=bool(valor), device_id=1)
            return bool(resp and not resp.isError())

        # Tipo inválido
        return False
    def escreveFloat(self, addr, valor):
        val_float = float(valor)
        payload = self._cliente.convert_to_registers(val_float, data_type=self._cliente.DATATYPE.FLOAT32)
        resp = self._cliente.write_registers(address=addr, values=payload, device_id=1)
        return not resp.isError()

    def lerFloat(self, addr):
        resp = self._cliente.read_holding_registers(address=addr, count=2, device_id=1)
        if resp and not resp.isError():
            return self._cliente.convert_from_registers(resp.registers, data_type=self._cliente.DATATYPE.FLOAT32)
        return None

    def lerBitsRegistrador(self, addr):
        valor = self.lerDado(1, addr)
        if valor is not None:
            return [(valor >> i) & 1 for i in range(16)]
        return None

    def escreveBitRegistrador(self, addr, bit_index, estado):
        valor_atual = self.lerDado(1, addr)
        if valor_atual is None:
            return False
            
        if estado == 1:
            novo_valor = valor_atual | (1 << bit_index)
        if estado == 0:
            novo_valor = valor_atual & ~(1 << bit_index)
            
        return self.escreveDado(1, addr, novo_valor)