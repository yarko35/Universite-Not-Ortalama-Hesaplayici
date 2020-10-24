import time
import math

def ortalamahesaplayıcı(x,y):
    vize=x*(4/10)
    final=y*(6/10)
    return vize+final

def ortalama_hesaplayıcı_yarısı(a,b):
    vize=a*(5/10)
    final=b*(5/10)
    return vize+final


while True:
    print("******** made by YAVUZ YARKIN OKULAR ********")

    işlem=input("\n----------PAÜ Ortalama hesaplayıcı----------\nStandart ortalama için:'1'\nOrtalama %50 ise: '2'\nÇıkmak için 'q' e  basınız: ")

    if işlem=='1':

        try:
            vize1=float(input("Vize notunuzu giriniz:"))
            final1=float(input("Final notunuzu giriniz:"))
            tamnot=ortalamahesaplayıcı(vize1,final1)
            print("Vize notunuz: {}\nFinal notunuz:{}\nOrtalamanız:{}".format(vize1,final1,tamnot))


            if tamnot>95:
                print("Harf notunuz: A1")

            elif tamnot>90:
                print("Harf notunuz: A2")

            elif tamnot>85:
                print("Harf notunuz: A3")

            elif tamnot>80:
                print("Harf notunuz: B1")

            elif tamnot>75:
                print("Harf notunuz: B2")

            elif tamnot>70:
                print("Harf notunuz: B3")

            elif tamnot>65:
                print("Harf notunuz: C1")

            elif tamnot>60:
                print("Harf notunuz: C2")

            elif tamnot>55:
                print("Harf notunuz: D1")

            elif tamnot>50:
                print("Harf notunuz: D2")

            else:
                print("Notunuzu 'F1' olarak işaretleyebilirsiniz.")
            print("Ana menüye yönlendiriliyorsunuz...")
            time.sleep(2)

        except ValueError:
            print("Lütfen sayısal bir karakter girin...")
            time.sleep(2)






    elif işlem=='2':

        try:
            vize2=float(input("Vize notunuzu giriniz:"))
            final2=float(input("Final notunuzu giriniz:"))
            tamnot1=ortalama_hesaplayıcı_yarısı(vize2,final2)
            print("Vize notunuz: {}\nFinal notunuz:{}\nOrtalamanız:{}".format(vize2,final2,tamnot1))



            if tamnot1>95:
                print("Harf notunuz: A1")

            elif tamnot1>90:
                print("Harf notunuz: A2")

            elif tamnot1>85:
                print("Harf notunuz: A3")

            elif tamnot1>80:
                print("Harf notunuz: B1")

            elif tamnot1>75:
                print("Harf notunuz: B2")

            elif tamnot1>70:
                print("Harf notunuz: B3")

            elif tamnot1>65:
                print("Harf notunuz: C1")

            elif tamnot1>60:
                print("Harf notunuz: C2")

            elif tamnot1>55:
                print("Harf notunuz: D1")

            elif tamnot1>50:
                print("Harf notunuz: D2")

            else:
                print("Notunuzu 'F1' olarak işaretleyebilirsiniz.")
            print("Ana menüye yönlendiriliyorsunuz...")
            time.sleep(2)
        except ValueError:
            print("Lütfen sayısal bir değer girin..")
            time.sleep(2)

    elif işlem=='q':
        break
