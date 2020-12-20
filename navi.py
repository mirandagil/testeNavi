import numpy as np

def paresMultiplos(n = 5000000, step = 37*49):
    rng = [i*step for i in range(1,int(n/step) +1) if i*step%2 == 0]
    return len(rng)


def paresMultiplosUnpack(n = 5000000, step = 37*49):
    if step % 2 == 0:
        m = 1
    else:
        m = 2
    rng = range(step*m, n, step*m)
    return len([*rng])

def paresMultiplosMat(n = 5000000, step = 37*49):
    if step % 2 == 0:
        m = 1
    else:
        m = 1/2
    return int(n/step * m)

def vetorX(n = 10):
    X = [3**i+7*np.math.gamma(i+1) if i%2 == 0 else 2**i+4*np.log(i) for i in range(n)]
    print(f'O indice do maior valor no vetor é {np.argmax(X)}, sua média é {np.mean(X):.2f}')
    return X

def vetorXMat(n = 10):
    pg1 = (3**(n)-1)/(3**2 -1)
    pg2 = 2*(2**n-1)/(2**(2)-1)
    log = 4*np.log(np.math.gamma(2*(n/2))/(2**(n/2) * np.math.factorial(n/2)) + 1)
    fact = np.array([7*np.math.gamma(i+1) for i in range(n) if i%2 == 0]).sum()
    print(f'O indice do maior valor no vetor é {(n-1)-(n-1)%2}, sua média é {(1/n * (pg1+pg2+log+fact)):.2f}')
    return None

def nota(n = 5):
    notas = []
    for i in range(1,n+1):
        while True:
            try:
                nota_aluno = (float(input('Insira a nota do aluno ' + str(i) +' ')))
                break
            except:
                print("Nota deve ser um valor númerico! Tente novamente")
        notas.append(nota_aluno)
    dic_notas = dict(zip(range(1,n+1), notas))
    maiorNota = max(dic_notas, key=dic_notas.get)
    print(f'O aluno com a maior nota é o aluno {maiorNota}, sua nota foi: {dic_notas[maiorNota]}')
    return dic_notas