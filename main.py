from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
root = Tk()

frm = ttk.Frame(root, padding=10)

root.geometry("450x700")
frm.grid()
ttk.Label(frm, text=" Watermark placing device ").grid(column=0, row=0)

root.title("Watermark Application")
image1 = Image.open("rsz_untitled_design.jpg")

#  background image Display
picture_1 = ImageTk.PhotoImage(image1)
pci = Label(root, image=picture_1)
pci.grid(row=1, columnspan=2)
picture = ''
def upload_file():
    file_type = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=file_type)
    image = Image.open(filename)
    global picture
    picture = image
    # resized image to enter the canvas
    resized_image = image.resize((397, 562))
    image1 = ImageTk.PhotoImage(resized_image)
    image_label = Label(root, image=image1)
    image_label.grid(columnspan=2, row=1)

label = Button(frm, text="Upload Image", command=upload_file)
label.grid(column=2, row=1)
final_watermarked_image = ''
def watermark():
    watermark_image = picture.copy()
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("BankGothic Bold.ttf", 15)
    #  Adding the watermark
    draw.text((10, 25), "zamani", (0, 0, 0), font=font)
    watermark_image.show()
    global final_watermarked_image
    final_watermarked_image = watermark_image
    return watermark_image


def download_watermarked_image():
    try:
        final_watermarked_image.save("testing_image.jpg")
    except:
        message_alert = Message(frm, text=" Please apply watermark first!")
        message_alert.config(fg="red")
        message_alert.grid(row=2, column=1)

# buttons
ttk.Button(frm, text='Download image', command=download_watermarked_image).grid(column=0, row=4)

ttk.Button(frm, text='Apply watermark', command=watermark).grid(column=3, row=4)



quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(columnspan=2, row=2)
quit_button.config(padding=10)

root.mainloop()
