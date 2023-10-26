
###
### Trabalho 01 de Metodos Numericos Para Equacoes Diferenciais II
### UERJ - IPRJ - 2023.2
### Professor: Grazione Souza
### Aluno: Manoel Rodrigues - 201910073511
###

###
### Lembre-se de instalar o matplotlib (pip install matplotlib ou pip3 install matplotlib)
###

import matplotlib.pyplot as plt

class MVF:
    def __init__(self, alfa, uBarra, comprimento, comprimeiroIntermediario, Ca, Cb, numVolumes, tempo,  deltaT, tempoIntermed):
        self.alfa = alfa
        self.uBarra = uBarra
        self.comprimento = comprimento
        self.comprimeiroIntermediario = comprimeiroIntermediario
        self.Ca = Ca
        self.Cb = Cb
        self.numVolumes = numVolumes
        self.tempo = tempo
        self.deltaT = deltaT
        self.deltaX = comprimento / numVolumes
        self.tempoIntermed = tempoIntermed
        

        self.deltaTMax = 0.9 * (1 / ((uBarra / self.deltaX) + (2 * alfa / (self.deltaX * self.deltaX))))
        print("DeltaTMax")
        print(self.deltaTMax)

        if self.deltaT > self.deltaTMax:
            print("DeltaT maior que o máximo permitido.")
            return
        else:
            print("DeltaT menor que o máximo permitido.")
                


    def generate(self):
        changed = False
        concentracaoInicialUsada = self.Ca

       
        Qn = [0.0] * int(self.numVolumes)
        QnMaisUm = [0.0] * int(self.numVolumes)

        for i in range(0, int(numVolumes)):
            if(i < numVolumes/2):
                Qn[i] = Ca
                QnMaisUm[i] = Ca
            else:
                Qn[i] = Cb
                QnMaisUm[i] = Cb


        tempoAux = 0.0

        self.deltaTMax = 0.8 * (1 / ((self.uBarra / self.deltaX) + (2 * self.alfa / (self.deltaX * self.deltaX))))
        
        if self.deltaT > self.deltaTMax:
            print("DeltaT maior que o máximo permitido.")
            return

        while tempoAux < self.tempo:
            if(tempoAux < self.tempoIntermed):
                concentracaoInicialUsada = self.Cb


            ###
            ### Contorno inicial
            ###
            QnMaisUm[0] = Qn[0] - (self.deltaT / self.deltaX) * ((self.uBarra * 2 * (Qn[0] - concentracaoInicialUsada) - (self.alfa * (Qn[1] - 3 * Qn[0] + 2 * concentracaoInicialUsada) /  self.deltaX)))
            
            ###
            ### Meio do volume
            ###
            for i in range(1, int(self.numVolumes) - 2):
                QnMaisUm[i] = Qn[i] - (self.deltaT / self.deltaX) * ( self.uBarra * (Qn[i] - Qn[i - 1]) - ((self.alfa * (Qn[i + 1] - 2 * Qn[i] + Qn[i - 1])) / self.deltaX))
            
            ###
            ### Contorno final
            ###
            QnMaisUm[int(self.numVolumes) - 1] =  Qn[int(self.numVolumes) - 1] - (self.deltaT / self.deltaX) * ( self.uBarra * (Qn[int(self.numVolumes) - 1] - Qn[int(self.numVolumes) - 2]) - ((self.alfa * (- Qn[int(self.numVolumes) - 1] + Qn[int(self.numVolumes) - 2])) / self.deltaX))

            Qn = QnMaisUm
            tempoAux += self.deltaT

        print('QnMaisUm:', QnMaisUm)
        return QnMaisUm
    

    def plotInitialValues(self):
        Qini = [self.Ca] * int(self.numVolumes)
        x = [i * self.deltaX / 2 for i in range(int(self.numVolumes))]
        
        for i in range(0, int(numVolumes)):
            if(i <= numVolumes/2):
                Qini[i] = Ca
            else:
                Qini[i] = Cb

        plt.plot(x, Qini)
        plt.xlabel('Posição')
        plt.ylabel('Concentração')
        plt.title('Difusão e Advecção - Valores Iniciais')
        plt.grid(True)
        plt.scatter(x, Qini)
        plt.show()
        

    def plot(self):
        Qn = self.generate()
        x = [i * self.deltaX / 2 for i in range(int(self.numVolumes))]
        plt.plot(x, Qn)
        plt.xlabel('Posição')
        plt.ylabel('Concentração')
        plt.title('Difusão e Advecção')
        plt.grid(True)
        plt.scatter(x, Qn)
        plt.show()

if __name__ == "__main__":
    alfa = 0.01
    uBarra = 0.0001
    comprimento = 18
    comprimeiroIntermediario = 6
    Ca = 0.9
    Cb = 0.2
    numVolumes = 64
    tempo = 300
    deltaT = 0.1
    tempoIntermed = 150


    mvf = MVF(alfa, uBarra, comprimento, comprimeiroIntermediario, Ca, Cb, numVolumes, tempo, deltaT, tempoIntermed)
    #mvf.plotInitialValues()
    mvf.plot()