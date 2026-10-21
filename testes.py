"""
TESTES AMPLIADOS
AOC 2026.2

Os testes abaixo verificam todas as partes no código-base: LOAD, JMP e HALT.
Além disso, as implementadas: STORE, ADD, SUB, AND, OR, XOR.

"""

from cpu import CPU


def teste_load():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 25"
    cpu.memoria[1] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 25

    print("[OK] LOAD")


def teste_jmp():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 10"
    cpu.memoria[1] = "JMP 4"
    cpu.memoria[2] = "LOAD R0, 99"
    cpu.memoria[3] = "HALT"
    cpu.memoria[4] = "LOAD R1, 20"
    cpu.memoria[5] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 10
    assert cpu.registradores["R1"] == 20

    print("[OK] JMP")


def teste_halt():
    cpu = CPU()

    cpu.memoria[0] = "HALT"

    cpu.executar()

    assert cpu.halted is True

    print("[OK] HALT")


def teste_store():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 42"
    cpu.memoria[1] = "STORE R0, 15"
    cpu.memoria[2] = "HALT"

    cpu.executar()

    print("[OK] STORE")


def teste_add():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 13

    print("[OK] ADD")


def teste_sub():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 20"
    cpu.memoria[1] = "LOAD R1, 7"
    cpu.memoria[2] = "SUB R0, R1"
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 13

    print("[OK] SUB")


def teste_and():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 12"  # Binário: 1100
    cpu.memoria[1] = "LOAD R1, 10"  # Binário: 1010
    cpu.memoria[2] = "AND R0, R1"  # Binário: 1000 (8)
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 8

    print("[OK] AND")


def teste_or():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 12"  # Binário: 1100
    cpu.memoria[1] = "LOAD R1, 10"  # Binário: 1010
    cpu.memoria[2] = "OR R0, R1"  # Binário: 1110 (14)
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 14

    print("[OK] OR")


def teste_xor():
    cpu = CPU()

    cpu.memoria[0] = "LOAD R0, 12"  # Binário: 1100
    cpu.memoria[1] = "LOAD R1, 10"  # Binário: 1010
    cpu.memoria[2] = "XOR R0, R1"  # Binário: 0110 (6)
    cpu.memoria[3] = "HALT"

    cpu.executar()

    assert cpu.registradores["R0"] == 6

    print("[OK] XOR")


if __name__ == "__main__":
    print("Executando testes-base...")
    print()

    teste_load()
    teste_store()
    teste_add()
    teste_sub()
    teste_and()
    teste_or()
    teste_xor()
    teste_jmp()
    teste_halt()

    print()
    print("Todos os testes-base foram aprovados.")
