#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   author :zhoujianjun
   date   :2017-10-24
   purpose:data_exp主函数
   log    :
"""
##导入所需要的包
import data_exp_NA_stat
import data_exp_fivenum
import data_exp_split
import pub_fun


if __name__=="__main__":	 
		print("fun_data_exp_main:")	 
		
##定义主函数
def fun_data_exp_main(filepath_input,filename_input,filepath_output,flag=0):
	"""
	   input_type:filepath_input,filename_input,filepath_output,flag
	   output_type：
	   purpose: data_exp主函数通过flag标识控制流程默认为0:全流程
	   												1:只做缺失值统计
	   												2:只做五分位数统计
	   												3:只做异常值
	   												4:缺失值五分位数
	   												5:缺失值异常值
	   												6:五分位数和异常值
	"""
	try:
		os.path.exists(file_path+'/'+file_name)

		os.chdir(file_path)

	except FileNotFoundError:
		print("filepath or file_name not existis")

		break
		#将文件转为dataframe
	else:

		dataframe_file = pub_fun.fun_from_file_to_dataframe(filepath_input,filename_input)
		
		list_rs = []
		if flag == 0:
	
			#计算缺失值
			dataframe_NA = data_exp_NA_stat(dataframe_file)
	
			#数据切片获取数值类型
			dataframe_intenger = data_exp_split(dataframe_file)[1]
	
			#计算fivenum
			dataframe_fivenum = data_exp_fivenum(dataframe_intenger)
	
			#异常值
			dataframe_exception = data_exp_exception(dataframe_file)
	
			#汇总值
			list_rs = [dataframe_NA,dataframe_fivenum,dataframe_exception]
	
		elif flag =1:
	
			#计算缺失值
			dataframe_NA = data_exp_NA_stat(dataframe_file)
	
			#汇总值
			list_rs = [dataframe_NA]
	
		elif flag =2:
	
			#数据切片获取数值类型
			dataframe_intenger = data_exp_split(dataframe_file)[1]
	
			#汇总值
			list_rs = [dataframe_intenger]
	
		elif flag =3:
	
			#异常值
			dataframe_exception = data_exp_exception(dataframe_file)
	
			#汇总值
			list_rs = [dataframe_exception]
	
		elif flag =4:
	
			#计算缺失值
			dataframe_NA = data_exp_NA_stat(dataframe_file)
	
			#数据切片获取数值类型
			dataframe_intenger = data_exp_split(dataframe_file)[1]
	
			#计算fivenum
			dataframe_fivenum = data_exp_fivenum(dataframe_intenger)
	
			#汇总值
			list_rs = [dataframe_NA,dataframe_fivenum]
	
		elif flag =5:
	
			#计算缺失值
			dataframe_NA = data_exp_NA_stat(dataframe_file)
	
			#数据切片获取数值类型
			dataframe_intenger = data_exp_split(dataframe_file)[1]
	
			#异常值
			dataframe_exception = data_exp_exception(dataframe_file)
	
			#汇总值
			list_rs = [dataframe_NA,dataframe_exception]
	
		elif flag =6:
	
			#数据切片获取数值类型
			dataframe_intenger = data_exp_split(dataframe_file)[1]
	
			#计算fivenum
			dataframe_fivenum = data_exp_fivenum(dataframe_intenger)
	
			#异常值
			dataframe_exception = data_exp_exception(dataframe_file)
	
			#汇总值
			list_rs = [dataframe_NA,dataframe_exception]
		else:
			print('流程不存在')

		for dataframe_list in list_rs:
			fun_pdf(dataframe_list)
			print('file is done')



