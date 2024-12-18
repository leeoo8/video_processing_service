from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os

from config.paths import PathConfig
from src.video_processing import extract_audio_from_video, generate_subtitles, embed_subtitles

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # 渲染主页

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is running'})

@app.route('/upload', methods=['POST'])
def upload_video():
    # 确保相关目录已存在
    PathConfig.ensure_dirs(
        [PathConfig.UPLOAD_DIR, PathConfig.OUTPUT_DIR, PathConfig.AUDIO_DIR, PathConfig.SUBTITLE_DIR])

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    video_path = PathConfig.get_upload_path(file.filename)
    file.save(video_path)

    # 音频提取
    audio_path = PathConfig.get_audio_path(f"{file.filename.split('.')[0]}.wav")
    extract_audio_from_video(video_path, audio_path)

    # 生成字幕
    subtitle_path = PathConfig.get_subtitle_path(f"{file.filename.split('.')[0]}.srt")
    generate_subtitles(audio_path, subtitle_path)

    # 嵌入字幕
    output_video_path = PathConfig.get_output_path(f"{file.filename.split('.')[0]}_with_subtitles.mp4")
    embed_subtitles(video_path, subtitle_path, output_video_path)

    return jsonify({
        'message': '视频处理完成',
        'download_url': f'/download/{os.path.basename(output_video_path)}'
    })

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(PathConfig.OUTPUT_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
