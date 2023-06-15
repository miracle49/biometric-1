import base64
import speech_recognition as sr
import moviepy.editor as mp
import os
import shutil
import uuid

recognizer = sr.Recognizer()

def speech_recog(request):
    data = {
        "success": False,
        "message": ""
    }
    if request.method == "POST":
        content = request.json
        # print(content)
        encode_string = content['base64_string']
        type = content['type']
        file_type = content['file_type']

        print(type, file_type)
        if not os.path.exists('sample_audio'):
            os.makedirs('sample_audio')
        
        temp_name = str(uuid.uuid1())
        temp_name_0 = temp_name + '.' + type
        temp_name_1 = temp_name + '.wav'
        deconde_string = base64.b64decode(encode_string)
        file = open("sample_audio/" + temp_name_0, "wb")
        file.write(deconde_string)

        if(file_type == 'video'):
            clip = mp.VideoFileClip("sample_audio/" + temp_name_0)
            clip.audio.write_audiofile("sample_audio/" + temp_name_1, codec='pcm_s16le')
        else :
            clip = mp.AudioFileClip("sample_audio/" + temp_name_0)
            clip.write_audiofile("sample_audio/" + temp_name_1,codec='pcm_s16le')
        
        with sr.AudioFile("sample_audio/" + temp_name_1) as source:
            recorded_audio = recognizer.listen(source)

        file.close()
        if os.path.exists('sample_audio/' + temp_name_0):
            os.remove('sample_audio/' + temp_name_0)
        if os.path.exists('sample_audio/' + temp_name_1):
            os.remove('sample_audio/' + temp_name_1)
        try:
            text = recognizer.recognize_google(
                    recorded_audio, 
                    language="es-MX"
                )
            data['success'] = True
            data['message'] = text
            return data

        except Exception as ex:
            print(ex)
    return data
    