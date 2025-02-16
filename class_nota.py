from datetime import datetime

from class_pedido import Pedido
from class_pessoa import Pessoa


class Nota:

    from datetime import datetime

class Nota:
    @classmethod
    def construtorDoRegistro(self, codigo_pedido, cliente, atendente,horaGerada,valorTotal):
        self._codigo_pedido = codigo_pedido
        self._cliente = cliente
        self._atendente = atendente
        self._horaGerada = horaGerada
        self._valorTotal = valorTotal


    def __init__(self, pedido, cliente, atendente):
        self.__pedido = pedido
        self.__cliente = cliente
        self.__atendente = atendente
        self.__horaGerada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      #  self.__valorTotal = 0.0  # Initialize __valorTotal
    #    for iterado in pedido._itens_pedidos:
 #           self.__valorTotal += iterado._produto._preco * iterado._quantidade
        self.__valorTotal = self.calcular_valor_total()

    @property
    def _pedido(self):
        return self.__pedido

    @_pedido.setter
    def _pedido(self, value):
        self.__pedido = value

    @property
    def _cliente(self):
        return self.__cliente
    
    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value
    
    @property
    def _atendente(self):
        return self.__atendente
    
    @_atendente.setter
    def _atendente(self, value):
        self.__atendente = value
    
    @property
    def _valorTotal(self):
        return self.__valorTotal
    
    @_valorTotal.setter
    def _valorTotal(self, value):
        self.__valorTotal = value
    
    @property
    def _horaGerada(self):
        return self.__horaGerada
    
    @_horaGerada.setter
    def _horaGerada(self, value):
        self.__horaGerada = value

    def calcular_valor_total(self):
        valor_total = 0.0
        for item in self.__pedido._itens_pedidos:
            valor_total += item._produto._preco * item._quantidade
        return valor_total


    def toString(self):
        info_nota = "\n --- INFO - NOTA FISCAL ---\n"
        info_nota += f"Pedido: {self._pedido._codigo_pedido}\n"
        info_nota += f"Cliente: {self._cliente._nome}\n"
        info_nota += f"Atendente: {self._atendente._nome}\n"
        info_nota += f"Data/Hora: {self._horaGerada}\n"
        info_nota += f"Valor Total: R$ {self._valorTotal:.2f}\n"
        info_nota += "----------------"
        return info_nota

    def toStringForSaveLoadMethod(self):
        return f'{self._pedido._codigo_pedido},{self._cliente._nome},{self._atendente._nome},{self._horaGerada},{self._valorTotal}'

    @staticmethod
    def fromStringToSaveLoadMethod(string):
        try:
            attributes = string.strip().split(',')        
            if len(attributes) == 5:
                codigo_pedido = int(attributes[0])
                cliente = str(attributes[1])
                atendente = str(attributes[2])
                horaGerada = str(attributes[3])
                horaObj = datetime.strptime(horaGerada, "%Y-%m-%d %H:%M:%S")
                valorTotal = float(attributes[4])
                

                newCliente = Pessoa(cliente, None, None, None, None)
                newAtendente = Pessoa(atendente, None, None, None, None)
                pedido = Pedido(codigo_pedido, None)
                nota = Nota(pedido, newCliente, newAtendente)  # Placeholder values
                nota.construtorDoRegistro(codigo_pedido, newCliente, newAtendente, horaGerada, valorTotal)
                return nota
                
            else:
                print(f"Erro na leitura do arquivo {string.strip()}")
                return None
        except Exception as e:
            print(f'Erro na leitura do arquivo {string.strip()}')
            print(f'Erro: {e}')
# Observar a funcinalidade da função calcular valor total e o toSting se está implementao corretamente
