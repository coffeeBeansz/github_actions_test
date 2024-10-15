import datetime

def main():
    with open('log.txt', 'a') as f:
        f.write(f'Writing to log at {datetime.datetime.now()}\n')

if __name__ == '__main__':
    main()