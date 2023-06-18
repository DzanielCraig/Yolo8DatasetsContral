import os
file_in_path=input("Input the path where lables exist:")
file_ot_path=input("Input the path where new lables folder will exist:")
lableSeri=input("Input the number of the lable that you want to remove:")

labels=os.listdir(file_in_path)
for label in labels:
    with open(os.path.join(file_in_path,label),'r') as fr:
        with open(os.path.join(file_ot_path,label),'w') as fw:
            for line in fr.readlines():
                if line[:len(lableSeri)]!=lableSeri:
                    fw.write(line)