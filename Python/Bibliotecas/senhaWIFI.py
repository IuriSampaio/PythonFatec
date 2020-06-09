import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']) \
    .decode('utf-8', errors="backslashreplace") \
    .split("/n")
profiles = [i.split(":")[1][1:-1]
            for i in data
            if "see user profile" in i]
print(data)
for i in profiles:

    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key = clear']) \
            .decode('utf-8', errors="backslashreplace") \
            .split(results=[b.split(":")[1][1:-1] for b in results if "key content" in b])
        try:
            print("{:<30}|{:<}".format(i, results[0]))
        except IndexError:
            print(("{:<30}|{:<}".format(i, " ")))
    except subprocess.calledProcessError:
        print(("{:<30}|{:<}".format(i, "ERRO PRA CARALHO")))
input("")
