n = int(input())
lines = [input() for i in range(n)]
times = [line.split(":") for line in lines] # 0 - h, 1 - min, 2 - sec

day_counter = 1
prev_time = int(times[0][0])*3600 + int(times[0][1])*60 + int(times[0][2])
for i in range(1, len(times)):
    curr_time = int(times[i][0])*3600 + int(times[i][1])*60 + int(times[i][2])
    if curr_time <= prev_time:
        day_counter += 1
    prev_time = curr_time

print(day_counter)