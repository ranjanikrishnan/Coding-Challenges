import os


def get_minimum_days(parcels):
    day_count = 0

    while True:
        min_parcel = parcels[0]
        for i in range(len(parcels)):
            if min_parcel > parcels[i] > 0:
                min_parcel = parcels[i]

        already_delivered = 0
        for i in range(len(parcels)):
            if parcels[i] > 0:
                parcels[i] = parcels[i] - min_parcel
            else:
                already_delivered += 1
        if already_delivered < len(parcels):
            day_count += 1
        else:
            break

    return day_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parcels_count = int(input().strip())

    parcels = []

    for _ in range(parcels_count):
        parcels_item = int(input().strip())
        parcels.append(parcels_item)

    result = get_minimum_days(parcels)

    fptr.write(str(result) + '\n')

    fptr.close()