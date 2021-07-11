"""
a module for storing variables into a file and reading the variables
\n usage:
\n vardb.readvars(filename="filename") \n \n to read variables into 'databasedata'dictionary \n \n
\n vardb.addvar(varname="name of variable", varval="variable value",filename="the file name to add data into")\n
to add a variable into the file \n\n
vardb.databasedata["variable name"] \n gives the value stored for the requested variable name
"""
databasedata = dict()
def readvars(filename):
    """
    This function reads variables from the file specified into a dictionary \n
    syntax: readvars(filename="the name of the file to read variables from")
    """
        
    databasefile = open(filename,"r")
    for line in databasefile.readlines():
        line_cont            = line.split("=")
            
        if "\n" in line_cont[1]:
            databasedata[line_cont[0]] = line_cont[1][:-1]
        else:
            databasedata[line_cont[0]] = line_cont[1]

def addvar(varname,varval,filename):
    """
    this function adds a  variable into the dictionary \n
    syntax addvar(varname="variable name", varval="variable value",filename="the name of the file")
    """
    databasefile=open(filename,"a")
    databasefile.write(str(varname+"="+varval+"\n"))