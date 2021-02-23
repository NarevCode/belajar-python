# LOOP PYTHON
""" Di dalam python pengulangan/loop dibagi menjadi 3, yaitu:
    -while loop
    -for loop
    -nested lopp """

#while loop
count = 0
while (count < 9):
    print ("The count is: ", count)
    count = count + 1

print ("Good Bye!")

# FOR LOOP
angka = [1,2,3,4,5]
for x in angka:
    print(x)

buah = ["nanas", "apel", "pisang"]
for makanan in buah:
    print ("Saya suka makan", makanan)

# NESTED LOOP
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
          if not(i%j): break
          j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + j
print("Good Bye!")