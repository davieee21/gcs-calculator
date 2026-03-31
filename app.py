from flask import Flask, render_template, request
from gcs import format_gcs_output
from datetime import datetime

app = Flask(__name__)


# -------------------------
# Home Route
# -------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            # Get form data
            eye = int(request.form.get("eye"))
            verbal = int(request.form.get("verbal"))
            motor = int(request.form.get("motor"))

            # Process using backend logic
            result = format_gcs_output(eye, verbal, motor)

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error,
        current_year=datetime.now().year  # automatically pass current year for footer
    )


# -------------------------
# Run App
# -------------------------

if __name__ == "__main__":
    app.run(debug=True)