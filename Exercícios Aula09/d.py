areas = [6.43423423,7.1923232, 3.365514256,8.8456346546,5.197895454]
round_areas = list(map(round, areas))
print(round_areas)

roud_areas_decimal = list(map(round, areas, range(2, len(areas) + 2)))
print(roud_areas_decimal)