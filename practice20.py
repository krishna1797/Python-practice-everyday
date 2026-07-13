import time

print("===== Countdown Timer =====")

while True:
    try:
        lala = int(input("Enter countdown time in seconds: "))

        if lala < 0:
            print("Please enter a positive number.\n")
            continue

        break

    except ValueError:
        print("Please enter a valid integer.\n")


while lala >= 0:

    minutes =lala // 60
    sec = lala % 60

    print(f"\rTime Left: {minutes:02d}:{sec:02d}", end="")

    time.sleep(1)

    lala -= 1

print("\n\n Time's Up!")