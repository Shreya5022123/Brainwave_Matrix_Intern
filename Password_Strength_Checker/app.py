from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    reasons = []
    
    # Check length
    length_criteria = len(password) >= 8
    length_feedback = f"Length: {'Meets' if length_criteria else 'Does not meet'} (at least 8 characters)"
    if not length_criteria:
        reasons.append("Password must be at least 8 characters long.")
    
    # Check complexity
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[@$!%*?&]', password))
    
    complexity_feedback = [
        f"Uppercase letter: {'Meets' if uppercase_criteria else 'Does not meet'}",
        f"Lowercase letter: {'Meets' if lowercase_criteria else 'Does not meet'}",
        f"Digit: {'Meets' if digit_criteria else 'Does not meet'}",
        f"Special character: {'Meets' if special_criteria else 'Does not meet'}"
    ]

    # Check uniqueness (for simplicity, let's just check if the password is a common one)
    common_passwords = {'password', '123456', '123456789', 'qwerty', 'abc123', 'letmein', 'monkey', '111111', '12345678', 'iloveyou'}
    uniqueness_criteria = password not in common_passwords
    uniqueness_feedback = f"Uniqueness: {'Meets' if uniqueness_criteria else 'Does not meet'} (common passwords)"
    if not uniqueness_criteria:
        reasons.append("Password is too common. Consider using a unique password.")

    # Calculate the strength
    strength = 0
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_criteria and uniqueness_criteria:
        strength += 1

    # Provide feedback based on the strength score
    if strength == 1:
        return "Strong password", reasons, length_feedback, complexity_feedback, uniqueness_feedback
    elif strength == 0:
        return "Very weak password", reasons, length_feedback, complexity_feedback, uniqueness_feedback

    return "Weak password", reasons, length_feedback, complexity_feedback, uniqueness_feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    reasons = []
    length_feedback = ""
    complexity_feedback = []
    uniqueness_feedback = ""
    if request.method == 'POST':
        password = request.form['password']
        result, reasons, length_feedback, complexity_feedback, uniqueness_feedback = check_password_strength(password)
    return render_template('index.html', result=result, reasons=reasons,
                           length_feedback=length_feedback,
                           complexity_feedback=complexity_feedback,
                           uniqueness_feedback=uniqueness_feedback)

if __name__ == '__main__':
    app.run(debug=True)
