def set_team_forreal(self, col):
    x = self.spinbox2.value()
    y = self.lineEdit.text()
    z = 0
    max_num_club = 0
    try:
        if not self.dicto_team_real[y]:
            n = 0
            for _ in range(x):
                self.dicto_team_real.setdefault(y, []).append([n, col, f"team{self.j+1}"])
                self.dicto_team_num.setdefault(y, []).append(x)
                self.j = self.j +1
                n = n+1
            self.value_automat.emit(self.dicto_team_real)
        else:
            diff = self.dicto_team_num[y][-1] - self.dicto_team_num[y][-2]
            if diff<0:
                for i in range(abs(diff)):
                    self.dicto_team_real[y][-i] = []
                self.value_automat.emit(self.dicto_team_real)
            else: 
                n = 0
                z = max_num_club
                for _ in range(z, x):
                    self.dicto_team_real.setdefault(y, []).append([n+max_num_club, col, f"team{self.j+1}"])
                    self.dicto_team_num.setdefault(y, []).append(x)
                    self.j = self.j +1
                    n = n+1
                self.value_automat.emit(self.dicto_team_real)
    except KeyError:
        n = 0
        for _ in range(x):
            self.dicto_team_real.setdefault(y, []).append([n, col, f"team{self.j+1}"])
            self.dicto_team_num.setdefault(y, []).append(x)
            self.j = self.j +1
            n = n+1
        self.value_automat.emit(self.dicto_team_real)