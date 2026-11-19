import sys
import xxhash

n = int(sys.argv[1])
s = int(sys.argv[2])

print("Number of buckets:", n)
print("Bucket size:", s)

while True:
    text = input("Please enter the string: ")

    hash_number = xxhash.xxh64(text).intdigest()
    bucket = hash_number % n + 1

    file_name = str(bucket) + ".txt"

    with open(file_name, "a") as file:
        file.write(text)

    print(text, "added to", file_name)
