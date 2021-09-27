
class Genetic:
    def __init__(self, size_population=2, number_of_generations):
        self.size_population = size_population
        self.number_of_generations = number_of_generations


    def CreatePopulation(self, graph, initial, ending):
        population = []
        for i in range(self.size_population):
            individual = []
            for j in range(len(graph)):
                if j == 0:
                    individual.append(initial)

                

            population.append(individual)

    def Selection(self):


    def targetet_genetic(self, graph, initial, ending):
        CreatePopulation(graph, initial, ending)
