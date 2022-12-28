from Env_Detect import*
from Env_Configure import*
from Pic_Craw import*
from Pic_Filter import*
from Pic_Analyse import*


Class_List = ['a','b']
Download_NUM = 100


def Main():
    PicCraw = Pic_Craw(Class_List, Download_NUM)
    PicCraw.Crawer(PicCraw.Set_Cookies, PicCraw.Set_Headers) # 这里两个参数继承自父类（详见Pic_Craw.py）


if __name__ == '__main__':
    Main()