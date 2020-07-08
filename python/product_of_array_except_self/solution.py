def product_except_self(nums):
    size = len(nums)
    pre = [1]*size
    post = [1]*size
    for i in range(1, size):
        pre[i] = pre[i-1]*nums[i-1]
    for i in range(size-2, -1, -1):
        post[i] = post[i+1]*nums[i+1]
    output = [1]*size
    for i in range(size):
        output[i] = pre[i]*post[i]
    return output


if __name__ == '__main__':
    prod_output = product_except_self([1, 2, 3, 4])
    print(prod_output)