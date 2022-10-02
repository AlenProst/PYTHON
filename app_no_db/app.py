from flask import Flask, render_template, request, flash


app= Flask(__name__)
app.secret_key = "super secret key"



notes = []

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", notes=notes)

@app.route("/remove", methods = ['GET', 'POST'])
def remove():
    if request.method == "POST":
        remove_note = request.form.get("note")
        if remove_note not in notes:
            flash('There is no such entry')
            return render_template("index.html", notes=notes)
        else:
            notes.remove(remove_note)
            return render_template("index.html", notes=notes)
    
    
    
    

if __name__ == '__main__':
   app.run(debug = True)