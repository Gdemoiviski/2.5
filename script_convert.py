import os
import os.path
import subprocess

def open_picture():
    source = 'Source'
    result_dir = 'Result'
    # filelist = glob.glob(os.path.join(source, '*.jpg'))
    os.makedirs(result_dir, exist_ok=True)
    for file in os.listdir(source):
        subprocess.Popen(['convert', os.path.join(source, file), '-resize', '200',
                          os.path.join(result_dir, file)])  # Задаем параметры конверта
    print('Процесс завершен')

open_picture()
