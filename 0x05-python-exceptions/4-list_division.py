#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    if (my_list_1 == [] or my_list_2 == []):
        return (result)
    for i in range(list_length):
        div = 0
        try:
            div = (my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
        except ValueError:
            print("wrong type")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
            return (result)
        finally:
            if (i < len(my_list_1) or i < len(my_list_2)):
                result.append(div)
    return (result)
