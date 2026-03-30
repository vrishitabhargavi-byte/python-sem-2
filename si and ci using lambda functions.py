ci=lambda p,t,r:(p*(1+r/100)**t)
print(ci(10000,2,3))
si=lambda p,t,r:(p*t*r)/100
print(si(10000,2,3))