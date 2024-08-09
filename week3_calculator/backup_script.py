import schedule
import os
import shutil
import datetime
import time

source_dir = "/Users/narender/Projects/python/my-python-projects/week1_numpy"
destination_dir = "/Users/narender/Projects/python/my-python-projects/backups"


def create_backup(source_dir, destination_dir):
    try:
        today = datetime.date.today()
        dest_dir = os.path.join(destination_dir, str(today))
        shutil.copytree(source_dir, dest_dir)
        print(f"backup created at: {dest_dir}")
    except FileExistsError:
        print(f"backup already exists at: {dest_dir}")


schedule.every().day.at("01:02").do(lambda: create_backup(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(10)
