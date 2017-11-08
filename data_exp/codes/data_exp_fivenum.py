#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
       作者: 郑喜民
   创建日期:2017-11-1
       功能:按列计算数据统计项（总数、均值、标准差、最小值、（25%、50%、75%）分位数、
           最大值、方差、偏度、峰度、中位数、变异系数、极差）
   维护日志:日期 作者 原因 内容
"""

import numpy as np
import pandas as pd


def fun_fivenum(df_input):
    """
    功能：按列计算数据统计项（总数、均值、标准差、最小值、（25%、50%、75%）分位数、
    最大值、方差、偏度、峰度、中位数、变异系数、极差）
    input: df_input(类型为DateFrame)
    output: df_output(类型为DateFrame)
    return: DateFrame(类型为DateFrame)
    """
    
    if True == df_input.empty:
        return pd.DataFrame()
    
    #df_input = pd.DataFrame(df_input)  
    
    df_describe = df_input.describe()
    
    #方差
    df_variance = df_input.var().rename('var')
    
    #偏度
    df_skewness = df_input.skew().rename('skew')
    
    #峰度
    df_kurtosis = df_input.kurt().rename('kurt')
    
    #中位数
    df_median = df_input.median().rename('median')
    
    #变异系数 = 标准差/均值
    df_std = df_describe.loc['std']    
    df_mean = df_describe.loc['mean']    
    df_cov = df_std.div(df_mean).rename('cov')
    
    #极差 = 最大值-最小值
    df_max = df_describe.loc['max']
    df_min = df_describe.loc['min']
    df_range = df_max.sub(df_min).rename('range')
    
    list_union = [df_variance, df_skewness, df_kurtosis, df_median, df_cov, df_range]

    #结果拼接
    df_fivenum_result = df_describe.append(list_union, ignore_index=False)   
    
    return df_fivenum_result


if __name__ == "__main__":
    row1 = pd.Series(np.array([1,2,3,4]))
    row2 = pd.Series(np.array([5,6,7,8]))
    row3 = pd.Series(np.array([7,10,11,12]))
    row4 = pd.Series(np.array([0,4,6,2]))
    
    df_test = pd.DataFrame({"A":row1, "B":row2, "C":row3, "D":row4})
    
    print('\n a test of fivenum() \n raw data:\n', df_test, '\n')
    
    print('processed data: \n', fun_fivenum(df_test), '\n')
    
# =============================================================================
#     df_null = pd.DataFrame()
#     
#     print('null:\n', df_null)
# =============================================================================
    
    