name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith("From "):
        line = line.rstrip()
        line = line.split()
        time = line[5].split(":")
        hour = time[0]
        counts[hour] = counts.get(hour, 0) + 1
        

ord = list()
for k, v in counts.items():
    counts[hour] = counts.get(hour, 0) + 1
    results = ((k, v))
    ord.append(results)
ord.sort()
    
for k,v in ord:
    print k[:2], v
