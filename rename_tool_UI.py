from maya import cmds

class rename_tool(object):

    #constructor
    def __init__(self):

        self.window = "rename_tool"
        self.title = "Rename Tool"
        winWidth = 600
        winHeight = 250

        # close old window if open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)

        #create new window
        self.window = cmds.window(self.window, title=self.title, width=winWidth, height=winHeight)

################################################################### UI LAYOUT

        mainCL = cmds.columnLayout()

        #TITLE
        cmds.setParent(mainCL)
        cmds.separator(h=10, w=winWidth)
        TitleRowWidth = [200, 200, 200]
        cmds.rowLayout(numberOfColumns=3, columnWidth3=TitleRowWidth)
        cmds.text(label="", w=TitleRowWidth[0])
        cmds.text(self.title, h=30, font="boldLabelFont", w=TitleRowWidth[1])
        cmds.text(label="", w=TitleRowWidth[2])

        cmds.setParent("..")
        
        cmds.separator(h=10, w=winWidth)

###################################################################
        #DEFINE TARGET ELEMENT(S) + QUICK SELECT (POSITION: UPPER MIDDLE)

        cmds.setParent(mainCL)

        cmds.text(label="Select target element(s)", w=winWidth)
        cmds.separator(h=10, w=winWidth)

        cmds.text(label="Quick selection:", w=winWidth, align="left")

        But1RowWidth = [125, 150, 50, 150, 125]
        cmds.rowLayout(numberOfColumns=5, columnWidth5=But1RowWidth)
        cmds.text(label="", w=But1RowWidth[0])
        self.SelHi = cmds.button(label="select hierarchy", w=But1RowWidth[1], command=self.SelHi)
        cmds.text(label="", w=But1RowWidth[2])
        self.SelJnt = cmds.button(label="select only joints", w=But1RowWidth[3], command=self.SelJnt)
        cmds.text(label="", w=But1RowWidth[4])

        cmds.setParent("..")

        But2RowWidth = [125, 150, 50, 150, 125]
        cmds.rowLayout(numberOfColumns=5, columnWidth5=But2RowWidth)
        cmds.text(label="", w=But2RowWidth[0])
        self.SelCrv = cmds.button(label="select only curves", w=But2RowWidth[1], command=self.SelCrv)
        cmds.text(label="", w=But2RowWidth[2])
        self.SelMesh = cmds.button(label="select only mesh", w=But2RowWidth[3], command=self.SelMesh)
        cmds.text(label="", w=But2RowWidth[4])

        self.SelTar = cmds.ls(sl=True)

        cmds.setParent("..")

        cmds.text(label="", h=5)
        cmds.separator(h=10, w=winWidth)
        
        cmds.setParent("..")        

################################################################### UI LAYOUT

        mainRLWidth = [300, 300]
        mainRL = cmds.rowLayout(w=winWidth, numberOfColumns=2, columnWidth2=mainRLWidth, rowAttach=(2, "both", 0))

################################################################### UI LAYOUT
        #ADD PREFIX OR SUFFIX (POSITION: LOWER LEFT)
        
        cmds.setParent(mainRL)
        cmds.columnLayout(w=mainRLWidth[0])

        cmds.text(label="Suffix and Prefix")
        cmds.separator(h=10, w=winWidth*0.5)
        cmds.text(label="", h=5)

        TextRowWidth = [90, 200]
        self.FixName = cmds.textFieldGrp(label="Name:", columnWidth=(2, 150), columnWidth2=TextRowWidth)
        cmds.text(label="", h=5)

        PreSufRowWidth = [110, 75, 110]
        cmds.rowLayout(numberOfColumns=3, columnWidth3=PreSufRowWidth)
        self.Pre = cmds.button(label="add as Prefix", command=self.Pre, w=PreSufRowWidth[0])
        cmds.text(label="", w=PreSufRowWidth[1])
        self.Suf = cmds.button(label="add as Suffix", command=self.Suf, w=PreSufRowWidth[2])

        cmds.setParent("..")

        cmds.text(label="", h=5)

        cmds.separator(h=10,w=winWidth*0.5)

        cmds.text(label="Quick sides:")
        cmds.text(label="", h=5)
        UpSideRowWidth = [150, 150]
        cmds.rowLayout(numberOfColumns=2, columnWidth2=UpSideRowWidth)
        self.LPre = cmds.button(label="Left Prefix", command=self.LPre, align="center", w=UpSideRowWidth[0])
        self.RPre = cmds.button(label="Right Prefix", command=self.RPre, align="center", w=UpSideRowWidth[1])
        
        cmds.setParent("..")

        LowSideRowWidth = [150, 150]
        cmds.rowLayout(numberOfColumns=2, columnWidth2=LowSideRowWidth)
        self.LSuf = cmds.button(label="Left Suffix", command=self.LSuf, align="center", w=LowSideRowWidth[0])
        self.RSuf = cmds.button(label="Right Suffix", command=self.RSuf, align="center", w=LowSideRowWidth[1])
        cmds.setParent("..")

        cmds.separator(h=10,w=winWidth*0.5)

        cmds.text(label="Quick suffix (type):")
        cmds.text(label="", h=5)
        UpSufRowWidth = [150, 150]
        cmds.rowLayout(numberOfColumns=2, columnWidth2=UpSufRowWidth)
        self.JntSuf = cmds.button(label="_JNT", command=self.JntSuf, align="center", w=UpSufRowWidth[0])
        self.CtrlSuf = cmds.button(label="_CTRL", command=self.CtrlSuf, align="center", w=UpSufRowWidth[1])
        
        cmds.setParent("..")

        LowSufRowWidth = [150, 150]
        cmds.rowLayout(numberOfColumns=2, columnWidth2=LowSufRowWidth)
        self.CrvSuf = cmds.button(label="_CRV", command=self.CrvSuf, align="center", w=LowSufRowWidth[0])
        self.GrpSuf = cmds.button(label="_GRP", command=self.GrpSuf, align="center", w=LowSufRowWidth[1])
        cmds.setParent("..")

###################################################################
        #RENAME & ORDER (POSITION: LOWER RIGHT)

        cmds.setParent(mainRL)
        cmds.columnLayout(w=mainRLWidth[1])

        cmds.text(label="Rename")
        cmds.separator(h=10, w=winWidth*0.5)
        cmds.text(label="", h=5)
        
        TextRowWidth = [90, 200]
        self.new_name = cmds.textFieldGrp(label="New name:", columnWidth=(2, 150), columnWidth2=TextRowWidth)
        cmds.text(label="", h=7)

        OptionRowWidth = [90, 200, 10]
        self.order = cmds.optionMenuGrp(label="Sort in", columnWidth=(2, 120), extraLabel="order", columnWidth3=OptionRowWidth)
        cmds.menuItem(label="-")
        cmds.menuItem(label="Numeric_0")
        cmds.menuItem(label="Numeric_1")
        cmds.menuItem(label="Alphabetic_UPPER")
        cmds.menuItem(label="Alphabetic_lower")

        cmds.text(label="", h=7)
        cmds.separator(h=10, w=winWidth*0.5)
        #cmds.text(label="*Skip if there's only 1 selection")

        new_name=self.new_name
        order=self.order
                
        def CheckName (*arg):

                check_new_name = cmds.textFieldGrp(new_name, query=True, text=True)
                check_order = cmds.optionMenuGrp(order, query=True, value=True)

                if check_order == "-":
                        check_text = str(check_new_name)
                if check_order == "Numeric_0":
                        check_text = str(check_new_name + "_0")
                if check_order == "Numeric_1":
                        check_text = str(check_new_name + "_1")
                if check_order == "Alphabetic_UPPER":
                        check_text = str(check_new_name + "_A")
                if check_order == "Alphabetic_lower":
                        check_text = str(check_new_name + "_a")
                
                cmds.text("___________________________", label=check_text, edit=True, font="boldLabelFont")

        cmds.text(label="Check:")

        cmds.text(label="Ex. New name would be:", w=winWidth*0.5)
        
        cmds.text(label="")

        CheckTxtWidth = [25, 250, 25]
        cmds.rowLayout(numberOfColumns=3, columnWidth3=CheckTxtWidth)
        cmds.text(label="", w=CheckTxtWidth[0])
        cmds.text("___________________________", font="boldLabelFont", w=CheckTxtWidth[1])
        cmds.text(label="", w=CheckTxtWidth[2])
        cmds.setParent("..")

        cmds.text(label="")
        
        CheckRowWidth = [120, 60, 120]
        cmds.rowLayout(numberOfColumns=3, columnWidth3=CheckRowWidth)
        cmds.text(label="", w=CheckRowWidth[0])
        cmds.button(label="Check", command=CheckName, w=CheckRowWidth[1])
        cmds.text(label="", w=CheckRowWidth[2])
        cmds.setParent("..")

        cmds.text(label="", h=5)
        cmds.separator(h=10, w=winWidth*0.5)
        cmds.text(label="", h=4)

        self.Rename = cmds.button(label="Rename", command=self.Rename, w=winWidth*0.5)

        cmds.setParent("..")

################################################################### UI CONTENT

        #display new window
        cmds.showWindow()

################################################################### SELECTION

    def SelHi(self, *arg):

        self.SelTar = cmds.ls(sl=True)
        cmds.select(self.SelTar, hi=True)


    def SelJnt(self, *arg):

        self.SelTar = cmds.ls(sl=True)
        cmds.select(self.SelTar, hi=True)
        target = cmds.ls (sl=True, type="joint")
        cmds.select(target)
        

    def SelCrv(self, *arg):

        self.SelTar = cmds.ls(sl=True)
        cmds.select(self.SelTar, hi=True)
        target = cmds.ls (sl=True, type="nurbsCurve")
        cmds.select(cmds.listRelatives(target, p=True))        

    def SelMesh(self, *arg):

        self.SelTar = cmds.ls(sl=True)
        cmds.select(self.SelTar, hi=True)
        target = cmds.ls (sl=True, type="mesh")
        cmds.select(cmds.listRelatives(target, p=True))        

################################################################### CUSTOMIZED Prefix Suffix

    def Pre(self, *arg):
        FixName = cmds.textFieldGrp(self.FixName, query=True, text=True)

        names = cmds.ls (sl=True, excludeType="transform")
        
        for name in names:
                cmds.rename(name, "{0}_{1}".format(FixName, name))


    def Suf(self, *arg):
        FixName = cmds.textFieldGrp(self.FixName, query=True, text=True)

        names = cmds.ls (sl=True, excludeType="transform")

        for name in names:
                cmds.rename(name, "{0}_{1}".format(name, FixName))

################################################################### L & R Sides' Prefix Suffix

    def LPre (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format("L", name))

    def LSuf (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format(name, "L"))

    def RPre (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format("R", name))

    def RSuf (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format(name, "R"))

################################################################### TYPES' Prefix Suffix

    def JntSuf (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format(name, "JNT"))

    def CtrlSuf (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format(name, "CTRL"))

    def CrvSuf (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format(name, "CRV"))

    def GrpSuf (self, *arg):
        
        targets = cmds.ls (sl=True, excludeType="transform")
        for name in targets:
                cmds.rename(name, "{0}_{1}".format(name, "GRP"))

################################################################### RENAME
    
    def Rename (self, *arg):

        new_name = cmds.textFieldGrp(self.new_name, query=True, text=True)
        order = cmds.optionMenuGrp(self.order, query=True, value=True)
        
        targets = cmds.ls (sl=True, excludeType="transform")
        length=len(targets)

        #CREATING & ORGANIZING LISTS

        Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        NullList = []
        NumericList_0 = []
        NumericList_1 = []
        AlphabeticList = []
        AlphabeticSecondList = []
        AlphabetsLow = []
        
        def CreateNullList(length):
                a=0
                while a<length:
                        a+=1
                        NullList.append("-")

        def CreateNumList_0(length):
                a=0
                while a<length:
                        a+=1
                        NumericList_0.append(a-1)
        
        def CreateNumList_1(length):
                a=0
                while a<length:
                        a+=1
                        NumericList_1.append(a)

        def Single(length):
                i = 0
                while i < length:
                        Letter=Alphabets[i]
                        i+=1
                        AlphabeticList.append(Letter)

        def Double(length):
                f=0
                s=0
                while f<int(length//26) :
                        Letter_First=Alphabets[f]
                        Letter_Second=Alphabets[s]
                        AlphabeticSecondList.append("{0}{1}".format(Letter_First,Letter_Second))
                        s+=1
                        if s==26 and f<int(length/26):
                                f+=1
                                s-=26
                del AlphabeticSecondList[length-26:]

        def CreateAlphabetList(length):
                f_count = length//26
                s_count = length%26
                if f_count <1:
                        Single(s_count)

                if 1 <= f_count <= 26:
                        Single(26)
                        Double(length)
                        AlphabeticList.extend(AlphabeticSecondList)

        if order == "-":
                CreateNullList(length)
                chosen_order = NullList
        if order == "Numeric_0":
                CreateNumList_0(length)
                chosen_order = NumericList_0
        if order == "Numeric_1":
                CreateNumList_1(length)
                chosen_order = NumericList_1
        if order == "Alphabetic_UPPER":
                CreateAlphabetList(length)
                chosen_order = AlphabeticList
        if order == "Alphabetic_lower":
                CreateAlphabetList(length)
                for x in AlphabeticList:
                        AlphabetsLow.append(x.lower())
                chosen_order = AlphabetsLow

        for tar, i in zip(targets, chosen_order):
                if order =="-":
                        cmds.rename(tar, new_name)
                else:
                        cmds.rename(tar, "{0}_{1}".format(new_name, i))


#IN Maya
rename_tool_UI.rename_tool()
