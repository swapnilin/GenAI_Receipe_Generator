import subprocess
import sys

def ensure_package_installed(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"{package_name} package not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        __import__(package_name)

# Check and install openai
ensure_package_installed("openai")

import openai

# Check and install flask
ensure_package_installed("flask")

from flask import Flask, render_template_string, request, redirect, url_for
import logging
logging.basicConfig(level=logging.DEBUG)

# Sets the API key for the OpenAI API using the value of the 'OPENAI_API_KEY' from the config file.  
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_tutorial(components):
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant"}, 
    {"role":"user", 
    "content": f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"}])
    return response.choices[0].message.content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    output = ""
    components = ""
    if request.method == 'POST':
        if 'reset' in request.form:
            return redirect(url_for('hello'))
        components = request.form['components']
        output = generate_tutorial(components)

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Custom Recipe Generator</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" />
        <script>
        function resetForm() {
            document.getElementById("tutorial-form").reset();
            document.getElementById("output").textContent = "";
        }
        async function generateTutorial() {
            const components = document.querySelector("#components").value;
            const output = document.querySelector("#output");
            output.textContent = "Cooking a recipe for you...";
            const response = await fetch("/generate", {
                method: "POST",
                body: new FormData(document.querySelector("#tutorial-form")),
            });
            const newOutput = await response.text();
            output.textContent = newOutput;
        }
        function copyToClipboard() {
            const output = document.querySelector("#output");
            const textarea = document.createElement("textarea");
            textarea.value = output.textContent;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand("copy");
            document.body.removeChild(textarea);
            alert("Copied to clipboard");
        }
        </script>
    </head>
    <body>
        <div class="container">
            <h1 class="my-4">Custom Recipe Tutorial Generator</h1>
            <form id="tutorial-form" method="post" class="mb-3">
                <div class="mb-3">
                    <label for="components" class="form-label">Ingredients / Items:</label>
                    <input type="text" class="form-control" id="components" name="components" placeholder="Enter the list of Ingredients or items you have e.g. Bread, jam, potato etc." required />
                </div>
                <button type="submit" class="btn btn-primary" onclick="event.preventDefault(); generateTutorial();">Create a receipe for me</button>
                <button type="button" class="btn btn-secondary" onclick="resetForm()">Reset</button>
            </form>
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    Output:
                    <button class="btn btn-secondary btn-sm" onclick="copyToClipboard()">Copy</button>
                </div>
                <div class="card-body">
                    <pre id="output" class="mb-0" style="white-space: pre-wrap">{{ output }}</pre>
                </div>
            </div>
        </div>
    </body>
    </html>
    ''', output=output)

@app.route('/generate', methods=['POST'])
def generate():
    components = request.form['components']
    return generate_tutorial(components)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
