# CPU Simulada - Código final
## AOC - 2026.2

### 1. Objetivo

Este pacote contém o código completo para o projeto de CPU Simulada.

A CPU possui: 
- dados de 8 bits;
- quatro registradores: R0, R1, R2 e R3;
- memória com 16 posições;
- PC (Program Counter);
- ULA;
- ciclo Fetch → Decode → Execute.

### 2. Arquivos

- `ula.py` — ULA e operações aritméticas/lógicas.
- `cpu.py` — estrutura principal da CPU.
- `main.py` — programa de demonstração.
- `testes.py` — testes das partes implementadas.

### 3. O que está implementado

No código, estão implementados:

- registradores;
- memória;
- PC;
- limitação para 8 bits;
- `LOAD`;
- `STORE`;
- `ADD`;
- `SUB`;
- `AND`;
- `OR`;
- `XOR`;
- `JMP`;
- `HALT`;
- estrutura do ciclo Fetch → Decode → Execute.

### 5. Como executar

No terminal, dentro da pasta:

```bash
python main.py
```

Para executar os testes:

```bash
python testes.py
```

### 6. Exemplo

O `main.py` contém:

```text
0: LOAD R0, 12
1: LOAD R1, 10
2: ADD R0, R1
3: SUB R0, R1
4: AND R0, R1
5: JMP 7
6: LOAD R2, 99
7: LOAD R2, 5
8: OR R2, R1
9: XOR R2, R0
10: STORE R0, 14
11: STORE R2, 15
12: HALT
```

0. A instrução `LOAD R0, 12` faz a CPU armazenar o valor 12 no registrador R0.

Portanto:

```text
R0 = 12
R1 = 0
R2 = 0
R3 = 0
```

1. A instrução `LOAD R1, 10` faz a CPU armazenar o valor 10 no registrador R1.

Portanto:

```text
R0 = 12
R1 = 10
R2 = 0
R3 = 0
```
2. A instrução `ADD R0, R1` soma os valores armazenados nos registradores R0 e R1 e os armazena o resultado em R0.

Portanto:

```text
R0 = 22
R1 = 10
R2 = 0
R3 = 0
```
3. A instrução `SUB R0, R1` subtrai o valor armazenado em R1 do valor armazenado em R0 e armazena o resultado em R0.

Portanto:

```text
R0 = 12
R1 = 10
R2 = 0
R3 = 0
```
4. A instrução `AND R0, 12` realiza a operação lógica entre os valores armazenados em R0 e R1 e armazena o resultado no registrador R0.

Portanto:

```text
R0 = 8  # Resultado de (1100 and(&) 1010) - 1000
R1 = 10
R2 = 0
R3 = 0
```
5. A instrução `JMP` faz a CPU saltar da posição 5 para a posição 7.

Portanto:

A instrução `LOAD R2, 99` não será executada.

6. A instrução `LOAD R2, 5` faz a CPU armazenar o valor 5 no registrador R2.

Portanto:

```text
R0 = 8
R1 = 10
R2 = 5
R3 = 0
```
7. A instrução `OR R2, R1` faz a CPU realizar a operação lógica OR entre os valores armazenados em R2 e R1 e armazenar o resultado em R2.

Portanto:

```text
R0 = 8
R1 = 10
R2 = 15  # Resultado de (1010 or(|) 0101) - 1111
R3 = 0
```
8. A instrução `XOR R2, R0` faz a CPU realizar a operação lógica XOR entre os valores armazenados em R2 e R0 e armazenar o resultado em R2.

Portanto:

```text
R0 = 8
R1 = 10
R2 = 7  # Resultado de (1111 xor (^) 1000) - 0111
R3 = 0
```

9. As instruções `STORE R0, 14` e `STORE R2, 15` faz a CPU armazenar os valores que estavam em R0 (8) e R2(7), nas psoições de memória 14 e 15, respectivamente.

Portanto:

```text
.
.
.
[14] = 8
[15] = 7
```

### 7. Regras

Não alterar:

- os nomes dos arquivos;
- a assinatura da função `ula()`;
- a estrutura dos registradores;
- o tamanho da memória;
- a representação de 8 bits.

O grupo pode acrescentar funções auxiliares e melhorar a visualização, desde que preserve a interface definida pelo professor.
