def no_c(my_string):
    for i in range(len(my_string)):
        print("{:s}".format(my_string[i]
                            if (my_string[i] != "c" and my_string[i] != "C")
                            else ""), end="")
