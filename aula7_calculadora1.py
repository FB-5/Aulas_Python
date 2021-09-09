# MÉTODO E FUNÇÕES(em minúscula)/CLASSES (em maiúscula)

# Funçao (return) é tudo aquilo que retorna um valo.
# Método (def - em python) não retorna valor.

class Calculadora:
    def _init_(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
     calculadora = Calculadora(10, 2)
     print(calculadora.soma())
     print(calculadora.subtracao())
     print(calculadora.divisao())
     print(calculadora.multiplicacao())


# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10, 2))
