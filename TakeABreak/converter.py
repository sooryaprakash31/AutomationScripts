import sys
time = str(sys.argv[1])
unit = time[len(time)-1:]
time = time[:len(time)-1]
if unit =="s":
    time = int(time) * 1
elif unit == "m":
    time = int(time) * 60
elif unit == "h":
    time = int(time) * 60 * 60
else:
    time = int(0)
sys.stdout.write(str(time))
sys.exit(0)
