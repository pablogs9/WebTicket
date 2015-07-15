from PIL import Image
from math import ceil
from math import floor


def ticketPreview(name,size):
    im = Image.open("uploads/" + name)
    t = size
    w, h = im.size

    #print "Original size: " + str(w) + " " + str(h)
    #print "Ratio: " +str(float(t*256)/w)
    #print "Calculated size: " + str(t*256) + " " + str(int(h*(float(t*256)/w)))

    im = im.resize((t*256,int(h*(float(t*256)/w))),Image.ANTIALIAS)
    w, h = im.size

    #print "Actual size: " + str(w) + " " + str(h)
    #print "Actual paper size: " + str(w/256) + " tiras, " + str(h/256) + " cuadrados de alto"

    im = im.crop((0,0,int(floor(w/256.0))*256,h))

    w, h = im.size
    wc = int(ceil(w/256.0))
    hc = int(ceil(h/256.0))
    im = im.convert('1')

    marginh = 30
    marginv = 2
    canvas = Image.new('1',(wc*256+(wc+1)*marginh,h+hc*marginv),1)

    ##IMPRESION
    for i in range(wc):
        hAux = h
        for j in range(hc):
                if hAux > 256:
                    #print "Imprimiendo " + str(j) + "/" + str(i)
                    imaux = im.crop((i*256,j*256,i*256+256,j*256+256))
                    hAux = hAux - 256
                else:
                    #print "Imprimiendo " + str(j) + "/" + str(i)
                    imaux = im.crop((i*256,j*256,i*256+256,j*256+hAux))
                    hAux = 0
                canvas.paste(imaux,(i*256+(i+1)*marginh,j*256+(j+1)*marginv))
    max_image_width = 2048*2
    if canvas.size[0] > max_image_width:
        canvas = canvas.resize((max_image_width,int(canvas.size[1]*(float(max_image_width)/float(canvas.size[0])))),Image.ANTIALIAS)
    canvas.save("static/images/" + name.split('.')[0]+ ".jpg")
    return 1
