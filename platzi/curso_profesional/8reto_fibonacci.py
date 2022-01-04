import time



class FiboIter():

    
    
    def __iter__(self): 
        max_valor = int(input("ingresa el maximo de numero hasta llegar la serie: "))
        self.max_valor = max_valor
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux

            if self.aux >= self.max_valor:
                raise StopIteration

            else:
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1)#pausar el eolemento 0.05 segundos antes de la siguiente vuelta