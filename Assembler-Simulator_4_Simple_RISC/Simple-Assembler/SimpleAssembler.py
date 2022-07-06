import sys

def  error(opcode,reg):
    erd={}
    f1=open("a.txt")
    d=f1.readlines()
    for i in d:
    
         
         j=i.split()
         if j==[]:
            continue
         elif j[0]=='hlt':
            continue
         elif j!=[]:
          print(i.split())
          if j[0] not in opcode:
             print("Error ,wrong instruction syntax")
             erd[j[0]]='err'
          
          if j[1] not in reg:
             
             print("Error in syntax , registor out of range")
             erd[j[1]]='err'
          if j[2] not in reg :
             
             print("Error in syntax , registor out of range")
             erd[j[2]]='err'
          if j[3] not in reg:
             
             print("Error in syntax , registor out of range")
             erd[j[3]]='err'
         
    return erd
    f1.close()

opcode={"add":10000,"sub":10001,"ld":10100,"st":10101,"mul":10110,"div":10111,"rs":11000,"ls":11001,'xor':11010,'or':11011,'and':11100,'hlt':'01010'}
reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}
errors=(error(opcode,reg))
print(errors)
print("===================loop2==============")

def code(opcode,reg):
 #print(errors)
 f1=open("a.txt")
 d=f1.readlines()
 fin=[]
 for i in d:
    #for j in i.split():
    
        
        j=i.split()
        if j==[]:
            continue
        elif j[0]=='hlt':
            continue
        elif j!=[]:
         print(i.split())
         m=0
         if j[m] in opcode:
             if j[m] not in errors:
                 
                 op1=(opcode[j[m]])
                 op11=str(op1)
         else:
                 op11=''
         m1=1   
         if j[m1] in reg:
             if j[m1] not in errors:
                 op2=(reg[j[m1]])
         else:
                 op2=''
         m2=2   
         if j[m2] in reg:
             if j[m2] not in errors:
               op3=(reg[j[m2]])
         else:
                 op3=''
         m3=3 
         if j[m3] in reg:
             if j[m3] not in errors:
              op4=(reg[j[m3]])
         else:
                 op4=''
        opfin=op11+'00'+op2+op3+op4
        #print(opfin)
        #print(len(opfin))
        fin.append(opfin)
 f1.close()
 return fin
t2=(code(opcode,reg))
#print(t2)


print("================= func3 =========================")


def hlt():
    f1=open("a.txt")
    d=f1.readlines()
    if d[-1]=='hlt':
     hres='0101000000000000'
     t2.append(hres)

    elif ("hlt\n") in d:

     print('error halt should be at end')
    else:
     print("invalid syntax no halt statement")

    f1.close()
hlt()



for i in t2 :
    if len(i)<16:
        print('error mentioned above')
    else:
        print(i)
