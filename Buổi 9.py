
#W9A1
def ghep_mang(a, b):
    c = a + b
    c.sort()
    return c

x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(*ghep_mang(x, y))

#W9A2
mang_tong = []
while True:
    try:
        dong = list(map(int, input().split()))
        mang_tong.append(dong)
    except EOFError:
        break

danh_sach = []
for i in range(len(mang_tong) - 1):
    danh_sach.append(mang_tong[i])

ket_qua = []
for hang in danh_sach:
    for so in hang:
        ket_qua.append(so)
ket_qua.sort()

vitri = mang_tong[-1][0] - 1
print(ket_qua[vitri])

#W9A3
chuoi = input()
nho_nhat = int(chuoi[0])
vi_tri = 0
for i in range(1, len(chuoi)):
    if int(chuoi[i]) <= nho_nhat:
        nho_nhat = int(chuoi[i])
        vi_tri = i
mang_tam = []

for c in chuoi:
    mang_tam.append(c)
if vi_tri == 0:
    mang_tam[-2], mang_tam[-1] = mang_tam[-1], mang_tam[-2]
else:
    diem_doi = 0
    for i in range(0, len(chuoi)):
        if nho_nhat < int(chuoi[i]):
            diem_doi = i
            break
    mang_tam[vi_tri], mang_tam[diem_doi] = mang_tam[diem_doi], mang_tam[vi_tri]
kq = ""

for c in mang_tam:
    kq += c
print(int(kq))

#W9A4
so_luong = int(input())
for _ in range(so_luong):
    chuoi1 = input()
    chuoi2 = input()

    i = 0
    j = 0
    while i < len(chuoi1) and j < len(chuoi2):
        if chuoi1[i].lower() == chuoi2[j].lower():
            j += 1
        i += 1
        
    if j == len(chuoi2): 
        print("YES")
    else: 
        print("NO")

#W9A5
mang1 = list(map(int, input().split()))
mang2 = list(map(int, input().split()))
tim_thay = False

for i in range(len(mang2) - len(mang1) + 1):
    khop = True
    for j in range(len(mang1)):
        if mang2[i + j] != mang1[j]:
            khop = False
            break
    if khop:
        tim_thay = True
        break

if tim_thay: 
    print("YES")
else: 
    print("NO")

#W9A6
so_phan_tu = int(input())
day_so = list(map(int, input().split()))
kiem_tra = False
kq_cuoi = 0

for i in range(len(day_so) - 2, -1, -1):
    if day_so[i] < day_so[i + 1]:
        kiem_tra = True
        gia_tri_tam = day_so[i + 1]
        vt_tam = i + 1
        for j in range(i + 1, len(day_so)):
            if day_so[j] > day_so[i]: 
                if day_so[j] < gia_tri_tam:
                    gia_tri_tam = day_so[j]
                    vt_tam = j
        day_so[i], day_so[vt_tam] = day_so[vt_tam], day_so[i]
        
        kq_cuoi = day_so[0: i + 1] + sorted(day_so[i + 1:])
        break

if kiem_tra == False:
    day_so.sort()
    print(*day_so)
else:
    print(*kq_cuoi)

#W9A7
def trong_hoa(luong_hoa, so_cay):
    mang_moi = [0] + luong_hoa + [0]
    dem = 0
    for i in range(1, len(mang_moi) - 1):
        if mang_moi[i - 1] == 0 and mang_moi[i] == 0 and mang_moi[i + 1] == 0:
            mang_moi[i] = 1
            dem += 1
    return dem >= so_cay

hoa = list(map(int, input().split()))
k = int(input())
print(trong_hoa(hoa, k))

#W9A8
def kiem_tra_cat_nhau(buoc_di):
    da_di = [[0, 0]]
    toa_do_x = 0
    toa_do_y = 0
    
    for huong in buoc_di:
        if huong == "R":
            toa_do_y += 1
        elif huong == "L":
            toa_do_y -= 1
        elif huong == "U":
            toa_do_x -= 1
        elif huong == "D":
            toa_do_x += 1
            
        vi_tri_hien_tai = [toa_do_x, toa_do_y]
        if vi_tri_hien_tai in da_di:
            return True
            
        da_di.append(vi_tri_hien_tai)
        
    return False

chuoi_buoc = input()
print(kiem_tra_cat_nhau(chuoi_buoc))

#W9A9
def tim_so(mang):
    v1, v2, v3, v4, v5 = mang[0], mang[1], mang[2], mang[3], mang[4]
    ket_qua = 0
    if v1 > v2: v1, v2 = v2, v1 
    if v3 > v4: v3, v4 = v4, v3 
    if v4 > v2:
        if v3 > v5: v3, v5 = v5, v3 
        if v5 > v2:
            if v2 > v3: ket_qua = v2
            else: ket_qua = v3 
        else:
            if v5 > v1: ket_qua = v5
            else: ket_qua = v1
    else:
        if v1 > v5: v1, v5 = v5, v1
        if v5 > v4:
            if v4 > v1: ket_qua = v4
            else: ket_qua = v1
        else:
            if v5 > v3: ket_qua = v5
            else: ket_qua = v3
    return ket_qua

dau_vao = list(map(int, input().split()))
print(tim_so(dau_vao))

#W9A10
def ban_kinh(nha, lo_suoi):
    max_khoang_cach = 0
    for vi_tri_nha in nha:
        trai = 0
        phai = len(lo_suoi) - 1
        while trai < phai:
            giua = (trai + phai) // 2
            if lo_suoi[giua] < vi_tri_nha:
                trai = giua + 1
            else: 
                phai = giua
                
        kc = abs(vi_tri_nha - lo_suoi[trai])
        if trai > 0:
            kc = min(kc, abs(vi_tri_nha - lo_suoi[trai - 1]))
            
        if kc > max_khoang_cach:
            max_khoang_cach = kc
            
    return max_khoang_cach

danh_sach_nha = sorted(list(map(int, input().split())))
danh_sach_lo = sorted(list(map(int, input().split())))
print(ban_kinh(danh_sach_nha, danh_sach_lo))
