#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   author : zhoujianjun
   date   :2017-10-24
   purpose:处理数据缺失值结果以dataframe形式展示
   log    :
"""
##导入所需要的包
import pandas as pd
import numpy as np
import datetime
import pub_fun  as pf


##定义获取列名函数
def fun_NA_stat(p_input):
        """
           input_type:dataframe
           output_type：dataframe
           purpose:通过分别统计dataframe行数 然后分别汇总最终每列数据的覆盖率
        """
        df = p_input
        ##定义数据行数
        data_cnt  = len(df)
        #定义返回值
        list_percent =[]
        ##获取数据属性
        data_date = pf.fun_get_dateframe_info(df,'data_date')
        file_name = pf.fun_get_dateframe_info(df,'file_name')
        etl_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ##获取每列覆盖率的l
        for column in df.columns:
                if column not in ['data_date','file_name','etl_time']:
                        ##获取覆盖率
                        percent = df[column].count()/data_cnt
                        list_percent.append([data_date,file_name,column,percent,etl_time])
        df_percent = pd.DataFrame(list_percent,index = list(range(len(df))),columns = ['data_date','file_name','column_name','percent','etl_time'])

        return df_percent

if __name__=="__main__":   
    print("fun_mis_val_stat")   

#######test

nest_dict = {'data_date':{0:'2017-10-22',1:'2017-10-22'},
             'file_name':{0:'student.csv',1:'student.csv'},
             'shanghai':{0:'100'},
             'beijing':{1:'102',0:'103'},
             'etl_time':{1:'2017-10-22',0:'2017-10-22'}} 
df=pd.DataFrame(nest_dict)
print(df)

print(fun_NA_stat(df))






