import datetime
import pytz

def main():
    timezone = pytz.timezone('Europe/Stockholm')
    with open('log.txt', 'a') as f:
        f.write(f'Writing to log at {datetime.datetime.now(timezone)}\n')

if __name__ == '__main__':
    main()