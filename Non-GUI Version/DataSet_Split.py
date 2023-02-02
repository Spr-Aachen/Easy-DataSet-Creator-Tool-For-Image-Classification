import os
import re
from tqdm import tqdm
import shutil
import random
import pandas


class DataSet_Split():
    def __init__(self, Fraction, SeedValue, FileName):
        self.WorkDir = 'DataSet'
        self.ValidationSet_Fraction = Fraction
        self.ListShuffle_SeedValue = SeedValue
        self.QuantityInfo_FileName = FileName

    def FolderCreator(self):
        if not os.path.exists(self.WorkDir + '/Training') and not os.path.exists(self.WorkDir + '/Validation'):
            os.mkdir(os.path.join(self.WorkDir, 'Training'), mode = 0o777)
            os.mkdir(os.path.join(self.WorkDir, 'Validation'), mode = 0o777)
        else:
            try:
                os.mkdir(os.path.join(self.WorkDir, 'Training'), mode = 0o777)
            except:
                os.mkdir(os.path.join(self.WorkDir, 'Validation'), mode = 0o777)

        for Subfolder in tqdm(os.listdir(self.WorkDir)):
            if os.path.basename(Subfolder) != 'Training' and os.path.basename(Subfolder) != 'Validation':
                os.mkdir(os.path.join(self.WorkDir, 'Training', Subfolder), mode = 0o777)
                os.mkdir(os.path.join(self.WorkDir, 'Validation', Subfolder), mode = 0o777)

    def FolderSplitter(self):
        #print('{:^21} {:^21} {:^21}'.format('数据类别', '训练集数据量', '验证集数据量'))

        DF = pandas.DataFrame()

        for Subfolder in tqdm(os.listdir(self.WorkDir)):
            if os.path.basename(Subfolder) != 'Training' and os.path.basename(Subfolder) != 'Validation':

                Folder_OldPath = os.path.join(self.WorkDir, Subfolder)
                FileList = os.listdir(Folder_OldPath)
                random.seed(self.ListShuffle_SeedValue)
                random.shuffle(FileList)

                ValidationSet_Content = FileList[:int(len(FileList) * self.ValidationSet_Fraction)]
                TrainingSet_Content   = FileList[int(len(FileList) * self.ValidationSet_Fraction):]

                for File in ValidationSet_Content:
                    File_OldPath = os.path.join(self.WorkDir, Subfolder, File)
                    File_NewPath = os.path.join(self.WorkDir, 'Validation', Subfolder, File)
                    shutil.move(File_OldPath, File_NewPath)

                for File in TrainingSet_Content:
                    File_OldPath = os.path.join(self.WorkDir, Subfolder, File)
                    File_NewPath = os.path.join(self.WorkDir, 'Training', Subfolder, File)
                    shutil.move(File_OldPath, File_NewPath)

                if len(os.listdir(Folder_OldPath)) == 0:
                    shutil.rmtree(Folder_OldPath)
                    #print('{:^21} {:^21} {:^21}'.format(Subfolder, len(TrainingSet_Content), len(ValidationSet_Content)))
                    DF = DF.append({'数据类别': Subfolder, '训练集数据量': len(TrainingSet_Content), '验证集数据量': len(ValidationSet_Content)}, ignore_index = True)
                else:
                    raise AssertionError

        DataSet_Name = re.split(pattern = '[-_]', string = self.WorkDir, maxsplit = 0, flags = 0)[0]
        shutil.move(self.WorkDir, DataSet_Name + '_Split')

        DF['数据集数据量'] = DF['训练集数据量'] + DF['验证集数据量']
        DF.to_csv(self.QuantityInfo_FileName + '.csv', index = False)

        return DF