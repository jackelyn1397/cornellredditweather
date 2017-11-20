file = open("weather2016.txt", "r")
cold = "Cold: "
medium = "Mild: "
hot = "Hot: "
for line in file:
	parts1 = line.split(",")
	date = parts1[0].split(": ")[1]
	temperature = parts1[2].split(": ")[1]
	if int(temperature)<40:
		cold+=date+", "
	elif int(temperature)>60:
		hot+=date+", "
	else:
		medium+=date+", "

print cold[:-2]
print medium[:-2]
print hot[:-2]

file.close()