import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# duplicates = []
# name_dict = {}
# count = 0
# for i in names_1 + names_2:
#     count += 1
#     if count <= len(names_1) and name_dict.get(i) is None:
#         name_dict[i] = True
#         continue

#     if count > len(names_1) and name_dict.get(i) is not None:
#         duplicates.append(i)

# duplicates = []
# names_2_set = set(names_2)
# for name in names_1:
#     if name in names_2_set:
#         duplicates.append(name)

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()
# import io
# from functools import partial
# import sys
# duplicates = []
# names_1_set = set(names_1)
# with open('names_2.txt', 'rb',0) as file:
    # fb = file.read()
    # print(file)
    # bytesIO = io.BytesIO(fb)
    # print(bytesIO.getvalue())

    # for line in file:
    #     print(line)

# chunk_size = 1
# with open('names_2.txt', 'rb') as in_file:    
#     for data in iter(partial(in_file.read, chunk_size), b''):
#         x = int.from_bytes(data, byteorder='big')
#         if (x > 64 and x < 91) or (x > 96 and x < 123) :
#             sys.stdout.write(chr(x))
#         else:
#             sys.stdout.write('.')
    

    # if name in names_1_set:
    #     print(True)
        # duplicates.append(file.read())


names_1_set = set(names_1)
names_2_set = set(names_2)
duplicates = names_1_set.intersection(names_2_set)
        

end_time = time.time()
# print(count)
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

