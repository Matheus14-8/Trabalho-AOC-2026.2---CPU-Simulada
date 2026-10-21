"""
MAIN — Execução Completa da CPU Simulada
AOC 2026.2

Programa main utilizando todas as instruções:
LOAD, STORE, ADD, SUB, AND, OR, XOR, JMP e HALT.
"""

from cpu import CPU


cpu = CPU()

# ==========================================
# PROGRAMA DE TESTE COMPLETO (Todas as instruções)
# ==========================================
# Mapeamento da Memória:
# [00] LOAD R0, 12   (R0 = 12 -> Binário: 1100)
# [01] LOAD R1, 10   (R1 = 10 -> Binário: 1010)
# [02] ADD R0, R1    (R0 = 12 + 10 = 22)
# [03] SUB R0, R1    (R0 = 22 - 10 = 12)
# [04] AND R0, R1    (R0 = 12 & 10 = 8  -> Binário: 1000)
# [05] JMP 7         (Pula a linha 6)
# [06] LOAD R2, 99   (Linha ignorada pelo JMP)
# [07] LOAD R2, 5    (R2 = 5)
# [08] OR R2, R1     (R2 = 5 | 10 = 15  -> Binário: 1111)
# [09] XOR R2, R0    (R2 = 15 ^ 8 = 7   -> Binário: 0111)
# [10] STORE R0, 14  (Grava R0 [8] na posição 14 da memória)
# [11] STORE R2, 15  (Grava R2 [7] na posição 15 da memória)
# [12] HALT          (Encerra a execução)

cpu.memoria[0] = "LOAD R0, 12"
cpu.memoria[1] = "LOAD R1, 10"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "SUB R0, R1"
cpu.memoria[4] = "AND R0, R1"
cpu.memoria[5] = "JMP 7"
cpu.memoria[6] = "LOAD R2, 99"
cpu.memoria[7] = "LOAD R2, 5"
cpu.memoria[8] = "OR R2, R1"
cpu.memoria[9] = "XOR R2, R0"
cpu.memoria[10] = "STORE R0, 14"
cpu.memoria[11] = "STORE R2, 15"
cpu.memoria[12] = "HALT"


print("======================================")
print("       CPU SIMULADA — 8 BITS          ")
print("======================================")

cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")

cpu.mostrar_estado()
print(f"Memória[14] (R0 final): {cpu.memoria[14]}")
print(f"Memória[15] (R2 final): {cpu.memoria[15]}")