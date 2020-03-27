import cv2
import os

# 此程式可把圖片中的車牌切下來(需有含車牌座標的 txt 檔)
# 將程式檔放在跟 txt 檔同一個的資料夾，然後執行程式

# 讀取 cut_image.py 的路徑
dir_path = os.path.abspath("cut_image.py")
# 轉換成目錄的路徑
file_dir = dir_path[:-12]
# 設定要搜尋的副檔名
picture_extension = input("輸入 txt 檔對應的圖片副檔名(jpg、jpeg or png...)：")
picture_extension = "." + picture_extension
# 最後儲存檔案的檔名
name = 0
files_with_problem = []
for parent, dirnames, filenames in os.walk(file_dir):
         for filename in filenames:  # 跑目錄內所有檔案
            if picture_extension in filename:  # 判斷檔案名稱中有附檔名的字串
                # 讀取照片檔
                try:
                    img = cv2.imread(filename)
                    print(img.shape)
                    # 讀取照片中的尺寸資訊
                    pic_h = img.shape[0]  # 照片的高度
                    pic_w = img.shape[1]  # 照片的寬度
                    # 轉換原檔名成 txt檔名
                    txt_filename = filename[:-len(picture_extension)] + ".txt"
                    # 開啟txt檔,如果失敗跑except內的程式
                    try:
                        f = open(txt_filename, "r", encoding="utf-8")
                    except:
                        print("No such file or directory: {}".format(txt_filename))
                        continue
                    for row in f.readlines():  # 跑txt檔的每一行
                        coordinate = row.split()[1:]
                        # original coordinate
                        x = float(coordinate[0])
                        y = float(coordinate[1])
                        w = float(coordinate[2])
                        h = float(coordinate[3])
                        # 轉換原比例的座標
                        x1 = x * pic_w
                        y1 = y * pic_h
                        w1 = w * pic_w
                        h1 = h * pic_h
                        # 車牌左上角的座標
                        x2 = x1 - 1 / 2 * w1
                        y2 = y1 - 1 / 2 * h1
                        # 切左上角到右下角的座標
                        crop_img = img[int(y2):int(y2 + h1), int(x2):int(x2 + w1)]
                        # 儲存切下的照片
                        cv2.imwrite(str(name) + '.jpg', crop_img)
                        print("save img: {}.jpg".format(name))
                        name += 1
                except:
                    files_with_problem.append(filename)
                    print("cant not read the image: {}".format(filename))

if files_with_problem:
    print("---------列出有問題的圖檔---------")
    for file in files_with_problem:
        print(file)


