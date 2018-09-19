/*
  将输入的字符进行加密和解密，加密方式是：将输入的每个字符的ASCii码值加3，所得到的即为加密后的密文
                            解密方式是：将输入的每个字符的ASCii码值减3,所得的即为解密后的明文
*/

//author = Qiufeng

#加密
plaincode = input("请输入明文:")
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):
        print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end = '')
    else:
        print(p,end = ' ')

#解密
plaincode = input("请输入密文:")
for p in plaincode:
    if ord("d") <= ord(p) <= ord("z"):
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26),end = '')
    else:
        print(chr(ord("a")+(ord(p)-ord("a")+23)%26),end = ' ')

