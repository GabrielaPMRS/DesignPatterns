from enteties import Monster, Creeper, Zombie, Witch, Skeleton, Spider, Enderman

class SingletonMonsterFactory():
    __instance = None
    monsterCounter = 0

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def getMonster(self, monsterType):

        if self.monsterCounter >= 10:
            raise OverflowError('Número máximo de monstros atingido!')
        
        self.monsterCounter += 1

        if monsterType == 'Zombie':
            return Zombie()
        elif monsterType == 'Witch':
            return Witch()
        elif monsterType == 'Spider':
            return Spider()
        elif monsterType == 'Enderman':
            return Enderman()
        elif monsterType == 'Creeper':
            return Creeper()
        elif monsterType == 'Skeleton':
            return Skeleton()
        


def player1():
    singletonMonsterFactory = SingletonMonsterFactory()
    print(f'Factory do player1: {singletonMonsterFactory}')
    print(f'Contagem de monstros: {singletonMonsterFactory.monsterCounter}')

    # Lista gerada por lógica do jogo
    monsterToSpawn = ['Creeper', 'Enderman', 'Skeleton', 'Zombie', 'Creeper', 'Spider']
    
    monstersSpawned = []

    for monsterName in monsterToSpawn:
        try:
            monster = singletonMonsterFactory.getMonster(monsterName)
        except OverflowError:
            print('Número máximo de monstros atingido!')
            break
            
        monstersSpawned.append(monster)
        print(monster)

def player2():
    singletonMonsterFactory = SingletonMonsterFactory()
    print(f'Factory do player2: {singletonMonsterFactory}')
    print(f'Contagem de monstros: {singletonMonsterFactory.monsterCounter}')

    # Lista gerada por lógica do jogo 
    monsterToSpawn = ['Enderman', 'Creeper', 'Skeleton', 'Zombie', 'Creeper', 'Enderman', 'Skeleton']
    
    monstersSpawned = []

    for monsterName in monsterToSpawn:
        try:
            monster = singletonMonsterFactory.getMonster(monsterName)
        except OverflowError:
            print('Número máximo de monstros atingido!')
            break
            
        monstersSpawned.append(monster)
        print(monster)

    print(f'Contagem de monstros: {singletonMonsterFactory.monsterCounter}')


if __name__ == "__main__":
    player1()
    player2()

        
        





        