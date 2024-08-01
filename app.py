import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    images = os.listdir(os.path.join(app.static_folder, "img/certificates"))
    project_img = os.listdir(os.path.join(app.static_folder, "img/projects"))
    return render_template('index.html', images=images, projects=project_img)

if __name__ == "__main__":
    app.run(debug=True)
