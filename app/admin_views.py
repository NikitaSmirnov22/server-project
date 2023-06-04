
# import library
from app import app

# add index route
@app.route("/admin/dashboard")
def admin_dashboard():
    return "Admin dashboard"

# add about route
@app.route("/admin/profile")
def admin_profile():
    return "Admin profile"
