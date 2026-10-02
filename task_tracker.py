def get_minutes():
    """Prompt for a positive whole-number duration."""
    while True:
        try:
            minutes = int(input("Minutes: "))

            if minutes > 0:
                return minutes

            print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter a positive whole number.")


def main():
    print("Task Duration Tracker")

    tasks = []

    while True:
        task_name = input("Task name (blank to finish): ")

        if task_name == "":
            break

        minutes = get_minutes()
        tasks.append((task_name, minutes))

    if not tasks:
        print("No tasks entered.")
        return

    total_minutes = sum(minutes for _, minutes in tasks)

    longest_task, longest_minutes = max(
        tasks,
        key=lambda task: task[1]
    )

    print(f"Total minutes: {total_minutes}")
    print(
        f"Longest task: {longest_task} "
        f"({longest_minutes} minutes)"
    )


if __name__ == "__main__":
    main()