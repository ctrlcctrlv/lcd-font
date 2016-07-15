## RUN ME VIA `fontforge -script build.py` ##

import fontforge, psMat
import math
fontforge.printSetup("pdf-file")

## regular

base_font = fontforge.open("sfd/14seg.sfd")

base_font.selection.all()

base_font.removeOverlap()

base_font.fontname = "LCD14"

base_font.save("sfd/14seg-gen.sfd")

base_font.generate("otf/"+base_font.fontname+".otf")

base_font.printSample("fontdisplay", 24, "", "specimens/"+base_font.fontname+".pdf")

print("Generated regular")

base_font.close()

## condensed

base_font = fontforge.open("sfd/14seg-gen.sfd")

base_font.selection.all()

matrix = psMat.scale(0.5, 1.0)

base_font.transform(matrix)

base_font.fullname = "LCD Display: 14 Segment (Condensed)"

base_font.fontname = "LCD14Condensed"

base_font.os2_width = 3 # Condensed

base_font.save("sfd/14seg-condensed.sfd")

base_font.generate("otf/"+base_font.fontname+".otf")

base_font.printSample("fontdisplay", 24, "", "specimens/"+base_font.fontname+".pdf")

base_font.close()

print("Generated condensed")

## italic

base_font = fontforge.open("sfd/14seg-gen.sfd")

base_font.selection.all()

matrix = psMat.skew(math.radians(12.5))

base_font.transform(matrix)

base_font.italicangle = -12.5

base_font.fullname = "LCD Display: 14 Segment (Italic)"

base_font.fontname = "LCD14Italic"

base_font.os2_stylemap = 0b1000000001 # italic https://www.microsoft.com/typography/otspec/os2.htm

base_font.save("sfd/14seg-italic.sfd")

base_font.generate("otf/"+base_font.fontname+".otf")

base_font.unlinkReferences() # This works around a FontForge bug

base_font.printSample("fontdisplay", 24, "", "specimens/"+base_font.fontname+".pdf")

base_font.close()

print("Generated italic")

## italic condensed

base_font = fontforge.open("sfd/14seg-condensed.sfd")

base_font.selection.all()

matrix = psMat.skew(math.radians(12.5))

base_font.transform(matrix)

base_font.italicangle = -12.5

base_font.fullname = "LCD Display: 14 Segment (Italic Condensed)"

base_font.fontname = "LCD14ItalicCondensed"

base_font.os2_width = 3 # Condensed

base_font.os2_stylemap = 0b1000000001 # italic https://www.microsoft.com/typography/otspec/os2.htm

base_font.save("sfd/14seg-italiccondensed.sfd")

base_font.generate("otf/"+base_font.fontname+".otf")

base_font.unlinkReferences() # This works around a FontForge bug

base_font.printSample("fontdisplay", 24, "", "specimens/"+base_font.fontname+".pdf")

base_font.close()

print("Generated italic condensed")
