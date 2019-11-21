# M311 Grade Calculator
## Introduction
This is the code base for a grade calculator app for [M311](https://github.com/timlai4/M311), as taught in Fall 2019. Students' gradebooks displayed their cumulative averages per categories, but the categories' weights were not incorporated. As a result, they would need to calculate their current grade in the course themselves. 
The first functionality of this app is to address this shortcoming. When I created the app, the students had numeric values in all their weighted categories except the final exam. The second and final functionality of the app describes what grade they'd need to get on the final exam in order to guarantee their desired final grade. 

## Acknowledgements 
The app is deployed on [Heroku](https://m311-grade-calculator.herokuapp.com/). The main calculating functions as seen in https://github.com/timlai4/Grade_calculator_heroku/blob/master/serve.py are my own. The flask code https://github.com/timlai4/Grade_calculator_heroku/blob/master/script.py I wrote by adapting two extremely helpful learning modules: 

* Rachael Tatman's [Intro to APIs](https://www.kaggle.com/rtatman/careercon-intro-to-apis) course from Kaggle's CareerCon 2019. 
* [This](https://blog.pythonanywhere.com/169/) helpful blog post by PythonAnywhere
