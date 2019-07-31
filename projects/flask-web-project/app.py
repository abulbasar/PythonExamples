#!/usr/bin/env python
# coding: utf-8


from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Load the model
with open("/data/stocks.small.csv") as f:
    csv_reader = csv.DictReader(f)
    rows = list(csv_reader)
    for i in range(len(rows)):
        rows[i]["id"] = i


@app.route('/')
def home():
    return render_template('index.html', items = rows)


@app.route('/edit/<row_id>')
def render_edit_form(row_id):
    record = rows[int(row_id)]
    record["volume"] = float(record["volume"])
    return render_template('edit.html', record = record)
    

@app.route('/save-stock', methods=["POST"])
def result():
    if request.method == "POST":
        request_data = dict(request.form)
        print(request_data)
        index = int(request_data["id"])
        rows[index] = request_data
        return render_template("index.html", items = rows)
    return redirect("/", code=302)
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    