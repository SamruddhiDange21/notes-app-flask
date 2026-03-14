from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

FILE = "notes.json"

def read_notes():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def write_notes(notes):
    with open(FILE,"w") as f:
        json.dump(notes,f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes",methods=["GET"])
def get_notes():
    return jsonify(read_notes())

@app.route("/add",methods=["POST"])
def add_note():
    data=request.json
    notes=read_notes()
    notes.append(data["text"])
    write_notes(notes)
    return {"status":"ok"}

@app.route("/delete",methods=["POST"])
def delete_note():
    data=request.json
    notes=read_notes()
    notes.remove(data["text"])
    write_notes(notes)
    return {"status":"deleted"}

if __name__=="__main__":
    app.run(debug=True)