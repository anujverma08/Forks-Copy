## ANGLE BETWEEN HOURS AND MINUTES HAND USING PYTHON LANGUAGE
# taking clock in 24 hours format
a = input("(HH:MM) : ")
time = a.split(":")
time = [int(i) for i in time]
if time[0] > 12:
    time[0] = time[0]-12
# total minute covered by hour hand is denoted by (tmh)
tmh = time[0]*60 + time[1]
# in one minute hour hand will cover 30/60=0.5
dmh = 0.5
# total minute covered by minute hand is denoted by (tmm)
tmm = time[1]
# in 1 minute minute hand will cover 360/60=6
dmm = 6
if time[0]<=12:
    b = abs(tmm*dmm - tmh*dmh)
    c = min(b,360-b)
    print(int(abs(c)),"°",sep="")
else:
    print("please input the time in 24 hours format")