from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table Generator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        input[type="number"] { padding: 8px; font-size: 16px; }
        input[type="submit"] { padding: 8px 15px; font-size: 16px; cursor: pointer; }
        ul { list-style-type: none; padding: 0; }
        li { font-size: 18px; margin: 5px 0; }
    </style>
</head>
<body>
    <h2>Multiplication Table Generator</h2>
    <form method="POST">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required value="{{ number if number }}">
        <input type="submit" value="Generate">
    </form>

    {% if table %}
        <h3>Table for {{ number }}</h3>
        <ul>
            {% for item in table %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    table = []
    number = None
    
    if request.method == "POST":
        try:
            number = int(request.form.get("number"))
            table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
        except (TypeError, ValueError):
            pass 

    return render_template_string(HTML_TEMPLATE, table=table, number=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)