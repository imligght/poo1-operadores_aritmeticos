# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
nome = input()
salario = float(input())
vendas = float(input())
comissao = (15/100) * vendas
salariofinal = salario + comissao

print("TOTAL = R$ %.2f" % salariofinal)