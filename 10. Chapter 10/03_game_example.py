class Remote():
    pass
class Player():
    def moveRight(self):
        pass
    def moveleft(self):
        pass
    def moveup(self):
        pass

remote1= Remote()   # here class is made object (object instantiation)
player1= Player()
if (remote1.isLeftPressed()):
    player1.moveleft()

