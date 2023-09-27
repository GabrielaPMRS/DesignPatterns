
class Monster():
    def __init__(self, hp = 100, attack = 10, defence = 10):
        self.hp = hp
        self.attack = attack
        self.defence = defence

    def ToWalk(self):
        pass

    def ToAttack(self):
        pass

    def ToDefend(self):
        pass

    def SetAgrassiveState():
        pass


class Zombie(Monster):
    def GroaningSound(self):
        pass

    def AttackingTurtles(self):
        pass

    def BurningUnderDaylight(self):
        pass

    def BecomingDrowned(self):
        pass


class Witch(Monster):
    def ThrowingPoison():
        pass

    def SelfHealing():
        pass


class Spider(Monster):
    def WallClimb():
        pass

    def Pounce():
        pass

    def SetAgrassiveState():
        # Agrassive at night
        pass


class Enderman(Monster):
    def SetAgrassiveState():
        # When makes eye contact
        pass

    def Flee():
        # When in contact with water
        pass

    def Teleportation():
        pass

    def MovingBlocks():
        pass
    

class Creeper(Monster):
    def Explodes():
        pass

    def ChargedItself():
        # When stroke by a lighting
        pass


class Skeleton(Monster):
    def Flee():
        # When a player approaches
        pass

    def ToAttack():
        # With an bow
        pass

