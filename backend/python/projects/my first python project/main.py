def ivairios_varzybos():
    visos_varzybos = [12, 123 ,23, 0, 10, 7]
    puikios_varzybos = []
    geros_varzybos = []
    prastos_varzybos = []
    for vienu_varzybu_taskai in visos_varzybos:
        if vienu_varzybu_taskai <10:
            prastos_varzybos.append(vienu_varzybu_taskai)
        if vienu_varzybu_taskai >9 and vienu_varzybu_taskai<20:
            geros_varzybos.append(vienu_varzybu_taskai)
        if vienu_varzybu_taskai >20:
            puikios_varzybos.append(vienu_varzybu_taskai)
    print(prastos_varzybos)
    print(geros_varzybos)
    print(puikios_varzybos)
def varzybos_ir_taskai():
    lietuva=["sabas", "rokas", "dimsa"]
    usa=["lebron", "curry", "lilard"]
    lietuvos_taskai=[40, 19, 9]
    usa_taskai=[30, 19, 23]
    for index in range(0, 3):
        if lietuvos_taskai[index]<usa_taskai[index]:
            print(lietuva[index]+"<"+usa[index])
        elif lietuvos_taskai[index]==usa_taskai[index]:
            print(lietuva[index]+"="+usa[index])
        else:
            print(lietuva[index]+">"+usa[index])
def fiba():
    Group_D=["mex", "egy", "mne", "ltu"]
    resultatu_komandos=["mex:egy", "mex:mne", "mex:ltu", "egy:mne", "egy:ltu", "mne:ltu"]
    result=["76:71", "65:70", "68:82", "72:64", "59:109", "60:75"]
    wins=[]
    for index in range(0, 4):
        #print(index)
        team=Group_D[index]
        vienos_komandos_wins=0
        print(team+"dirbame su situo")
        for index2 in range(0, 6):
            vienu_varzybu_komandos=resultatu_komandos[index2]
            print(vienu_varzybu_komandos)
            vienu_varzybu_result=result[index2]
            print(vienu_varzybu_result)
            pirmoji_komanda=vienu_varzybu_komandos[0:3]
            antra_komanda=vienu_varzybu_komandos[4:7]
            print(pirmoji_komanda)
            print(antra_komanda)
            #issitraukineju varzybu taskus
            pirmosios_komandos_taskai = int(vienu_varzybu_result[0:2])
            antrosios_komandos_taskai = int(vienu_varzybu_result[3:6])
            print(pirmosios_komandos_taskai)
            print(antrosios_komandos_taskai)
            if pirmosios_komandos_taskai >antrosios_komandos_taskai and pirmoji_komanda==team:
                print("pergale")
                vienos_komandos_wins=vienos_komandos_wins+1
            if pirmosios_komandos_taskai <antrosios_komandos_taskai and antra_komanda==team:
                print("pergale")
                vienos_komandos_wins=vienos_komandos_wins+1
        wins.append(vienos_komandos_wins)
    print(wins)

def kiek_imete_per_dvi_varzybas():
    zaidejai=["evans", "lekavicius"]
    pirmos_varzybos=[25, 12]
    antros_varzybos=[28, 17]
    kiek_is_viso=[]
    for index in range(0, 2):
        #print(pirmos_varzybos[index])
        #print(antros_varzybos[index])
        kiek_is_viso_vieno_zaidejo=pirmos_varzybos[index]+antros_varzybos[index]
        #print(kiek_is_viso_vieno_zaidejo)
        kiek_is_viso.append(kiek_is_viso_vieno_zaidejo)

        if index==1:
            print(kiek_is_viso)

if __name__ == '__main__':

    #ivairios_varzybos()
    #varzybos_ir_taskai()
    #fiba()
    kiek_imete_per_dvi_varzybas()
