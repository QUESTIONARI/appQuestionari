from flask import Blueprint, render_template, request

crea_bp = Blueprint("crea", __name__)

@crea_bp.route("/", methods=['GET', 'POST'])

def index():
    

    if request.method == 'POST':
        # Form being submitted; grab data from form.
        first_name = request.form['nome']
        last_name = request.form['email']
        other_name = request.form['subject']
        text = request.form['text']



        # Validate form data
        if len(first_name) == 0 or len(last_name) == 0:
            # Form data failed validation; try again
            error = "Please supply both first and last name"
        else:
            # Form data is valid; move along
            return render_template('creaQuestionario.html', var=first_name, var2=last_name, var3=other_name)

    elif request.method=='GET':
            return render_template('creaQuestionario.html')

    # Render the sign-up page
    
    
    
    
    
    
    
    
    return render_template('creaQuestionario.html')

