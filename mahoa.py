import sys
sys.stdout.reconfigure(encoding='utf-8')
Plaintext="LeThiTuongVy"
k=23
chucaithuong = "abcdefghijklmnopqrstuvwxyz"
chucaihoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ketqua = ""
for char in Plaintext:
    if char in chucaithuong:
        newtext=(chucaithuong.index(char)+k)%26
        ketqua+=chucaithuong[newtext]
    elif char in chucaihoa:
        newtext=(chucaihoa.index(char)+k)%26
        ketqua+=chucaihoa[newtext]
    else:
        ketqua+=char
print(f"Kết quả mã hóa: {ketqua}")
