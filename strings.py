# -*- coding: latin1 -*-

s = 'Camel'

# Concatenação
print 'The ' + s + ' run away!'

# Interpolação
print 'tamanho de %s => %d' % (s, len(s))

# String tratada como sequência
for ch in s: print ch

# Strings são objetos
if s.startswith('C'): print s.upper()

# O que acontecerá?
print 3 * s