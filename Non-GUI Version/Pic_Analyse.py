import os
import pandas
import cv2
import numpy
from tqdm import tqdm
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def AnalyseInfo():
    global DF
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

    DF


def Visualize():
    X = DF['图像宽度']
    Y = DF['图像高度']

    Axis_Max = max(max(X), max(Y))

    XY = numpy.vstack([X, Y])
    Kernel_Destiny = stats.gaussian_kde(XY)(XY)

    idx = Kernel_Destiny.argsort()
    X, Y, Kernel_Destiny = X[idx], Y[idx], Kernel_Destiny[idx]

    plt.figure(figsize = (9,9))

    plt.scatter(X, Y, s = 5, c = Kernel_Destiny, cmap = 'Spectral_r')

    plt.tick_params(labelsize = 15)

    plt.xlim(xmin = 0, xmax = Axis_Max)
    plt.ylim(ymin = 0, ymax = Axis_Max)

    plt.ylabel('height', fontsize = 25)
    plt.xlabel('width', fontsize = 25)

    plt.savefig('数据集图像尺寸数据分布图.pdf', dpi = 120, bbox_inches = 'tight')

    plt.show()