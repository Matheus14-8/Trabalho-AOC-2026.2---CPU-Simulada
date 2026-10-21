"""
CPU SIMULADA — Código completo
AOC 2026.2

CPU de 8 bits:
- 4 registradores: R0, R1, R2, R3
- memória com 16 posições
- PC (Program Counter)
- ULA
- instruções LOAD, STORE, ADD, SUB, AND, OR, XOR, JMP e HALT

Código com todas as funções implementadas
"""

from ula import ula, limitar_8bits


class CPU:

    def __init__(self):
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        # 16 posições de memória
        self.memoria = [0] * 16

        # Program Counter
        self.pc = 0

        # Estado da CPU
        self.halted = False

    def executar_instrucao(self, instrucao):

        # Exemplo:
        # "LOAD R0, 5"
        # "ADD R0, R1"
        # "JMP 4"

        # Se a instrução na memória for um inteiro(posição vazia/não inicializada), evita erro

        if not isinstance(instrucao, str):
            raise ValueError(f"Instrução inválida ou vazia no endereço PC={self.pc}: {instrucao}")

        partes = instrucao.replace(",", "").split()

        operacao = partes[0]

        # ==============================================
        # LOAD — IMPLEMENTADO
        # ==============================================
        # LOAD R0, 5
        # R0 <- 5

        if operacao == "LOAD":

            registrador = partes[1]
            valor = int(partes[2])

            self.registradores[registrador] = limitar_8bits(valor)

            self.pc += 1

        # ==============================================
        # STORE — IMPLEMENTADO
        # ==============================================
        # STORE R0, 15
        # MEM[15] <- R0

        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])

            valor = self.registradores[registrador]

            self.memoria[endereco] = valor

            self.pc += 1

            # IMPLEMENTADO
            # pass

        # ==============================================
        # ADD — IMPLEMENTADO
        # ==============================================
        # ADD R0, R1
        # R0 <- R0 + R1

        elif operacao == "ADD":
            reg_destino = partes[1]
            reg_origem = partes[2]

            val_a = self.registradores[reg_destino]
            val_b = self.registradores[reg_origem]

            self.registradores[reg_destino] = ula("ADD", val_a, val_b)

            self.pc += 1

            # IMPLEMENTADO

        # ==============================================
        # SUB — IMPLEMENTADO
        # ==============================================

        elif operacao == "SUB":
            reg_destino = partes[1]
            reg_origem = partes[2]

            val_a = self.registradores[reg_destino]
            val_b = self.registradores[reg_origem]

            self.registradores[reg_destino] = ula("SUB", val_a, val_b)

            self.pc += 1
            # IMPLEMENTADO

        # ==============================================
        # AND — IMPLEMENTADO
        # ==============================================

        elif operacao == "AND":
            reg_destino = partes[1]
            reg_origem = partes[2]

            val_a = self.registradores[reg_destino]
            val_b = self.registradores[reg_origem]

            self.registradores[reg_destino] = ula("AND", val_a, val_b)

            self.pc += 1

            # IMPLEMENTADO

        # ==============================================
        # OR — IMPLEMENTADO
        # ==============================================

        elif operacao == "OR":
            reg_destino = partes[1]
            reg_origem = partes[2]

            val_a = self.registradores[reg_destino]
            val_b = self.registradores[reg_origem]

            self.registradores[reg_destino] = ula("OR", val_a, val_b)

            self.pc += 1

            # IMPLEMENTADO

        # ==============================================
        # XOR — IMPLEMENTADO
        # ==============================================

        elif operacao == "XOR":
            reg_destino = partes[1]
            reg_origem = partes[2]

            val_a = self.registradores[reg_destino]
            val_b = self.registradores[reg_origem]

            self.registradores[reg_destino] = ula("XOR", val_a, val_b)

            self.pc += 1

            # IMPLEMENTADO

        # ==============================================
        # JMP — IMPLEMENTADO
        # ==============================================
        # JMP 8
        # PC <- 8

        elif operacao == "JMP":

            endereco = int(partes[1])

            if endereco < 0 or endereco >= len(self.memoria):
                raise ValueError("Endereço de salto inválido")

            self.pc = endereco

        # ==============================================
        # HALT — IMPLEMENTADO
        # ==============================================

        elif operacao == "HALT":

            self.halted = True

        else:

            raise ValueError(f"Instrução desconhecida: {operacao}")

    def ciclo(self):

        if self.halted:
            return

        # ==============================================
        # FETCH
        # ==============================================

        instrucao = self.memoria[self.pc]

        print()
        print("--------------------------------")
        print("FETCH")
        print("PC:", self.pc)
        print("Instrução:", instrucao)

        # ==============================================
        # DECODE + EXECUTE
        # ==============================================

        print("DECODE + EXECUTE")

        self.executar_instrucao(instrucao)

        # ==============================================
        # ESTADO
        # ==============================================

        self.mostrar_estado()

    def executar(self, max_ciclos=100):

        ciclos = 0

        while not self.halted:

            if ciclos >= max_ciclos:
                raise RuntimeError(
                    "Número máximo de ciclos atingido. "
                    "Verifique se existe um loop infinito."
                )

            self.ciclo()
            ciclos += 1

    def mostrar_estado(self):

        print("Registradores:")

        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} ({valor})")
