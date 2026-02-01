from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from topsis_yash_102303701.topsis import topsis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- MAIL CONFIG ----------------
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "ram098763@gmail.com"
app.config["MAIL_PASSWORD"] = "xoyrypsnemlddkwu"

mail = Mail(app)
# ---------------------------------------------


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        file = request.files.get("file")
        weights = request.form.get("weights")
        impacts = request.form.get("impacts")
        email = request.form.get("email")

        if not file or not weights or not impacts or not email:
            return "Error: All fields are required"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

        file.save(input_path)

        try:
            topsis(input_path, weights, impacts, output_path)
        except Exception as e:
            return f"Error while processing TOPSIS: {str(e)}"

        # -------- SEND EMAIL --------
        msg = Message(
            subject="TOPSIS Result File",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email]
        )
        msg.body = "Please find the attached TOPSIS result file."

        with open(output_path, "rb") as fp:
            msg.attach("result.csv", "text/csv", fp.read())

        mail.send(msg)
        # ----------------------------

        return "TOPSIS completed successfully. Result sent to your email."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

