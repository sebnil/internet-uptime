import time
import urllib.request
from datetime import date

def internet_on():
    try:
        urllib.request.urlopen('http://google.se', timeout=5)
        return 1
    except urllib.request.URLError:
        print('URLError')
    except:
        print('could not do urlopen')
    return 0


if __name__ == "__main__":
    now = date.today()
    filename = '{:04d}-{:02d}-{:02d} uptime.csv'.format(now.year, now.month, now.day)
    with open(filename, 'a') as f:
            for i in range(0, 5):
                internet_ok = internet_on()
                if internet_ok:
                    break
                else:
                    print('internet not ok. loop {}. trying again'.format(i))
            iso_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
            line = '{:.6f},{},{}\n'.format(time.time(), iso_time, internet_ok)
            print(line)
            f.write(line)
            f.flush()
