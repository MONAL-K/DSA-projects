name = str(input("enter the name"))

def fun(name):
    vowels = ""
    list = ['a','e','i','o','u']
    for x in name:
          if x in list:
              pass
          else:
              vowels += x

    return vowels
print(fun(name))



