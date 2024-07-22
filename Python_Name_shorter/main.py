b = input("ENTER THE NAME : ")
char_list = [char for char in b]
if len(char_list)>20 : 
    char_list = [char for char in b]
    
    c = ''.join(char_list)+'..'
    print(c)
else:
    print(f"NAME IS : {b}")    
    