import sys


def bin_search(arr, num):
    start = 0
    end = len(arr) -1

    while end >= start:

        mid = (start + end) // 2


        if abs(start - end) < 2:
            if abs(num-arr[start]) < abs(num-arr[end]):
                return start
            return end

        # If element is present at the middle itself
        if arr[mid] == num:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > num:
            end = mid - 1  

        # Else the element can only be present in right subarray
        else:
            start = mid + 1
    


def find_yield(file_input):

    #read from input file
    with open(file_input, 'r') as f:
        sample_input = f.read()
        sample_input = sample_input.splitlines()

    #separate government bonds from corporate ones
    C_bonds = []
    G_bonds = []

    for line in sample_input[1:]:
        line = line.replace("years", "")
        line = line.replace("%", "")
        line_arr = line.split(",")
        line_arr[2] = float(line_arr[2])
        line_arr[3] = float(line_arr[3])

        if "C" in line[0]:
            C_bonds.append(line_arr)
        

        if "G" in line[0]:
            G_bonds.append(line_arr)

        #get the term years into an array

    G_years = [G_bond[2] for G_bond in G_bonds]
    
    
    result = ""
    
    for C_bond in C_bonds:
        #find which government bond is closest in terms of years to 
        # the given corporate bond
        index = bin_search(G_years, C_bond[2])
        result += C_bond[0] + ","+ G_bonds[index][0] + "," + str(round(abs(C_bond[3] - G_bonds[index][3]), 3))+"%"  + "\n"     
    
    return result





if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Missing argument: sample_input")
        exit()

    print(find_yield(sys.argv[1]))

    assert find_yield("zero_input.csv") == "" 