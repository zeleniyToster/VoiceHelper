from email.mime import audio
import speech_recognition
import os


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {'commands':{
    'create_task':['добавить задачу','задача'],
    'open_opera': ['открой оперу','открой браузер','браузер'],
    'open_lol': ['открой лол', 'лигу']
}}

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic,duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query    
    except speech_recognition.UnknownValueError:
        return 'Damn...'



def create_task():
    print ('Что добавим в список дел?')

    query = listen_command()

    if query == 'ничего':
        print("ok")
    else:
        with open('todo-list.txt', 'a') as file:
            file.write(f'{query}\n')
    
        return f'Задача {query} добавлена в todo-list!'


def open_opera():
    os.startfile(r"C:\Users\Kouko\AppData\Local\Programs\Opera GX\launcher.exe")
    print('Открываю!')

def open_lol():
    os.startfile(r"C:\Riot Games\Riot Client\RiotClientServices.exe")
    print('Запускаю!')


def main():
    query = listen_command()
    
    for k,v in commands_dict['commands'].items():
        if query in v:
            globals()[k]()

if __name__ == '__main__':
    main()
 