name = input("Enter your name with no spaces: ")
print("Total matches: ", str(len([line for line in open('dictionary.txt', 'r') for x in [name[i:i+3] for i in range(len(name)-2)] if x.lower() in line.lower()])))
