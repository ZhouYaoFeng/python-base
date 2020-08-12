import os

os.remove(r"E:\temp\libihua\result.txt")
fo=open(r"E:\temp\libihua\result.txt","w",encoding='gb18030')


g=os.walk(r"E:\temp\libihua")
for path,dir_list,file_list in g:
    for file_name in file_list:
        # fo.write(os.path.join(path, file_name))
        txt=open(os.path.join(path, file_name),'r',encoding='gb18030')
        fo.write(txt.read())
        fo.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        fo.write("\n")
        fo.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        fo.write("\n")
        fo.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        fo.write("\n")
        fo.write("章节分割")
        fo.write("\n")
        fo.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        fo.write("\n")
        fo.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        fo.write("\n")
        fo.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        fo.write("\n")
        fo.write("\n")
        # print(txt.read())
        txt.close()

fo.close()