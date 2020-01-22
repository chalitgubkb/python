#จงแสดงข้อมูลตามผลรันต่อไปนี้ ด้วย forloop และให้แสดงลำดับของแต่ละข้อมูล
#  1. P
#  2. K
#  3. R
#  4. U
def a():
    c='P','K','R','U'
    for i in range(len(c)):
     print(i+1,c[i],sep='. ')
a()