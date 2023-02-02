from Env_Detect import*
from Env_Configure import*
from Pic_Craw import*
from Pic_Filter import*
from Pic_Analyse import*
from DataSet_Split import*


Pic_Craw_Class_List = ['a','b']
Pic_Craw_Download_NUM = 100

def Execute_Pic_Craw():
    PicCraw = Pic_Craw(Pic_Craw_Class_List, Pic_Craw_Download_NUM)
    PicCraw.Crawer(PicCraw.Set_Cookies, PicCraw.Set_Headers) # 这俩参数继承自父类（详见Pic_Craw.py）


Pic_Analyse_Size = (9, 9)
Pic_Analyse_Colormap = 'Spectral_r'
Pic_Analyse_XLable = 'width'
Pic_Analyse_YLable = 'height'
Pic_Analyse_FontSize = 25
Pic_Analyse_FileName = '数据集图像尺寸数据分布图'
Pic_Analyse_FileType = '.pdf'
Pic_Analyse_Quality = 120

def Execute_Pic_Analyse():
    InfoVisualize = Info_Visualize(Pic_Analyse_Size, Pic_Analyse_Colormap, Pic_Analyse_XLable, Pic_Analyse_YLable, Pic_Analyse_FontSize, Pic_Analyse_FileName, Pic_Analyse_FileType, Pic_Analyse_Quality)
    PicInfo = InfoVisualize.GetInfo() # 这个函数继承自父类（详见Pic_Analyse.py）
    InfoVisualize.CreateTable(PicInfo)
    InfoVisualize.ScatterPlot(PicInfo)


DataSet_Split_Fraction = 0.3
DataSet_Split_SeedValue = 210
DataSet_Split_FileName = '数据量统计'
#DataSet_Split_FileType = '.csv'

def Execute_DataSet_Split():
    '''
    DataSet_Split.FolderCreator()
    DataSet_Split(DataSet_Split_Fraction, DataSet_Split_SeedValue, DataSet_Split_FileName).FolderSplitter()
    '''
    DataSetSplit = DataSet_Split(DataSet_Split_Fraction, DataSet_Split_SeedValue, DataSet_Split_FileName)
    DataSetSplit.FolderCreator()
    DataSetSplit.FolderSplitter()
    

if __name__ == '__main__':
    Execute_Pic_Craw()
    Execute_Pic_Analyse()
    Execute_DataSet_Split()