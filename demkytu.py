def dem_ky_tu(txt):
    result = 0
    for kytu in txt:
        result += 1
    return result
    
chuoi = input('nhap chuoi: ')

print('so ky tu: ', dem_ky_tu(chuoi))