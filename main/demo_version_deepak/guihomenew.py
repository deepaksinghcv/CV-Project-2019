from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from skimage import io,color,filters,feature
import numpy as np
import sys
from python_exec2_withEs import *

modelpath='./cache/forest/model.mat'
edgeImageFileName = "edgeImage.jpg"
sobelImageFileName = "sobelTemp.jpg"
cannyEdgeFileName = "cannyTemp.jpg"
oefImageFileName = "oef.jpg"

def btnRunFunction(event):
    print("run clicked")
    statusframelabel.config(text="Running...")
    global modelpath
    global edgeImageFileName
    global sobelImageFileName
    global cannyEdgeFileName
    global oefImageFileName
    # global imagepath
    # print(modelpath)

    edgeDispButton.configure(state=DISABLED)

    filename = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    # print (filename)
    try:


        #load original image
        statusframelabel.config(text="Loading Image...")
        ioImage = getImageIO(filename)
        statusframelabel.config(text="Image loaded in buffer")
        # print(type(ioImage))
        photoImage = ImageTk.PhotoImage(Image.fromarray(ioImage))
        #load image into left frame
        for widget in frame1.winfo_children():
            widget.destroy()
        for widget in frame2.winfo_children():
            widget.destroy()
        for widget in frame3.winfo_children():
            widget.destroy()
        for widget in frame4.winfo_children():
            widget.destroy()
        

        frame1contentlabel = Label(frame1,image=photoImage)#,width=480,height=320)
        frame1contentlabel.image=photoImage
        frame1contentlabel.pack(fill=X)
        
        statusframelabel.config(text="Test Image Loaded")
        #run oef image

        #E=runOEF(modelpath,filename)

        #######
        [E,Es]=runOEF(modelpath,filename)
        #######

        
        # print("guihomenew.py-->",type(E))

        oefImage = ImageTk.PhotoImage(image=Image.fromarray(E.astype('uint8')))

        # print(type(oefImage))

        # print(type(oefImage))

        frame2contentlabel = Label(frame2,image=oefImage)#,width=480,height=320)
        frame2contentlabel.image=oefImage
        frame2contentlabel.pack(fill=X)

        # tempOEFImage = Image.fromarray(E.astype('uint8'))
        # tempOEFImage.write(oefImageFileName)

        # plt.imshow(E,cmap='gray')
        # plt.axis('off')
        # plt.savefig(oefImageFileName)
        io.imsave(oefImageFileName,E/255)

        #show sobeled image
        sobeledImage = getSobelImage(ioImage)
        # print(type(sobeledImage))
        io.imsave(sobelImageFileName,sobeledImage)
        #sobeledPhotoImage = ImageTk.PhotoImage(Image.fromarray(sobeledImage))
        sobeledPhotoImage = ImageTk.PhotoImage(file=sobelImageFileName)
        frame3contentlabel = Label(frame3,image=sobeledPhotoImage)#,width=480,height=320)
        frame3contentlabel.image=sobeledPhotoImage
        frame3contentlabel.pack(fill=X)

        #show canny edge
        cannyEdImage = getCannyEdgeImage(ioImage)
        # print(type(cannyEdImage))
        io.imsave(cannyEdgeFileName,cannyEdImage*255)
        cannyEdPhotoImage = ImageTk.PhotoImage(file=cannyEdgeFileName)
        frame4contentlabel = Label(frame4,image=cannyEdPhotoImage)#,width=480,height=320)
        frame4contentlabel.image=cannyEdPhotoImage
        frame4contentlabel.pack(fill=X) 

        statusframelabel.config(text="Images Loaded")

        #####
        rows=2
        cols=4
        fig=plt.figure(figsize=(10, 10))
        for i in range(1, cols*rows +1):
            fig.add_subplot(rows, cols, i)
            plt.imshow(Es[:,:,i-1],cmap='gray')
            plt.title("bin"+ str(i))
            plt.axis('off')
        plt.savefig(edgeImageFileName)
        #####
        edgeDispButton.configure(state=NORMAL)


    except Exception as e:
        print(e)
        print("no file")
        statusframelabel.config(text="No Image selected!")

def getImage(filePath):
    imgImage = Image.open(filePath)
    # imgImage = imgImage.resize((480, 320), Image.ANTIALIAS)
    photoImage = ImageTk.PhotoImage(imgImage)

    return photoImage,imgImage

def getImageIO(filePath):
    image = io.imread(filePath)
    return image

def getCannyEdgeImage(image):
    greyImage = color.rgb2grey(image)
    cannyedImage = feature.canny(greyImage)

    return cannyedImage

def getSobelImage(image):
    greyImage = color.rgb2grey(image)
    sobeledImage = filters.sobel(greyImage)

    return sobeledImage


def showEdgeImage():
    global edgeImageFileName
    tempImg = Image.open(edgeImageFileName)
    tempImg.show()
    statusframelabel.config(text="Edge Space Image Loaded")

def btnRunFunctionTester(event):
    print("running temporary run function change this during publish")
    print("run clicked")
    global edgeImageFileName
    global sobelImageFileName
    global cannyEdgeFileName
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    print (filename)
    try:
        #imageMatPhotoImage,imageMatImage = getImage(filename)
        ioImage = getImageIO(filename)
        print(type(ioImage))
        photoImage = ImageTk.PhotoImage(Image.fromarray(ioImage))
        #load image into left frame
        for widget in frame1.winfo_children():
            widget.destroy()
        for widget in frame2.winfo_children():
            widget.destroy()
        for widget in frame3.winfo_children():
            widget.destroy()
        for widget in frame4.winfo_children():
            widget.destroy()

            
        statusframelabel.config(text="Loading image...")
        print(type(photoImage))

        frame1contentlabel = Label(frame1,image=photoImage)#,width=480,height=320)
        frame1contentlabel.image=photoImage
        frame1contentlabel.pack(fill=X)
  
        statusframelabel.config(text="Result Image Loaded")
        

        # print("photoimage type",type(photoImage))
        # # print("image type",type(imageMatImage))
        # npedImage = np.array(photoImage)

        # print(type(npedImage))
        # print(npedImage.shape)

        #show sobeled image
        sobeledImage = getSobelImage(ioImage)
        print(type(sobeledImage))
        io.imsave(sobelImageFileName,sobeledImage)
        #sobeledPhotoImage = ImageTk.PhotoImage(Image.fromarray(sobeledImage))
        sobeledPhotoImage = ImageTk.PhotoImage(file=sobelImageFileName)
        frame3contentlabel = Label(frame3,image=sobeledPhotoImage)#,width=480,height=320)
        frame3contentlabel.image=sobeledPhotoImage
        frame3contentlabel.pack(fill=X)

        #show canny edge
        cannyEdImage = getCannyEdgeImage(ioImage)
        print(type(cannyEdImage))
        io.imsave(cannyEdgeFileName,cannyEdImage*255)
        cannyEdPhotoImage = ImageTk.PhotoImage(file=cannyEdgeFileName)
        frame4contentlabel = Label(frame4,image=cannyEdPhotoImage)#,width=480,height=320)
        frame4contentlabel.image=cannyEdPhotoImage
        frame4contentlabel.pack(fill=X)  




    except Exception as e:
        print(e)
        print("no file")
        statusframelabel.config(text="No Image selected!")



root = Tk()

root.title("Oriented Edge Forests for Boundary Detection by TEAMDASH")

titleframe1 = Frame(root,bg="green",height=48,width=320)
titleframe2 = Frame(root,bg="blue",height=48,width=320)
titleframe3 = Frame(root,bg="red",height=48,width=320)
titleframe4 = Frame(root,bg="red",height=48,width=320)

frame1 = Frame(root,bg="red",height=480,width=320)
frame2 = Frame(root,bg="green",height=480,width=320)
frame3 = Frame(root,bg="blue",height=480,width=320)
frame4 = Frame(root,bg="yellow",height=480,width=320)

actionframe = Frame(root,bg="purple",height=48,width=1280)
statusframe = Frame(root,bg="white",height=48,width=1280)

titleframe1.grid(row=0,column=0)
titleframe2.grid(row=0,column=1)
titleframe3.grid(row=0,column=2)
titleframe4.grid(row=0,column=3)

frame1.grid(row=1,column=0)
frame2.grid(row=1,column=1)
frame3.grid(row=1,column=2)
frame4.grid(row=1,column=3)

actionframe.grid(row=2,columnspan=4)
statusframe.grid(row=3,columnspan=4)

titleframe1label = Label(titleframe1,text="Input Image",font='Helvetica 16 bold')
titleframe1label.pack()

titleframe2label = Label(titleframe2,text="OEF",font='Helvetica 16 bold')
titleframe2label.pack()

titleframe3label = Label(titleframe3,text="Sobel",font='Helvetica 16 bold')
titleframe3label.pack()

titleframe4label = Label(titleframe4,text="Canny-Edge",font='Helvetica 16 bold')
titleframe4label.pack()

statusframelabel = Label(statusframe,anchor="w",text="Current status goes here",font='Helvetica 12 bold')
statusframelabel.grid()

runButton = Button(actionframe,text="RUN")
runButton.grid(row=0,column=0,sticky="nsew")
runButton.bind("<Button-1>",btnRunFunction)

edgeDispButton = Button(actionframe,text="SHOW EDGE SPACE",state=DISABLED)
edgeDispButton.grid(row=0,column=1,sticky="nsew")
# edgeDispButton.bind("<Button-1>",showEdgeImage)
edgeDispButton.configure(command=showEdgeImage)


root.mainloop()

