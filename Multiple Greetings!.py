

def say_hello_with_name(name, num_times):
    for _ in range(num_times):
        print(f"Hello, {name}!")

# Get user input for name and number of times
user_name = input("Enter your name: ")
num_greetings = int(input("How many times do you want to be greeted? "))

# Call the function
say_hello_with_name(user_name, num_greetings)