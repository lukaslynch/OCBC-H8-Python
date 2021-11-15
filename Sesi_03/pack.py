# import pkg.mod1, pkg.mod2
# print(pkg.mod1.kitchen_sets)
# print(pkg.mod2.artist_kits)

# from pkg.mod1 import kitchen_sets
# print(kitchen_sets)

# from pkg.mod1 import kitchen_sets as ks
# print(ks)

# from pkg import mod1
# print(mod1.kitchen_sets)


from pkg import mod2 as m2
print(m2.color)
print(m2.artist_name)