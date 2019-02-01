import random
from abc import dna

population=[]

for _ in range(200):
    population.append(dna())
    print(population[0].phrase)

while 1:
    for i in range(200):
        population[i].fitness()
        pool=[]
        for i in range(200):
        	n=int(population[i].f*100)
        	for _ in range(n):
        		pool.append(population[i])
        
        for i in range(200):
        	a=random.randrange(len(pool))


    print(population[i].f)
    break