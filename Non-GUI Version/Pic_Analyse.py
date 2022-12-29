import os
import pandas
import cv2
import numpy
from tqdm import tqdm
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


class Pic_Analyse:
    def GetInfo(self):
        DF = pandas.DataFrame()
        WorkDir = 'DataSet'
        os.chdir(WorkDir)
        for Subfolder in tqdm(os.listdir()):
            os.chdir(Subfolder)
            for File in os.listdir():
                try:
                    Image = cv2.imread(File, cv2.IMREAD_COLOR)
                    DF = DF.append({'类别': Subfolder, '文件名': File, '图像宽度': Image.shape[1], '图像高度': Image.shape[0]}, ignore_index = True)
                except:
                    print(os.path.join(Subfolder, File), '无法读取，未能添加')
            os.chdir('../')
        os.chdir('../')
        return DF


class Info_Visualize(Pic_Analyse):
    def __init__(self, Size, Colormap, XLable, YLable, FontSize, FileName, Quality):
        self.Atrr_Size = Size
        self.Atrr_Colormap = Colormap
        self.Atrr_XLable = XLable
        self.Atrr_YLable = YLable
        self.Atrr_FontSize = FontSize
        self.Attr_FileName = FileName
        self.Atrr_Quality = Quality
    
    def CreateTable(self, Info):
        plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体为黑体，解决中文显示问题
        mpl.rcParams['axes.unicode_minus'] = False # 解决负号显示问题
        fig = plt.figure(figsize = (3, 4), dpi = 1400) # dpi set to HD
        ax = fig.add_subplot(111, frame_on = False) # no visible frame
        ax.xaxis.set_visible(False) # hide the x axis
        ax.yaxis.set_visible(False) # hide the y axis
        pandas.plotting.table(ax, Info, loc = 'center') # where df is your data frame
        plt.savefig('表格.jpg')

    def ScatterPlot(self, Info):
        X = Info['图像宽度']
        Y = Info['图像高度']
        Axis_Max = max(max(X), max(Y))
        XY = numpy.vstack([X, Y])
        Kernel_Destiny = stats.gaussian_kde(XY)(XY)
        idx = Kernel_Destiny.argsort()
        X, Y, Kernel_Destiny = X[idx], Y[idx], Kernel_Destiny[idx]
        plt.figure(figsize = self.Atrr_Size)
        plt.scatter(X, Y, s = 5, c = Kernel_Destiny, cmap = self.Atrr_Colormap)
        plt.tick_params(labelsize = 15)
        plt.xlim(xmin = 0, xmax = Axis_Max)
        plt.ylim(ymin = 0, ymax = Axis_Max)
        plt.xlabel(self.Atrr_XLable, fontsize = self.Atrr_FontSize)
        plt.ylabel(self.Atrr_YLable, fontsize = self.Atrr_FontSize)
        plt.savefig(self.Attr_FileName, dpi = self.Atrr_Quality, bbox_inches = 'tight')
        plt.show()