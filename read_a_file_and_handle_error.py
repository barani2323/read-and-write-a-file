try:
    with open("sample.txt","r") as file:
        print("Reading file content:\n")
        for line_number,line in enumerate(file,strat=1):
            print(f"{line_number}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'samople.txt' was not found.")
