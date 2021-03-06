# -*- coding: utf-8 -*-

"""
INTRODUCTION
------------
Programme de création/verification de fichiers HTML5
et CSS balisés.

Créateur: Alexandre BONIN 2016
PYTHON
"""

from tkinter import Tk, Toplevel, Button, Label, Frame, PhotoImage, TclError


class Application(object):

    def __init__(self):
        self.master = Tk()
        self.master.title('HTML Creator')

        try:
            self.master.iconbitmap('logo.ico')
        except TclError:
             # Pour les utilisateurs non Windows
             pass

        self.frame = Frame(borderwidth=1, relief='sunken')
        self.frame.grid(row=0, column=0, pady=20, padx=5)

        message_base = ("Bonjour, HTML Creator vous permet de créer "
        "des fichiers HTML5 et CSS 3 balisés et fonctionnels en un seul "
        "clic ! Vous voulez essayer ? Cliquez donc sur le bouton ci-dessous")
        message_base = resize_text(message_base, 20)

        self.description = Label(master=self.frame,
                                 text=message_base,
                                 font="Times 9")
        self.description.grid(row=0, column=0)

        self.button_html = Button(master=self.master,
                                  text="Créer fichier HTML & CSS",
                                  font="Georgia 8",
                                  command=self.creer_fichiers)
        self.button_html.grid(row=0, column=1, padx=5)

        #VERSION#
        Label(master = self.master,
              text = '1.1',
              font = 'Times 8').place(x=0,y=0)

    def creer_fichiers(self):
        self.creer_fichier_html()
        self.creer_fichier_css()

    def creer_fichier_html(self):
        fichier = open(file="page.html", mode="w+")

        contenu=('<!DOCTYPE html>\n<!-- Generated by HTML Creator (2016) -->\n'
        '<html>\n'
        '    <head>\n'
        '        <meta charset="UTF-8"/>\n'
        '        <link rel="Stylesheet" href="style.css"/>\n'
        '        <title>Titre Page</title>\n'
        '    </head>\n\n'
        '    <body>\n'
        '        <header>\n        </header>\n\n'
        '        <section>\n        </section>\n\n'
        '        <footer>\n        </footer>\n\n'
        '    </body>\n'
        '</html>')

        fichier.write(contenu)
        fichier.close()

    def creer_fichier_css(self):

        fichier = open(file="style.css", mode="w+")

        contenu = ("/* CSS generated by HTML Creator (2016) */\n\n"
        "@font-face\n{\n\n}\n\n" "body\n{\n\n}\n")

        fichier.write(contenu)
        fichier.close()

def resize_text(text, max_chars):
    list_tmp = []
    string_tmp = ""
    char_suivant = ""
    compteur = 0

    for char in text:
        string_tmp += char

        try:
            char_suivant = text[compteur + 1]
        except IndexError:
            pass

        if len(string_tmp) >= max_chars and char_suivant == " ":
            list_tmp.append(string_tmp)
            string_tmp = ""

        compteur += 1


    string_final = "\n".join(list_tmp)
    return string_final

def main():
    app = Application()
    app.master.mainloop()

main()


if __name__ == "__main__":

    def test():
        text = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        "ccccccccccccccccccccccccccccccccccccccccccccccccccccccc")

        print(resize_text(text = text, max_chars = 10))

    test()
