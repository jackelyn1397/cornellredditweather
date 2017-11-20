file = open("weather2016.txt", "r")
sunny = "Sunny: "
cloudy = "Cloudy: "
rain = "Rain: "
snow = "Snow: "
for line in file:
	parts1 = line.split(",")
	date = parts1[0].split(": ")[1]
	condition = parts1[1].split(": ")[1]
	if "Clear" in condition:
		sunny+=date+", "
	elif "Snow" in condition:
		snow+=date+", "
	elif "Cloud" in condition:
		cloudy+=date+", "
	else:
		rain+=date+", "

print sunny[:-2]
print cloudy[:-2]
print rain[:-2]
print snow[:-2]

file.close()