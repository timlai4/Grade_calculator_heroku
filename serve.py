# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 00:22:49 2019

@author: Tim
"""

def calculate_grade(hw, quiz, exam_1, exam_2):
    return (0.15*(hw + quiz) + 0.2*(exam_1 + exam_2))/0.7

def final_grade(current_grade, desired_grade):
    return (desired_grade - 0.7*current_grade)/0.3

  
    
