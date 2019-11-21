# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 00:22:49 2019

@author: Tim Lai

Computation functions to be used in script.py

"""
#Calculates students' current grades given their HW and Quiz averages, each worth 15%, and exam scores, each worth 20%. 
def calculate_grade(hw, quiz, exam_1, exam_2):
    return (0.15*(hw + quiz) + 0.2*(exam_1 + exam_2))/0.7

#From this output, calculates what students should get on the final exam, which is worth 30%, to guarantee their desired grade. 
def final_grade(current_grade, desired_grade):
    return (desired_grade - 0.7*current_grade)/0.3

  
    
