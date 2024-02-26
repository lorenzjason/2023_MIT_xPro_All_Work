class codeFile:
    def __init__(self, serial, monument, rotationAngle, gridGround, comments, calcAcreage, createDate, killDate, deedAcreage, tielegs, geomlines):
        self.serial = serial
        self.monument = monument
        self.rotationAngle = rotationAngle
        self.gridGround = gridGround
        self.comments = comments
        self.calcAcreage = calcAcreage
        self.createDate = createDate
        self.killDate = killDate
        self.deedAcreage = deedAcreage
        self.tielegs = tielegs
        self.geomlines = geomlines

    def acreageDiff(self):
        acrDiff = self.calcAcreage - self.deedAcreage
        return acrDiff

    def printCodeFile(self):
        printstr = ''
        printstr += "S " + str(self.serial) + '\n'
        printstr += "C " + self.comments[0] + '\n'
        printstr += "P " + str(self.monument) + '\n'
        printstr += "C " + self.comments[1] + '\n'
        printstr += 'R ' + str(self.rotationAngle) + '\n'
        printstr += 'G ' + str(self.gridGround) + '\n'
        for tie in self.tielegs:
            printstr += tie + '\n'
        for geom in self.geomlines:
            printstr += geom + '\n'
        printstr += 'DC ' + str(self.calcAcreage) + '\n'
        printstr += 'DD ' + str(self.deedAcreage) + '\n'

        return printstr
            
comments = ['WARRANTY DEED', 'SOUTH QUARTER CORNER OF SECTION 15']
tielegs = ['T N00-00-00E 45.03', 'T N90-00-00W 3C']
geomlines = ['B N90-00-00WE 90', 'B N90-00-00E 90' , 'F CR R 10 D 90', 'B N90-00-00W 90', 'B N00-00-00E 100']

cf = codeFile(180510008, 1502, .98997, 1, comments, 2.4, '11/27/02', '11/31/50', 2.56, tielegs, geomlines)

print(cf.printCodeFile())
print(cf.acreageDiff())

