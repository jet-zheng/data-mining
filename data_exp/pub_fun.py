#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   author : zhoujianjun
   date   :2017-10-24
   purpose:处理各类公共函数
   log    :
"""
##导入所需要的包
import pandas as pd
import numpy as np
import datetime

def fun_get_dateframe_info(p_input,p_column):

        """
           input_type:dataframe,string
           output_type：string
           purpose:输入dataframe和其列名获取dataframe公共值
        """
        df = p_input
        column = p_column
        if column in ['data_date','file_name','etl_time']:
         df_info = df[column][0]
         return df_info
