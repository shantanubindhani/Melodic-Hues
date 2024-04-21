# Melodic Hues: Sentiment-Driven Soundscapes

This web application, Melodic Hues, empowers users to upload images and receive song recommendations based on the mood detected in the uploaded image. Users can also select the language in which they want to receive song recommendations.

## Features

- **Image Upload**: Users can upload images from their local file system or capture images using their device's webcam.
- **Mood Detection**: The application analyzes the uploaded image to detect the mood of the person in the image.
- **Song Recommendations**: Based on the detected mood, the application provides song recommendations that match the user's mood.
- **Language Selection**: Users can select the language in which they want to receive song recommendations.

## Installation

To run the web application locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your Spotify API credentials by obtaining a client ID and client secret from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/). Replace the placeholders in the `songRecommender.py` file with your actual credentials.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Upload or capture an image.
2. Select the desired language.
3. Click the "Upload" button to receive song recommendations based on the detected mood.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Term Paper: "Melodic Hues: Leveraging OpenCV, Deep Learning, and Spotify API for Emotionally Intelligent Music Discovery"

This project is accompanied by a term paper titled "Melodic Hues: Leveraging OpenCV, Deep Learning, and Spotify API for Emotionally Intelligent Music Discovery." The term paper explores the technical details and methodologies employed in the development of the Melodic Hues web application. It delves into the integration of computer vision techniques using OpenCV for mood detection in uploaded images, the utilization of deep learning models for emotion recognition, and the integration with the Spotify API for dynamically recommending songs that match the detected mood.

For more in-depth information about the project and its underlying technologies, please refer to the accompanying term paper.
