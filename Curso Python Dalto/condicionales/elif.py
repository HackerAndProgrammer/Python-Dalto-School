ingreso_mensual = 0

gasto_mensual = 15000

#if anidados y else-if(elif)

if ingreso_mensual > 10000:
     if ingreso_mensual - gasto_mensual <= 0:
         print("estas en deficit")
     elif ingreso_mensual - gasto_mensual > 3000:
         print("bien pa, estas bien") 
     else:
         print("y pa, estas gastando una banda, hay que ver si te alcanza")         

elif ingreso_mensual > 1000:
     print("estas bien economicamente en latinoamerica")
elif ingreso_mensual > 500:
     print("estas bien economicamente en Argentina")
elif ingreso_mensual > 200:
     print("estas bien economicamente en Venezuela")     
else:
    print("sos pobre")

       
         