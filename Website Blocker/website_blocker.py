import time
from datetime import datetime as dt

host_temp = "hosts" #Will use it for temporary/testing purpose
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_path = "127.0.0.1"
websites = ["facebook.com", "www.facebook.com", "quora.com", "www.quora.com", "youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("working hours...")
        with open(host_temp, 'r+') as hostfile:
            content = hostfile.read()
            print(content)
            for website in websites:
                print("working hours inside for")
                if website in content:
                    print("working hours inside if")
                    pass
                else:
                    print("working hours inside else")
                    hostfile.write("\n" + redirect_path + " " + website)
    else:
        print("Fun hours...")
        with open(host_temp, 'r+') as hostfile:
            content = hostfile.readlines()
            hostfile.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    hostfile.write(line)
            hostfile.truncate()
    time.sleep(3)

     
