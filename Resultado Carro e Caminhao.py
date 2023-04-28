d = 100

vel_carro = 110

vel_caminhao = 80

t_carro = d / vel_carro

t_caminhao = d / vel_caminhao + 2 * 5 / 60

d_carro = vel_carro * t_carro

d_caminhao = vel_caminhao * t_caminhao

if d_carro < d_caminhao:
    print("O carro está mais próximo de Ribeirão Preto")
else:
    print("O caminhão está mais próximo de Ribeirão Preto")
