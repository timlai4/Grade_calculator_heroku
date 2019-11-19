from flask import Flask, request
from serve import calculate_grade, final_grade

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        hw = None
        quiz = None
        exam1 = None
        exam2 = None
        desired_grade = None
        try: 
            hw = float(request.form["hw"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["hw"])
        try: 
            quiz = float(request.form["quiz"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["quiz"])     
        try: 
            exam1 = float(request.form["exam1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["exam1"])               
        try: 
            exam2 = float(request.form["exam2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["exam2"])       
        try: 
            desired_grade = float(request.form["desired_grade"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["desired_grade"])
            
            
        if hw is not None and quiz is not None and exam1 is not None and exam2 is not None and desired_grade is not None:
            current_grade = calculate_grade(hw, quiz, exam1, exam2)
            final = final_grade(current_grade, desired_grade)
            return '''
                <html>
                    <body>
                        <p>Your current grade is {}%</p>
                        <p>To get a {}%, you need a {}% on the final exam. </p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(current_grade, desired_grade, final)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your grades as a percentage:</p>
                <form method="post" action=".">
                    <p>HW: <input name="hw" />%</p>
                    <p>Quiz: <input name="quiz" />%</p>
                    <p>Exam 1: <input name="exam1" />%</p>
                    <p>Exam 2: <input name="exam2" />%</p>
                    <p>Desired final grade: <input name="desired_grade" />%</p>
                    <p><input type="submit" value="Calculate" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
