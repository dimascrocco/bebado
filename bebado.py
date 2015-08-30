import random
import collections

print "Bebado..."

MAX_PASSOS = 10
passo = ['F', 'T']
origem = 0

p = 0.5

print passo



for i in range(MAX_PASSOS):
  trupicada = passo[0] if random.random() < p else passo[1]
  if trupicada == 'F':
    origem += 1
  else:
    origem += -1

print origem

// TODO save results in a map with the result count and plot the results

