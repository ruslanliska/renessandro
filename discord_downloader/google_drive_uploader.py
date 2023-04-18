import logging
import shutil

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def upload_creatives_to_drive(creatives_path: str) -> None:
    try:
        drive = GoogleDrive(gauth)
        for file_name in os.listdir(creatives_path):
            creative_file = drive.CreateFile({'parents': [{"kind": "drive#fileLink", "id": '14KMLslRZNplXWh8NeDSKnscKD1zThcgE'}],
                                              'title': file_name})
            creative_file.SetContentFile(os.path.join(creatives_path, file_name))
            creative_file.Upload()
            logging.info(f"File {file_name} was uploaded to drive!")
            print(f"File {file_name} was uploaded to drive!")
    except Exception as e:
        print("BBB")
        print(e)
        logging.error(e)
    finally:
        shutil.rmtree(creatives_path)

# directory = os.getcwd()
# upload_creatives_to_drive(f"{directory}/output")

