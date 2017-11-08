#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	 author :zhoujianjun
	 date	 :2017-10-24
	 purpose:缺失值统计
	 log		: date	author	reason content
"""
##导入所需要的包
import pandas as pd
import numpy as np
import pub_fun	as pf


##定义获取列名函数
def fun_NA_stat(dataframe_input):
				"""
					 input_type:dataframe
					 output_type：dataframe
					 purpose:通过分别统计dataframe行数 然后分别汇总最终每列数据的覆盖率
				"""
				##定义数据行数
				dataframe_count	= len(dataframe_input)
				##获取每列覆盖率
				list_percent = [[column,dataframe_input[column].count()/dataframe_count]]

				dataframe_output = pd.DataFrame(list_percent,columns = ['column_name','column_percent'])

				return dataframe_output

if __name__=="__main__":	 
		print("fun_NA_stat:")	 

