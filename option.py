# Create an empty list to store students and scores
students = []

# Define a function to display the menu


def menu():
    print("Please select an option:")

    print("1. Add a new student and their score to the list.")

    print("2. Display the list of students and their scores.")

    print("3. Calculate and display the average score of all students.")

    print("4. Display the names of students who scored above a certain threshold.")

    print("5. End.")


# Use a while loop to repeat the menu until the user exits

while True:

    # Display the menu

    menu()

    # Get the user's option

    option = input("Enter your option: ")

    # Check if the option is valid

    if option not in ["1", "2", "3", "4", "5"]:

        # If not, display an error message and continue the loop

        print("Invalid option. Please try again.")
        continue

    # If the option is valid, perform the corresponding operation

    if option == "1":

        # Add a new student and their score to the list
        # Get the student's name

        name = input("Enter the student's name: ")

        # Get the student's score

        score = int(input("Enter the student's score: "))

        # Create a tuple of name and score and append it to the list

        students.append((name, score))

        # Display a success message and continue the loop

        print(f"{name} and their score {score} have been added to the list.")
        continue

    if option == "2":

        # Display the list of students and their scores
        # Check if the list is empty

        if len(students) == 0:

            # If yes, display a message and continue the loop

            print("The list is empty. Please add some students first.")
            continue

        # If not, display each student and their score in a new line

        for name, score in students:
            print(f"{name}: {score}")
        # Continue the loop
        continue

    if option == "3":

        # Calculate and display the average score of all students
        # Check if the list is empty

        if len(students) == 0:

            # If yes, display a message and continue the loop

            print("The list is empty. Please add some students first.")
            continue

        # If not, calculate the sum and count of scores using a for loop

        total = 0
        count = 0
        
        for name, score in students:
            total += score
            count += 1

        # Calculate the average by dividing the sum by the count

        average = total / count

        # Display the average with two decimal places and continue the loop

        print(f"The average score of all students is {average:.2f}.")
        continue
    if option == "4":

        # Display the names of students who scored above a certain threshold
        # Check if the list is empty

        if len(students) == 0:

            # If yes, display a message and continue the loop

            print("The list is empty. Please add some students first.")
            continue

        # If not, get the threshold from the user and validate it as an integer using a try-except block
        try:
            threshold = int(input("Enter the threshold: "))
        except ValueError:

            # If the input is not an integer, display an error message and continue the loop

            print("Invalid input. Please enter an integer.")
            continue

        # Create an empty list to store the names of students who scored above the threshold

        above_threshold = []

        # Use a for loop to iterate over the students and check their scores

        for name, score in students:

            # If the score is greater than or equal to the threshold, append the name to the list

            if score >= threshold:
                above_threshold.append(name)

        # Check if there are any students who scored above the threshold

        if len(above_threshold) == 0:

            # If not, display a message and continue the loop

            print(f"There are no students who scored above {threshold}.")
            continue

        # If yes, display their names in a comma-separated string and continue the loop

        print(f"The following students scored above {threshold}: {', '.join(above_threshold)}.")
        continue

    if option == "5":

        # Exit the program
        # Display a farewell message and break out of the loop

        print("Program End.")
        print("Thank you!!!")
        break
