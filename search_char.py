import cv2
import os

# 此程式可刪除有特定標籤的 txt 檔及對應的圖片
# 將程式檔放在跟 txt 檔同一個的資料夾，然後執行程式

# 讀取 search_char.py 的路徑
dir_path = os.path.abspath("search_char.py")
# 轉換成目錄的路徑
file_dir = dir_path[:-14]
# 設定要搜尋的副檔名
picture_extension = input("輸入 txt 檔對應的圖片副檔名(jpg、jpeg or png...)：")
# 最後儲存檔案的檔名
label = input("輸入要刪除的標籤：")
for parent, dirnames, filenames in os.walk(file_dir):
         for filename in filenames:  # 跑目錄內所有檔案
            if ".txt" in filename:  # 判斷檔案名稱中有附檔名的字串
                # 讀取照片檔
                f = open(filename, "r", encoding="utf-8")
                for row in f.readlines():
                    if row.split()[0] == label:
                        f.close()
                        try:
                            picture_file = filename[:-3] + picture_extension
                            os.remove(picture_file)
                            print("{} is removed".format(picture_file))
                        except:
                            print("can not find {}".format(picture_file))
                        os.remove(filename)
                        print("{} is removed".format(filename))
                        break
                    else:
                        continue




