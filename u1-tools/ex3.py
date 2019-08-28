
zip = int(input())
all_zips = {}
while(zip != 0):
    if zip not in all_zips:
        all_zips[zip] = 1
    else:
        all_zips[zip] += 1
    zip = int(input())
for myzip in all_zips:
    print(myzip, ":", all_zips[myzip])
