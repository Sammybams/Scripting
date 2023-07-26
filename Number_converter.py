# Number Converter from integers (or strings containing integers) to words.
# Range - 0 <= num < 1 000 000 000 000

# Created by Bamgbola Samuel Aduragbemi - samuelbamgbola@gmail.com

def unit(num):
    """Returns the equivalent of inputted parameter in words from 1 to 9."""
    
    a = ['one','two','three','four','five','six','seven','eight','nine']
    return a[num-1]

def tens(num):
    """Returns the equivalent of inputted parameter in words.from 11 to 19."""
    a = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    return a[num-1]

def tens_multiple(num):
    """Returns the equivalent of inputted parameter in words for multiples of 10 above 10."""
    a = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    return a[num-2]


def add_and(my_list):
    """Checks through the inputted list, finds were to add the conjunction 'and' and returns the restructured list."""

    #compare is a list of numbers in words in the units and tens position.
    compare_first = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven',
               'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen',
               'nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    
    compare_second = ['million', 'thousand','hundred']
    
    a = " ".join(my_list)   #Joins the words in the inputted list by space 
    a = a.split()   #splits the joined words individiually by space
    
    #Checks if 'billion' is in inputted parameter
    if 'billion' in a:
        pos = a.index('billion')
        #Checks if there is a word after 'billion'
        if pos+1<len(a):
            #Checks if any of the words after 'billion' is in the list of numbers in compare_second.
            if any(ext in a[pos+1:] for ext in compare_second)==False:
                #Checks if the word after 'billion' is in the list of numbers in compare_first.
                if a[pos+1] in compare_first:
                    a.insert(pos+1,'and')

    #Checks if 'million' is in inputted parameter
    if 'million' in a:
        pos = a.index('million')
        #Checks if there is a word after 'million'
        if pos+1<len(a):
            #Checks if any of the words after 'million' is in the list of numbers in compare_second.
            if any(ext in a[pos+1:] for ext in compare_second)==False:
                #Checks if the word after 'million' is in the list of numbers in compare_first.
                if a[pos+1] in compare_first:
                    a.insert(pos+1,'and')

    #Checks if 'thousand' is in inputted parameter
    if 'thousand' in a:
        pos = a.index('thousand')
        #Checks if there is a word after 'thousand'
        if pos+1<len(a):
            #Checks if any of the words after 'hundred' is in the list of numbers in compare_second.
            if any(ext in a[pos+1:] for ext in compare_second)==False:
                #Checks if the word after 'million' is in the list of numbers in compare_first.
                if a[pos+1] in compare_first:
                    a.insert(pos+1,'and')

    #Checks if 'hundred' is in inputted parameter
    if 'hundred' in a:
        pos = a.index('hundred')
        #Checks if there is a word after 'hundred'
        if pos+1<len(a):
            #Checks if the word after 'hundred' is in the list of numbers in compare_first.
            if a[pos+1] in compare_first:
                a.insert(pos+1,'and')
                
    return a

def one(num):
    """Processes a set of 3 numbers from the hundred to unit."""
    converted = []
    if num[-2]!='0':
        if num[-2]=='1':
            if num[-1]!='0':
                converted.append(tens(int(num[-1])))
            else:
                converted.append('ten')
        else:
            converted.append(tens_multiple(int(num[-2])))
            
    if num[-2]!='1':
        if num[-1]!='0':
            converted.append(unit(int(num[-1])))

    if num[-3]!='0':
        converted.insert(0,unit(int(num[-3])) + ' hundred')
        
    return add_and(converted)

def two(num):
    """Processes a set of 3 numbers from the hundred of thousand to thousand."""
    
    converted = []
    if num[-2]!='0':
        if num[-2]=='1':
            if num[-1]!='0':
                converted.append(tens(int(num[-1])) + ' thousand')
            else:
                converted.append('ten thousand')
        else:
            if num[-1]=='0':
                converted.append(tens_multiple(int(num[-2])) + ' thousand')
            else:
                converted.append(tens_multiple(int(num[-2])))
            
    if num[-2]!='1':
        if num[-1]!='0':
            converted.append(unit(int(num[-1])) + ' thousand')

    if num[-3]!='0':
        if converted==[]:
            converted.insert(0,unit(int(num[-3])) + ' hundred'+' thousand')
        else:
            converted.insert(0,unit(int(num[-3])) + ' hundred')
        
    return add_and(converted)

def three(num):
    """Processes a set of 3 numbers from the hundred of million to million."""

    converted = []
    if num[-2]!='0':
        if num[-2]=='1':
            if num[-1]!='0':
                converted.append(tens(int(num[-1])) + ' million')
            else:
                converted.append('ten million')
        else:
            if num[-1]=='0':
                converted.append(tens_multiple(int(num[-2])) + ' million')
            else:
                converted.append(tens_multiple(int(num[-2])))
            
    if num[-2]!='1':
        if num[-1]!='0':
            converted.append(unit(int(num[-1])) + ' million')

    if num[-3]!='0':
        if converted==[]:
            converted.insert(0,unit(int(num[-3])) +' hundred' +' million')
        else:
            converted.insert(0,unit(int(num[-3])) +' hundred')
        
    return add_and(converted)

def four(num):
    """Processes a set of 3 numbers from the hundred of billion to billion."""

    converted = []
    if num[-2]!='0':
        if num[-2]=='1':
            if num[-1]!='0':
                converted.append(tens(int(num[-1])) +' billion')
            else:
                converted.append('ten billion')
        else:
            if num[-1]=='0':
                converted.append(tens_multiple(int(num[-2])) +' billion')
            else:
                converted.append(tens_multiple(int(num[-2])))
            
    if num[-2]!='1':
        if num[-1]!='0':
            converted.append(unit(int(num[-1])) +' billion')

    if num[-3]!='0':
        if converted==[]:
            converted.insert(0,unit(int(num[-3])) +' hundred billion')
        else:
            converted.insert(0,unit(int(num[-3])) +' hundred')
        
    return add_and(converted)

def number_converter(num):
    """Converts numbers inputted in the form of strings or integers to words."""
    
    #converts the input into a string, if it's an integer
    if type(num)==int:
        num = str(num)
        
    #Checks if inputted number is equal to '0' and returns 'zero'
    if num =='0':
        return 'zero'
    
    converted = []
    num = list(str(num))
    first = []
    #print(num)
    left_over = len(num)%3
    
    #Adds the last part of the input to the list 'first'
    if left_over!=0:
        first.append("".join(num[0:left_over]))
    c = left_over
    
    #Adds the left over parts of the input to the list 'first' in 3's.
    while c<len(num)-2:
        first.append("".join(num[c:c+3]))
        c+=3
        
    #Runs through if inputted number is in billions.
    if len(first)==4:
        while len(first[0])!=3:
            first[0] = '0' + first[0]
            
        final_result = []
        final_result += four(first[0])
        final_result += three(first[1])
        final_result = add_and(final_result)
        final_result += two(first[2])
        final_result = add_and(final_result)
        final_result += one(first[3])

        return " ".join(add_and(final_result))
        
    #Runs through if inputted number is in millions.
    elif len(first)==3:
        while len(first[0])!=3:
            first[0] = '0' + first[0]
            
        final_result = []
        final_result += three(first[0])
        final_result += two(first[1])
        final_result = add_and(final_result)
        final_result += one(first[2])
        
        return " ".join(add_and(final_result))

    #Runs through if inputted number is in thousands.
    elif len(first)==2:
        while len(first[0])!=3:
            first[0] = '0' + first[0]
            
        final_result = []
        final_result += two(first[0])
        final_result += one(first[1])
        
        #print(final_result)
        return " ".join(add_and(final_result))

    #Runs through if inputted number is in hundreds, tens or unit.
    elif len(first)==1:
        while len(first[0])!=3:
            first[0] = '0' + first[0]
            
        final_result = []
        final_result += one(first[0])
        
        #print(final_result)
        return " ".join(add_and(final_result))
