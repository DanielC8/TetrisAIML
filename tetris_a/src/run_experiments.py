from genetic2 import Genetic_AI
from game import Game

from multiprocessing import Pool
import random
import numpy as np
import pickle
import joblib



def run(model):
        game = Game("student", model)
        drops, clears = game.run_no_visual()
        return clears

    
    
def children(parent1, parent2):
    #setting child as one genotype and then randomly selecting items of the other to form child
    child = parent1.genotype
    for i in range(len(parent1.genotype)):
        if random.randint(0, 1) == 1:
            child[i] = parent2.genotype[i]

    return Genetic_AI(genotype=np.array(child), mutate=True)





def main():
    popsize = 100
    generations = 100

    population = []
    for i in range(popsize):
        population.append(Genetic_AI())

    
    bestscore = 0
    bestgen = 0
    bestchild = 0
    bestchildgen = 0
    bestscoregen = 0   
    with Pool(30) as pool:
        for gen in range(generations):
            scores = pool.map(run, population)
            scoreslist = []
            for i, score in enumerate(scores):
                scoreslist.append((score,i))
            scoresort = sorted(scoreslist, key=lambda x: x[0], reverse=True)

            survivors = []
            for a, b in scoresort[:int(0.3*popsize)]:
                survivors.append(population[b]
            

            bestrn, childID = scoresort[0][0], scoresort[0][1]

            if bestrn > bestscore:
                bestscore = bestrn
                bestgen = gen+1
                bestchild = childID
                bestchildgen = population[int(childID)]
                bestscoregen = bestrn


            bestscore = 0
            joblib.dump(bestchildgen, f'genes/test2/g{bestgen}.joblib')
            with open(f'genes/test2/log.txt', 'a') as f:
                f.write(f'Generation: {bestgen}, Child: {bestchild}, Score: {bestscoregen}\n')
                
            
            newpop = []
            counts = 0
            while counts < popsize:
                parent1 = random.choice(survivors)
                parent2 = random.choice(survivors)
                child = children(parent1, parent2)
                if child is not None:
                    newpop.append(child)
                    counts += 1

            population = newpop

        joblib.dump(population[int(childID)], 'genes/test2f.joblib')

    print('Done')

if __name__ == '__main__':
    main()
