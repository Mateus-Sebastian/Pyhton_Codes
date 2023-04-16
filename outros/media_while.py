soma = 0
quantidadenotas = int(input('Quantas notas a serem calculadas?\n'))
i = 1

while i <= quantidadenotas:
    nota = float(input('Digite a nota %.0f: '%i))
    soma += nota
    i += 1

print("\nA média das notas é %.1f"%(soma / quantidadenotas))