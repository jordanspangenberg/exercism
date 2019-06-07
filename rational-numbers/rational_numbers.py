from __future__ import division
from fractions import gcd
from math import sqrt


class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be 0")
        _gcd = gcd(numer, denom)
        self.numer = numer / _gcd
        self.denom = denom / _gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self , other):
        n = (self.numer * other.denom) + (other.numer * self.denom)
        d =  (self.denom * other.denom)
        return Rational(n, d)

    def __sub__(self, other):
        n = (self.numer * other.denom) - (other.numer * self.denom)
        d =  (self.denom * other.denom)
        return Rational(n, d)

    def __mul__(self, other):
        n = (self.numer * other.numer)
        d = (self.denom * other.denom)
        return Rational(n, d)

    def __truediv__(self, other):
        n = self.numer * other.denom
        d = self.denom * other.numer

        if d == 0:
            raise ValueError("Denominator cannot be 0")
        return Rational(n,d)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer**power, self.denom**power)
        if power < 0:
            power = abs(power)
            return Rational(self.denom**power, self.numer**power)
        return Rational(1,1)


    def __rpow__(self, base):
        return base**(self.numer / self.denom)
        
