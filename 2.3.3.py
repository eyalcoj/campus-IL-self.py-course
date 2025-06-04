
if __name__ == '__main__':
    numbers = input("Enter three digits (each digit for one pig): ")
    num_of_brick_pig1 = int(numbers[0])
    num_of_brick_pig2 = int(numbers[1])
    num_of_brick_pig3 = int(numbers[2])

    total_bricks = num_of_brick_pig1 + num_of_brick_pig2 + num_of_brick_pig3
    print(f"Number of total bricks: {total_bricks}")

    we_like_socialism = total_bricks // 3
    print(f"Number of bricks if we were in Russia: {we_like_socialism}")

    whats_left = total_bricks % 3
    print(f"Number of bricks left: {whats_left}")

    print(f"Is it divided perfectly? {whats_left == 0}")



