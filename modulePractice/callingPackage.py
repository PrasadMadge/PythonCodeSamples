# calling main package here
# __init__ files make sure that python treats the folder as python package and not a normal folder

# from folderName of python package
from MyMainPackage import someMainScript
from MyMainPackage.SubPackage import mySubscript

someMainScript.report_main()
mySubscript.sub_func()
