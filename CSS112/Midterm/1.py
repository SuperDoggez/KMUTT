dog_age = int(input("ใส่อายุสุนัขของท่าน (เป็นจำนวนปีถ้วนๆ) : "))
human_age = 0
if dog_age <=2 :
    if dog_age == 1 :
        human_age = 11
    elif dog_age == 2 :
        human_age = 22
    else :
        human_age = 0
else :
    dog_agebefore2 = 2*11
    human_age = dog_agebefore2 + ((dog_age - 2)*4)

print("อายุสุนัขของท่านเทียบเท่ากับมนุษย์อายุ {} ปี " .format(human_age))