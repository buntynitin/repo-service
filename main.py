from flask import Flask
from report.routes import report
# from listconfig.routes import list_config
# from listassociation.routes import list_association

# Init app
app = Flask(__name__)

app.register_blueprint(report)
# app.register_blueprint(list_config)
# app.register_blueprint(list_association)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
