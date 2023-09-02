import re
liste_de_chaines = ["Il y a 42 pommes.", "Le prix est de 3.14 euros.", "123 est un nombre.", "Pas de nombre ici."]
liste_de_nombres = []
pattern = r'\d+\.\d+|\d+'

for chaine in liste_de_chaines:
    correspondances = re.findall(pattern, chaine)
    for correspondance in correspondances:
        nombre = float(correspondance)
        liste_de_nombres.append(nombre)

print(liste_de_nombres)


def set_team_forreal(self, col):
        num4 = 0
        num3 = 0
        num2 = 0
        pattern = r'\d+\.\d+|\d+'
        ls = ["0"]
        
        num = int
        if self.dicto_team_real:
            for i in self.dicto_team_real:
                for chaine in i:
                    correspondences = re.findall(pattern, chaine)
                    for correspondence in correspondences:
                        num = correspondence
                        ls.append(num)
        else:
            pass
        #ls = [float(item) for item in ls]
        num4 = max(ls)
        num3 = int(num4)
        if num3 == 0:
            pass
        else:
            num3 = num3-1
        num2 = self.spinbox2.value()+ num3
        for i in range(num3, num2):
            try:
                try :
                    for k in self.dicto_team_real[self.lineEdit.text()][2]:
                     
                        if k == f"team{i+1}":
                            pass
                        else:
                            self.dicto_team_real.setdefault(self.lineEdit.text(), []).append([self.j, col, f"team{i+1}"])
                except IndexError:
                    self.dicto_team_real.setdefault(self.lineEdit.text(), []).append([self.j, col, f"team{i+1}"])
            except KeyError:
                self.dicto_team_real.setdefault(self.lineEdit.text(), []).append([self.j, col, f"team{i+1}"])
            self.j = self.j +1
            #print(self.dicto_team_real)
        print(self.dicto_team_real)
        self.value_automat.emit(self.dicto_team_real)

    