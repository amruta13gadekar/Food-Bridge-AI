import mysql.connector
from flask import Flask, render_template, request, redirect, session
import joblib

# ---------------- DATABASE ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="foodbridge"
)

cursor = db.cursor()

# ---------------- FLASK ----------------

app = Flask(__name__)
app.secret_key = "foodbridge"

# ---------------- AI MODEL ----------------

model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        sql = "SELECT * FROM users WHERE email=%s AND password=%s"

        cursor.execute(sql, (email, password))

        user = cursor.fetchone()

        if user:

            session["name"] = user[1]
            session["email"] = user[2]
            session["role"] = user[4]

            if user[4] == "donor":
                return redirect("/donate")

            elif user[4] == "ngo":
                return redirect("/donations")

        else:

            return render_template(
                "login.html",
                error="Invalid Email or Password"
            )

    return render_template("login.html")


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        sql = """
        INSERT INTO users(name, email, password, role)
        VALUES(%s, %s, %s, %s)
        """

        values = (
            name,
            email,
            password,
            role
        )

        cursor.execute(sql, values)
        db.commit()

        return render_template(
            "register.html",
            success="Registration Successful! You can now login."
        )

    return render_template("register.html")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ---------------- DONATE PAGE ----------------

@app.route("/donate")
def donate():

    if "role" not in session:
        return redirect("/login")

    if session["role"] != "donor":
        return "Access Denied"

    return render_template("donate.html")


# ---------------- SAVE DONATION ----------------

@app.route("/save_donation", methods=["POST"])
def save_donation():

    if "role" not in session:
        return redirect("/login")

    donor_name = request.form["donor_name"]
    donor_email = session["email"]

    food_type = request.form["food_type"]
    quantity = request.form["quantity"]
    location = request.form["location"]
    contact = request.form["contact"]

    sql = """
    INSERT INTO donation
    (donor_name, donor_email, food_type, quantity, location, contact, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        donor_name,
        donor_email,
        food_type,
        quantity,
        location,
        contact,
        "Pending"
    )

    cursor.execute(sql, values)
    db.commit()

    return redirect("/my_donations")


# ---------------- NGO DONATIONS ----------------

@app.route("/donations")
def donations():

    if "role" not in session:
        return redirect("/login")

    if session["role"] != "ngo":
        return "Access Denied"

    cursor.execute("SELECT * FROM donation")

    data = cursor.fetchall()

    return render_template(
        "donations.html",
        donations=data
    )


# ---------------- ACCEPT DONATION ----------------

@app.route("/accept/<int:id>")
def accept(id):

    if "role" not in session:
        return redirect("/login")

    if session["role"] != "ngo":
        return "Access Denied"

    sql = """
    UPDATE donation
    SET status='Accepted'
    WHERE donation_id=%s
    """

    cursor.execute(sql, (id,))
    db.commit()

    return redirect("/donations")


# ---------------- COMPLETE DONATION ----------------

@app.route("/complete/<int:id>")
def complete(id):

    if "role" not in session:
        return redirect("/login")

    if session["role"] != "ngo":
        return "Access Denied"

    sql = """
    UPDATE donation
    SET status='Completed'
    WHERE donation_id=%s
    """

    cursor.execute(sql, (id,))
    db.commit()

    return redirect("/donations")


# ---------------- MY DONATIONS ----------------

@app.route("/my_donations")
def my_donations():

    if "role" not in session:
        return redirect("/login")

    if session["role"] != "donor":
        return "Access Denied"

    sql = """
    SELECT * FROM donation
    WHERE donor_email=%s
    """

    cursor.execute(sql, (session["email"],))

    data = cursor.fetchall()

    return render_template(
        "my_donations.html",
        donations=data
    )


# ---------------- AI PREDICTION ----------------

# ---------------- AI PREDICTION ----------------

@app.route("/predict", methods=["POST"])
def predict():

    food_input = request.form.get("food", "").strip()
    quantity_input = request.form.get("quantity", "").strip()

    foods = [food.strip().title() for food in food_input.split(",")]
    quantities = [q.strip() for q in quantity_input.split(",")]

    predictions = []

    try:

        if len(foods) != len(quantities):

            return render_template(
                "donate.html",
                prediction_error="Please enter the same number of foods and quantities."
            )

        total = 0

        for food, quantity_text in zip(foods, quantities):

            quantity = float(quantity_text)

            if quantity <= 0:
                continue

            # Convert food name using trained encoder
            food_encoded = encoder.transform([food])[0]

            # Actual ML prediction
            prediction = model.predict(
                [[food_encoded, quantity]]
            )

            meals = round(prediction[0])

            predictions.append({
                "food": food,
                "quantity": quantity,
                "meals": meals
            })

            total += meals

        return render_template(
            "donate.html",
            predictions=predictions,
            total_prediction=total
        )

    except ValueError:

        return render_template(
            "donate.html",
            prediction_error="Please enter valid quantities in kg."
        )

    except Exception as e:

        print("AI ERROR:", e)

        return render_template(
            "donate.html",
            prediction_error="One or more food names are not available in the AI model."
        )
# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)