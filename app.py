from flask import Flask, request
from service import process_task

app = Flask(__name__)

@app.route("/run")
def run():
    user_input = request.args.get("task")
    return process_task(user_input)

if __name__ == "__main__":
    app.run()
