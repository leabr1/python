tempo_seg=int(input("Insira o tempo do relógio: "))
tempo=tempo_seg
tempo_min= tempo_seg//60
tempo_seg=tempo_seg%60
tempo_hora=tempo_min//60
tempo_min=tempo_min%60
print("Tempo %d -> %d horas %d minutos %d segundos" %(tempo,tempo_hora,tempo_min,tempo_seg))