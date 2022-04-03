class run():
    # Objects
    Path = ""
    Type = 0
    FileType = ""
    ListItems = []    
    ListItemsRun = []

    def __init__(self, FilePath):
        self.Path = FilePath
        self.Type = 1
        # Open file
        FileType = open(self.Path, "r")
        self.ListItems=FileType.readlines()
        # is '=' to do kill for
        for x in self.ListItems :
            b = x.split('=', 1)
            self.ListItemsRun.append(b)
            
    def add(self, Item, vaule):
        add = []
        add [0] = Item
        add [1] = vaule
        self.ListItemsRun.append[add]

    def remove(self, Item) :
        a = 0
        for x in self.ListItemsRun:
            a+=1
            if x[1] == Item:
                self.ListItemsRun.remove(a)
                return x

    def create(self) :
        pass
    
    def set(self, Item, vaule):
        pass
    
    def save(self):
        pass
    
    def show(self):
        return ListItemsRun

    def get(self, Item):
        for x in self.ListItemsRun:
            if x[0] == Item:
                return x[1]

    def showType(self):
        return self.Type
