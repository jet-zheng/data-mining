#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
       作者: 郑喜民
   		 创建日期:2018-3-15
       功能:定义代码编写规范例子，例子功能为在传入参数后添加“Hello World!!”并返回
   		 维护日志:日期 作者 原因 内容
"""
#如果依赖其他非本项目模块，可以在pub_model.py中添加，此处引用
#import pub_model

#引用本项目其他模块直接添加即可
#import data_exp_fivenum

def fun_example(input_param):
    """    
    input_param: df_input(类型为String类型)
    return: DateFrame(类型为String)
    """
    
    #要追加的字符串
    append_str = 'Hello World!!' 
    
    #为输入参数追加追加字符串
    result_str = input_param + append_list
    
    return result_str


if __name__ == "__main__":
    
    print('fun_example')
    
    #本model的其他测试代码，可以在此处添加
    