import sys


def bin_search(arr, num):
    start = 0
    end = len(arr) -1 

    while end >= start:
        mid = (start + end) // 2

        #cover edge cases
        if abs(start - end) < 2:


            if start == end:    

                #min array size is 2 by assumption
                if len(arr) == 2:
                    return 0,1
                else:
                    #array is at least 3 elements, check which pair is closest to given corporate bond
                    if start+1< len(arr) and arr[start] <= num <= arr[start+1]:

                        return start, start+1
                    return start-1, start            
            else:
                return start, end 


        # If element is present at the middle itself
        if arr[mid] == num:

            #min array size is 2 by assumption
            if len(arr) == 2:
                return 0,1
            else:
                #array is at least 3 elements, check which pair is closest to given corporate bond
                if mid+1< len(arr) and arr[mid] <= num <= arr[mid+1]:
                    return mid, mid+1
                return mid-1, mid  

            if abs(num-arr[mid-1]) < abs(num-arr[mid+1]):
                return mid-1, mid
            return mid, mid+1

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > num:
            end = mid - 1  

        # Else the element can only be present in right subarray
        else:
            start = mid + 1
    


def find_curve_spread(file_input):

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
        i,j = bin_search(G_years, C_bond[2])

        lower_bond, larger_bond = (G_bonds[i], G_bonds[j])
        #y = mx + b
        m = (larger_bond[3] - lower_bond[3])/(larger_bond[2] - lower_bond[2])
        b = lower_bond[3] - m*lower_bond[2]

        #x for C_bond is C_bond[2]
        #interpolation of C_bond on the line:
        y = m*C_bond[2] + b


        result += C_bond[0] + "," + str(round(C_bond[3] - y,2 )) + "\n"    

    return result   






if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Missing argument: sample_input")
        exit()

    print(find_curve_spread(sys.argv[1]))