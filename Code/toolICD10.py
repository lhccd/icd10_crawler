import csv

with open('/Users/lorenz/PycharmProjects/ICD_10_Scraper/WHO_ICD10_Codes_220820181401.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    linklist = []
    for index, row in enumerate(readCSV):
        linklist.append(row[0])
      #  print(index, row[0])

linklist = linklist[10374:10387]
print("\n".join(linklist))


subdivisions = []
subdivisions.append("")
subdivisions.append("Diagnostic and monitoring devices")
subdivisions.append("Therapeutic (nonsurgical) and rehabilitative devices")
subdivisions.append("Prosthetic and other implants, materials and accessory devices")
subdivisions.append("Surgical instruments, materials and devices (including sutures)")
subdivisions.append("Miscellaneous devices, not elsewhere classified")

output = []

for i in linklist:
    output.append(i[i.index('; '):].replace('; ', ""))
    for l in subdivisions[1:]:
        stre = (str(i[i.index('; '):].replace('; ', "")) + ": " + str(l))
        output.append(stre)

print("\n".join(output))

f = open("subdivisions.csv", "a+")
for e in output:
    f.write(e + "\n")
f.close()


#print("\n".join(linklist))