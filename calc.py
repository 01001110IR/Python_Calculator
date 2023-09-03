import logging

# Configure logging
logging.basicConfig(filename='calculator.log', format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s', level=logging.INFO)

def calc():
    while True:
        user_input = input("\n\nPlease enter a mathematical expression: \nTo exit, write 'exit': ")

        if user_input == 'exit':
            print("Thank you for using the Calculator. Goodbye!")
            break

        try:
            result = eval(user_input)
            if result == 0:
                raise ZeroDivisionError("Division by zero")

            print("Result:", result)

            # Log the user's input
            logging.info(f'User input: {user_input}')
        except ZeroDivisionError as e:
            print("Error:", e)
            logging.error(f'Error: {e}')
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calc()
