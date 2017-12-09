rows = int(input("Enter How many rows you want = "))
columns = int(input("Enter How many columns you want = "))

sub = []
main = []

for i in range(rows):
    for j in range(columns):
        items = input("Enter data to display 2D array = ")
        sub.append(items)
    main.append(sub)
    sub = []

for k in main:
    for elem in k:
        print(elem,end=" ")
    print()

