import os
import cv2
import uuid
from flask import Flask, request, jsonify, render_template, send_from_directory
from ultralytics import YOLO

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
DOWNLOAD_FOLDER = os.path.join('static', 'downloads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

model = YOLO(r"D:\yolo\PKLot.v2-640.yolov8\best.pt")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_video', methods=['POST'])
def predict_video():
    if 'video_file' not in request.files:
        return jsonify({"error": "No video file provided"}), 400
    
    file = request.files['video_file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        try:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
            
            file.save(input_path)
            
            cap = cv2.VideoCapture(input_path)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                
                results = model(frame)
                
                annotated_frame = results[0].plot()

                out.write(annotated_frame)

            cap.release()
            out.release()
            
            return jsonify({"download_url": f"/downloads/{filename}"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/downloads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)