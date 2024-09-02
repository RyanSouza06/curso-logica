print('0 - fim')
print('1 - Inclui ')
print('2 - Altera ')
print('3 - Exclui ')
print('4 - Consulta')

escolha = int(input('opção: '))
if escolha == 0:
    print('fim do cadastro')
elif escolha == 1:
    print('Item incluído')
elif escolha == 2:
    print('Item alterado')
elif escolha == 3:
    print('Item excluído')
elif escolha == 4:
    print('Item consultado')
else: print('Opção inválida')
