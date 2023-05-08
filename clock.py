import tkinter as tk
from PIL import Image, ImageTk

# ウィンドウを作る
root = tk.Tk()

# ウィンドウの最大化
root.state("zoomed")  # Windowsでも動作可能
# root.attributes("-fullscreen", True)  # Mac, Linuxでのみ動作可能

# ウィンドウのタイトルの設定
root.title("clock app")
root.configure(bg="lightblue")



# 画像の読み込み
img_path = "./data/sample.jpeg"
img = Image.open(img_path)
# tkinterで扱える画像形式に変換
bg_img = ImageTk.PhotoImage(img)
# 画像をラベルとして設定
label = tk.Label(root, image=bg_img)
# 画像ラベルを配置
label.pack(fill=tk.BOTH, expand=True)

# ウィンドウの表示
root.mainloop()
