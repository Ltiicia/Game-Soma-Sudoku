'''/**************************** 
 Autor: Letícia Gonçalves Souza
 Componente Curricular: MI algoritmos  
 Concluido em:11/11/2022 
 Declaro que este código foi elaborado por mim de forma individual e não contém nenhum  
 trecho de código de colega ou de outro autor, tais como provindos de livros e apostilas,
 e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra 
 autoria que não a minha está destacado com uma citação do autor e a fonte do código, e estou  
 ciente que estes trechos não serão considerados para fins de avaliação. 
 /*****************************'''


import random

def tabuleiro_4x4(sec1_oc, sec2_oc, sec3_oc, sec4_oc): #FUNÇAO PARA PRINTAR O TABULEIRO 4X4
    print(f'[{sec1_oc[0]}  {sec1_oc[1]}] | [{sec2_oc[0]}  {sec2_oc[1]}] ', end='')
    print(f'{somalin1}')
    print(f'[{sec1_oc[2]}  {sec1_oc[3]}] | [{sec2_oc[2]}  {sec2_oc[3]}] ', end='')
    print(f'{somalin2}')
    print('----'*4)
    print(f'[{sec3_oc[0]}  {sec3_oc[1]}] | [{sec4_oc[0]}  {sec4_oc[1]}] ', end = '')
    print(f'{somalin3}')
    print(f'[{sec3_oc[2]}  {sec3_oc[3]}] | [{sec4_oc[2]}  {sec4_oc[3]}] ', end='')
    print(f'{somalin4}')
    print(f'{somacol1}   {somacol2}   {somacol3}  {somacol4}  ',end='')
    if sessão1_oc[0] !=0 and sessão1_oc[3] !=0 and sessão4_oc[0] !=0 and sessão4_oc[3] !=0:
        print(f'{somadiag}')
    print()

def sec_jogadas4x4(opc_sec, opc_val, sec_oc, sec, n, x): #FUNÇÃO PARA AS JOGADAS EM CADA SESSÃO DO TABULEIRO 4X4
    if int(opc_sec) == n and int(opc_val) == x:
        if sec[0] == x and sec_oc[0] == 0:
            sec_oc[0] = x
        elif sec[1] == x and sec_oc[1] == 0:
            sec_oc[1] = x
        elif sec[2] == x and sec_oc[2] == 0:
            sec_oc[2] = x
        elif sec[3] == x and sec_oc[3] == 0:
            sec_oc[3] = x
        else:
            print('Valor repetido, jogada perdida')

def substitui4x4(jogadas, esc_sec, esc_val, sec_oc, sec, n): #FUNÇÃO PARA SUBSTITUIR VALORES NO TABULEIRO 4X4
    if int(esc_sec) == n:
        if int(esc_val) == 1:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 1)
        elif int(esc_val) == 2:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 2)
        elif int(esc_val) == 3:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 3)
        elif int(esc_val) == 4:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 4)

def tabuleiro_9x9(sec1_oc, sec2_oc, sec3_oc, sec4_oc, sec5_oc, sec6_oc, sec7_oc, sec8_oc, sec9_oc): #FUNÇÃO PARA PRINTAR O TABULEIRO 9X9
    print(f'[{sec1_oc[0]}  {sec1_oc[1]}  {sec1_oc[2]}] | [{sec2_oc[0]}  {sec2_oc[1]}  {sec2_oc[2]}] | [{sec3_oc[0]}  {sec3_oc[1]}  {sec3_oc[2]}] ', end='')
    print(f'{somalin1}')
    print(f'[{sec1_oc[3]}  {sec1_oc[4]}  {sec1_oc[5]}] | [{sec2_oc[3]}  {sec2_oc[4]}  {sec2_oc[5]}] | [{sec3_oc[3]}  {sec3_oc[4]}  {sec3_oc[5]}] ', end='')
    print(f'{somalin2}')
    print(f'[{sec1_oc[6]}  {sec1_oc[7]}  {sec1_oc[8]}] | [{sec2_oc[6]}  {sec2_oc[7]}  {sec2_oc[8]}] | [{sec3_oc[6]}  {sec3_oc[7]}  {sec3_oc[8]}] ', end='')
    print(f'{somalin3}')
    print('----'*10)
    print(f'[{sec4_oc[0]}  {sec4_oc[1]}  {sec4_oc[2]}] | [{sec5_oc[0]}  {sec5_oc[1]}  {sec5_oc[2]}] | [{sec6_oc[0]}  {sec6_oc[1]}  {sec6_oc[2]}] ', end='')
    print(f'{somalin4}')
    print(f'[{sec4_oc[3]}  {sec4_oc[4]}  {sec4_oc[5]}] | [{sec5_oc[3]}  {sec5_oc[4]}  {sec5_oc[5]}] | [{sec6_oc[3]}  {sec6_oc[4]}  {sec6_oc[5]}] ', end='')
    print(f'{somalin5}')
    print(f'[{sec4_oc[6]}  {sec4_oc[7]}  {sec4_oc[8]}] | [{sec5_oc[6]}  {sec5_oc[7]}  {sec5_oc[8]}] | [{sec6_oc[6]}  {sec6_oc[7]}  {sec6_oc[8]}] ', end='')
    print(f'{somalin6}')
    print('----'*10)
    print(f'[{sec7_oc[0]}  {sec7_oc[1]}  {sec7_oc[2]}] | [{sec8_oc[0]}  {sec8_oc[1]}  {sec8_oc[2]}] | [{sec9_oc[0]}  {sec9_oc[1]}  {sec9_oc[2]}] ', end='')
    print(f'{somalin7}')
    print(f'[{sec7_oc[3]}  {sec7_oc[4]}  {sec7_oc[5]}] | [{sec8_oc[3]}  {sec8_oc[4]}  {sec8_oc[5]}] | [{sec9_oc[3]}  {sec9_oc[4]}  {sec9_oc[5]}] ', end='')
    print(f'{somalin8}')
    print(f'[{sec7_oc[6]}  {sec7_oc[7]}  {sec7_oc[8]}] | [{sec8_oc[6]}  {sec8_oc[7]}  {sec8_oc[8]}] | [{sec9_oc[6]}  {sec9_oc[7]}  {sec9_oc[8]}] ', end='')
    print(f'{somalin9}')
    print(f'{somacol1} {somacol2} {somacol3}    {somacol4} {somacol5} {somacol6}    {somacol7} {somacol8} {somacol9}  ', end='')
    if sessão1_oc[0]!=0 and sessão1_oc[4]!=0 and sessão1_oc[8]!=0 and sessão5_oc[0]!=0 and sessão5_oc[4]!=0 and sessão5_oc[8]!=0 and sessão9_oc[0]!=0 and sessão9_oc[4]!=0 and sessão9_oc[8]!=0:
        print(f'{somadiag}')
    print()

def sec_jogadas9x9(opc_sec, opc_val, sec_oc, sec, n, x): #FUNÇÃO PARA AS JOGADAS EM CADA SESSÃO DO TABULEIRO 9X9
    if int(opc_sec) == n and int(opc_val) == x:
        if sec[0] == x and sec_oc[0] == 0:
            sec_oc[0] = x
        elif sec[1] == x and sec_oc[1] == 0:
            sec_oc[1] = x
        elif sec[2] == x and sec_oc[2] == 0:
            sec_oc[2] = x
        elif sec[3] == x and sec_oc[3] == 0:
            sec_oc[3] = x
        elif sec[4] == x and sec_oc[4] == 0:
            sec_oc[4] = x
        elif sec[5] == x and sec_oc[5] == 0:
            sec_oc[5] = x
        elif sec[6] == x and sec_oc[6] == 0:
            sec_oc[6] = x
        elif sec[7] == x and sec_oc[7] == 0:
            sec_oc[7] = x
        elif sec[8] == x and sec_oc[8] == 0:
            sec_oc[8] = x
        else:
            print('Valor repetido, jogada perdida')

def substitui9x9(jogadas, esc_sec, esc_val, sec_oc, sec, n): #FUNÇÃO PARA SUBSTITUIR VALORES NO TABULEIRO 9X9
    if int(esc_sec) == n:
        if int(esc_val) == 1:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 1)
        elif int(esc_val) == 2:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 2)
        elif int(esc_val) == 3:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 3)
        elif int(esc_val) == 4:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 4)
        elif int(esc_val) == 5:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 5)
        elif int(esc_val) == 6:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 6)
        elif int(esc_val) == 7:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 7)
        elif int(esc_val) == 8:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 8)
        elif int(esc_val) == 9:
            jogadas(esc_sec, esc_val, sec_oc, sec, n, 9)
        
val = [1,2,3,4]
val9x9 = [1,2,3,4,5,6,7,8,9]

opção = 0
print('-=-='*10)
print('       BEM VINDO AO SOMA SUDOKU!       ')
print('-=-='*10)
while int(opção) != 3:
    print('Qual nivel deseja jogar? \n[ 1 ] Nivel 1\n[ 2 ] Nivel 2\n[ 3 ] Sair do Jogo')
    opção = input('Qual sua opção? ')
    if type(opção) != int:
        while opção.isdigit() == False:
            print('Valor inválido')
            opção = input('Qual sua opção? ')
    while int(opção)<=0 or int(opção)>3:
        print('Valor inválido')
        opção = input('Qual sua opção? ')
    
    #NIVEL 1 4X4
    if int(opção) == 1:
        #LISTAS DO TABULEIRO
        sessão1_oc = [0,0,0,0]
        sessão2_oc = [0,0,0,0]
        sessão3_oc = [0,0,0,0]
        sessão4_oc = [0,0,0,0]
        sessão1 = random.sample(val, 4)
        sessão2 = random.sample(val, 4)
        sessão3 = random.sample(val, 4)
        sessão4 = random.sample(val, 4)
        jogador1 = input('Jogador 1: ')
        jogador2 = input('Jogador 2: ')
        
        #SOMA LINHA
        somalin1 = sessão1[0]+sessão1[1]+sessão2[0]+sessão2[1]
        somalin2 = sessão1[2]+sessão1[3]+sessão2[2]+sessão2[3]
        somalin3 = sessão3[0]+sessão3[1]+sessão4[0]+sessão4[1]
        somalin4 = sessão3[2]+sessão3[3]+sessão4[2]+sessão4[3]
        
        #SOMA COLUNA
        somacol1 = sessão1[0]+sessão1[2]+sessão3[0]+sessão3[2]
        somacol2 = sessão1[1]+sessão1[3]+sessão3[1]+sessão3[3]
        somacol3 = sessão2[0]+sessão2[2]+sessão4[0]+sessão4[2]
        somacol4 = sessão2[1]+sessão2[3]+sessão4[1]+sessão4[3]

        #SOMA DIAGONAL
        somadiag = sessão1[0]+sessão1[3]+sessão4[0]+sessão4[3]
        
        #CONTADORES PARA LINHAS, COLUNAS E DIAGONAL
        cont_pont_lin1 = 0
        cont_pont_lin2 = 0
        cont_pont_lin3 = 0
        cont_pont_lin4 = 0
        cont_pont_col1 = 0
        cont_pont_col2 = 0
        cont_pont_col3 = 0
        cont_pont_col4 = 0
        cont_pont_dia = 0
        pontos_jog1=0
        pontos_jog2=0
        print('-=-='*10)
        tabuleiro_4x4(sessão1_oc, sessão2_oc, sessão3_oc, sessão4_oc)
        #LOOP DAS JOGADAS
        jogada = 0
        while 0 in sessão1_oc or 0 in sessão2_oc or 0 in sessão3_oc or 0 in sessão4_oc:
            jogada+=1
            print('-=-='*10)
            if jogada%2 != 0:
                print(f'Vez de {jogador1}:')
            else:
                print(f'Vez de {jogador2}:')
            escolha_sessao = input('Qual sessão deseja acrescentar? ')
            #VERIFICAÇÃO DAS ENTRADA
            if type(escolha_sessao) != int:
                while escolha_sessao.isdigit() == False:
                    print('Valor inválido')
                    escolha_sessao = input('Qual sessão deseja acrescentar?')
            while int(escolha_sessao)<=0 or int(escolha_sessao)>4:
                print('Valor inválido')
                escolha_sessao = input('Qual sessão deseja acrescentar? ')
            escolha_valor = input('Qual Valor?')
            #VERIFICAÇÃO DAS ENTRADA
            if type(escolha_valor) != int:
                while escolha_valor.isdigit() == False:
                    print('Valor inválido')
                    escolha_valor = input('Qual Valor?')
            while int(escolha_valor)<=0 or int(escolha_valor)>4 :
                print('Valor inválido')
                escolha_valor = input('Qual Valor?')

            #SUBSTITUIÇÃO DOS VALORES
            substitui4x4(sec_jogadas4x4, escolha_sessao, escolha_valor, sessão1_oc, sessão1, 1)
            substitui4x4(sec_jogadas4x4, escolha_sessao, escolha_valor, sessão2_oc, sessão2, 2)
            substitui4x4(sec_jogadas4x4, escolha_sessao, escolha_valor, sessão3_oc, sessão3, 3)
            substitui4x4(sec_jogadas4x4, escolha_sessao, escolha_valor, sessão4_oc, sessão4, 4)
            
            #PONTUAÇÃO DOS JOGADORES
            if jogada%2==0:
                #LINHAS
                if sessão1_oc[0] != 0 and sessão1_oc[1] != 0 and sessão2_oc[0] != 0 and sessão2_oc[1] != 0 and cont_pont_lin1 == 0:
                    pontos_jog2 += somalin1
                    cont_pont_lin1 += 1
                if sessão1_oc[2] != 0 and sessão1_oc[3] !=0 and sessão2_oc[2] != 0 and sessão2_oc[3] != 0 and cont_pont_lin2 == 0:
                    pontos_jog2 += somalin2
                    cont_pont_lin2 += 1
                if sessão3_oc[0] != 0 and sessão3_oc[1] !=0 and sessão4_oc[0] != 0 and sessão4_oc[1] != 0 and cont_pont_lin3 == 0:
                    pontos_jog2 += somalin3
                    cont_pont_lin3 += 1
                if sessão3_oc[2] != 0 and sessão3_oc[3] !=0 and sessão4_oc[2] != 0 and sessão4_oc[3] != 0 and cont_pont_lin4 == 0:
                    pontos_jog2 += somalin4
                    cont_pont_lin4 += 1
                #COLUNAS
                if sessão1_oc[0] != 0 and sessão1_oc[2] != 0 and sessão3_oc[0] != 0 and sessão3_oc[2] != 0 and cont_pont_col1 == 0:
                    pontos_jog2 += somacol1
                    cont_pont_col1 += 1
                if sessão1_oc[1] != 0 and sessão1_oc[3] !=0 and sessão3_oc[1] != 0 and sessão3_oc[3] != 0 and cont_pont_col2 == 0:
                    pontos_jog2 += somacol2
                    cont_pont_col2 += 1
                if sessão2_oc[0] != 0 and sessão2_oc[2] !=0 and sessão4_oc[0] != 0 and sessão4_oc[2] != 0 and cont_pont_col3 == 0:
                    pontos_jog2 += somacol3
                    cont_pont_col3 += 1
                if sessão2_oc[1] != 0 and sessão2_oc[3] !=0 and sessão4_oc[1] != 0 and sessão4_oc[3] != 0 and cont_pont_col4 == 0:
                    pontos_jog2 += somacol4
                    cont_pont_col4 += 1
                #DIAGONAL
                if sessão1_oc[0] !=0 and sessão1_oc[3] !=0 and sessão4_oc[0] !=0 and sessão4_oc[3] !=0 and cont_pont_dia == 0:
                    pontos_jog2 += somadiag*2
                    cont_pont_dia += 1

            else:
                #LINHAS
                if sessão1_oc[0] != 0 and sessão1_oc[1] != 0 and sessão2_oc[0] != 0 and sessão2_oc[1] != 0 and cont_pont_lin1 == 0:
                    pontos_jog1 += somalin1
                    cont_pont_lin1 += 1
                if sessão1_oc[2] != 0 and sessão1_oc[3] !=0 and sessão2_oc[2] != 0 and sessão2_oc[3] != 0 and cont_pont_lin2 == 0:
                    pontos_jog1 += somalin2
                    cont_pont_lin2 += 1
                if sessão3_oc[0] != 0 and sessão3_oc[1] !=0 and sessão4_oc[0] != 0 and sessão4_oc[1] != 0 and cont_pont_lin3 == 0:
                    pontos_jog1 += somalin3
                    cont_pont_lin3 += 1
                if sessão3_oc[2] != 0 and sessão3_oc[3] !=0 and sessão4_oc[2] != 0 and sessão4_oc[3] != 0 and cont_pont_lin4 == 0:
                    pontos_jog1 += somalin4
                    cont_pont_lin4 += 1
                #COLUNAS
                if sessão1_oc[0] != 0 and sessão1_oc[2] != 0 and sessão3_oc[0] != 0 and sessão3_oc[2] != 0 and cont_pont_col1 == 0:
                    pontos_jog1 += somacol1
                    cont_pont_col1 += 1
                if sessão1_oc[1] != 0 and sessão1_oc[3] !=0 and sessão3_oc[1] != 0 and sessão3_oc[3] != 0 and cont_pont_col2 == 0:
                    pontos_jog1 += somacol2
                    cont_pont_col2 += 1
                if sessão2_oc[0] != 0 and sessão2_oc[2] !=0 and sessão4_oc[0] != 0 and sessão4_oc[2] != 0 and cont_pont_col3 == 0:
                    pontos_jog1 += somacol3
                    cont_pont_col3 += 1
                if sessão2_oc[1] != 0 and sessão2_oc[3] !=0 and sessão4_oc[1] != 0 and sessão4_oc[3] != 0 and cont_pont_col4 == 0:
                    pontos_jog1 += somacol4
                    cont_pont_col4 += 1
                #DIAGONAL
                if sessão1_oc[0] !=0 and sessão1_oc[3] !=0 and sessão4_oc[0] !=0 and sessão4_oc[3] !=0 and cont_pont_dia == 0:
                    pontos_jog1 += somadiag*2
                    cont_pont_dia += 1
            print('-=-='*10)
            tabuleiro_4x4(sessão1_oc, sessão2_oc, sessão3_oc, sessão4_oc)
            print('-=-='*10)
            print(f'{jogador1} tem {pontos_jog1} pontos')
            print(f'{jogador2} tem {pontos_jog2} pontos')
            

        if pontos_jog1>pontos_jog2:
            print('-=-='*10)
            print(f'    {jogador1} VENCEU!   ')
        elif pontos_jog1<pontos_jog2:
            print('-=-='*10)
            print(f'    {jogador2} VENCEU!    ')
        elif pontos_jog1 == pontos_jog2:
            print('-=-='*10)
            print('     EMPATE!     ')
        print('-=-='*10)     
    #NIVEL 2 9X9
    if int(opção) == 2:
        #LISTAS DOS TABULEIROS
        sessão1_oc = [0,0,0,0,0,0,0,0,0]
        sessão2_oc = [0,0,0,0,0,0,0,0,0]
        sessão3_oc = [0,0,0,0,0,0,0,0,0]
        sessão4_oc = [0,0,0,0,0,0,0,0,0]
        sessão5_oc = [0,0,0,0,0,0,0,0,0]
        sessão6_oc = [0,0,0,0,0,0,0,0,0]
        sessão7_oc = [0,0,0,0,0,0,0,0,0]
        sessão8_oc = [0,0,0,0,0,0,0,0,0]
        sessão9_oc = [0,0,0,0,0,0,0,0,0]
        sessão1 = random.sample(val9x9, 9)
        sessão2 = random.sample(val9x9, 9)
        sessão3 = random.sample(val9x9, 9)
        sessão4 = random.sample(val9x9, 9)
        sessão5 = random.sample(val9x9, 9)
        sessão6 = random.sample(val9x9, 9)
        sessão7 = random.sample(val9x9, 9)
        sessão8 = random.sample(val9x9, 9)
        sessão9 = random.sample(val9x9, 9)
        
        jogador1 = input('Jogador 1: ')
        jogador2 = input('Jogador 2: ')

        #SOMA LINHA
        somalin1 = sessão1[0]+sessão1[1]+sessão1[2]+sessão2[0]+sessão2[1]+sessão2[2]+sessão3[0]+sessão3[1]+sessão3[2]
        somalin2 = sessão1[3]+sessão1[4]+sessão1[5]+sessão2[3]+sessão2[4]+sessão2[5]+sessão3[3]+sessão3[4]+sessão3[5]
        somalin3 = sessão1[6]+sessão1[7]+sessão1[8]+sessão2[6]+sessão2[7]+sessão2[8]+sessão3[6]+sessão3[7]+sessão3[8]
        somalin4 = sessão4[0]+sessão4[1]+sessão4[2]+sessão5[0]+sessão5[1]+sessão5[2]+sessão6[0]+sessão6[1]+sessão6[2]
        somalin5 = sessão4[3]+sessão4[4]+sessão4[5]+sessão5[3]+sessão5[4]+sessão5[5]+sessão6[3]+sessão6[4]+sessão6[5]
        somalin6 = sessão4[6]+sessão4[7]+sessão4[8]+sessão5[6]+sessão5[7]+sessão5[8]+sessão6[6]+sessão6[7]+sessão6[8]
        somalin7 = sessão7[0]+sessão7[1]+sessão7[2]+sessão8[0]+sessão8[1]+sessão8[2]+sessão9[0]+sessão9[1]+sessão9[2]
        somalin8 = sessão7[3]+sessão7[4]+sessão7[5]+sessão8[3]+sessão8[4]+sessão8[5]+sessão9[3]+sessão9[4]+sessão9[5]
        somalin9 = sessão7[6]+sessão7[7]+sessão7[8]+sessão8[6]+sessão8[7]+sessão8[8]+sessão3[6]+sessão9[7]+sessão9[8]
        #SOMA COLUNA
        somacol1 = sessão1[0]+sessão1[3]+sessão1[6]+sessão4[0]+sessão4[3]+sessão4[6]+sessão7[0]+sessão7[3]+sessão7[6]
        somacol2 = sessão1[1]+sessão1[4]+sessão1[7]+sessão4[1]+sessão4[4]+sessão4[7]+sessão7[1]+sessão7[4]+sessão7[7]
        somacol3 = sessão1[2]+sessão1[5]+sessão1[8]+sessão4[2]+sessão4[5]+sessão4[8]+sessão7[2]+sessão7[5]+sessão7[8]
        somacol4 = sessão2[0]+sessão2[3]+sessão2[6]+sessão5[0]+sessão5[3]+sessão5[6]+sessão8[0]+sessão8[3]+sessão8[6]
        somacol5 = sessão2[1]+sessão2[4]+sessão2[7]+sessão5[1]+sessão5[4]+sessão5[7]+sessão8[1]+sessão8[4]+sessão8[7]
        somacol6 = sessão2[2]+sessão2[5]+sessão2[8]+sessão5[2]+sessão5[5]+sessão5[8]+sessão8[2]+sessão8[5]+sessão8[8]
        somacol7 = sessão3[0]+sessão3[3]+sessão3[6]+sessão6[0]+sessão6[3]+sessão6[6]+sessão9[0]+sessão9[3]+sessão9[6]
        somacol8 = sessão3[1]+sessão3[4]+sessão3[7]+sessão6[1]+sessão6[4]+sessão6[7]+sessão9[1]+sessão9[4]+sessão9[7]
        somacol9 = sessão3[2]+sessão3[5]+sessão3[8]+sessão6[2]+sessão6[5]+sessão6[8]+sessão9[2]+sessão9[5]+sessão9[8]

        #SOMA DIAGONAL
        somadiag = sessão1[0]+sessão1[4]+sessão1[8]+sessão5[0]+sessão5[4]+sessão5[8]+sessão9[0]+sessão9[4]+sessão9[8] 
        print('-=-='*10)    
        tabuleiro_9x9(sessão1_oc, sessão2_oc, sessão3_oc, sessão4_oc, sessão5_oc, sessão6_oc, sessão7_oc, sessão8_oc, sessão9_oc)

        #CONTADORES PARA LINHAS, COLUNAS E DIAGONAL
        cont_pont_lin1 = 0
        cont_pont_lin2 = 0
        cont_pont_lin3 = 0
        cont_pont_lin4 = 0
        cont_pont_lin5 = 0
        cont_pont_lin6 = 0
        cont_pont_lin7 = 0
        cont_pont_lin8 = 0
        cont_pont_lin9 = 0

        cont_pont_col1 = 0
        cont_pont_col2 = 0
        cont_pont_col3 = 0
        cont_pont_col4 = 0
        cont_pont_col5 = 0
        cont_pont_col6 = 0
        cont_pont_col7 = 0
        cont_pont_col8 = 0
        cont_pont_col9 = 0

        cont_pont_dia = 0
        pontos_jog1=0
        pontos_jog2=0

        #LOOP DAS JOGADAS
        jogada = 0
        while 0 in sessão1_oc or 0 in sessão2_oc or 0 in sessão3_oc or 0 in sessão4_oc or 0 in sessão5_oc or 0 in sessão6_oc or 0 in sessão7_oc or 0 in sessão8_oc or 0 in sessão9_oc:
            jogada+=1
            print('-=-='*10)
            if jogada%2 != 0:
                print(f'Vez de {jogador1}:')
            else:
                print(f'Vez de {jogador2}:')
            escolha_sessao = input('Qual sessão deseja acrescentar? ')
            if type(escolha_sessao) != int:
                while escolha_sessao.isdigit() == False:
                    print('Valor inválido')
                    escolha_sessao = input('Qual sessão deseja acrescentar?')
            while int(escolha_sessao)<=0 or int(escolha_sessao)>9:
                print('Valor inválido')
                escolha_sessao = input('Qual sessão deseja acrescentar? ')
            escolha_valor = input('Qual Valor?')
            if type(escolha_valor) != int:
                while escolha_valor.isdigit() == False:
                    print('Valor inválido')
                    escolha_valor = input('Qual Valor?')
            while int(escolha_valor)<=0 or int(escolha_valor)>9 :
                print('Valor inválido')
                escolha_valor = input('Qual Valor?')

            #SUBSTITUIÇÃO DOS VALORES
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão1_oc, sessão1, 1)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão2_oc, sessão2, 2)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão3_oc, sessão3, 3)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão4_oc, sessão4, 4)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão5_oc, sessão5, 5)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão6_oc, sessão6, 6)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão7_oc, sessão7, 7)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão8_oc, sessão8, 8)
            substitui9x9(sec_jogadas9x9, escolha_sessao, escolha_valor, sessão9_oc, sessão9, 9)

            #PONTUAÇÃO DOS JOGADORES
            if jogada%2==0:
                #LINHAS
                if sessão1_oc[0]!=0 and sessão1_oc[1]!=0 and sessão1_oc[2]!=0 and sessão2_oc[0]!=0 and sessão2_oc[1]!=0 and sessão2_oc[2]!=0 and sessão3_oc[0]!=0 and sessão3_oc[1]!=0 and sessão3_oc[2]!=0 and cont_pont_lin1 == 0:
                    pontos_jog2 += somalin1
                    cont_pont_lin1 += 1
                if sessão1_oc[3]!=0 and sessão1_oc[4]!=0 and sessão1_oc[5]!=0 and sessão2_oc[3]!=0 and sessão2_oc[4]!=0 and sessão2_oc[5]!=0 and sessão3_oc[3]!=0 and sessão3_oc[4]!=0 and sessão3_oc[5]!=0 and cont_pont_lin2 == 0:
                    pontos_jog2 += somalin2
                    cont_pont_lin2 += 1
                if sessão1_oc[6]!=0 and sessão1_oc[7]!=0 and sessão1_oc[8]!=0 and sessão2_oc[6]!=0 and sessão2_oc[7]!=0 and sessão2_oc[8]!=0 and sessão3_oc[6]!=0 and sessão3_oc[7]!=0 and sessão3_oc[8]!=0 and cont_pont_lin3 == 0:
                    pontos_jog2 += somalin3
                    cont_pont_lin3 += 1
                if sessão4_oc[0]!=0 and sessão4_oc[1]!=0 and sessão4_oc[2]!=0 and sessão5_oc[0]!=0 and sessão5_oc[1]!=0 and sessão5_oc[2]!=0 and sessão6_oc[0]!=0 and sessão6_oc[1]!=0 and sessão6_oc[2]!=0 and cont_pont_lin4 == 0:
                    pontos_jog2 += somalin4
                    cont_pont_lin4 += 1
                if sessão4_oc[3]!=0 and sessão4_oc[4]!=0 and sessão4_oc[5]!=0 and sessão5_oc[3]!=0 and sessão5_oc[4]!=0 and sessão5_oc[5]!=0 and sessão6_oc[3]!=0 and sessão6_oc[4]!=0 and sessão6_oc[5]!=0 and cont_pont_lin5 == 0:
                    pontos_jog2 += somalin5
                    cont_pont_lin5 += 1
                if sessão4_oc[6]!=0 and sessão4_oc[7]!=0 and sessão4_oc[8]!=0 and sessão5_oc[6]!=0 and sessão5_oc[7]!=0 and sessão5_oc[8]!=0 and sessão6_oc[6]!=0 and sessão6_oc[7]!=0 and sessão6_oc[8]!=0 and cont_pont_lin6 == 0:
                    pontos_jog2 += somalin6
                    cont_pont_lin6 += 1
                if sessão7_oc[0]!=0 and sessão7_oc[1]!=0 and sessão7_oc[2]!=0 and sessão8_oc[0]!=0 and sessão8_oc[1]!=0 and sessão8_oc[2]!=0 and sessão9_oc[0]!=0 and sessão9_oc[1]!=0 and sessão9_oc[2]!=0 and cont_pont_lin7 == 0:
                    pontos_jog2 += somalin7
                    cont_pont_lin7 += 1
                if sessão7_oc[3]!=0 and sessão7_oc[4]!=0 and sessão7_oc[5]!=0 and sessão8_oc[3]!=0 and sessão8_oc[4]!=0 and sessão8_oc[5]!=0 and sessão9_oc[3]!=0 and sessão9_oc[4]!=0 and sessão9_oc[5]!=0 and cont_pont_lin8 == 0:
                    pontos_jog2 += somalin8
                    cont_pont_lin8 += 1
                if sessão7_oc[6]!=0 and sessão7_oc[7]!=0 and sessão7_oc[8]!=0 and sessão8_oc[6]!=0 and sessão8_oc[7]!=0 and sessão8_oc[8]!=0 and sessão3_oc[6]!=0 and sessão9_oc[7]!=0 and sessão9_oc[8]!=0 and cont_pont_lin9 == 0:
                    pontos_jog2 += somalin9
                    cont_pont_lin9 += 1

                #COLUNAS
                if sessão1_oc[0]!=0 and sessão1_oc[3]!=0 and sessão1_oc[6]!=0 and sessão4_oc[0]!=0 and sessão4_oc[3]!=0 and sessão4_oc[6]!=0 and sessão7_oc[0]!=0 and sessão7_oc[3]!=0 and sessão7_oc[6]!=0 and cont_pont_col1 == 0:
                    pontos_jog2 += somacol1
                    cont_pont_col1 += 1
                if sessão1_oc[1]!=0 and sessão1_oc[4]!=0 and sessão1_oc[7]!=0 and sessão4_oc[1]!=0 and sessão4_oc[4]!=0 and sessão4_oc[7]!=0 and sessão7_oc[1]!=0 and sessão7_oc[4]!=0 and sessão7_oc[7]!=0 and cont_pont_col2 == 0:
                    pontos_jog2 += somacol2
                    cont_pont_col2 += 1
                if sessão1_oc[2]!=0 and sessão1_oc[5]!=0 and sessão1_oc[8]!=0 and sessão4_oc[2]!=0 and sessão4_oc[5]!=0 and sessão4_oc[8]!=0 and sessão7_oc[2]!=0 and sessão7_oc[5]!=0 and sessão7_oc[8]!=0 and cont_pont_col3 == 0:
                    pontos_jog2 += somacol3
                    cont_pont_col3 += 1
                if sessão2_oc[0]!=0 and sessão2_oc[3]!=0 and sessão2_oc[6]!=0 and sessão5_oc[0]!=0 and sessão5_oc[3]!=0 and sessão5_oc[6]!=0 and sessão8_oc[0]!=0 and sessão8_oc[3]!=0 and sessão8_oc[6]!=0 and cont_pont_col4 == 0:
                    pontos_jog2 += somacol4
                    cont_pont_col4 += 1
                if sessão2_oc[1]!=0 and sessão2_oc[4]!=0 and sessão2_oc[7]!=0 and sessão5_oc[1]!=0 and sessão5_oc[4]!=0 and sessão5_oc[7]!=0 and sessão8_oc[1]!=0 and sessão8_oc[4]!=0 and sessão8_oc[7]!=0 and cont_pont_col5 == 0:
                    pontos_jog2 += somacol5
                    cont_pont_col5 += 1
                if sessão2_oc[2]!=0 and sessão2_oc[5]!=0 and sessão2_oc[8]!=0 and sessão5_oc[2]!=0 and sessão5_oc[5]!=0 and sessão5_oc[8]!=0 and sessão8_oc[2]!=0 and sessão8_oc[5]!=0 and sessão8_oc[8]!=0 and cont_pont_col6 == 0:
                    pontos_jog2 += somacol6
                    cont_pont_col6 += 1
                if sessão3_oc[0]!=0 and sessão3_oc[3]!=0 and sessão3_oc[6]!=0 and sessão6_oc[0]!=0 and sessão6_oc[3]!=0 and sessão6_oc[6]!=0 and sessão9_oc[0]!=0 and sessão9_oc[3]!=0 and sessão9_oc[6]!=0 and cont_pont_col7 == 0:
                    pontos_jog2 += somacol7
                    cont_pont_col7 += 1
                if sessão3_oc[1]!=0 and sessão3_oc[4]!=0 and sessão3_oc[7]!=0 and sessão6_oc[1]!=0 and sessão6_oc[4]!=0 and sessão6_oc[7]!=0 and sessão9_oc[1]!=0 and sessão9_oc[4]!=0 and sessão9_oc[7]!=0 and cont_pont_col8 == 0:
                    pontos_jog2 += somacol8
                    cont_pont_col8 += 1
                if sessão3_oc[2]!=0 and sessão3_oc[5]!=0 and sessão3_oc[8]!=0 and sessão6_oc[2]!=0 and sessão6_oc[5]!=0 and sessão6_oc[8]!=0 and sessão9_oc[2]!=0 and sessão9_oc[5]!=0 and sessão9_oc[8]!=0 and cont_pont_col9 == 0:
                    pontos_jog2 += somacol9
                    cont_pont_col9 += 1
                
                #DIAGONAL
                if sessão1_oc[0]!=0 and sessão1_oc[4]!=0 and sessão1_oc[8]!=0 and sessão5_oc[0]!=0 and sessão5_oc[4]!=0 and sessão5_oc[8]!=0 and sessão9_oc[0]!=0 and sessão9_oc[4]!=0 and sessão9_oc[8]!=0 and cont_pont_dia == 0:
                    pontos_jog2 += somadiag*2
                    cont_pont_dia += 1

            else:
                 #LINHAS
                if sessão1_oc[0]!=0 and sessão1_oc[1]!=0 and sessão1_oc[2]!=0 and sessão2_oc[0]!=0 and sessão2_oc[1]!=0 and sessão2_oc[2]!=0 and sessão3_oc[0]!=0 and sessão3_oc[1]!=0 and sessão3_oc[2]!=0 and cont_pont_lin1 == 0:
                    pontos_jog1 += somalin1
                    cont_pont_lin1 += 1
                if sessão1_oc[3]!=0 and sessão1_oc[4]!=0 and sessão1_oc[5]!=0 and sessão2_oc[3]!=0 and sessão2_oc[4]!=0 and sessão2_oc[5]!=0 and sessão3_oc[3]!=0 and sessão3_oc[4]!=0 and sessão3_oc[5]!=0 and cont_pont_lin2 == 0:
                    pontos_jog1 += somalin2
                    cont_pont_lin2 += 1
                if sessão1_oc[6]!=0 and sessão1_oc[7]!=0 and sessão1_oc[8]!=0 and sessão2_oc[6]!=0 and sessão2_oc[7]!=0 and sessão2_oc[8]!=0 and sessão3_oc[6]!=0 and sessão3_oc[7]!=0 and sessão3_oc[8]!=0 and cont_pont_lin3 == 0:
                    pontos_jog1 += somalin3
                    cont_pont_lin3 += 1
                if sessão4_oc[0]!=0 and sessão4_oc[1]!=0 and sessão4_oc[2]!=0 and sessão5_oc[0]!=0 and sessão5_oc[1]!=0 and sessão5_oc[2]!=0 and sessão6_oc[0]!=0 and sessão6_oc[1]!=0 and sessão6_oc[2]!=0 and cont_pont_lin4 == 0:
                    pontos_jog1 += somalin4
                    cont_pont_lin4 += 1
                if sessão4_oc[3]!=0 and sessão4_oc[4]!=0 and sessão4_oc[5]!=0 and sessão5_oc[3]!=0 and sessão5_oc[4]!=0 and sessão5_oc[5]!=0 and sessão6_oc[3]!=0 and sessão6_oc[4]!=0 and sessão6_oc[5]!=0 and cont_pont_lin5 == 0:
                    pontos_jog1 += somalin5
                    cont_pont_lin5 += 1
                if sessão4_oc[6]!=0 and sessão4_oc[7]!=0 and sessão4_oc[8]!=0 and sessão5_oc[6]!=0 and sessão5_oc[7]!=0 and sessão5_oc[8]!=0 and sessão6_oc[6]!=0 and sessão6_oc[7]!=0 and sessão6_oc[8]!=0 and cont_pont_lin6 == 0:
                    pontos_jog1 += somalin6
                    cont_pont_lin6 += 1
                if sessão7_oc[0]!=0 and sessão7_oc[1]!=0 and sessão7_oc[2]!=0 and sessão8_oc[0]!=0 and sessão8_oc[1]!=0 and sessão8_oc[2]!=0 and sessão9_oc[0]!=0 and sessão9_oc[1]!=0 and sessão9_oc[2]!=0 and cont_pont_lin7 == 0:
                    pontos_jog1 += somalin7
                    cont_pont_lin7 += 1
                if sessão7_oc[3]!=0 and sessão7_oc[4]!=0 and sessão7_oc[5]!=0 and sessão8_oc[3]!=0 and sessão8_oc[4]!=0 and sessão8_oc[5]!=0 and sessão9_oc[3]!=0 and sessão9_oc[4]!=0 and sessão9_oc[5]!=0 and cont_pont_lin8 == 0:
                    pontos_jog1 += somalin8
                    cont_pont_lin8 += 1
                if sessão7_oc[6]!=0 and sessão7_oc[7]!=0 and sessão7_oc[8]!=0 and sessão8_oc[6]!=0 and sessão8_oc[7]!=0 and sessão8_oc[8]!=0 and sessão3_oc[6]!=0 and sessão9_oc[7]!=0 and sessão9_oc[8]!=0 and cont_pont_lin9 == 0:
                    pontos_jog1 += somalin9
                    cont_pont_lin9 += 1

                #COLUNAS
                if sessão1_oc[0]!=0 and sessão1_oc[3]!=0 and sessão1_oc[6]!=0 and sessão4_oc[0]!=0 and sessão4_oc[3]!=0 and sessão4_oc[6]!=0 and sessão7_oc[0]!=0 and sessão7_oc[3]!=0 and sessão7_oc[6]!=0 and cont_pont_col1 == 0:
                    pontos_jog1 += somacol1
                    cont_pont_col1 += 1
                if sessão1_oc[1]!=0 and sessão1_oc[4]!=0 and sessão1_oc[7]!=0 and sessão4_oc[1]!=0 and sessão4_oc[4]!=0 and sessão4_oc[7]!=0 and sessão7_oc[1]!=0 and sessão7_oc[4]!=0 and sessão7_oc[7]!=0 and cont_pont_col2 == 0:
                    pontos_jog1 += somacol2
                    cont_pont_col2 += 1
                if sessão1_oc[2]!=0 and sessão1_oc[5]!=0 and sessão1_oc[8]!=0 and sessão4_oc[2]!=0 and sessão4_oc[5]!=0 and sessão4_oc[8]!=0 and sessão7_oc[2]!=0 and sessão7_oc[5]!=0 and sessão7_oc[8]!=0 and cont_pont_col3 == 0:
                    pontos_jog1 += somacol3
                    cont_pont_col3 += 1
                if sessão2_oc[0]!=0 and sessão2_oc[3]!=0 and sessão2_oc[6]!=0 and sessão5_oc[0]!=0 and sessão5_oc[3]!=0 and sessão5_oc[6]!=0 and sessão8_oc[0]!=0 and sessão8_oc[3]!=0 and sessão8_oc[6]!=0 and cont_pont_col4 == 0:
                    pontos_jog1 += somacol4
                    cont_pont_col4 += 1
                if sessão2_oc[1]!=0 and sessão2_oc[4]!=0 and sessão2_oc[7]!=0 and sessão5_oc[1]!=0 and sessão5_oc[4]!=0 and sessão5_oc[7]!=0 and sessão8_oc[1]!=0 and sessão8_oc[4]!=0 and sessão8_oc[7]!=0 and cont_pont_col5 == 0:
                    pontos_jog1 += somacol5
                    cont_pont_col5 += 1
                if sessão2_oc[2]!=0 and sessão2_oc[5]!=0 and sessão2_oc[8]!=0 and sessão5_oc[2]!=0 and sessão5_oc[5]!=0 and sessão5_oc[8]!=0 and sessão8_oc[2]!=0 and sessão8_oc[5]!=0 and sessão8_oc[8]!=0 and cont_pont_col6 == 0:
                    pontos_jog1 += somacol6
                    cont_pont_col6 += 1
                if sessão3_oc[0]!=0 and sessão3_oc[3]!=0 and sessão3_oc[6]!=0 and sessão6_oc[0]!=0 and sessão6_oc[3]!=0 and sessão6_oc[6]!=0 and sessão9_oc[0]!=0 and sessão9_oc[3]!=0 and sessão9_oc[6]!=0 and cont_pont_col7 == 0:
                    pontos_jog1 += somacol7
                    cont_pont_col7 += 1
                if sessão3_oc[1]!=0 and sessão3_oc[4]!=0 and sessão3_oc[7]!=0 and sessão6_oc[1]!=0 and sessão6_oc[4]!=0 and sessão6_oc[7]!=0 and sessão9_oc[1]!=0 and sessão9_oc[4]!=0 and sessão9_oc[7]!=0 and cont_pont_col8 == 0:
                    pontos_jog1 += somacol8
                    cont_pont_col8 += 1
                if sessão3_oc[2]!=0 and sessão3_oc[5]!=0 and sessão3_oc[8]!=0 and sessão6_oc[2]!=0 and sessão6_oc[5]!=0 and sessão6_oc[8]!=0 and sessão9_oc[2]!=0 and sessão9_oc[5]!=0 and sessão9_oc[8]!=0 and cont_pont_col9 == 0:
                    pontos_jog1 += somacol9
                    cont_pont_col9 += 1
                
                #DIAGONAL
                if sessão1_oc[0]!=0 and sessão1_oc[4]!=0 and sessão1_oc[8]!=0 and sessão5_oc[0]!=0 and sessão5_oc[4]!=0 and sessão5_oc[8]!=0 and sessão9_oc[0]!=0 and sessão9_oc[4]!=0 and sessão9_oc[8]!=0 and cont_pont_dia == 0:
                    pontos_jog1 += somadiag*2
                    cont_pont_dia += 1
            print('-=-='*10)
            tabuleiro_9x9(sessão1_oc, sessão2_oc, sessão3_oc, sessão4_oc, sessão5_oc, sessão6_oc, sessão7_oc, sessão8_oc, sessão9_oc)
            print('-=-='*10)
            print(f'{jogador1} tem {pontos_jog1} pontos')
            print(f'{jogador2} tem {pontos_jog2} pontos')
            

        if pontos_jog1>pontos_jog2:
            print('-=-='*10)
            print(f'    {jogador1} VENCEU!   ')
        elif pontos_jog1<pontos_jog2:
            print('-=-='*10)
            print(f'    {jogador2} VENCEU!    ')
        elif pontos_jog1 == pontos_jog2:
            print('-=-='*10)
            print('     EMPATE!     ')
        print('-=-='*10)









            
        


