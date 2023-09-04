def set_team_forreal(self, col):
        x = self.spinbox2.value()
        y = self.lineEdit.text()
        z = 0
        max_num_club = 0
        try:
            if not self.dicto_team_real[y]:
                pass
            else:
                try:
                    self.dicto_team_num.setdefault(y, []).append(x)
                    print(self.dicto_team_num[y][-1])
                    print(f"{self.dicto_team_num[y][-2]}\n")
                    diff = self.dicto_team_num[y][-1] - self.dicto_team_num[y][-2]
                    #print(diff)
                    max_num_club = len(self.dicto_team_real[y])
                    n = 0
                    z = max_num_club
                    if diff<0:
                        print("feur")
                        for i in range(abs(diff)):
                            #self.dicto_team_real[y][-i] = [int, int, ""]
                            del self.dicto_team_real[y][i]
                            self.j = self.j -1
                            n = n+1
                        self.value_automat.emit(self.dicto_team_real)
                        print(self.dicto_team_real)
                    else: 
                        max_num_club = len(self.dicto_team_real[y])
                        #print(max_num_club)
                except Exception as e: 
                    max_num_club = len(self.dicto_team_real[y])
                    #print(e)
        except KeyError:
            pass
        n = 0
        z = max_num_club
        for _ in range(z, x):
            self.dicto_team_real.setdefault(y, []).append([n+max_num_club, col, f"team{self.j+1}"])
            self.j = self.j +1
            n = n+1
        self.value_automat.emit(self.dicto_team_real)
        #print(self.dicto_team_real)