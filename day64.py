class food():
    def __init__(self,name,color):
        self.name=name
        self.color =color
    def show(self):
        print(self.color)
        print(self.name)

apple = food('apple','red')
graph = food('graph','yellow')

apple.show()