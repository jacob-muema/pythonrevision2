#direct concatenation causes an error(TypeError: can only concatenate str (not "int") to str)
#example
age=36
txt="My name is John, I am " +age
print(txt)
# to solve we use f-string method