from flask import Flask  # pip install flask as flask not in default python, to check if app.py can run, key in python app.py in terminal
from flask import render_template, request  # user page is using render_template, request (old way)frontend & backend throw template and request input, perform calculationn & throw back ans
# now, all done in frontend, to go backend too slow, only like password or bank balance go backend, frontend is like wallet

app = Flask(__name__)  #indicates who launches the programme in website so render can look for developer. sign on agreement

@app.route("/", methods=["GET","POST"]) #call programme, default come to here "/" backend get from frontend (request), frontend to backend = post
# backend = flash,  front = html, CSS, jS
# backend (from flash perspective, get (request from frontend, return result to frontend = post))
def index():
        return(render_template("index.html"))  # no need to call index, just a naming convention

@app.route("/prediction_DBS", methods=["GET","POST"])
def prediction_DBS():
        q = float(request.form.get("q"))
        return(render_template("prediction_DBS.html", r = 90.2 + (-50.6*q)))
    
if __name__ == "__main__":  # confirm if the programme run by developer
    app.run()
#go to explorer (2 files in left icon, create folder called templates under the repository), new file inside templates folder
# backend to communicate frontend in python to run, need protocol WSGI and need gunicorn (programme) to run WSGI
# WSGI communicate between backend and frontend text, so need to convert to number
# result r = model coeff * input by user + intercept
# need to sync (left linkage) to update to github, commit, key in any number & click on tick on the right top icon
# google colab - have chatgp in coding, for model programming - easier to do in google colab