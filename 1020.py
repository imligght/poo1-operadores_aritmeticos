# -*- coding: utf-8 -*-

idadeDias = int(input())
anos = idadeDias//365
meses = (idadeDias - anos*365)//30
dias = idadeDias - meses*30 - anos*365

print("%d ano(s)" % (anos))
print("%d mes(es)" % (meses))
print("%d dia(s)" % (dias))