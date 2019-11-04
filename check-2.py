filename = r'1102 [emotion1 10201-10300].txt'

with open(r'dan/' + filename,encoding="utf-8") as dan:
    danlines = dan.readlines()

with open(r'xie/' + filename,encoding="utf-8") as xie:
    xielines = xie.readlines()
    

with open(r'result/' + filename,'w+',encoding="utf-8") as r:
    for i,danline in enumerate(danlines):
        if(danline != xielines[i]):
            line = str(i+1) + '\n' + '丹 ' + danline  + '谢 ' + xielines[i] + '\n'
            r.write(line)