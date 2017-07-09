class postava:
    hp = 100

    def __init__(self, jmeno, attack):
        self.utok = attack
        self.hp = postava.hp
        self.jmeno = jmeno
    def attack(self, cil):
        cil.hp = cil.hp - self.utok
        print cil.jmeno, " HP:", cil.hp

drak = postava("Bucifal", 25)
postava.hp = 50
rytir = postava("Bajaja", 15)

while(drak.hp > 0 and rytir.hp > 0):
    drak.attack(rytir)
    rytir.attack(drak)

if rytir.hp < 1:
    print drak.jmeno, " vyhral."
elif drak.hp < 1:
    print rytir.jmeno, " vyhral."
