#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   author :zhoujianjun
   date   :2017-10-24
   purpose:处理各类公共函数
   log    :
"""
##导入所需要的包
import os
import pandas as pd
import numpy as ny
import time
import datetime


def fun_from_file_to_dataframe(file_path,file_name):
	"""
	   input_type:filepath,filename
	   output_type：dataframe
	   purpose: export dataframe from different file types 
	   			后续增加读取xml格式
	"""
	##定义返回值
	dataframe_file = ''

	try:
		os.path.exists(file_path+'/'+file_name)

		os.chdir(file_path)

		time.strptime(create_date, "%Y-%m-%d")

	except FileNotFoundError:
		print("filepath or file_name not existis")

		break
		
	else:
		##文件类型
		file_type = file_name.split('.')[len(file_name.split('.'))-1]

		##处理json文件
		if file_name.split('.')[1] == 'json':
	
			dataframe_file = pd.read_json(file_name,encoding = 'utf-8')
		##处理csv文件	
		elif file_name.split('.')[1] == 'csv':
	
			dataframe_file = pd.read_csv(file_name,header = 0,encoding = 'utf-8')
		##处理excle文件	
		elif file_name.split('.')[1] in ('xls','xlsx'):
	
			dataframe_file = pd.read_excle(file_name,header = 0,encoding = 'utf-8')\
		else:
			print('the file tpye is error')

			break
		dataframe_output = dataframe_file

			return dataframe_output

