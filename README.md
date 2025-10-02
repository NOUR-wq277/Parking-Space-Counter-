YOLOv8 Flask Video Object Detection 🎥

A simple web application built with Flask to process videos and perform object detection using a custom YOLOv8 model.

✨ Features

    Modern Web Interface: Easily upload video files for processing.

    Video Processing: Analyze videos frame-by-frame using YOLOv8.

    Result Visualization: Draw bounding boxes and class labels directly onto the video.

    Direct Download: Download the processed video immediately after analysis is complete.


🚀 Setup & Installation

To run this project on your local machine, follow these steps:

1. Clone the repository:
Bash

git clone https://github.com/your-username/yolo-flask-video-detection.git
cd yolo-flask-video-detection

2. Create a virtual environment:
Bash

python -m venv venv

3. Activate the environment:

    On Windows:
    Bash

.\venv\Scripts\activate

On macOS/Linux:
Bash

    source venv/bin/activate

4. Install dependencies:
Bash

pip install -r requirements.txt

5. Add your model:

    Place your custom model file (e.g., best.pt) into the models/ directory.

6. Run the application:
Bash

python app.py

7. Open your browser:

    Navigate to http://127.0.0.1:5000/.

🛠️ Technologies Used

    Backend: Flask

    Object Detection: Ultralytics YOLOv8

    Video Processing: OpenCV

    Frontend: HTML, CSS, JavaScript

📄 License

This project is licensed under the MIT License.
