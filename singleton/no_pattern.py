from enteties import Monster, Creeper, Zombie, Witch, Skeleton, Spider, Enderman

class MonsterFactory():
    monsterCounter = 0
    
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
    monsterFactory = MonsterFactory()
    print(f'Factory do player1: {monsterFactory}')
    print(f'Contagem de monstros: {monsterFactory.monsterCounter}')

    # Lista gerada por lógica do jogo
    monsterToSpawn = ['Creeper', 'Enderman', 'Skeleton', 'Zombie', 'Creeper', 'Spider']
    
    monstersSpawned = []

    for monsterName in monsterToSpawn:
        try:
            monster = monsterFactory.getMonster(monsterName)
        except OverflowError:
            print('Número máximo de monstros atingido!')
            break
            
        monstersSpawned.append(monster)
        print(monster)

    print(f'Contagem de monstros: {monsterFactory.monsterCounter}')

def player2():
    monsterFactory = MonsterFactory()
    print(f'Factory do player2: {monsterFactory}')
    print(f'Contagem de monstros: {monsterFactory.monsterCounter}')

    # Lista gerada por lógica do jogo 
    monsterToSpawn = ['Enderman', 'Creeper', 'Skeleton', 'Zombie', 'Creeper', 'Enderman', 'Skeleton']
    
    monstersSpawned = []

    for monsterName in monsterToSpawn:
        try:
            monster = monsterFactory.getMonster(monsterName)
        except OverflowError:
            print('Numero máximo de monstros atingido!')
            break
            
        monstersSpawned.append(monster)
        print(monster)

    print(f'Contagem de monstros: {monsterFactory.monsterCounter}')


if __name__ == "__main__":
    player1()
    player2()

        
        





        