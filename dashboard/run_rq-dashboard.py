#import os
#os.execl('/opt/app-root/run_rq-dashboard.sh', 'rq-dashboard')

from flask import Flask
import rq_dashboard
import os


app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

app.config['REDIS_HOST'] = os.environ['DATABASE_SERVICE_NAME']
app.config['REDIS_PASSWORD'] = os.environ['REDIS_PASSWORD']

@app.route("/")
def root():
    redirect("/rq")

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9181)
