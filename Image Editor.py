from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog

root = tk.Tk()
STR = 'Invalid Input'
THRESHOLD = 1
P_THRESHOLD = 127

root.title(" IMAGE EDITOR ")
root.geometry('1920x1080')

#ICON
ic = PhotoImage(file = 'C:\\Users\\DAKSH\\OneDrive\\Desktop\\Project\\download.png')
root.iconphoto(False, ic)

header = Frame(root, width=750, height=800, bg="white", bd = 10, relief = GROOVE)
header.grid(columnspan=1, rowspan=20, column = 0,row = 0, sticky =N + E + W + S)
header.grid_columnconfigure(0, weight = 2)
header.grid_propagate(0)

#bg = ImageTk.PhotoImage(file = "C:\\Users\\DAKSH\\OneDrive\\Desktop\\Project\\wp.jpg")
main = Canvas(root, width=750, height=800, bg="#FFA500", bd = 10, relief = GROOVE)
main.grid(columnspan=1, rowspan=7, column = 1, row = 0, sticky = N + E + W + S)
#main.create_image(1, 1, image=bg, anchor="n")
main.grid_propagate(0)

main_content = LabelFrame(root, width=750, height=800, text = " PREVIEW ", bg="#FFA500", bd = 10, font = " Times ", labelanchor = N)
main_content.grid(columnspan=1, rowspan=7, column = 1, row = 0, sticky = N + E + W + S)
main_content.grid_propagate(0)

#logo
logo = Image.open('C:\\Users\\DAKSH\\OneDrive\\Desktop\\Project\\logo1.png')
logo = ImageTk.PhotoImage(logo)
logo_lable = tk.Label(header,image = logo, bd = 0)
logo_lable.image = logo
logo_lable.grid(column = 0, row = 0)

#instruction1
instruction = tk.Label(header, text = " PROCESS YOUR IMAGE WITH : ",font = "Times", bg = "white")
instruction.grid(rowspan = 1,column = 0, row = 1)

def get_img():
    global file
    file = filedialog.askopenfile(parent = root, mode = 'rb', title = "Choose An Image ", filetype=[("Image Files", "*.png"), ("jpg", "*.jpg"), ("jpeg", "*.jpeg"),("All Files", "*.*")])
    if file:
        main_content.grid()
        img = Image.open(file)
        img = iresize(img,750,320)
        img = ImageTk.PhotoImage(img)
        img_lable = tk.Label(main_content,image=img,bd = 0)
        img_lable.image = img
        img_lable.grid(rowspan=1, row=1, sticky = N + E + W + S)
        #canvas.create_window(1125, 210, window=img_lable)
        # instruction2
        temp = tk.Label(main_content, text=" Original Image : ", font="Times", bg="#FFA500")
        temp.grid(rowspan=1, row=0, sticky = N + E + W + S)

def outimg(fimg):
    fimg1 = iresize(fimg,750,320)
    fimg1 = ImageTk.PhotoImage(fimg1)
    fimg_lable = tk.Label(main_content,image=fimg1, bd = 0)
    fimg_lable.image = fimg1
    fimg_lable.grid(rowspan=1, row=4)

    def saveimg(fimg):
        save_text.set("             SAVING              ")
        tefp = filedialog.asksaveasfilename(title="Save Edited Image As")
        fimg.save(tefp)
        save_button.grid_remove()
        #fimg_lable.destroy()

    def closewindow():
        save_button.grid_remove()
        fimg_lable.grid_remove()
        cbutton.grid_remove()
        main_content.grid_remove()

    #BUTTON1
    save_text = tk.StringVar()
    save_button = tk.Button(main_content, command = lambda:saveimg(fimg), textvariable = save_text, width = 20, font = "Times", bg = "#A9A9A9")
    save_text.set(" SAVE EDITED IMAGE ")
    save_button.grid(rowspan=1, row=5)

    #BUTTON2
    cbutton = tk.Button(main_content, command = lambda:closewindow(), width = 20, text = " CLOSE ", font = "Times", bg = "#A9A9A9")
    cbutton.grid(rowspan=1, row=6)

def iresize(image_pil, width, height):
    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height
    if ratio_w < ratio_h:
        #It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        #Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height
    image_resize = image_pil.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (width, height), (255, 160, 0, 255))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')

#FILTERS
def filter():
    ft.config(state="disabled")
    sub = Frame(header, width=750, height=450, relief = GROOVE, bd = 10, bg="white")
    sub.grid(columnspan=1, rowspan=10, column=0, row=3)
    br_button.grid(rowspan=1, column=0, row=23)
    crop_button.grid(rowspan=1, column=0, row=24)
    b_button.grid(rowspan=1, column=0, row=25)
    rb.grid(rowspan=1, column=0, row=26)
    close.grid(rowspan=1, column=0, row=27)
    #greyscale function
    def greyscale():
        gs_text.set(" Loading..... ")
        get_img()
        if file:
            #main_content.grid()
            pik = Image.open(file)
            for i in range(0, pik.size[0] - 1):
                for j in range(0, pik.size[1] - 1):
                    pixelColorVals = pik.getpixel((i, j))
                    avg = int(pixelColorVals[0]*0.299 + pixelColorVals[1]*0.587 + pixelColorVals[2]*0.114)
                    redPixel = avg
                    greenPixel = avg
                    bluePixel = avg
                    pik.putpixel((i, j), (redPixel, greenPixel, bluePixel))
            #instruction2
            temp = tk.Label(main_content, text=" GreyScale Image : ", font="Times", bg="#FFA500")
            temp.grid(rowspan = 1, row=3)
            outimg(pik)
            #export_file_path = filedialog.asksaveasfilename(title="Save Edited Image As")
            #imgGray.save(export_file_path)
        gs_text.set(" GREYSCALE FILTER")

    #BUTTON2
    gs_text = tk.StringVar()
    gs_button = tk.Button(sub, command = lambda:greyscale(), textvariable = gs_text, width = 23, font = "Times", bg = "#A9A9A9", justify=CENTER)
    gs_text.set(" GREYSCALE FILTER ")
    gs_button.grid(rowspan = 1,column = 0, row = 1)

    def negative():
        nr_text.set(" Loading..... ")
        get_img()
        if file:
            img3 = Image.open(file)
            for i in range(0, img3.size[0] - 1):
                for j in range(0, img3.size[1] - 1):
                    pixelColorVals = img3.getpixel((i, j))
                    redPixel = 255 - pixelColorVals[0]
                    greenPixel = 255 - pixelColorVals[1]
                    bluePixel = 255 - pixelColorVals[2]
                    img3.putpixel((i, j), (redPixel, greenPixel, bluePixel))
            outimg(img3)
            # instruction4
            temp2 = tk.Label(main_content, text="   Inverted Image : ", font="Times", bg="#FFA500")
            temp2.grid(rowspan = 1, row=3)
        nr_text.set(" INVERT IMAGE ")

    #BUTTON3
    nr_text = tk.StringVar()
    nr_button = tk.Button(sub, command = lambda:negative(), textvariable = nr_text, width = 23, font = "Times", bg = "#A9A9A9", justify=CENTER)
    nr_text.set(" INVERT IMAGE ")
    nr_button.grid(rowspan = 1,column = 0, row = 2)

    def sepia():
        mr_text.set(" Loading..... ")
        get_img()
        if file:
            img3 = Image.open(file)
            width, height = img3.size
            pixels = img3.load()  # create the pixel map
            for py in range(height):
                for px in range(width):
                    r, g, b = img3.getpixel((px, py))
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                    if tr > 255:
                        tr = 255
                    if tg > 255:
                        tg = 255
                    if tb > 255:
                        tb = 255
                    pixels[px, py] = (tr, tg, tb)
            outimg(img3)
            # instruction4
            temp2 = tk.Label(main_content, text="   MonoChrome Image :     ", font="Times", bg="#FFA500")
            temp2.grid(rowspan = 1, row=3)
        mr_text.set(" MONOCHROME FILTER")

    #BUTTON4
    mr_text = tk.StringVar()
    mr_button = tk.Button(sub, command = lambda:sepia(), textvariable = mr_text, width = 23, font = "Times", bg = "#A9A9A9", justify=CENTER)
    mr_text.set(" MONOCHROME FILTER ")
    mr_button.grid(rowspan = 1,column = 0, row = 3)

    def pixel_image():
        r_text.set(" Loading..... ")
        get_img()
        if file:
            img4 = Image.open(file)
            imgSmall = img4.resize((96, 96))
            # Scale back up using NEAREST to original size
            result = imgSmall.resize(img4.size, Image.NEAREST)
            outimg(result)
            #instruction4
            temp2 = tk.Label(main_content, text=" Pixelized Image : ", font="Times", bg="#FFA500")
            temp2.grid(rowspan = 1, row=3)
        r_text.set(" PIXELIZE IMAGE ")

    #BUTTON5
    r_text = tk.StringVar()
    r_button = tk.Button(sub, command = lambda:pixel_image(), textvariable = r_text, width = 23, font = "Times", bg = "#A9A9A9", justify=CENTER)
    r_text.set(" PIXELIZE IMAGE ")
    r_button.grid(rowspan = 1,column = 0, row = 4)

    def posterize():
        tx.set(" Loading..... ")
        get_img()
        if file:
            img5 = Image.open(file)
            for i in range(0, img5.size[0] - 1):
                for j in range(0, img5.size[1] - 1):
                    pixelColorVals1 = img5.getpixel((i, j))
                    redPixel = pixelColorVals1[0]
                    greenPixel = pixelColorVals1[1]
                    bluePixel = pixelColorVals1[2]
                    if redPixel > P_THRESHOLD:
                        redPixel = 255
                    else:
                        redPixel = 0
                    if greenPixel > P_THRESHOLD:
                        greenPixel = 255
                    else:
                        greenPixel = 0
                    if bluePixel > P_THRESHOLD:
                        bluePixel = 255
                    else:
                        bluePixel = 0
                    img5.putpixel((i, j), (redPixel, greenPixel, bluePixel))
            outimg(img5)
            # instruction5
            temp2 = tk.Label(main_content, text="  Posterize Image : ", font="Times", bg="#FFA500")
            temp2.grid(rowspan=1, row=3)
        tx.set(" POSTERIZE IMAGE ")

    #BUTTON6
    tx = tk.StringVar()
    tx_button = tk.Button(sub, command = lambda:posterize(), textvariable = tx, width = 23, font = "Times", bg = "#A9A9A9", justify=CENTER)
    tx.set(" POSTERIZE IMAGE ")
    tx_button.grid(rowspan = 1,column = 0, row = 5)

    def solarize():
        stext.set(" Loading..... ")
        get_img()
        if file:
            png = Image.open(file)
            for i in range(png.size[0]):
                for j in range(png.size[1]):
                    pixel = png.getpixel((i, j))
                    red = pixel[0]
                    green = pixel[1]
                    blue = pixel[2]
                    if red > P_THRESHOLD:
                        red = 255 - red
                    else:
                        red *= 1
                    if green > P_THRESHOLD:
                        green = 255 - green
                    else:
                        green *= 1
                    if blue > P_THRESHOLD:
                        blue = 255 - blue
                    else:
                        blue *= 1
                    png.putpixel((i, j), (red, green, blue))
            outimg(png)
            # instruction4
            temp2 = tk.Label(main_content, text=" Solarize Image : ", font="Times", bg="#FFA500")
            temp2.grid(rowspan = 1, row=3)
        stext.set(" SOLARIZE IMAGE ")

    #BUTTON7
    stext = tk.StringVar()
    sbutton = tk.Button(sub, command = lambda:solarize(), textvariable = stext, width = 23, font = "Times", bg = "#A9A9A9", justify=CENTER)
    stext.set(" SOLARIZE IMAGE ")
    sbutton.grid(rowspan = 1,column = 0, row = 6)

    def ht():
        htext.set(" Loading.... ")
        get_img()
        if file:
            im = Image.open(file)
            width, height = im.size
            new = Image.new("RGB", (width, height), "white")
            pixels = new.load()
            for i in range(0, width, 2):  # transform to half tones
                for j in range(0, height, 2):

                    p1 = im.getpixel((i, j))  # get Pixels
                    p2 = im.getpixel((i, j + 1))
                    p3 = im.getpixel((i + 1, j))
                    p4 = im.getpixel((i + 1, j + 1))
                    gray1 = (p1[0] * 0.299) + (p1[1] * 0.587) + (p1[2] * 0.114)  # Transform to grayscale
                    gray2 = (p2[0] * 0.299) + (p2[1] * 0.587) + (p2[2] * 0.114)
                    gray3 = (p3[0] * 0.299) + (p3[1] * 0.587) + (p3[2] * 0.114)
                    gray4 = (p4[0] * 0.299) + (p4[1] * 0.587) + (p4[2] * 0.114)
                    sat = (gray1 + gray2 + gray3 + gray4) / 4  # saturation percentage
                    if sat > 223:
                        pixels[i, j] = (255, 255, 255)  # White
                        pixels[i, j + 1] = (255, 255, 255)  # White
                        pixels[i + 1, j] = (255, 255, 255)  # White
                        pixels[i + 1, j + 1] = (255, 255, 255)  # White
                    elif sat > 159:
                        pixels[i, j] = (255, 255, 255)  # White
                        pixels[i, j + 1] = (0, 0, 0)  # Black
                        pixels[i + 1, j] = (255, 255, 255)  # White
                        pixels[i + 1, j + 1] = (255, 255, 255)  # White
                    elif sat > 95:
                        pixels[i, j] = (255, 255, 255)  # White
                        pixels[i, j + 1] = (0, 0, 0)  # Black
                        pixels[i + 1, j] = (0, 0, 0)  # Black
                        pixels[i + 1, j + 1] = (255, 255, 255)  # White
                    elif sat > 32:
                        pixels[i, j] = (0, 0, 0)  # Black
                        pixels[i, j + 1] = (255, 255, 255)  # White
                        pixels[i + 1, j] = (0, 0, 0)  # Black
                        pixels[i + 1, j + 1] = (0, 0, 0)  # Black
                    else:
                        pixels[i, j] = (0, 0, 0)  # Black
                        pixels[i, j + 1] = (0, 0, 0)  # Black
                        pixels[i + 1, j] = (0, 0, 0)  # Black
                        pixels[i + 1, j + 1] = (0, 0, 0)  # Black
            outimg(new)
            temp2 = tk.Label(main_content, text=" HalfTone Image : ", font="Times", bg="#FFA500")
            temp2.grid(rowspan=1, row=3)
        htext.set(" HALFTONE IMAGE ")

    #BUTTON8
    htext = tk.StringVar()
    hbutton = tk.Button(sub, command=lambda: ht(), textvariable=htext, width=23, font="Times", bg="#A9A9A9", justify=CENTER)
    htext.set(" HALFTONE IMAGE ")
    hbutton.grid(rowspan=1, column=0, row=7)

    def cw1():
        sub.grid_remove()
        br_button.grid(rowspan=1, column=0, row=3)
        crop_button.grid(rowspan=1, column=0, row=5)
        b_button.grid(rowspan=1, column=0, row=7)
        rb.grid(rowspan=1, column=0, row=9)
        close.grid(rowspan=1, column=0, row=11)
        ft.config(state="normal")

    #BUTTON8
    cbutton = tk.Button(sub, command=lambda: cw1(), width=23, text=" CLOSE ", font="Times", bg="#A9A9A9")
    cbutton.grid(rowspan=1, row=8)

#BUTTON1
ft = tk.Button(header, command=lambda: filter(), text=" IMAGE FILTERS ", width = 23, font = "Times", bg = "#8c92ac")
ft.grid(rowspan = 1,column = 0, row = 2)

def brighteness():
    br_button.config(state="disabled")
    br_text.set(" Loading... ")
    br = Frame(header, width=250, height=200, bg="white", relief=GROOVE, bd=10)
    br.grid(rowspan=6, column=0, row=4)
    crop_button.grid(rowspan=1, column=0, row=10)
    b_button.grid(rowspan=1, column=0, row=11)
    rb.grid(rowspan=1, column=0, row=12)
    close.grid(rowspan=1, column=0, row=13)
    def darken():
        sd_text.set(" Loading.... ")
        get_img()
        if file:
            img2 = Image.open(file)
            factor = fac.get()
            for i in range(0, img2.size[0] - 1):
                for j in range(0, img2.size[1] - 1):
                    pixelColorVals = img2.getpixel((i, j))
                    redPixel = pixelColorVals[0] // int(factor)
                    greenPixel = pixelColorVals[1] // int(factor)
                    bluePixel = pixelColorVals[2] // int(factor)
                    img2.putpixel((i, j), (redPixel, greenPixel, bluePixel))
            outimg(img2)
            # instruction3
            temp1 = tk.Label(main_content, text=" Darkened Image : ", font="Times", bg="#FFA500")
            temp1.grid(rowspan = 1, row=3)
        sd_text.set(" DECREASE IMAGE BRIGHTNESS ")
    def brighten():
        sb_text.set(" Loading.... ")
        get_img()
        if file:
            img1 = Image.open(file)
            factor = fac.get()
            for i in range(0, img1.size[0]):
                for j in range(0, img1.size[1]):
                    pixelColorVals = img1.getpixel((i, j))
                    redPixel = pixelColorVals[0] * int(factor)
                    greenPixel = pixelColorVals[1] * int(factor)
                    bluePixel = pixelColorVals[2] * int(factor)
                    img1.putpixel((i, j), (redPixel, greenPixel, bluePixel))
            outimg(img1)
            fac.delete(0, END)
            # instruction3
            temp1 = tk.Label(main_content, text="Brightened Image : ", font="Times", bg="#FFA500")
            temp1.grid(rowspan = 1, row=3)
        sb_text.set(" INCREASE IMAGE BRIGHTNESS ")

    def cw3():
        br.grid_remove()
        crop_button.grid(rowspan=1, column=0, row=5)
        b_button.grid(rowspan=1, column=0, row=7)
        rb.grid(rowspan=1, column=0, row=9)
        close.grid(rowspan=1, column=0, row=11)
        br_button.config(state="normal")

    inst = tk.Label(br,text = " Enter Enhancement Factor : ", font="Times", bg="#A9A9A9")
    inst.grid(row=0, sticky=N + S)
    fac = tk.Entry(br,font = "Times",width = 7)
    fac.grid(row=1, sticky=N + S)

    sb_text = tk.StringVar()
    sb_button = tk.Button(br, command=lambda: brighten(), textvariable=sb_text, font="Times", bg="#8c92ac")
    sb_text.set(" INCREASE IMAGE BRIGHTNESS ")
    sb_button.grid(rowspan=1, row = 2, sticky=N + S)

    sd_text = tk.StringVar()
    sd_button = tk.Button(br, command=lambda: darken(), textvariable=sd_text, font="Times", bg="#8c92ac")
    sd_text.set(" DECREASE IMAGE BRIGHTNESS ")
    sd_button.grid(rowspan=1, row = 3, sticky=N + S)

    cb = tk.Button(br, command=lambda: cw3(), width=23, text=" CLOSE ", font="Times", bg="#A9A9A9")
    cb.grid(rowspan=1, row=4)

    br_text.set(" MODIFY BRIGHTNESS ")


#BUTTON2
br_text = tk.StringVar()
br_button = tk.Button(header, command = lambda:brighteness(), textvariable = br_text, width = 23,  font = "Times", bg = "#8c92ac", justify=CENTER)
br_text.set(" MODIFY BRIGHTNESS ")
br_button.grid(rowspan = 1,column = 0, row = 3)

def crop_img():
    crop_text.set(" Loading..... ")
    get_img()
    crop = Frame(header, width=250, height=200, bg="white", relief = GROOVE, bd = 10)
    crop.grid(rowspan=6, column=0, row=6)
    b_button.grid(rowspan=1, column=0, row=12)
    rb.grid(rowspan=1, column=0, row=13)
    close.grid(rowspan=1, column=0, row=14)
    if file:
        crop_button.config(state="disabled")
        crop.grid()
        img4 = Image.open(file)
        width = img4.size[0]
        height = img4.size[1]
        def get_input():
            ip_text.set(" Croping... ")
            var1 = var1_lab.get()
            var2 = var2_lab.get()
            var3 = var3_lab.get()
            var4 = var4_lab.get()
            if (int(var1) + int(var3) < width) and (int(var2) + int(var4) < height):
                m1 = int(var1) + int(var3)
                m2 = int(var2) + int(var4)
                cropimg = Image.new("RGB", (width - m1, height - m2), "white")
                cp = img4.load()
                cp1 = cropimg.load()
                for i in range(width - m1):
                    for j in range(height - m2):
                        cp1[i,j] = cp[i + int(var1),j + int(var2)]
                #cropimg = img4.crop((int(var1),int(var2), width - int(var3), height - int(var4)))
                temp2 = tk.Label(main_content, text="Cropped Image : ", font="Times", bg="#FFA500")
                temp2.grid(rowspan = 1, row=3)
                outimg(cropimg)
                var1_lab.delete(0, END)
                var2_lab.delete(0, END)
                var3_lab.delete(0, END)
                var4_lab.delete(0, END)
                #crop.grid_remove()

            else:
                crop_text.set(STR)
                ip_button.config(state="disabled")

            ip_text.set(" CROP ")


        def cw2():
            crop.grid_remove()
            b_button.grid(rowspan=1, column=0, row=7)
            rb.grid(rowspan=1, column=0, row=9)
            close.grid(rowspan=1, column=0, row=11)
            crop_text.set(" CROP IMAGE ")
            crop_button.config(state="normal")

        temp5 = tk.Label(main_content, text="                                ", font="Times", bg="#FFA500")
        temp5.grid(rowspan=1, row=3)

        temp3 = tk.Label(crop, text=" Enter The pixels values for cropping Image ", font="Times", bg = "white")
        temp3.grid(row=0, sticky = N)

        v1 = tk.Label(crop, text=" Horizontal Left Pixels ", font="Times", bg="white")
        v1.grid(row=1, sticky = W)

        v2 = tk.Label(crop, text=" Vertical Left Pixels ", font="Times", bg="white")
        v2.grid(row=2, sticky = W)

        v3 = tk.Label(crop, text=" Horizontal Right Pixels ", font="Times", bg="white")
        v3.grid(row=3, sticky = W)

        v4 = tk.Label(crop, text=" Vertical Right Pixels ", font="Times", bg="white")
        v4.grid(row=4, sticky = W)

        var1_lab = tk.Entry(crop,font = "Times",width = 7)
        var1_lab.grid(row=1, sticky = E)

        var2_lab = tk.Entry(crop,font = "Times",width = 7)
        var2_lab.grid(row=2, sticky = E)

        var3_lab = tk.Entry(crop,font = "Times",width = 7)
        var3_lab.grid(row=3, sticky = E)

        var4_lab = tk.Entry(crop,font = "Times",width = 7)
        var4_lab.grid(row=4, sticky = E)

        #BUTTON
        ip_text = tk.StringVar()
        ip_button = tk.Button(crop, command=lambda: get_input(), textvariable=ip_text, font="Times", bg="#8c92ac")
        ip_text.set(" CROP ")
        ip_button.grid(rowspan=1, row = 5)

        cb1 = tk.Button(crop, command=lambda: cw2(), text=" CLOSE ", font="Times", bg="#8c92ac")
        cb1.grid(rowspan=1, sticky=S)

    crop_text.set(" CROP IMAGE ")

#BUTTON3
crop_text = tk.StringVar()
crop_button = tk.Button(header, command = lambda:crop_img(), textvariable = crop_text, width = 23, font = "Times", bg = "#8c92ac", justify=CENTER)
crop_text.set(" CROP IMAGE ")
crop_button.grid(rowspan = 1,column = 0, row = 5)

def border():
    b_button.config(state="disabled")
    bd = Frame(header, width=250, height=200, bg="white", relief=GROOVE, bd=10)
    bd.grid(rowspan=6, column=0, row=8)
    rb.grid(rowspan=1, column=0, row=15)
    close.grid(rowspan=1, column=0, row=16)
    btext.set(" Loading..... ")
    def gip():
        bg_text.set(" Framing.... ")
        get_img()
        if file:
            img6 = Image.open(file)
            width = img6.size[0]
            height = img6.size[1]
            sz = bl.get()
            sz1 = int(sz)
            for i in range(0, width):
                for j in range(0, height):
                    pixelColorVals2 = img6.getpixel((i, j))
                    if j <= sz1:
                        redPixel = 0
                        greenPixel = 0
                        bluePixel = 0
                        img6.putpixel((i, sz1 - j), (redPixel, greenPixel, bluePixel))
                    elif j >= (height - sz1) and j <= height:
                        redPixel = 0
                        greenPixel = 0
                        bluePixel = 0
                        img6.putpixel((i, j), (redPixel, greenPixel, bluePixel))
                    elif i <= sz1:
                        redPixel = 0
                        greenPixel = 0
                        bluePixel = 0
                        img6.putpixel((sz1 - i,j), (redPixel, greenPixel, bluePixel))
                    elif i >= (width - sz1) and i <= width:
                        redPixel = 0
                        greenPixel = 0
                        bluePixel = 0
                        img6.putpixel((i, j), (redPixel, greenPixel, bluePixel))
            outimg(img6)
            bl.delete(0, END)
            # instruction4
            temp2 = tk.Label(main_content, text=" Framed Image : ", font="Times", bg="#FFA500")
            temp2.grid(rowspan = 1, row=3)
            bg_text.set(" FRAME ")

    def cw4():
        bd.grid_remove()
        rb.grid(rowspan=1, column=0, row=9)
        close.grid(rowspan=1, column=0, row=11)
        b_button.config(state="normal")

    lbl = tk.Label(bd, text=" Enter Frame Size In Pixels : ", font="Times", bg="#A9A9A9")
    lbl.grid(row=0, sticky=N + S)
    bl = tk.Entry(bd, font="Times", width=7)
    bl.grid(row=1, sticky=N + S)

    bg_text = tk.StringVar()
    bg_button = tk.Button(bd, command=lambda: gip(), textvariable=bg_text, font="Times", bg="#8c92ac")
    bg_text.set(" FRAME ")
    bg_button.grid(rowspan=1, row=2, sticky=N + S)

    cb = tk.Button(bd, command=lambda: cw4(), text=" CLOSE ", font="Times", bg="#8c92ac")
    cb.grid(rowspan=1, row=4)
    btext.set(" FRAMING IMAGE ")

#BUTTON4
btext = tk.StringVar()
b_button = tk.Button(header, command = lambda:border(), textvariable = btext, width = 23, font = "Times", bg = "#8c92ac", justify=CENTER)
btext.set(" FRAMING IMAGE ")
b_button.grid(rowspan = 1,column = 0, row = 7)

def rotate():
    main_content.grid()
    rt.set(" Loading.... ")
    get_img()
    pf = Frame(header, width=250, height=50, bg="white", relief=GROOVE, bd=10)
    pf.grid(rowspan=2, column=0, row=10)
    rf = Frame(pf, width=250, height=50, bg="white", bd=0)
    rf.grid(rowspan=1, column=0, row=0)
    close.grid(rowspan=1, column=0, row=14)
    if file:
        rb.config(state="disabled")
        tmp = Image.open(file)
        w = tmp.size[0]
        h = tmp.size[1]
        def ninty():
            new1 = Image.new("RGB", (h, w), "white")
            t1 = tmp.load()
            n1 = new1.load()
            for i in range(0, h):
                for j in range(0, w):
                    n1[i,j] = t1[j,h - i - 1]
            temp5 = tk.Label(main_content, text=" Rotated Image : ", font="Times", bg="#FFA500")
            temp5.grid(rowspan=1, row=3)
            outimg(new1)

        def one80():
            new2 = Image.new("RGB", (w, h), "white")
            t2 = tmp.load()
            n2 = new2.load()
            for i in range(0, w):
                for j in range(0, h):
                    n2[i, j] = t2[i, h - j - 1]
            temp6 = tk.Label(main_content, text=" Rotated Image : ", font="Times", bg="#FFA500")
            temp6.grid(rowspan=1, row=3)
            outimg(new2)

        def two70():
            new3 = Image.new("RGB", (h, w), "white")
            t3 = tmp.load()
            n3 = new3.load()
            for i in range(0, h):
                for j in range(0, w):
                    n3[i, j] = t3[w - j - 1, i]
            temp7 = tk.Label(main_content, text=" Rotated Image : ", font="Times", bg="#FFA500")
            temp7.grid(rowspan=1, row=3)
            outimg(new3)

        def three60():
            temp5 = tk.Label(main_content, text=" Rotated Image : ", font="Times", bg="#FFA500")
            temp5.grid(rowspan=1, row=3)
            outimg(tmp)

        def exitwindow():
            pf.grid_remove()
            close.grid(rowspan=1, column=0, row=12)
            rb.config(state="normal")

        button1 = tk.Button(rf, command=lambda: ninty(), text=" 90° ", font="Times", bg="#8c92ac", justify=CENTER)
        button1.grid(rowspan=1, column=0, row=0)

        button2 = tk.Button(rf, command=lambda: one80(), text=" 180° ", font="Times", bg="#8c92ac", justify=CENTER)
        button2.grid(rowspan=1, column=1, row=0)

        button3 = tk.Button(rf, command=lambda: two70(), text=" 270° ", font="Times", bg="#8c92ac", justify=CENTER)
        button3.grid(rowspan=1, column=2, row=0)

        button4 = tk.Button(rf, command=lambda: three60(), text=" 360° ", font="Times", bg="#8c92ac", justify=CENTER)
        button4.grid(rowspan=1, column=3, row=0)

        rf1 = Frame(pf, width=250, height=50, bg="white", bd=0)
        rf1.grid(rowspan=1, column=0, row=1)
        close.grid(rowspan=1, column=0, row=15)

        b5 = tk.Button(rf1, command=lambda: exitwindow(), width = 22, text=" CLOSE ", font="Times", bg="#8c92ac")
        b5.grid(rowspan=1)

    rt.set(" ROTATE IMAGE ")

#BUTTON5
rt = tk.StringVar()
rb = tk.Button(header, command = lambda:rotate(), textvariable = rt, width = 23, font = "Times", bg = "#8c92ac", justify=CENTER)
rt.set(" ROTATE IMAGE ")
rb.grid(rowspan = 1,column = 0, row = 9)


def call():
    close.config(state="disabled")
    res = mb.askquestion('Exit Application',
                         'Do you really want to exit ?')

    if res == 'yes':
        root.destroy()

    else:
        mb.showinfo('Return', 'Returning to the application')
        close.config(state="normal")

#BUTTON6
close = tk.Button(header,text = " EXIT ", command = lambda:call(), width = 23, font = "Times", bg = "#8c92ac", justify=CENTER)
close.grid(rowspan = 1,column = 0, row = 12)

root.state('zoomed')

#END OF WINDOW
root.mainloop()
