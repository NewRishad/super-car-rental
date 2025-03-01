import inquirer
from pyfiglet  import Figlet

if __name__ == "__main__":
    title = Figlet(font='sub-zero')
    print(title.renderText('Super Car Rentals'))

    user_options = [
        inquirer.List(
            "user",
            message="Please select your option",
            choices=["Admin", "Registered", "Un-registered", "Exit"],
        ),
    ]

    answers = inquirer.prompt(user_options)

    print(answers)



