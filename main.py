import inquirer
from pyfiglet  import Figlet

if __name__ == "__main__":
    title_text = Figlet(font='sub-zero')
    print(title_text.renderText('Super Car Rentals'))