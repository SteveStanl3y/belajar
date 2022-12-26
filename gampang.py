# kegiatan assignment nilai
a = 10
x = 5

# pemanggilan pertama
panjang = 1000
print("nilai a =", a)
print("nilai x =", x)
print("nilai panjang =", panjang)


# penamaan
nilai_y = 15
juta10 = 10000000
nilaiZ = 17.5

# pemanggilan kedua
print("nilai a =", a)
a = 7
print("nilai a =", a)

# assignment indirect
b = a
print("nilai b =", b)
# a = 10, a adalah variabel dengan nilai 10

# tipe data: angka satuan (integer)
data_integer = 1
print("data :", data_integer)
print("- bertipe :", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data :", data_float)
print("- bertipe : ", type(data_float))

# tipe data: angka dengan karakter (string)
data_string = "steve"
print("data :", data_string)
print("- bertipe : ", type(data_string))

# tipe data : biner true / false (boolean)
data_bool = True
print("data :", data_bool)
print("- bertipe : ", type(data_bool))

# bilangan kompleks
data_complex = complex(5, 6)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))


# tipe data integer
data_integer = 1
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data float
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))


# tipe data string
data_string = "steve"
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data bool
data_bool = True
print("data : ", data_bool, ", bertipe : ", type(data_bool))

# tipe data khusus
data_complex = complex(7, 6)
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# belajar casting
# merubah dari satu tipe ke tipe lain

## INTEGER##


data_integer = 0
print("data = ", data_integer, ", type =", type(data_integer))

data_float = float(data_integer)
data_string = str(data_integer)
data_bool = bool(data_integer)  # akan false jika nilai int = 0

print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_integer, ", type =", type(data_integer))
print("data = ", data_bool, ", type =", type(data_bool))

## FLOAT##


data_float = 0
print("data = ", data_float, ", type =", type(data_float))

data_integer = int(data_float)  # akan di bulatkan kebawah
data_string = str(data_float)
data_bool = bool(data_float)  # false jika nilai = 0

print("data = ", data_integer, ", type =", type(data_integer))
print("data = ", data_string, ", type =", type(data_string))
print("data = ", data_bool, ", type =", type(data_bool))

## BOOLEAN##

data_bool = True
print("data = ", data_bool, ", type =", type(data_bool))

data_integer = int(data_bool)  # akan di bulatkan kebawah
data_string = str(data_bool)
data_bool = float(data_bool)  # false jika nilai = 0

print("data = ", data_integer, ", type =", type(data_integer))
print("data = ", data_string, ", type =", type(data_string))
print("data = ", data_bool, ", type =", type(data_bool))

## STRING##

data_string = "10"
print("data = ", data_string, ", type =", type(data_string))

data_integer = int(data_string)  # string harus angka
data_float = float(data_string)  # string harus angka
data_bool = bool(data_string)  # false jika nilai string 0
print("data = ", data_integer, ", type =", type(data_integer))
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))
