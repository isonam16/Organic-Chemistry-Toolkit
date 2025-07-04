from flask import Flask, request, jsonify, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/toolkit')
def toolkit_page():
    return render_template("index.html")

@app.route('/get_iupac', methods=['POST'])
def get_iupac():
    formula = request.json['formula']
    try:
        result = subprocess.run(["./toolkit"], input=formula.encode(), capture_output=True, timeout=5)
        output = result.stdout.decode()
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
