import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshols = 0.5


def greetng():
    """greetngc fi"""

    return 'Привет цырен'


def create_task():
    """create_tas"""

    print('')
    
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognizer_google(audio_data=audio, language='ru-RU').lower()
 
    with open('', 'a') as file:
        file.write(f'| {query}\n')

    return f' {query} '


with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    audio = sr.listen(source=mic)
    query = sr.recognizer_google(audio_data=audio, language='ru-RU').lower()

if query == 'Привет друг':
    print(greetng())
else:
    print('как тебя зовут')        