import sys,argparse

def OpenImageData2Mine():
    import csv, cv2,os

    def GetRealClsNames(ClsDescptBoxPath):
        ClsDescpts = csv.reader(open(ClsDescptBoxPath, 'r'))
        RealClsNames = {}
        for ClsDescpt in ClsDescpts:
            LabelName, ClsName = ClsDescpt[0], ClsDescpt[1]
            RealClsNames[LabelName] = ClsName
        return RealClsNames

    def GetAnnotInfos(AnnotPath):
        AnnotInfos = []
        with open(AnnotPath, 'r') as FId:
            for AnnotInfo in csv.reader(FId):
                AnnotInfos.append(AnnotInfo)
        return AnnotInfos

    ImCls = 'Truck'
    DataTypes = ('train', 'test', 'validation')
    ExpectClss = ('crane', 'forklift', ImCls.lower(), 'pickup truck', 'tractor', 'van', 'car', 'person', 'bird')
    OpenImDir = '/Users/chenchaocun/Downloads/'
    #CSVMainDir = os.path.join(OpenImDir, ImCls, 'csv_folder')
    CSVMainDir = os.path.join(OpenImDir)
    SelectDataMainDir = os.path.join(OpenImDir)
    ImMainDir = os.path.join(OpenImDir, ImCls, 'Dataset')

    ClsDescptBoxPath = os.path.join(CSVMainDir, 'class-descriptions-boxable.csv')
    RealClsNames = GetRealClsNames(ClsDescptBoxPath)

    for DataType in DataTypes:
        ClsCounter = {}
        for ExpectCls in ExpectClss:
            ClsCounter[ExpectCls] = 0
        SubDirName = DataType.capitalize()
        SelectDataSubDir = os.path.join(SelectDataMainDir, 'SelectOpenImage', SubDirName)
        if not os.path.exists(SelectDataSubDir):
            os.makedirs(SelectDataSubDir)

        AnnotName = '{}-annotations-bbox.csv'.format(DataType)
        AnnotPath = os.path.join(CSVMainDir, AnnotName)
        AnnotInfos = GetAnnotInfos(AnnotPath)
        ImDir = os.path.join(ImMainDir, DataType, ImCls)
        ImNames = os.listdir(ImDir)
        for ImName in ImNames[:]:
            ImPath = os.path.join(ImDir, ImName)
            if os.path.isfile(ImPath):
                ImPath = os.path.join(ImDir, ImName)
                Im = cv2.imread(ImPath)
                ImH, ImW, ImD = Im.shape
                CurImName, CurImExpName = os.path.splitext(ImName)
                SelectObjBoxs = {}
                ContinueFindCount = 0  # 同一张图片的标记框是连续罗列的#现在想想其实设置一个标记符号判断最简单
                for AnnotInfo in AnnotInfos:
                    if AnnotInfo[0] == CurImName:

                        xxyy = [float(AnnotInfo[4]), float(AnnotInfo[5]), float(AnnotInfo[6]), float(AnnotInfo[7])]
                        BBox = [int(xxyy[0] * ImW), int(xxyy[2] * ImH), int(xxyy[1] * ImW), int(xxyy[3] * ImH)]

                        BBoxArea = (BBox[2] - BBox[0]) * (BBox[3] - BBox[1])
                        if BBoxArea >= BBoxAreaTol:
                            LabelName = AnnotInfo[2]
                            RealClsName = RealClsNames[LabelName].lower()
                            if RealClsName in ExpectClss:
                                if RealClsName in SelectObjBoxs.keys():
                                    SelectObjBoxs[RealClsName].append(BBox)
                                else:
                                    SelectObjBoxs[RealClsName] = [BBox]
                        ContinueFindCount += 1  # 每找到一个计数一下
                        if ContinueFindCount > 50:  # 一张图片中最大有50个框（我猜想的）
                            break
            if SelectObjBoxs:
                for ExpectCls in ExpectClss:
                    if SelectObjBoxs.has_key(ExpectCls):
                        ClsCounter[ExpectCls] += 1
                        ExpectClsStr = ExpectCls + str(ClsCounter[ExpectCls]).zfill(ObjIdLen)
                        NewAnnotName = 'OpIm-{}_{}'.format(ExpectClsStr, CurImName + AnnotExpName)
                        break

                ImWHD = (ImW, ImH, ImD)
                SelectAnnotDir = os.path.join(SelectDataSubDir, ExpectCls, 'AnnotSet')
                if not os.path.exists(SelectAnnotDir):
                    os.makedirs(SelectAnnotDir)
                VOCXml2MyXml(NewAnnotName, ImName, SelectObjBoxs, SelectAnnotDir, ImWHD,
                             AnnotImFolder='OpenImage2019', CurY_M_D=Y_M_D, NotesDict={})

                SelectImDir = os.path.join(SelectDataSubDir, ExpectCls, 'ImSet')
                if not os.path.exists(SelectImDir):
                    os.makedirs(SelectImDir)
                NewImName = NewAnnotName[:-4] + ImExpName
                NewImPath = os.path.join(SelectImDir, NewImName)
                if CurImExpName == ImExpName:
                    shutil.copy(ImPath, NewImPath)
                    MsgStr = '{}--->{}\n'.format(ImPath, NewImPath)
                else:
                    cv2.imwrite(NewImPath, Im)
                    MsgStr = 'imwrite Im--->{}\n'.format(NewImPath)
                print
                MsgStr

    ImClsInfoTxtName = 'SelectOpenImage({})Info.txt'.format(SubDirName)
    ImClsInfoTxtPath = os.path.join(SelectDataSubDir, ImClsInfoTxtName)
    with open(ImClsInfoTxtPath, 'w') as FId:
        TotalImNum = 0
        for ExpectCls in ClsCounter.keys():
            TotalImNum += ClsCounter[ExpectCls]
            LineStr = '{}ImNum={}\n'.format(ExpectCls, ClsCounter[ExpectCls])
            FId.writelines(LineStr)
        LineStr = 'TotalImNum={}\n'.format(TotalImNum)
        FId.writelines(LineStr)



if __name__ == '__main__':
    OpenImageData2Mine()
