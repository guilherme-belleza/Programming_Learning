# =============================================================================
# MÉTODOS MÁGICOS PARA OPERADORES
# =============================================================================

# Comparação
# -----------------------------------------------------------------------------
# Equal to (igual)                  p1 == p2        p1.__eq__(p2)
# Not equal (diferente)             p1 != p2        p1.__ne__(p2)
# Less than (menor que)             p1 < p2         p1.__lt__(p2)
# Less or equal (menor/igual)       p1 <= p2        p1.__le__(p2)
# Greater than (maior que)          p1 > p2         p1.__gt__(p2)
# Greater or equal (maior/igual)    p1 >= p2        p1.__ge__(p2)

# Atribuição aumentada
# -----------------------------------------------------------------------------
# Add and assign (somar e atribuir)          p1 += p2       p1.__iadd__(p2)
# Subtract and assign (subtrair e atribuir)  p1 -= p2       p1.__isub__(p2)
# Multiply and assign (multiplicar e atribuir) p1 *= p2     p1.__imul__(p2)
# Divide and assign (dividir e atribuir)     p1 /= p2       p1.__itruediv__(p2)
# Floor divide and assign                   p1 //= p2      p1.__ifloordiv__(p2)
# Modulo and assign                         p1 %= p2       p1.__imod__(p2)
# Power and assign                          p1 **= p2      p1.__ipow__(p2)

# Matemáticos
# -----------------------------------------------------------------------------
# Add (somar)                       p1 + p2        p1.__add__(p2)
# Subtract (subtrair)               p1 - p2        p1.__sub__(p2)
# Multiply (multiplicar)            p1 * p2        p1.__mul__(p2)
# True division (divisão)           p1 / p2        p1.__truediv__(p2)
# Floor division (divisão inteira)  p1 // p2       p1.__floordiv__(p2)
# Modulo (resto da divisão)         p1 % p2        p1.__mod__(p2)
# Power (potência)                  p1 ** p2       p1.__pow__(p2)


# Outros
# -----------------------------------------------------------------------------
# Negative (negativo)               -p1            p1.__neg__()
# Positive (positivo)               +p1            p1.__pos__()
# Length (tamanho)                  len(p1)         p1.__len__()
# Get item (obter item)             p1[key]         p1.__getitem__(key)
# String (texto)                    str(p1)         p1.__str__()
# Representation (representação)    repr(p1)        p1.__repr__()