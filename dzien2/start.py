import pakiet

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()

from pakiet import fun1

fun1.powitanie()  # Hello!!!

# import jako alias
import pakiet.fun1 as pk1

pk1.powitanie()  # Hello!!!

pakiet.info()  # Wersja pakietu v1.1.23
