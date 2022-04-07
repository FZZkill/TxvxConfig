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
        new = [] 
        FileType.close()
        for i in range(len(self.ListItems)-1) :
            if self.ListItems[i][0] != '#':
                new.append(self.ListItems[i])
        
        for i in range(len(new)-1):
            new[i] = new[i].replace("\n","")
        
        for x in new :
            b = x.split('=', 1)
            self.ListItemsRun.append(b)
        self.Type += 1

    def add(self, Item, vaule):
        add = []
        add [0] = Item
        add [1] = vaule
        self.new(add)

    def remove(self, Item) :
        for x in range(len(self.ListItemsRun)-1):
            if self.ListItemsRun[x][0]== Item:
                self.ListItemsRun.pop(x)
                return x

    def create(self) :
        self.FileType = open(self.Path, "w")

    def set(self, Item, vaule):
        for x in self.ListItemsRun:
            if x[0] == Item:
                x[1] = vaule

    def save(self):
        self.Type +=1
        # Code to save
        SaveObject = ""
        for x in self.ListItemsRun:
            SaveObject = SaveObject + x[0] + "=" + x[1] + "\n"
        self.FileType = open(self.Path, "w")
        self.Type -=1
        self.FileType.write(SaveObject)
        self.FileType.close()

    def show(self) :
        return self.ListItemsRun

    def get(self, Item):
        for x in self.ListItemsRun:
            if x[0] == Item:
                return x[1]

    def showType(self):
        return self.Type

    def new(self,Lists, Type=2):
        if Type == 2:
            self.ListItemsRun.append(Lists)
        else:
            self.ListItemsRun = Lists

    def search(self,Item):
        for x in range((self.ListItemsRun)-1):
            if self.ListItemsRun[x][0] == Item:
                return x
        return False
