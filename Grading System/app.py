from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_required_grades(prelim):
    try:
        prelim = float(prelim)
        if prelim < 0 or prelim > 100:
            return "Invalid input. Prelim grade should be between 0 and 100."
        
        # Assuming passing grade is 60
        passing_grade = 60
        
        # Calculate required average for midterm and finals
        required_average = (3 * passing_grade - prelim) / 2
        
        if required_average > 100:
            return "Unfortunately, it's not possible to pass the subject based on the given prelim grade."
        elif required_average <= 0:
            return "You've already passed the subject based on your prelim grade alone!"
        else:
            return f"To pass the subject, you need an average of {required_average:.2f} for your midterm and finals."
    except ValueError:
        return "Invalid input. Please enter a numerical value for the prelim grade."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        prelim = request.form['prelim_grade']  # Match the name attribute in the form
        result = calculate_required_grades(prelim)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
