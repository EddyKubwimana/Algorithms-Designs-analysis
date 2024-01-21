
'''2. We are given numbers n and m, and the following operations:
•n → n + 1
•n → n + 2
•n → n * 2 '''



def increment(lower, upper):
    sequence = [upper]
    if lower>=upper:
        return None

    else:

        while lower <= upper:

            if upper%2 ==0 and int(upper/2)>=lower:

               
                upper = int(upper/2)
                sequence.append(upper)

            else :

                if (upper-1)%2 >= lower:
                    
                    upper = upper-1
                    sequence.append(upper)


                elif upper-2>=lower:
                    upper = upper-2
                    sequence.append(upper)

                else:

                    if upper-1>=lower:
                         
                         upper = upper-1
                         sequence.append(upper)

                    else:
                        result = ""
                        for i in sequence:

                            result = f"-->{i}{result}"
                            print(result)




                        return sequence

        return sequence
        



             




print(increment(3,10))