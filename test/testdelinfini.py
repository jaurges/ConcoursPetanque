def set_team_forreal(self, col):
    x = self.spinbox2.value()
    y = self.lineEdit.text()
    z = 0
    max_num_club = 0
    z = max_num_club
    def del_team():
        for i in range(abs(diff)):
            #self.dicto_team_real[y][-i] = [int, int, ""]
            del self.dicto_team_real[y][i]
            self.j = self.j -1
            n = n+1
        self.value_automat.emit(self.dicto_team_real)
    def add_team():
        for _ in range(z, x):
            self.dicto_team_real.setdefault(y, []).append([n+max_num_club, col, f"t{self.j+1}"])
            self.j = self.j +1
            n = n+1
        self.value_automat.emit(self.dicto_team_real)


    if y in self.dicto_team_real:
        if not len(self.dicto_team_real[y])>= 2:
            add_team()
        else:
            max_num_club = len(self.dicto_team_real[y])
            diff = self.dicto_team_num[y][-1] - self.dicto_team_num[y][-2]
            if diff<0:
                del_team()
            else:
                max_num_club = len(self.dicto_team_real[y])
                add_team()
    else:
        add_team()