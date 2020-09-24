from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.png")

breedte = achtergrond.width
hoogte = achtergrond.height

lettertype = ImageFont.truetype("impact", 40)

tekengebied = ImageDraw.Draw(achtergrond)

tekst = "Me when\n the egirl\n\n\n\n\n\nstops selling\nbathwater"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font=lettertype)
print("tekstbreedte=" + str(tekst_breedte) + ", tekst_hoogte=" + str(tekst_hoogte))


tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) /2

tekengebied.multiline_text((tekst_x, tekst_y), tekst, font=lettertype, fill=(0,0,0))
tekengebied.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

achtergrond.show()

achtergrond.save("meme_met_tekst.png")
