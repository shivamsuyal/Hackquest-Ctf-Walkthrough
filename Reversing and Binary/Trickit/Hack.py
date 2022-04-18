a=r"\x101e\x1019\x101f\x1008\x101e\x101e\x1008\x1009\x1010\x105d\x100f\x105f\x1018\x1009\x1032\x105c\x100f\x1018\x105f\x1009\x1032\x100c\x100f\x100f\x1018\x105f\x105e\x1021\x1032\x100c\x100f\x100f\x105c\x1018\x103a\x1016\x100a\x100c\x1001\x102b\x106d\x121".replace("\\x"," ").split()
flag=""

for i in range(4200,4255):
    flag = "".join([chr(int(x,16)^i^5) for x in a])
    if "stressed" in flag:
        # print(flag[::-1])
        print(i)