#
# Complete the 'findMaximumSustainableClusterSize' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processingPower
#  2. INTEGER_ARRAY bootingPower
#  3. LONG_INTEGER powerMax
#

def isSustainable(processingPower, bootingPower, powerMax):
    max_booting = max(bootingPower)
    sum_processing = sum(processingPower)
    k = len(processingPower)

    return ((max_booting + sum_processing) * k) <= powerMax


def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    # Write your code here
    n = len(processingPower)
    max_cluster_size = 0

    for i in range(n):
        for j in range(i, n):
            sustainable = isSustainable(processingPower[i:j+1], bootingPower[i:j+1], powerMax)
            if sustainable and max_cluster_size <= abs(i-(j+1)):
                max_cluster_size = abs(i-(j+1))

    return max_cluster_size
