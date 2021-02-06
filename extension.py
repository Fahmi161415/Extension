# Getting extension of file

filename = input("Enter the filename:")
file_extension=filename.split(".")
print("The extension of file is" + repr(file_extension[-1]),":'python'" )

