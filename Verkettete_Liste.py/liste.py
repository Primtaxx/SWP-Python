class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None
        
    def setNextElem(self, nextElem):
        self.nextElem = nextElem
        
    def getNextElem(self):
        return self.nextElem
    
    def getObj(self):
        return self.obj

class EinfachVerketteteListe:
    def __init__(self):
        self.startElem = ListElement("Kopf")
    
    def getFirstElem(self):
        return self.startElem
    
    def getLastElem(self):
        start = self.startElem
        while start.getNextElem() is not None:
            start = start.getNextElem()
        return start

    def addLast(self, element):
        newElem = ListElement(element)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)

    def writeList(self):
        write = self.startElem
        while write is not None:
            print(write.getObj())
            write = write.getNextElem()

if __name__ == '__main__':
    list = EinfachVerketteteListe()
    list.addLast("1")
    list.addLast("2")
    list.addLast("3")
    list.addLast("4")
    list.addLast("5")
    list.writeList()
