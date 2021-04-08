def yoda():
    print("Smart, you are!")


print("The __name__ variable is:", __name__)

if __name__ == "__main__":
    print("This is being run directly.")
else:
    print("This is being imported.")
