from string import digits
from string import ascii_letters
from string import punctuation

search = "91!H"
for i in digits + ascii_letters + punctuation:
    for j in digits + ascii_letters + punctuation:
            for k in digits + ascii_letters + punctuation:
                    for l in digits + ascii_letters + punctuation:
                        #print(i, j)
                        if(search == (i + j + k + l)):
                            print("Found: " + i, j, k, l)
