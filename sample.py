import os,json
class DynamicValue:
    textbox={}
    password={}
    dropdown={}
    radiobutton={}
    name={}
    size={}
    displayValue={}
    value={}
    rdisplayValue={}
    rvalue={}
    length=0
    buttonName=""
    
    def __init__(self):
        with open("data2.json","r") as json_file:
            try:
                content=json.loads(json_file.read())
                self.buttonName=content["ActionDisplayName"]
                self.length=len(content["Attributes"])
                self.dynamicCheck(content["Attributes"],self.length)
                self.printValues()
                print("\n")
            except json.decoder.JSONDecodeError as err:
                print(f"could not load json from {doc}.. {err}",end="\n")
                
    @classmethod
    def singleCheck(self,content):
        if isinstance(content,list) or isinstance(content,dict) or isinstance(content,tuple):
            return True
        else:
            return False
        
    @classmethod    
    def dynamicCheck(self,content,length):
        for i in range(length):
            if (self.singleCheck(content[i])):
                if(content[i].get("Type")=="TextBox"):
                    self.name[i]=content[i]['Name']
                    self.size[i]=int(content[i]['Size'])
                    self.textbox[i]=f"txt{i}"
                    
                elif(content[i].get("Type")=="SecretTextBox"):
                    self.name[i]=content[i]['Name']
                    self.size[i]=int(content[i]['Size'])
                    self.password[i]=f"pwd{i}"
            
                elif(content[i].get("Type")=="Dropdown"):
                    self.name[i]=content[i]['Name']
                    self.dropdown[i]=f"dropdwn{i}"
                    dropdown_list=content[i]['DropDownValues']
                    for j in range(len(dropdown_list)):
                        self.displayValue[f"{i}.{j}"]=dropdown_list[j]['DisplayValue']
                        self.value[f"{i}.{j}"]=dropdown_list[j]['Value']

                elif(content[i].get("Type")=="RadioButton"):
                    self.name[i]=content[i]['Name']
                    self.radiobutton[i]=f"radiobtn{i}"
                    radioButton=content[i]['Options']
                    for j in range(len(radioButton)):
                        self.rdisplayValue[f"{i}.{j}"]=radioButton[j]['DisplayValue']
                        self.rvalue[f"{i}.{j}"]=radioButton[j]['Value']

    def getAttribute(self):
        return self.textbox,self.password,self.dropdown,self.radiobutton,self.name,self.size,self.displayValue,self.value,self.rdisplayValue,self.rvalue,self.length,self.buttonName
    
    def printValues(self):
         print(self.radiobutton),print(self.dropdown),print(self.textbox),print(self.password),print(self.name),print(self.size),print(self.displayValue),print(self.value)
         print(self.rdisplayValue),print(self.rvalue),print(self.length),print(self.buttonName)

if __name__=="__main__":
    dataSample=DynamicValue()
