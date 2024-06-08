import pathlib
import string

root = pathlib.Path(__file__).parent


cn_lv1 = []
cn_lv2=[]
for i in range(16,87+1):
    v1 = i+0xA0
    for j in range(1,94+1):
        v2 = j+0xA0
        v = (v1<<8)|v2
        
        try:
            if i>10-1 and i<55+1:
                
                cn_lv1.append(v.to_bytes(2,'big').decode('gbk'))
            else:
                cn_lv2.append(v.to_bytes(2,'big').decode('gbk'))
        except:
            pass
print(f'一级汉字：{len(cn_lv1)} , 二级汉字: {len(cn_lv2)}, 共 {len(cn_lv1)+len(cn_lv2)}')

with open(root / 'cn_gb2312_lv1.txt','w',encoding='utf-8') as f:
    f.write(string.printable.strip() +' '+ ''.join(cn_lv1))

with open(root / 'cn_gb2312_lv2.txt','w',encoding='utf-8') as f:
    f.write(string.printable.strip() +' '+ ''.join(cn_lv2))

with open(root / 'cn_gb2312_full.txt','w',encoding='utf-8') as f:
    f.write(string.printable.strip() +' '+ ''.join(cn_lv1)+ ''.join(cn_lv2))