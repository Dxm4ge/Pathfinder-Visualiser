# https://www.dcode.fr/maze-generator use settings 30,30 black block, empty space and single character
# lmao this is a maze stealer/scraper

mapData = ""
mapSize = int(input("Map Size: "))
mapName = input("Map Name: ") + ".txt"

for i in range(mapSize):
    mapData += input()
mapData = mapData.replace("█", "1")
mapData = mapData.replace(" ", "0")

mapData = mapData[0:0] + '2' + mapData[1: ]
mapData = mapData[0:1] + '1' + mapData[2: ]

mapData += "03"

file = open(mapName, 'w')
file.write(mapData)
file.close()

print("\nSaved Map into: " + mapname + ".txt\nFiltered Map:")
print(mapData)
input()
