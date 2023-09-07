from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'John Bonham rocks.'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey", methods=['POST'])
def form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/results")

@app.route("/results")
def show_results():
    print("Survey Results")
    return render_template('show.html')

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)