from django import template

register = template.Library()

@register.filter(name='calculo_emprestimo')
def mostrar_duracao_emprestimo(data_devolucao, data_emprestimo):
    return (data_devolucao - data_emprestimo).days