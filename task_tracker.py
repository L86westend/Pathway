tasks = []

while True:
    name = input("Enter task name (blank to finish): ")

    if name == "":
        break

    while True:
        minutes_text = input("Enter minutes: ")

        if not minutes_text.isdigit():
            print("Please enter a positive whole number.")
            continue

        minutes = int(minutes_text)

        if minutes <= 0:
            print("Please enter a positive whole number.")
            continue

        break

    tasks.append((name, minutes))

if not tasks:
    print("No tasks were entered.")
else:
    total_minutes = sum(minutes for _, minutes in tasks)
    longest_task = max(tasks, key=lambda task: task[1])

    print("\nTask Summary")
    print("------------")

    for name, minutes in tasks:
        print(f"{name}: {minutes} minutes")

    print(f"\nTotal minutes: {total_minutes}")
    print(
        f"Longest task: {longest_task[0]} "
        f"({longest_task[1]} minutes)"
    )

