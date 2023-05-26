# Import lib
from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg
import os
import datetime

sg.theme('BlueMono')  # theme for windows

layout = [[sg.Text('Prénom Nom : '), sg.InputText()],  # row 1
          [sg.Button('VIP1'), sg.Button('VIP2'), sg.Button('VIP3')]]  # row 2

window = sg.Window('Génération de Carte VIP - Unicorn', layout)  # windows name


def ds(vip):  # define that vip1 = 7 days, vip = 14 days, etc...
    return 7 if int(vip[len(vip)-1]) == 1 else 14 if int(vip[len(vip)-1]) == 2 else 31


def exp(nvip):  # calculate the expiry date from today's date to a certain date
    return datetime.date.today() + datetime.timedelta(days=nvip)


try:
    while True:  # as long as the window is open
        event, values = window.read()  # reading the parameters entered
        name = values[0]  # line 1 event
        font = ImageFont.truetype(font='afont/Montserrat-Light.otf', size=55)  # font definition (Monserrat) with a
        # size of 55
        fontexp = ImageFont.truetype(font='afont/Montserrat-Light.otf', size=15)  # font definition (Monserrat) with
        # a size of 55
        if event != sg.WIN_CLOSED:  # if you don't close the page
            img = Image.open(r'./TemplateCarte/' + event + '.png')  # open a card template according to the vip selected
        else:
            break
        draw = ImageDraw.Draw(img)  # image initialization
        width, height = img.size  # define image size
        whname = ((width / 4) - 10, (height / 12) * 8)  # definition of the zone in which the 'First name last name'
        # will be entered
        whxp = ((width / 10), (height / 24) * 23)  # definition of the zone in which the expiry date will be entered
        draw.text(whname, name, font=font, fill='ghostwhite', stroke_width=2, anchor='mm')  # write the 'First name
        # Last name' in the field provided for this purpose with the font defined beforehand, the 'ghostwhite'
        # filling and a centering of the text with anchor
        draw.text(whxp, str(exp(ds(event))), font=fontexp, fill='ghostwhite', stroke_width=1, anchor='mm')  # same
        # thing with the expiration date and the different function calls defined before
        img.save(os.path.abspath('CarteClient') + '/' + event + '-' + name + '.png')  # save the image in the
        # appropriate folder
    window.close()  # close input window
except TypeError:  # management of 'TypeError' exceptions
    pass
