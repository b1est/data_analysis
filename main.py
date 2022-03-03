from lab1 import *
from lab2 import *
import schedule
  

def main():
    schedule.every().day.at((datetime.now()+ timedelta(minutes=1)).strftime('%H:%M')).do(download)
    schedule.every().day.at((datetime.now()+ timedelta(minutes=2)).strftime('%H:%M')).do(convert_to_json)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    #main()
    download()
    convert_to_json()
