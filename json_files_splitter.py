with open("data_Copy.json", "r") as data:
    # raw_json : string
    raw_json = data.read()
    data.close()
# 1 entry = 1 line
json1 = raw_json.split("\n")
starts = []
ends = []
for place, i in enumerate(json1):
    if i == "{":
        starts.append(place)
    elif i == "}":
        ends.append(place)

dates = []
for i in starts:
    # 21 char to 31 char
    date = json1[i + 3][21:31]
    dates.append(date)

for i in range(len(starts)):
    one_day = json1[starts[i]:ends[i]+1]
    one_date = dates[i]
    filename = "wind_villers_"+one_date+".json"
    text = ""
    for j in one_day:
        text += j
        text += "\n"
    with open(filename, "w") as new_file:
        new_file.write(text)
