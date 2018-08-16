from application.views import app
from application.authentication.auth import auth

app.register_blueprint(auth)
app.run(debug=True, host="0.0.0.0", port=5000)
