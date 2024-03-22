class paper:

    def __init__(self):
        self.author = None
        self.title = None
        self.references = 0
        self.isPlagiarised = False
        self.price = 0
        self.priceCurrency = None

    def changeAuthor(self, newAuthor: str):
        self.author = newAuthor

    def changeTitle(self, newTitle: str):
        self.title = newTitle

    def addReference(self):
        self.references += 1

    def removeReference(self):
        if (self.references == 0):
            return
        self.references -= 1

    def markAsPlagiarised(self):
        self.isPlagiarised = True

    def changePrice(self, newPrice: float, newCurrency: str):
        self.price = newPrice
        self.priceCurrency = newCurrency
