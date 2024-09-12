import requests
from PIL import Image

# работа по запросам
r = requests.get('https://ru.wallpaper.mob.org/pc/')  # получить запрос с сайта
list_url_image = []
if r.status_code == 200:  # ошибки нет
    # print('Успешный запрос')
    site_list = list(r.iter_lines())
    # получим список адресов для скачивания обоев рабечего стола
    for i in range(0, len(site_list)):
        if "src=" in str(site_list[i]) and ".jpeg" in str(site_list[i]):
            list_url_image.append(str(site_list[i]).split('"')[1])
    print(list_url_image)
    # сохраним список адресов с обоями в файл
    with open('images.txt', 'w', encoding="utf-8") as file:
        for i in list_url_image:
            file.writelines(str(i) + '\n')
else:
    print('Ошибка запроса:', r.status_code)

# получим файлы по адресам и сохраним на НЖМД
list_files_image = []
for i in range(5):  # 5 файлов для примера
    r = requests.get(list_url_image[i], allow_redirects=True)
    outfile = list_url_image[i].split('/')
    list_files_image.append(outfile[-1])
    with open(outfile[-1], "wb") as file_image:
        file_image.write(r.content)

# работа с рисунками: проверим параметры рисунков (обоев), создадим миниатюру и запишем на НЖМД
for infile in list_files_image:
    im = Image.open(infile)
    print(infile, im.format, f"size= {im.size}, mode= {im.mode}")
    im.thumbnail(size=(200, 150))
    outfile = infile.split('.')
    outfile = outfile[-2] + '_thumbnail.' + outfile[-1]
    print(outfile)
    im.save(outfile, "JPEG")
