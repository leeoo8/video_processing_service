import os

class PathConfig:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 上传文件目录
    UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
    # 输出目录
    OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
    # 临时音频存储目录
    AUDIO_DIR = os.path.join(OUTPUT_DIR, 'audio')
    # 临时字幕文件存储目录
    SUBTITLE_DIR = os.path.join(OUTPUT_DIR, 'subtitles')
    # 视频帧存储目录
    FRAMES_DIR = os.path.join(OUTPUT_DIR, 'frames')

    @classmethod
    def ensure_dirs(cls, dirs):
        if isinstance(dirs, list):
            for dir in dirs:
                cls.ensure_dir(dir)
        else:
            cls.ensure_dir(dirs)

    @classmethod
    def get_upload_path(cls, filename):
        return os.path.join(cls.UPLOAD_DIR, filename)

    @classmethod
    def get_output_path(cls, filename):
        return os.path.join(cls.OUTPUT_DIR, filename)

    @classmethod
    def get_audio_path(cls, filename):
        return os.path.join(cls.AUDIO_DIR, filename)

    @classmethod
    def get_subtitle_path(cls, filename):
        return os.path.join(cls.SUBTITLE_DIR, filename)

    @classmethod
    def get_frames_path(cls, filename):
        return os.path.join(cls.FRAMES_DIR, filename)

    @classmethod
    def ensure_dir(cls, path):
        """
        确保目录存在，不存在则创建
        """
        if not os.path.exists(path):
            os.makedirs(path)
        pass