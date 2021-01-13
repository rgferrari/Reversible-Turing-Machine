# Reversible Turing Machine

### Alunos: René Gargano Ferrari, Leonardo Militz, Augusto Gai Dal'Asta.

Implementação de uma Máquina de Turing Reversível para a cadeira de Teoria da Computação no curso de Ciência da Computação da UFSM.

## Execução
```bash
python3 main.py < entrada-quintupla.txt
```

## Padrão de Entrada

A entrada do algoritmo é o arquivo [entrada-quintupla.txt](https://github.com/rgferrari/Reversible-Turing-Machine/blob/main/entrada-quintupla.txt). A primeira linha apresenta números, que indicam: número de estados, número de símbolos no alfabeto de entrada, número de símbolos no alfabeto da fita e número de transições, respectivamente. A seguir, temos os estados, na próxima linha alfabeto de entrada e logo alfabeto da fita. Nas linhas sequentes temos as funções de transição. Depois das funções de transição, segue uma entrada.

## Output

O output do programa para a [entrada-quintupla.txt](https://github.com/rgferrari/Reversible-Turing-Machine/blob/main/entrada-quintupla.txt) é o seguinte:

```bash
Computing...
Input Tape                       History Tape
['0', '0', '1', '1', 'B']        [0]
['$', '0', '1', '1', 'B']        [0, 3]
['$', '0', '1', '1', 'B']        [0, 3, 5]
['$', '0', 'X', '1', 'B']        [0, 3, 5, 9]
['$', '0', 'X', '1', 'B']        [0, 3, 5, 9, 12]
['$', '0', 'X', '1', 'B']        [0, 3, 5, 9, 12, 14]
['$', 'X', 'X', '1', 'B']        [0, 3, 5, 9, 12, 14, 4]
['$', 'X', 'X', '1', 'B']        [0, 3, 5, 9, 12, 14, 4, 5]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13, 13]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13, 13, 13]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13, 13, 13, 16]
Copying from input to output...
Retracing...
Input Tape                       History Tape
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13, 13, 13, 16]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13, 13, 13]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13, 13]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12, 13]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11, 12]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11, 11]
['$', 'X', 'X', 'X', 'B']        [0, 3, 5, 9, 12, 14, 4, 5, 11]
['$', 'X', 'X', '1', 'B']        [0, 3, 5, 9, 12, 14, 4, 5]
['$', 'X', 'X', '1', 'B']        [0, 3, 5, 9, 12, 14, 4]
['$', '0', 'X', '1', 'B']        [0, 3, 5, 9, 12, 14]
['$', '0', 'X', '1', 'B']        [0, 3, 5, 9, 12]
['$', '0', 'X', '1', 'B']        [0, 3, 5, 9]
['$', '0', '1', '1', 'B']        [0, 3, 5]
['$', '0', '1', '1', 'B']        [0, 3]
['0', '0', '1', '1', 'B']        [0]
Input:  ['0', '0', '1', '1', 'B']
History:  []
Output:  ['$', 'X', 'X', 'X', 'B']
```
