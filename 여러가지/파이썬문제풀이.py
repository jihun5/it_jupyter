# 다음의 주가가 89,000 네이버의 주가가 751,000일 때
# 다음 주식 100주,네이버 주식 20주를 가지고 있을 떄 
# 그 사람이 가지고 있는 주식의 총액을 계산하는 프로그램을 작성하시오
# Daum = 89000
# Naver = 751000
# x = int(input("다음은 몇 주를 가지고 있습니까?"))
# y = int(input("네이버는 몇 주를 가지고 있습니까?"))
# print(f"다음의 주식의 총액은? :{Daum*x}, 네이버의 주식총액은{Naver*y}")
# --------------------------------------------------------------------------
# 문제 1에서 구한 주식 총액에서 
# 다음과 네이버의 주가가 각각 5%씩 10%씩 하락한 경우에 손실액을 구하는
# 프로그램을 작성하시오
# a = int(input("다음 하락한 퍼센트:"))
# b = int(input("네이버 하락한 퍼센트:"))
# print(f"다음의 주식이 하락한 경우{(Daum*x)*(a/100)},네이버 주식이 하락한 경우{(Naver*y)*(b/100)}")
#------------------------------------------------------------------------------
# myWeight = int(input("체중을 입력해주세요(kg):"))
# myHeight = int(input("키를 입력해주세요:"))/100
# # 신체질량 지수(BMI) = 체중(kg)/[신장(m)]**2
# my_BMI = int(myWeight/(myHeight**2))
# print(my_BMI)
#------------------------------------------------------------------------------
# s = "Daum KaKao"
# new_s1 = s[0:4]
# new_s2 = s[5:-1]
# print(new_s2 +' '+ new_s1)
#------------------------------------------------------------------------------
# url = r'C:\myphoto\helloworld.jpg'
# path = "C:\\myphoto\\helloworld.jpg"
# # 마지막 역슬레시의 위치
# p1 = path.rfind("\\")
# # 마지막 점(.)의 위치
# p2 = path.rfind(".")
# # 폴더 위치
# folder = path[:p1]
# print(f"폴더의 위치 :{folder}")
# file = path[p1+1:p2]
# ext = path[p2+1:]
#------------------------------------------------------------------------------

grade = [82,74,93,65,32,71,90,88,74]
# w = max(grade)
# grade.remove(w)
# w1 = max(grade)
# grade.remove(w1)
# w2 = max(grade)
# print((w+w1+w2)/3)
    
math = [82,74,93,65,32,71,90,88,74]
# math.sort()
# print(math[-3:])
# A = math[-3:]
# sum(A)
# print(sum(A)/len(A))
# math.sort(reverse=True)
# print(math)

# for a in range(0, len(grade)-1):
#     for b in range(a+1, len(grade)):
#         if grade[a] > grade[b]:
#             grade[a],grade[b] = grade[b],grade[a]
# print(set(grade))

#------------------------------------------------------------------------------
# my_age = int(input("본인의 나이를 입력해주세요:"))
# if my_age < 10:
#     print("어린이입니다.")
# if my_age < 20:
#     print("10대입니다.")
# if my_age < 30:
#     print("20대입니다.")
# if my_age < 40:
#     print("30대입니다.")
# if my_age < 50:
#     print("40대입니다.")
# if my_age < 60:
#     print("50대입니다.")
# else:
#     print("노년층입니다.")

#------------------------------------------------------------------------------
# myWeight = int(input("체중을 입력해주세요(kg):"))
# myHeight = int(input("키를 입력해주세요:"))
# # 키 150이하면 표준체중 = 신장 -110
# # 키 150초과 표준체중 (신장 - 110) x 0.9
# avg = 0
# if myHeight <= 150:
#     avg = myHeight - 110
# elif myHeight > 150:
#     avg = (myHeight -110) *0.9
# obesity = ((myWeight-avg)/avg)*100
# print(obesity)
# if obesity < 20:
#     print("정상")
# elif obesity <= 30:
#     print("경도비만(주의)")
# elif obesity <= 50:
#     print("중증도비만(위험)")
# else:
#     print("고도비만(매우위험)")

#------------------------------------------------------------------------------

# 짝수의 합 구하기
# 조건문을 안쓰고?
# a = 1
# while a < 101 and a%2==0:
#     a += 1
# print(a)
# for a in 100:
#     if a
#------------------------------------------------------------------------------
# lista = ["A","A","A",'O','B','B','O','AB','AB','O']
# dicta = {}
# # result = {"A": 0}
# for a in lista:
#     if a not in dicta.keys():
#         dicta[a] = lista.count(a)
# print(dicta)
#------------------------------------------------------------------------------
# a = int(input("숫자를 입력해주세요 : "))
# result = 1
# for i in range(1, a+1):
#     result *= i
# print(result)
#------------------------------------------------------------------------------
# dice = [1,2,3,4,5,6]
# result = []
# for a in range(len(dice)): # a = 1,2,3,4,5,6
#     for i in range(len(dice)):
#         if dice[a] + dice[i] == 6:
#             result.append(a+1)
#             result.append(i+1)
# print(result)
# A = result[0:2] 
# print(A)
#------------------------------------------------------------------------------
# x = int(input("숫자를 입력하세요 :"))
# y = int(input("숫자를 입력하세요 :"))
# num = 0
# for a in range(1, 100):
#     if x%a ==0 and y%a ==0:
#         num += a
# print(num)
#------------------------------------------------------------------------------
# 평일에는 시급 9500원, 주말에는 시급 13000원
# 일주일간 총 급여
# t1 = 4*9500
# t2 = 3*9500
# t3 = 3*9500
# t4 = 4*9500
# t5 = 5*9500
# s1 = 7*13000
# s2 = 6*13000
# w = [4,3,3,4,5]
# s = [7,6]
# A = 9500
# B = 13000
# # w[a]번째에 A를 곱하면 되겠군
# # s[a]번째에 B를 곱하면
# num1 = 0
# num2 = 0
# for a in range(len(w)):
#     num1 += w[a]*A
# print(num1)
# for b in range(len(s)):
#     num2 += s[b]*B
# print(num2)
# print(num1+num2)

#------------------------------------------------------------------------------

# lista = [291,586,460,558,18,72] # 수량리스트
# listb = [500,320,100,120,92,30] # 가격리스트

# dict1 = {"수량":lista[0], "단가":listb[1]}