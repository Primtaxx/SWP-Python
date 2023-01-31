import random

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

    def addLast(self, o):
        newElem = ListElement(o)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)

    def insertAfter(self, prevItem, newItem):
        newElem = ListElement(newItem)
        pointerElem = self.startElem.getNextElem()
        
        while pointerElem != None and pointerElem.getObj() != prevItem:
            pointerElem = pointerElem.getNextElem()

        nextElem = pointerElem.getNextElem()
        pointerElem.setNextElem(newElem)
        newElem.setNextElem(nextElem)

    def delete(self, o):
        sElement = self.startElem
        
        while sElement.getNextElem() is not None and sElement.getObj() != o:
            if sElement.getNextElem().getObj() == o:
                if sElement.getNextElem().getNextElem() is not None:
                    sElement.setNextElem(sElement.getNextElem().getNextElem())
                else:
                    sElement.setNextElem(None)
                    break
            sElement = sElement.getNextElem()

    def find(self, o):
        sElement = self.startElem

        while sElement != None:
            if sElement.getObj() == o:
                return True
            sElement = sElement.nextElem
        return False

    def getFirstElem(self):
        return self.startElem

    def getLastElem(self):
        sElement = self.startElem
        while sElement.getNextElem() != None:
            sElement = sElement.getNextElem()
        return sElement
    
    def get_length(self):
        sElement = self.startElem
        count = 0

        while sElement:
            count += 1
            sElement = sElement.getNextElem()
        return count

    def writeList(self):
        sElement = self.startElem

        while sElement != None:
            print(sElement.getObj())
            sElement = sElement.getNextElem()
    

if __name__ == "__main__":
    list = EinfachVerketteteListe()
    list.addLast("2")
    list.addLast("3")
    for i in range(5):
        list.addLast(str(random.randint(10, 1000)))
    list.insertAfter("2", "neu")
    list.delete("3")
    list.writeList()
    print("erstes Element:", list.getFirstElem().getObj())
    print("ist '3' enthalten?", list.find("3"))
    print("ist '5' enthalten?", list.find("5"))
    print("letztes Element:", list.getLastElem().getObj())
    print(list.get_length()) 

