#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
       作者: 贾爱平
   创建日期:2017-11-20
       功能:1.计算dataframe的所有数值列相关系数、异常值
            2.将dataframe的分布情况打印到pdf中

"""
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd

def main():

    # 获取数据
    dataframe = pd.read_csv("c:/data/train.csv")

    # 计算相关系数
    corr_res=get_corr(dataframe)
    print("-------------------------相关系数-------------------------")
    print(corr_res)
    # 计算异常值
    outlier_res=get_outlier(dataframe)
    print("-------------------------异常值-------------------------")
    print(outlier_res)


    #将数据分布情况到引导pdf

    pdf = PdfPages('C://test.pdf')
    hist_plot(dataframe, pdf)
    boxplot_plot(dataframe, pdf)
    corr_plot(dataframe, pdf)
    pdf.close()

def hist_plot(data_df,pdf,figsize=None):
    """
    展示dataframe直方图

    参数
    ----------
    data_df : 待展示数据
    pdf : 图形输出文件
    figsize : s输出图形大小
    返回值
    -------
    _ : 无
    """
    if figsize == None:
        figsize=(8,8)
    # plt.figure(figsize=figsize)
    data_df.hist(figsize=figsize)
    pdf.savefig()

def boxplot_plot(data_df,pdf,figsize=None):
    """
    展示dataframe箱线图

    参数
    ----------
    data_df : 待展示数据
    pdf : 图形输出文件
    figsize : s输出图形大小
    返回值
    -------
    _ : 无
    """
    if figsize == None:
        figsize=(8,8)
    plt.figure(figsize=figsize)
    data_df.boxplot(figsize=figsize)
    pdf.savefig()

def corr_plot(data_df,pdf,figsize=None):
    """
    展示dataframe特征相关系数

    参数
    ----------
    data_df : 待展示数据
    pdf : 图形输出文件
    figsize : s输出图形大小
    返回值
    -------
    _ : 无
    """
    if figsize == None:
        figsize=(8,8)
    plt.figure(figsize=figsize)
    sns.heatmap(data_df.corr())
    pdf.savefig()

def get_corr(df_input,method='pearson', min_periods=1):
    """
    计算dataframe中数值列的相关系数

    参数
    ----------
    method : {'pearson', 'kendall', 'spearman'}
        *皮尔森：标准相关系数
        *肯德尔：Kendall Tau相关系数
        *等级：Spearman等级相关
    min_periods : int, optional
        每列所需的最小观测数。目前只对皮尔森和Spearman相关系数有效

    返回值
    -------
    _ : DataFrame
    """
    return df_input.corr(method=method, min_periods=min_periods)

def get_outlier(df_input,method='zscore',outlier_threshod=3):
    """
    获取dataframe中所有数值列的异常值

    参数
    ----------
    method : {'zscore'}
        *  zscore:标准分数也叫z分数

    返回值
    -------
    return_data : DataFrame
    """
    # 获取每个数值列，并结算他们的异常值
    if method=='zscore':
        outlier = [compute_outlier_withzscore(series,outlier_threshod) for _, series in df_input.iteritems() if series.dtype in (np.int64,int, float)]
    # 返回只有异常值得列
    return_data = [series for series in outlier if(isinstance(series,pd.Series))]

    # 返回的数据类型是Series数组
    return return_data

def compute_outlier_withzscore(series,outlier_threshod):
    """
    通过zscore算法计算当前列的异常值，默认阈值为3
    参数
    ----------
    outlier_threshod : 当zscore值大于outlier_threshod，则为异常值

    返回值
    -------
    _ : DataFrame
    """
    # 计算Z-score
    outlier_series= series[abs(series-series.mean())/series.std() >=outlier_threshod].unique()

    # 比较Z-score，超过阈值则判断为异常值
    if(outlier_series.size >0):
        return pd.Series([outlier_series],index=[series.name])

# def dataframe_to_pdf(df_input,titles,doc):
#     """
#     将输入的df_input中的每一个dataframe，输出到doc中.titles中为每个dataframe的标题
#
#     参数
#     ----------
#     df_input : 格式是dataframe列表
#     titles : 格式是字符串列表,内容为dataframe标题
#
#     返回值
#     -------
#      无返回值
#     """
#     if(len(df_input) != len(titles)):
#         print("数据和标题个数不匹配")
#         return
#
#     # 定义元素
#     elements = []
#     styles = getSampleStyleSheet()
#
#     for index in range (len(df_input)):
#
#         #计算列的个数
#         clen = len(df_input[index].columns.tolist())
#         read_postition = 0
#         elements.append(Paragraph(titles[index], styles['Title']))
#
#         # 因为没行超过4列后容易造成显示不正常，所以需要让每行只显示4列
#         while(read_postition<clen):
#
#             if(read_postition <(clen-4)):
#                 pdf_df = df_input[index].ix[:,read_postition:read_postition+4]
#             else:
#                 pdf_df = df_input[index].ix[:, read_postition:clen]
#             # 将index加入到dataframe中作为一列，方便输出
#             pdf_df=pdf_df.reset_index()
#             pdf_df.rename(columns={'index': ''}, inplace=True)
#             lista = ['', pdf_df.columns.tolist()] + pdf_df.values.tolist()
#             table = Table(lista, longTableOptimize=1)
#             elements.append(table)
#             read_postition +=4
#
#     doc.build(elements)
#
# def distribution_to_pdf(df_input,path):
#     """
#     将输入的dataframe每个数值列的分布直方图打印到pdf文件中
#
#     参数
#     ----------
#     path : 输出目标pdf路径
#
#     Returns
#     -------
#     无返回值
#     """
#
#
#     # 计算当前dataframe各数值列的直方图
#     plt.figure(figsize=(8,8))
#     plt.clf()
#
#     pdf = PdfPages('C://test.pdf')
#
#     fig_dims = (8, 2)
#     plt.subplot2grid(fig_dims, (0, 0))
#
#     df_input.hist()
#     # 直方图会自动保存到拍pdf中
#     plt.subplot2grid(fig_dims, (7, 0))
#     df_input.Age.hist()
#
#     pdf.savefig(plt.gcf())
#     # plt.close()
#     # pdf.close()

if __name__ == '__main__':
    main()