import vardb as vdb
dbname="chatbotdatabase"
open(dbname,"a")
print("hi :D")
while True:
    vdb.readvars(filename=dbname)
    response=input()
    try:
        print("bot: "+vdb.databasedata[response])
    except:
        newresponse=input("what do you want me to say next time you say this to me ? ")
        vdb.addvar(varname=response,varval=newresponse,filename=dbname)
        print("bot: thank you so much for your help :D")