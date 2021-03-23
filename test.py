from sample import DynamicValue
dynamicweb=DynamicValue()
first_wrapper="""<!doctype html>
<html>
    <head>
        <title></title>
    </head>
    <body>
        <form>"""
textbox,password,dropdown,radiobutton,name,size,displayValue,value,rdisplayValue,rvalue,length,butname=dynamicweb.getAttribute()

for ite in range(length):
    temp_string=" "
    if bool(textbox):
        for key in textbox.keys():
            if key==ite:
                print(key,textbox.get(key))
                for x,y in ((key1,key2) for key1 in name.keys() for key2 in size.keys()):
                    if x==ite and y == ite:
                        temp_string="""\n
            <label>%s:</label>
                <input type="text" id="%s%d" size="%d"><br><br>"""
                        first_wrapper+=temp_string%(name[x],name[x],ite,size[y])

    if bool(password):        
        for key in password.keys():
            if key==ite:
                print(key,password.get(key))
                for x,y in ((key1,key2) for key1 in name.keys() for key2 in size.keys()):
                    if x==ite and y == ite:
                        temp_string="""\n
            <label>%s:</label>
                <input type="password" id="%s" size="%d"><br><br>"""
                        first_wrapper+=temp_string%(name[x],password[x],size[y])

    if bool(dropdown):
        for key in dropdown.keys():
            if key==ite:
                print(key,dropdown.get(key))
                temp_string="""\n
            <label>%s</label>
                <select id="%s%d">\n"""
                first_wrapper+=temp_string%(name[ite],name[ite],ite)
                temp_string=""
                for x in range(len(value)):
                    temp_string+="""
                    <option value={}>{}</option>""".format(value['{}.{}'.format(ite,x)],displayValue['{}.{}'.format(ite,x)])
                temp_string+="""\n
                </select><br><br>"""
                first_wrapper+=temp_string
                print(first_wrapper)
    elif bool(radiobutton):
        for key in radiobutton.keys():
            if key==ite:
                print(key,radiobutton.get(key))
                temp_string="""\n
            <label>%s</label>"""
                first_wrapper+=temp_string%(name[ite])
                temp_string=""
                for x in range(len(rvalue)):
                    temp_string+="""
                    <input type="radio" id="{}" value="{}">""".format(rvalue['{}.{}'.format(ite,x)],rvalue['{}.{}'.format(ite,x)])
                    temp_string+="""<label>{}</label>""".format(rdisplayValue['{}.{}'.format(ite,x)])
                first_wrapper+=temp_string
                
    else:
        temp_string+=""
        
first_wrapper+="""<br><br>
        <button>%s</button> 
        </form>
    </body>
</html>"""
first_wrapper=first_wrapper%(butname)
print(first_wrapper)
file=open("program.html",'w')
file.write(first_wrapper)   
file.close()
