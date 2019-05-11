class bebe:
    def __init__(self, nombre):
        self.nombre_bebe= nombre

    def llora(self):
        print('Llorar')

    def come(self):
       print('bebe come')

    def respira(self):
        print('respira')

    def duerme(self):
        print('duerme')

    def crecer(self,edad=1):
        self.edad=edad + 1






d=bebe('Cicieron')
d.come()
d.llora()
d.respira()
d.crecer()
print('Mi nombre es ', d.nombre_bebe,'y tengo' , d.edad, 'años de edad')

