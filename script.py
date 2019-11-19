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
            hw = float(request.form["HW grade (%)"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["HW grade"])
        try: 
            quiz = float(request.form["Quiz grade (%)"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["Quiz grade"])     
        try: 
            exam1 = float(request.form["Exam 1 grade (%)"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["Exam 1 grade"])               
        try: 
            exam2 = float(request.form["Exam 2 grade (%)"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["Exam 2 grade"])       
        try: 
            desired_grade = float(request.form["Desired final grade (%)"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["Desired grade"])
            
            
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
                    <p><input name="HW" /></p>
                    <p><input name="Quiz" /></p>
                    <p><input name="Exam 1" /></p>
                    <p><input name="Exam 2" /></p>
                    <p><input name="Desired grade" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
