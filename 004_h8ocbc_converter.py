# ------ readMe ------
# Program ini sudah dibuat sesuai requirements assignment yang ada pada modul kode.id
# Program ini terdapat improve untuk melakukan validasi input
# 3 fungsi utama yang dibuat sudah sesuai dengan apa yang diminta pada modul kode.id
# FSDO001ONL004 - Lukas Hansel Ganda

# FUNGSI kelcev
# Buatlah sebuah function yang dapat mengkonversi suhu
# dari kelvin ke celcius, dan celcius ke kelvin.
def kelcev(drjt, inputan):
    if inputan.upper() == 'C':
        result = float(drjt + 273.15)
        jenis = "Celcius"
        converto = "Kelvin"
    elif inputan.upper() == 'K':
        result = float(drjt - 273.15)
        jenis = "Kelvin"
        converto = "Celcius"
    else:
        result = "Error"
        jenis = ''
        converto = ''
    return result, jenis, converto

# FUNGSI goFahrenheit
# Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
# Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan 
# adalah celcius atau kelvin. 
# Panggil function yang pertama jika diperlukan.
def goFahrenheit (drjt, inputan):
    if inputan.upper() == 'K':
        panggil = kelcev(drjt, inputan)
        drjt = panggil[0]
        jenis = "Kelvin"
        converto = "Fahrenheit"
        result = float((9 * drjt) / 5 + 32)
    elif inputan.upper() == 'C':
        jenis = "Celcius"
        converto = "Fahrenheit"
        result = float((9 * drjt) / 5 + 32)
    else:
        result = "Error"
    return result, jenis, converto

# FUNGSI fromFahrenheit
# Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. 
# Berikan argumen untuk memastikan bahwa 
# outputnya dalah celcius atau kelvin.
def fromFahrenheit (drjt, inputan):
    if inputan.upper() == 'F':
        resultcel = float((drjt - 32) * 5 / 9)
        convertocel = "Celcius"
        resultkel = float(((drjt - 32) * 5 / 9) + 273.15)
        convertokel = "Kelvin"
        jenis = "Fahrenheit"
    return jenis, resultcel, convertocel, resultkel, convertokel

# FUNGSI validasi jenis suhu input dan range suhu input
def validasi(drjt, inputan):
    rangecelcius = range(0,101,1)
    rangekelvin = range(273,374,1)
    rangefahrenheit = range(32,213,1)
    result = "MASUKKAN JENIS SUHU DENGAN BENAR!"
    if inputan.upper() == 'C':
        if drjt not in rangecelcius:
            result = "SUHU Celcius OUT OF RANGE"
        else:
            result = "Good"
    elif inputan.upper() == 'K':
        if drjt not in rangekelvin:
            result = "SUHU Kelvin OUT OF RANGE"
        else:
            result = "Good"    
    elif inputan.upper() == 'F':
        if drjt not in rangefahrenheit:
            result = "SUHU Fahrenheit OUT OF RANGE"
        else:
            result = "Good"
    return result

def main():
    print("Program konversi suhu")
    loop = True
    while(loop):
        suhu = input("Masukkan suhu? (Misal: 30C, 20F, 21K): ")
        # Mengambil selain karakter terakhir
        drjt = int(suhu[:-1])
        # Mengambil karakter terakhir
        inputan = suhu[-1]
        valid = validasi(drjt, inputan)
        if valid == "Good":
            if (inputan.upper() == 'C') or (inputan.upper() == 'K'):
                ocbc = kelcev(drjt, inputan)
                print(drjt, ocbc[1], "=", "{:.1f}".format(ocbc[0]), ocbc[2])
                toFahren = goFahrenheit(drjt, inputan)
                print(drjt, toFahren[1], "=", "{:.1f}".format(toFahren[0]), toFahren[2])
            elif inputan.upper() == 'F':
                fromFahren = fromFahrenheit(drjt, inputan)
                print(drjt, fromFahren[0], "=", "{:.1f}".format(fromFahren[1]), fromFahren[2])
                print(drjt, fromFahren[0], "=", "{:.1f}".format(fromFahren[3]), fromFahren[4])
        else:
            print(valid)
        bom = input("Konversi suhu lagi? [y/n]")
        if bom.upper() == 'N':
            loop = False
            print("Terimakasih")
            break
        elif bom.upper() == 'Y':
            loop = True
        else:
            print("MASUKKAN INPUT DENGAN BENAR")
            break

main()