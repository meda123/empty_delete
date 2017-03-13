from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def view_homepage():
    """ This route takes us to the homepage"""
    return render_template("index.html") 

@app.route("/application-form")
def view_application_form():
    """ This route takes us to the application form """
    return render_template("application-form.html")

@app.route("/application-success", methods=["POST"])

def view_application_response():
    """ This route takes us to the homepage"""

    applicant_first = request.form.get("firstname")
    applicant_last = request.form.get("lastname")
    applicant_salary = int(request.form.get("salary requirements"))
    applicant_position = request.form.get("position")

    return render_template("application-response.html",
        firstJ = applicant_first,
        lastJ = applicant_last,
        salaryJ = applicant_salary,  
        positionJ = applicant_position,)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
