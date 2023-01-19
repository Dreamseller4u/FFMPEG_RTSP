import ffmpeg
import json
from pprint import pprint

def record_rtsp(input_rtsp: str = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4", durattion: int = 30):
    
    stream = ffmpeg.input(input_rtsp, ss=0, t = durattion)

    stream = ffmpeg.output(stream, 'output.mp4')

    try:
        ffmpeg.run(stream, overwrite_output=True)
    except ffmpeg._run.Error as e:     # предполагаю что именна так обрабатывать ошибки 
        print(e)                        
    else:
        print('Video is ok')

    logs = ffmpeg.probe('output.mp4')  # логирование выходного файла 

    json_object = json.dumps(logs, indent=4) 

    with open('logs.txt', 'w') as f:  # сохранение логов в файл logs.txt
        f.write(json_object)

    pprint(logs)

def encode_video(input_file: str, format_to_encode: str):

    stream = ffmpeg.input(input_file)

    stream = ffmpeg.output(stream, f'{input_file}_encode.{format_to_encode}')

    ffmpeg.run(stream, overwrite_output=True)

