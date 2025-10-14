for i in range(1, 7):
    if i == 3:
        continue  # It skips number 3
    if i == 5:
        continue
    if i == 7:
        break     # stops the loop
    print(i)