
# import library
from app import app
from flask import render_template
# add index route
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("/admin/dashboard.html")

# add about route
@app.route("/admin/profile")
def admin_profile():
    return "Admin profile"
