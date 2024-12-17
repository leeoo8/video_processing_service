import whisper
from config.paths import PathConfig

def transcribe_audio(audio_path, language='zh'):
    """使用 Whisper 进行音频转录"""
    try:
        model = whisper.load_model("large-v3")
        result = model.transcribe(audio_path, language=language)
        return result["text"]
    except Exception as e:
        print(f"音频转录时出错: {str(e)}")
        return None