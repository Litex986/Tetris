import tkinter as tk
import random as rand
import copy

class Tetris:
    def __init__(self):
        self.touche = {'Gauche': 'q', 'Droite': 'd', 'Bas': 's', 'Rotation': 'z', 'Pause': 'Escape', 'option': False}
        self.credit = False
        self.score = [0, 0]
        self.debugmod = [False, True, False, False]
        self.forme_color = ['blue', 'red', 'purple', 'pink', 'yellow', 'green', 'orange']
        self.color = [0, rand.randint(0, 6)]
        self.forme = [[[196, 195, 194, 193], [185, 195, 205, 215], [194, 195, 196, 197], [205, 195, 185, 175]],[[205, 204, 195, 194], [205, 204, 195, 194], [205, 204, 195, 194], [205, 204, 195, 194]],[[205, 196, 195, 194], [196, 185, 195, 205], [185, 194, 195, 196], [194, 205, 195, 185]],[[205, 195, 194, 193], [185, 184, 194, 204], [183, 193, 194, 195], [203, 204, 194, 184]],[[204, 196, 195, 194], [206, 185, 195, 205], [186, 194, 195, 196], [184, 205, 195, 185]],[[205, 204, 196, 195], [196, 206, 185, 195], [185, 186, 194, 195], [194, 184, 205, 195]], [[205, 206, 194, 195], [196, 186, 205, 195], [185, 184, 196, 195], [194, 204, 185, 195]]]
        self.next_forme = [[[350, 52, 375, 77], [375, 52, 400, 77], [400, 52, 425, 77], [425, 52, 450, 77]], [[375, 40, 400, 65], [375, 65, 400, 90], [400, 40, 425, 65], [400, 65, 425, 90]], [[355, 65, 385, 95], [385, 65, 415, 95], [415, 65, 445, 95], [385, 35, 415, 65]], [[355, 65, 385, 95], [385, 65, 415, 95], [415, 65, 445, 95], [355, 35, 385, 65]], [[355, 65, 385, 95], [385, 65, 415, 95], [415, 65, 445, 95], [415, 35, 445, 65]], [[355, 65, 385, 95], [385, 65, 415, 95], [385, 35, 415, 65], [415, 35, 445, 65]], [[355, 35, 385, 65], [385, 65, 415, 95], [385, 35, 415, 65], [415, 65, 445, 95]]]
        self.next_forme_id = [1000, 1000, 1000, 1000]
        self.element = [None, copy.deepcopy(self.forme[self.color[1]])]
        self.end = True
        self.time = [0, 0]
        self.pause = [True, ['pause_bg', 'pause_pause', 'pause_play', 'pause_recommencer', 'pause_option', 'pause_menu', 'pause_leave']]

    def start(self):
        self.app = tk.Tk()
        self.can = tk.Canvas(self.app, height=600, width=500, background='black')
        self.can.pack()
        self.app.title('Tetris - v1.0.1')
        self.start_page_accueil()
        self.app.mainloop()
    
    def start_page_accueil(self, event=None):
        self.unbind_all()
        self.can.delete('all')
        self.open_score()
        self.can.create_text(250, 348, fill=self.forme_color[rand.randint(0, 6)], font=('Consolas', 7), text=""":::::::::  :::            :::     :::   :::\n:+:    :+: :+:          :+: :+:   :+:   :+:\n+:+    +:+ +:+         +:+   +:+   +:+ +:+\n+#++:++#+  +#+        +#++:++#++:   +#++:\n+#+        +#+        +#+     +#+    +#+\n#+#        #+#        #+#     #+#    #+#\n###        ########## ###     ###    ###""")
        self.can.create_text(250, 350, fill='white', activefill='grey', font=('Consolas', 7), tag="jouer_bouton", text=""":::::::::  :::            :::     :::   :::\n:+:    :+: :+:          :+: :+:   :+:   :+:\n+:+    +:+ +:+         +:+   +:+   +:+ +:+\n+#++:++#+  +#+        +#++:++#++:   +#++:\n+#+        +#+        +#+     +#+    +#+\n#+#        #+#        #+#     #+#    #+#\n###        ########## ###     ###    ###""")
        self.can.create_text(250, 420, fill='white', activefill='grey', font=('Consolas', 3), tag="option_bouton", text="""::::::::  :::::::::  ::::::::::: :::::::::::  ::::::::  ::::    :::\n:+:    :+: :+:    :+:     :+:         :+:     :+:    :+: :+:+:   :+:\n+:+    +:+ +:+    +:+     +:+         +:+     +:+    +:+ :+:+:+  +:+\n+#+    +:+ +#++:++#+      +#+         +#+     +#+    +:+ +#+ +:+ +#+\n+#+    +#+ +#+            +#+         +#+     +#+    +#+ +#+  +#+#+#\n#+#    #+# #+#            #+#         #+#     #+#    #+# #+#   #+#+#\n ########  ###            ###     ###########  ########  ###    ####""")
        self.can.create_text(250, 465, fill='white', activefill='grey', font=('Consolas', 3), tag="credit_bouton", text=""" ::::::::  :::::::::  :::::::::: :::::::::  ::::::::::: :::::::::::\n:+:    :+: :+:    :+: :+:        :+:    :+:     :+:         :+:\n+:+        +:+    +:+ +:+        +:+    +:+     +:+         +:+\n+#+        +#++:++#:  +#++:++#   +#+    +:+     +#+         +#+\n+#+        +#+    +#+ +#+        +#+    +#+     +#+         +#+\n#+#    #+# #+#    #+# #+#        #+#    #+#     #+#         #+#\n ########  ###    ### ########## #########  ###########     ###""")
        self.can.create_text(250, 510, fill='white', activefill='grey', font=('Consolas', 3), tag="quitter_bouton", text=""" ::::::::   :::    ::: ::::::::::: ::::::::::: ::::::::::: :::::::::: :::::::::\n:+:    :+:  :+:    :+:     :+:         :+:         :+:     :+:        :+:    :+:\n+:+    +:+  +:+    +:+     +:+         +:+         +:+     +:+        +:+    +:+\n+#+    +:+  +#+    +:+     +#+         +#+         +#+     +#++:++#   +#++:++#:\n+#+  # +#+  +#+    +#+     +#+         +#+         +#+     +#+        +#+    +#+\n#+#   +#+   #+#    #+#     #+#         #+#         #+#     #+#        #+#    #+#\n ###### ###  ########  ###########     ###         ###     ########## ###    ###""")
        self.can.create_text(247, 150, fill=self.forme_color[rand.randint(0, 6)], font=("Consolas", 10), text="""        ,----,\n      ,/   .`|\n    ,`   .'  :                ___\n  ;    ;     /              ,--.'|_               ,--,\n.'___,/    ,'               |  | :,'    __  ,-. ,--.'|\n|    :     |                :  : ' :  ,' ,'/ /| |  |,       .--.--.\n;    |.';  ;      ,---.   .;__,'  /   '  | |' | `--'_      /  /    '\n`----'  |  |     /     \  |  |   |    |  |   ,' ,' ,'|    |  :  /`./\n    '   :  ;    /    /  | :__,'| :    '  :  /   '  | |    |  :  ;_\n    |   |  '   .    ' / |   '  : |__  |  | '    |  | :     \  \    `.\n    '   :  |   '   ;   /|   |  | '.'| ;  : |    '  : |__    `----.   \\\n    ;   |.'    '   |  / |   ;  :    ; |  , ;    |  | '.'|  /  /`--'  /\n    '---'      |   :    |   |  ,   /   ---'     ;  :    ; '--'.     /\n                \   \  /     ---`-'             |  ,   /    `--'---'\n                 `----'                          ---`-'""")
        self.can.create_text(250, 148, fill=self.forme_color[rand.randint(0, 6)], font=("Consolas", 10), text="""        ,----,\n      ,/   .`|\n    ,`   .'  :                ___\n  ;    ;     /              ,--.'|_               ,--,\n.'___,/    ,'               |  | :,'    __  ,-. ,--.'|\n|    :     |                :  : ' :  ,' ,'/ /| |  |,       .--.--.\n;    |.';  ;      ,---.   .;__,'  /   '  | |' | `--'_      /  /    '\n`----'  |  |     /     \  |  |   |    |  |   ,' ,' ,'|    |  :  /`./\n    '   :  ;    /    /  | :__,'| :    '  :  /   '  | |    |  :  ;_\n    |   |  '   .    ' / |   '  : |__  |  | '    |  | :     \  \    `.\n    '   :  |   '   ;   /|   |  | '.'| ;  : |    '  : |__    `----.   \\\n    ;   |.'    '   |  / |   ;  :    ; |  , ;    |  | '.'|  /  /`--'  /\n    '---'      |   :    |   |  ,   /   ---'     ;  :    ; '--'.     /\n                \   \  /     ---`-'             |  ,   /    `--'---'\n                 `----'                          ---`-'""")
        self.can.create_text(253, 150, fill=self.forme_color[rand.randint(0, 6)], font=("Consolas", 10), text="""        ,----,\n      ,/   .`|\n    ,`   .'  :                ___\n  ;    ;     /              ,--.'|_               ,--,\n.'___,/    ,'               |  | :,'    __  ,-. ,--.'|\n|    :     |                :  : ' :  ,' ,'/ /| |  |,       .--.--.\n;    |.';  ;      ,---.   .;__,'  /   '  | |' | `--'_      /  /    '\n`----'  |  |     /     \  |  |   |    |  |   ,' ,' ,'|    |  :  /`./\n    '   :  ;    /    /  | :__,'| :    '  :  /   '  | |    |  :  ;_\n    |   |  '   .    ' / |   '  : |__  |  | '    |  | :     \  \    `.\n    '   :  |   '   ;   /|   |  | '.'| ;  : |    '  : |__    `----.   \\\n    ;   |.'    '   |  / |   ;  :    ; |  , ;    |  | '.'|  /  /`--'  /\n    '---'      |   :    |   |  ,   /   ---'     ;  :    ; '--'.     /\n                \   \  /     ---`-'             |  ,   /    `--'---'\n                 `----'                          ---`-'""")
        self.can.create_text(480, 590, text='v 1.0.1', fill='grey', font=('Small Fonts', 8))
        self.can.tag_bind('jouer_bouton', '<Button-1>', self.start_game)
        self.can.tag_bind('option_bouton', '<Button-1>', self.option_menu)
        self.can.tag_bind('credit_bouton', '<Button-1>', self.credit_menu)
        self.can.tag_bind('quitter_bouton', '<Button-1>', self.leave)
    
    def start_game(self, event=None):
        self.end = False
        self.pause[0] = False
        self.can.delete('all')
        self.unbind_all()
        self.debugmod = [False, True, False, False]
        self.create_grille()
        self.create_logo()
        self.create_next()
        self.create_decor()
        self.score[1] = 0
        self.multiplicateur_score = [1, 0, 0]
        self.time[0] = 0
        self.speed = 1000
        self.create_score_timeur()
        self.case = [[-1 for i in range(10)] for i in range(22)]
        self.app.bind('<Key>', self.bind_app)
        self.summon_element()
        self.edit_timeur_title()
        self.id = self.app.after(self.speed, self.down_element)
    
    def create_grille(self,):
        for j in range(22):
            for i in range(10):
                self.can.create_rectangle(30 * i, 30 * (j - 2), 30 * (i + 1), 30 * (j - 1), outline='grey', width=4, tag=str(219 - j * 10 - i) + 'i', fill=('white' if j == 22 else 'black'))
    
    def create_next(self):
        self.can.create_rectangle(325, 20, 475, 110, outline='grey')
    
    def create_logo(self):
        self.can.create_text(400, 150, fill='white', font=('Small Fontsaa', 8), tag='title', text=""" _____                _                      _\n/__      \   ___     |  | _     _ __     (_)   ___\n   /  / \ /   /   _   \  |  __|   |   '__ |   |  |   /  __|\n  /  /       |   __ /   |  |_     |  |         |  |    \__  \\\n  \ /         \___|    \__|    |_|         |_|     |___/""")
    
    def create_decor(self):
        self.can.create_polygon((366, 199, 345, 220, 366, 241, 408, 199, 366, 241, 387, 262, 429, 220, 408, 199, 387, 220, 408, 241, 429, 220, 450, 241, 429, 262), width=4, outline='grey')
        self.can.create_polygon((345, 450, 366, 429, 387, 450, 366, 471, 387, 450, 408, 471, 387, 492, 408, 471, 429, 492, 408, 513, 429, 492, 450, 513, 429, 534), width=4, outline='grey')
    
    def create_score_timeur(self):
        self.can.create_text(400, 290, text='Meilleur  score:', fill='grey', font=('Small Fonts', 16))
        self.can.create_text(400, 315, text=self.score[0], fill='grey', font=('Small Fonts', 16), tag='mscore')
        self.can.create_text(400, 350, text='Score  actuel:', fill='grey', font=('Small Fonts', 16))
        self.can.create_text(400, 375, text=self.score[1], fill='grey', font=('Small Fonts', 16), tag='score')
        self.can.create_text(400, 400, text='', fill=self.forme_color[rand.randint(0, 6)], font=('Small Fonts', 16), tag='xx')
        
        timeur = str(self.time[0] // 60) + 'min ' + str(self.time[0] - (self.time[0] // 60) * 60) + 's'
        self.can.create_text(400, 580, text=timeur,  fill='grey', font=('Small Fonts', 12), tag='timeur')
    
    def edit_timeur_title(self):
        self.time[0] += 1
        timeur = str(self.time[0] // 60) + 'min ' + str(self.time[0] - (self.time[0] // 60) * 60) + 's'
        self.can.itemconfigure('timeur', text=timeur)
        self.can.itemconfigure('title', fill=self.forme_color[self.time[0] % 7])
        self.time[1] = self.app.after(1000, self.edit_timeur_title)

    def edit_score(self, x):
        if x == 0:
            self.score[1] += (self.multiplicateur_score[0] + self.multiplicateur_score[1]) * 100
            self.multiplicateur_score[0] += 1
        elif x == 1:
            self.score[1] += 10
        if self.score[1] > self.score[0]:
            self.score[0] = self.score[1]
            self.can.itemconfig('mscore', text=str(self.score[1]))
        self.can.itemconfig('score', text=str(self.score[1]))
        if self.speed > 100 and not self.debugmod[3]:self.speed = 1000 - (self.score[1] // 100) * 10
    
    def open_score(self):
        try:
            file = open('score.tkt', 'r')
            self.score[0] = int(file.read().split('|')[0])
            file.close()
        except:self.score[0] = 0
    
    def unbind_all(self):
        try:
            self.app.after_cancel(self.id)
            self.app.after_cancel(self.time[1])
        except:pass
        try:
            self.app.unbind('<Key>')
            self.can.unbind('<Motion>')
            self.can.tag_unbind('gm', '<Button-1>')
        except:pass

    def bind_app(self, event):
        x = event.keysym
        if not self.pause[0]:
            if x == self.touche.get('Gauche'):
                if self.debugmod[2]:print('Left')
                self.move_hori_element(1)
            elif x == self.touche.get('Droite'):
                if self.debugmod[2]:print('Right')
                self.move_hori_element(-1)
            elif x == self.touche.get('Bas'):
                if self.debugmod[2]:print('Down')
                if not self.end:
                    self.app.after_idle(self.down_element, -10)
            elif x == self.touche.get('Rotation'):
                if self.debugmod[2]:print('Rotation')
                self.rotation_element()
            elif x == 'N':
                print("Debugmode On")
                try:
                    self.debugmod[0] = True
                    self.app.after_cancel(self.id)
                except:self.start_game()
            elif self.debugmod[0]:
                if x == 'c':
                    if self.debugmod[2]:print('Debugmod Stop')
                    self.app.after_cancel(self.id)
                    self.debugmod[1] = False
                elif x == 'v':
                    if self.debugmod[2]:print('Debugmod Start')
                    self.app.after_cancel(self.id)
                    self.debugmod[1] = True
                    self.down_element()
                elif x == 'a':
                    if self.debugmod[2]:print('Up')
                    self.down_element(10)
                elif x == 't':
                    print('Debugmod Chat: On/Off')
                    self.debugmod[2] = False if self.debugmod[2] else True
                elif x == 'l':
                    self.debugmod[3] = True
                    self.speed -= 100
                elif x == 'm':
                    self.debugmod[3] = True
                    self.speed += 100
                else:
                    for i in range(8):
                        if x == str(i):
                            if self.debugmod[2]:print('Debugmod: Change Next')
                            self.next_elemrnt_loding(i - 1)
        if not self.end:
            if x == self.touche.get('Pause'):
                self.echap_menu()
    
    def verif_line(self):
        x = 0
        while x != len(self.case):
            if self.case[x].count(-1) == 0:
                self.delete_line(x)
                x = -1
            x += 1
        for i in range(4):
            if self.case[-3][3 + i] != -1:
                self.party_end()
        self.edit_score(1)
        if self.multiplicateur_score[0] != 1:
            self.multiplicateur_animation(0)
            self.multiplicateur_score[1] += 1
        else:
            self.multiplicateur_score[1] = 0
        self.multiplicateur_score[0] = 1
        self.summon_element()

    def next_element(self):
        for i in range(4):
            self.can.delete(self.next_forme_id[i])
        self.next_forme_id = []
        for i in self.next_forme[self.color[1]]:
            self.next_forme_id.append(self.can.create_rectangle(i[0], i[1], i[2], i[3], width=4, fill=self.forme_color[self.color[1]], outline='grey'))
    
    def next_elemrnt_loding(self, x):
        self.color[1] = x
        self.next_element()
        self.element[1] = copy.deepcopy(self.forme[self.color[1]])
    
    def summon_element(self):
        self.element[0] = self.element[1].copy()
        self.color[0] = self.color[1]
        self.next_elemrnt_loding(rand.randint(0, 6))
        self.rotation = 0
        if self.debugmod[2]:print('Summon:', self.element[0][self.rotation])
        for i in self.element[0][self.rotation]:
            self.can.itemconfigure(str(i) + 'i', fill=self.forme_color[self.color[0]])
    
    def delete_line(self, index):
        if self.debugmod[2]:print('Delete Line')
        self.edit_score(0)
        for i in range(len(self.case[index])):
            self.case[index][i] = -1
            self.can.itemconfigure(str(index * 10 + i) + 'i', fill='black')
        self.complete_line(index)
    
    def complete_line(self, index):
        for i in range(index, 21):
            for j in range(len(self.case[i])):
                self.case[i][j] = self.case[i + 1][j]
                self.can.itemconfigure(str(i * 10 + j) + 'i', fill=(self.forme_color[self.case[i][j]] if self.case[i][j] != -1 else 'black'))
    
    def down_element(self, direction=-10):
        try:
            self.app.after_cancel(self.id)
        except:
            pass
        fixe = False
        for i in self.element[0][self.rotation]:
            if i < 10 or self.case[(i - 10) // 10][int(str(i - 10)[-1])] != -1:
                fixe = True
        if fixe:
            if self.debugmod[2]:print('fixe:', self.element[0][self.rotation])
            for i in self.element[0][self.rotation]:
                    self.case[i // 10][int(str(i)[-1])] = self.color[0]
            self.verif_line()
        else:
            for i in self.element[0][self.rotation]:
                self.can.itemconfigure(str(i) + 'i', fill='black')
            for j in range(len(self.element[0])):
                for i in range(len(self.element[0][j])):
                    self.element[0][j][i] += direction
            for i in self.element[0][self.rotation]:
                self.can.itemconfigure(str(i) + 'i', fill=self.forme_color[self.color[0]])
        if (not self.end) and (self.debugmod[1]):
            self.id = self.app.after(self.speed, self.down_element)
        if self.multiplicateur_score[2] % 4 == 0:
            self.multiplicateur_score[2] = 0
            self.multiplicateur_animation(1)
        else:
            self.multiplicateur_score[2] += 1

    def move_hori_element(self, direction):
        fixe = False
        for i in self.element[0][self.rotation]:
            if direction == 1:
                if int(str(i)[-1]) == 9 or self.case[i // 10][int(str(i + 1)[-1])] != -1:
                    fixe = True
            elif direction == -1:
                if int(str(i)[-1]) == 0 or self.case[i // 10][int(str(i - 1)[-1])] != -1:
                    fixe = True
        if not fixe:
            for i in self.element[0][self.rotation]:
                self.can.itemconfigure(str(i) + 'i', fill='black')
            for j in range(len(self.element[0])):
                for i in range(len(self.element[0][j])):
                    self.element[0][j][i] += direction
            for i in self.element[0][self.rotation]:
                self.can.itemconfigure(str(i) + 'i', fill=self.forme_color[self.color[0]])

    def rotation_element(self):
        fixe = False
        temp = ''
        for i in self.element[0][(self.rotation + 1) % 4]:
            if self.case[i // 10][int(str(i)[-1])] != -1 or i < 10:
                fixe = True
            temp += str(i)[-1]
        if temp.find('0') != -1 and temp.find('9') != -1:
            fixe = True
        if not fixe:
            for i in self.element[0][self.rotation]:
                    self.can.itemconfigure(str(i) + 'i', fill='black')
            self.rotation = (self.rotation + 1) % 4
            for i in self.element[0][self.rotation]:
                    self.can.itemconfigure(str(i) + 'i', fill=self.forme_color[self.color[0]])

    def multiplicateur_animation(self, x):
        if x == 0:
            self.can.itemconfigure('xx', fill=self.forme_color[rand.randint(0, 6)])
            self.can.itemconfigure('xx', text=('x' + str(self.multiplicateur_score[x] - 1) if self.multiplicateur_score[x] - 1 > 1 else ''))
            if self.multiplicateur_score[x] - 1 > 1:
                self.multiplicateur_score[2] = 1
        elif x == 1:
            self.can.itemconfigure('xx', fill=self.forme_color[rand.randint(0, 6)])
            self.can.itemconfigure('xx', text=('x' + str(self.multiplicateur_score[x]) if self.multiplicateur_score[x] > 1 else ''))
    
    def echap_menu(self, event=None):
        if not self.pause[0]:
            if self.debugmod[2]:print('Pause')
            self.pause[0] = True
            self.unbind_all()
            self.can.create_polygon(20, 100, 280, 100, 280, 160, 20, 160, 280, 160, 280, 300, 20, 300, fill='black', outline="white", tag='pause_bg')
            self.can.create_text(150, 130, text='Pause', fill='grey', font=('Small Fonts', 40), tag='pause_pause')
            self.can.create_text(150, 180, text='Reprendre', fill='grey', activefill='white', font=('Small Fonts', 18), tag='pause_play')
            self.can.create_text(150, 205, text='Recommencer', fill='grey', activefill='white', font=('Small Fonts', 18), tag='pause_recommencer')
            self.can.create_text(150, 230, text='Option', fill='grey', activefill='white', font=('Small Fonts', 18), tag='pause_option')
            self.can.create_text(150, 255, text='Menu Principal', fill='grey', activefill='white', font=('Small Fonts', 18), tag='pause_menu')
            self.can.create_text(150, 280, text='Quitter le Jeu', fill='grey', activefill='white', font=('Small Fonts', 18), tag='pause_leave')
            self.can.tag_bind('pause_play', '<Button-1>', self.echap_menu)
            self.can.tag_bind('pause_recommencer', '<Button-1>', self.start_game)
            self.can.tag_bind('pause_option', '<Button-1>', self.option_menu)
            self.can.tag_bind('pause_menu', '<Button-1>', self.start_page_accueil)
            self.can.tag_bind('pause_leave', '<Button-1>', self.leave)
        elif self.pause[0]:
            if self.debugmod[2]:print('Play')
            self.pause[0] = False
            for i in self.pause[1]:
                self.can.delete(i)
                self.can.tag_unbind(i, '<Button-1>')
                self.app.bind('<Key>', self.bind_app)
            self.down_element()
            self.edit_timeur_title()

    def option_menu(self, event=None):
        if not self.touche.get('option'):
            self.touche['option'] = True
            self.can.create_rectangle(0, 0, 500, 600, fill='black', tag='option_bg')
            self.can.create_text(250, 50, text='Option', fill='white', font=('Small Fonts', 60), tag='option_title')
            self.can.create_text(250, 580, text='Back', activefill='grey', fill='white', font=('Small Fonts', 25), tag='option_back')
            x = 0
            for cle, valeur in self.touche.items():
                self.can.create_text(100 if not cle == 'option' else 250, 170 + x, text=cle +' :' if not cle == 'option' else '', fill='white', font=('Small Fonts', 20), tag='option_' + cle +'_text')
                self.can.create_rectangle(290, 150 + x, 410, 195 + x, fill='black', outline='white', tag='option_' + cle +'_cadre') if not cle == 'option' else ''
                self.can.create_text(350, 170 + x, text=valeur if not cle == 'option' else '', fill='white', font=('Small Fonts', 25), tag='option_' + cle +'_touche')
                x += 50
            self.can.tag_bind('option_Gauche_cadre', '<Button-1>', lambda event:self.option_touche(event, 'Gauche'))
            self.can.tag_bind('option_Droite_cadre', '<Button-1>', lambda event:self.option_touche(event, 'Droite'))
            self.can.tag_bind('option_Bas_cadre', '<Button-1>', lambda event:self.option_touche(event, 'Bas'))
            self.can.tag_bind('option_Rotation_cadre', '<Button-1>', lambda event:self.option_touche(event, 'Rotation'))
            self.can.tag_bind('option_Pause_cadre', '<Button-1>', lambda event:self.option_touche(event, 'Pause'))
            self.can.tag_bind('option_back', '<Button-1>', self.option_menu)
        else:
            self.can.unbind_all('<Button-1>')
            self.touche['option'] = False
            temp = [['option_bg', 'option_title', 'option_back'], ['option_Gauche_', 'option_Droite_', 'option_Bas_', 'option_Rotation_', 'option_Pause_']]
            for i in temp[0]:
                self.can.delete(i)
            for i in temp[1]:
                for j in ['text', 'cadre', 'touche']:
                    self.can.delete(i + j)

    def option_touche(self, event, tag):
        self.tag = tag
        self.can.itemconfigure('option_option_text', text='Presser une touche')
        self.can.itemconfigure('option_' + tag +'_touche', text='')
        self.app.bind('<Key>', self.option_key)

    def option_key(self, event):
        if self.touche.get('option'):
            self.app.unbind('<Key>')
            self.can.itemconfigure('option_option_text', text='')
            self.can.itemconfigure('option_' + self.tag +'_touche', text=event.keysym)
            self.touche[self.tag] = event.keysym

    def credit_menu(self, event=None):
        if not self.credit:
            self.credit = True
            self.can.create_rectangle(0, 0, 500, 600, fill='black', tag='credit_bg')
            self.can.create_text(250, 30, text='Credit', fill='white', font=('Small Fonts', 40), tag='credit_title')
            self.can.create_text(250, 580, text='Back', activefill='grey', fill='white', font=('Small Fonts', 25), tag='credit_back')
            self.can.create_text(250, 315, fill='white', font=('Small Fonts', 12), tag='credit_text', justify='center', text='Chef de Projet: Litex986\nResponsable Projet: Litex986\n\nResponsable Développement: Litex986\nDéveloppeur: Litex986\nCo-Développeur: Litex986\n\nResponsable Graphique: Litex986\nGraphiste: Litex986\nCo-Graphiste: Litex986\n\nModélisateur 2D: Litex986\n\nResponsable Marketing: Litex986\nMarketing: Litex986\n\nFinancement: Absent comme mon avenir\n\nBeta-Testeur:\nLitex986\nMère  Litex986\nSoeur Litex986\nPère Litex986\nFrère Litex986')
            self.can.tag_bind('credit_back', '<Button-1>', self.credit_menu)
        else:
            self.can.unbind_all('<Button-1>')
            self.credit = False
            temp = ['credit_bg', 'credit_title', 'credit_back', 'credit_text']
            for i in temp:
                self.can.delete(i)

    def party_end(self):
        self.end = True
        if self.debugmod[2]:print('End Game:', self.case)
        self.app.after_cancel(self.id)
        self.app.after_cancel(self.time[1])
        self.can.create_rectangle(20, 100, 280, 300, fill='black', outline="white")
        self.can.create_text(150, 200, fill='grey', font=('Consolas', 7), activefill='white', tag='gm', text="""MM'\"""\""`MM\nM' .mmm. `M\nM  MMMMMMMM .d8888b. 88d8b.d8b. .d8888b.\nM  MMM   `M 88'  `88 88'`88'`88 88ooood8\nM. `MMM' .M 88.  .88 88  88  88 88.  ...\nMM.     .MM `88888P8 dP  dP  dP `88888P'\nMMMMMMMMMMM\nMMP\""\"""YMM\nM' .mmm. `M\nM  MMMMM  M dP   .dP .d8888b. 88d888b.\nM  MMMMM  M 88   d8' 88ooood8 88'  `88\nM. `MMM' .M 88 .88'  88.  ... 88\nMMb     dMM 8888P'   `88888P' dP\nMMMMMMMMMMM""")
        self.can.bind('<Motion>', self.party_end_gm)
        self.can.tag_bind('gm', '<Button-1>', self.start_game)
        try:
            file = open('score.tkt', 'r')
            temp = file.read().split('|')
            file.close()
            temp.pop(0)
            a = str(self.score[0])
            for i in temp:
                a += '|' + i
        except:a = str(self.score[0])
        file = open('score.tkt', 'w')
        file.write(a)
        file.close()
    
    def party_end_gm(self, event):
        if event.x > 20 and event.x < 280 and event.y > 100 and event.y < 300:
            self.can.itemconfigure('gm', text="""MM""\"""\""`MM          oo\nMM  mmmm,  M\nM'        .M .d8888b. dP .d8888b. dP    dP .d8888b. 88d888b.\nMM  MMMb. "M 88ooood8 88 88'  `88 88    88 88ooood8 88'  `88\nMM  MMMMM  M 88.  ... 88 88.  .88 88.  .88 88.  ... 88\nMM  MMMMM  M `88888P' 88 `88888P' `88888P' `88888P' dP\nMMMMMMMMMMMM          88\n                      dP""", font=('Consolas', 5))
        else:
            self.can.itemconfigure('gm', text="""MM'\"""\""`MM\nM' .mmm. `M\nM  MMMMMMMM .d8888b. 88d8b.d8b. .d8888b.\nM  MMM   `M 88'  `88 88'`88'`88 88ooood8\nM. `MMM' .M 88.  .88 88  88  88 88.  ...\nMM.     .MM `88888P8 dP  dP  dP `88888P'\nMMMMMMMMMMM\nMMP\""\"""YMM\nM' .mmm. `M\nM  MMMMM  M dP   .dP .d8888b. 88d888b.\nM  MMMMM  M 88   d8' 88ooood8 88'  `88\nM. `MMM' .M 88 .88'  88.  ... 88\nMMb     dMM 8888P'   `88888P' dP\nMMMMMMMMMMM""", font=('Consolas', 7))

    def leave(self, event=None):
        self.unbind_all()
        self.app.quit()



a = Tetris()
a.start()