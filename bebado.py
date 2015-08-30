import random
import collections

print "O Bebado e o Equilibrista..."

M=100000
MAX_PASSOS = 10
passo = ['F', 'T']
resultado = {}

p = 0.5

print passo

def caminhar():
  origem = 0
  passos = []
  for i in range(MAX_PASSOS):
    trupicada = passo[0] if random.random() < p else passo[1]
    if trupicada == 'F':
      origem += 1
    else:
      origem += -1
    passos.append(trupicada)

  if resultado.get(origem) == None: 
    resultado[origem] = 0

  resultado[origem] += 1

  # print origem
  # print passos

for i in range(M):
  caminhar()

total = 0
for k in sorted(resultado.keys()):
  result =  resultado[k] / float(M)
  print str(k) + " : " + str(result*100) + "%"
  total += result

print "Total = " + str(total)

# TODO save results in a map with the result count and plot the results

