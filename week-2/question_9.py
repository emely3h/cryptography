"""
Question 9:

Let R:={0,1}4 and consider the following PRF F:R5xR->R defined as follows:

F(k,x):= t=k[0] for i=1 to 4 doif (x[i-1]==1) t=t xor k[i] output t 

That is, the key is k=(k[0],k[1],k[2],k[3],k[4]) in R5 and the function at, for example, 0101 is defined as F(k,0101)=k[0] xor k[2] xor k[4]. 

For a random key k unknown to you, you learn that 
F(k,0110)=0011  and  F(k,0101)=1010  and  F(k,1110)=0110 . 
What is the value of F(k,1101)?    Note that since you are able to predict the function at a new point, this PRF is insecure.


Bruteforce approach:
the idea is to calcualate all possible keys and loop trough them while checking if the given equations add up.
If all given equations add up, this means we have a valid key, which we then can use to calculate the value of F(k,1101).

"""

# helper function to get all possible 2^20 keys
def calculate_keys(n):
    keys = []
    count = 0
    for i in range(1<<n):
        count += 1
        s=bin(i)[2:] 
        s='0'*(n-len(s))+s
        key = (list(map(int,list(s))))
        keys.append(key)
    return keys

# given PRF
def F(k,x):		
    t = k[0]
    for i in range(1,5):
        if x[i-1]=='1': 
            t = bin(int(t,2) ^ int(k[i],2))[2:].zfill(4)
    return t

# helper function to format possible keys in nested list
def int_to_string (input):
    string= ''
    key_list = []
    counter = 0
    for bit in input:
        string += str(bit)
        counter += 1
        if(counter == 4):
            key_list.append(string)
            counter = 0
            string = ''
    return key_list

# loop through all possible keys and check if they allign with the given equations
# if valid key is found exit
def calculate(keys, equations):
    for key in keys:
        key = int_to_string(key)
        valid = True
        for entry in equations:
            result = F(key, entry[0])
            if(result != entry[1]):
                valid = False
                break
            
        if (valid):
            return key

# all given equations
given_equations = [['0110', '0011'], ['0101', '1010'], ['1110', '0110']]

possible_keys = calculate_keys(20) 

valid_key = calculate(possible_keys, given_equations)

print('Valid key: ' + str(valid_key))
print('Value of F(k,1101): ' + F(valid_key, '1101'))


