from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import songRecommender as sr
import base64

app = Flask(__name__)

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        image_data = request.form["image_data"]
        lang = request.form["lang_type"]

        image_data_decoded = base64.b64decode(image_data.split(",")[1])
        file_path = "static/file.jpg"

        with open(file_path, "wb") as file:
            file.write(image_data_decoded)

        image = cv2.imread("static/file.jpg")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

        faces = cascade.detectMultiScale(gray, 1.1, 3)

        for x, y, w, h in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped = image[y : y + h, x : x + w]
        cv2.imwrite("static/after.jpg", image)

        try:
            cv2.imwrite("static/file.jpg", cropped)
        except:
            pass

        try:
            img = cv2.imread("static/file.jpg", 0)
        except:
            pass

        img = cv2.resize(img, (48, 48))
        img = img / 255

        img = img.reshape(1, 48, 48, 1)

        model = load_model("emotion_detection_model.h5")

        pred = model.predict(img)
        label_map = ["Angered", "Neutral", "Fearful", "Happy", "Sad", "Surprised"]
        pred = np.argmax(pred)

        final_pred = label_map[pred]
        songs = sr.find_songs_by_mood(final_pred, lang)

        return render_template("predict.html", mood=final_pred, songs=songs)


if __name__ == "__main__":
    app.run(debug=True)
