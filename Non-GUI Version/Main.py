from Env_Detect import*
from Env_Configure import*
from Pic_Craw import*
from Pic_Filter import*
from Pic_Analyse import*


Class_List = ['a','b']
Download_NUM = 100

def Execute_Pic_Craw():
    PicCraw = Pic_Craw(Class_List, Download_NUM)
    PicCraw.Crawer(PicCraw.Set_Cookies, PicCraw.Set_Headers) # 这里两个参数继承自父类（详见Pic_Craw.py）


Size = (9, 9)
Colormap = 'Spectral_r'
XLable = 'width'
YLable = 'height'
FontSize = 25
FileName = '数据集图像尺寸数据分布图.pdf'
Quality = 120

def Execute_Pic_Analyse():
    InfoVisualize = Info_Visualize(Size, Colormap, XLable, YLable, FontSize, FileName, Quality)
    PicInfo = InfoVisualize.GetInfo() # 这个函数继承自父类（详见Pic_Analyse.py）
    InfoVisualize.CreateTable(PicInfo)
    InfoVisualize.ScatterPlot(PicInfo)


if __name__ == '__main__':
    Execute_Pic_Craw()
    Execute_Pic_Analyse()