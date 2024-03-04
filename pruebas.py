import time 
hora = time.strftime("%I:%M:%p %d/%m/%Y")
a = ["cocina","lavar","caminar"]


m = [f"{(1+i)}. {n} {hora}" for i, n in enumerate(a)]

print(" ".join(m))

