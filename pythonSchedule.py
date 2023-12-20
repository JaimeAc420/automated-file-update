import shutil
import schedule
import time
from datetime import datetime
import os

def backup_files(source, destination):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)

        for root, dirs, files in os.walk(source):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination, file)
                shutil.copy2(source_path, destination_path)

        print(f"Actualización -backup- exitoso en {datetime.now()}")
    except Exception as e:
        print(f"Actualización -backup- fallido: {e}")

def main():
    
    source_directory = r"use a personal directory here"
    destination_directory = r"use a personal directory here"

    schedule.every(1).minutes.do(backup_files, source_directory, destination_directory)
    #schedule.every().day.at("12:00").do(backup_files, source_directory, destination_directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
