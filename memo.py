import tkinter as tk
from tkinter import messagebox

def get_text():
  data = text.get("1.0", "end-1c")
  print(f"{len(data)}文字")
  memo = data

def show_text():
  data = text.get("1.0", "end-1c")
  messagebox.showinfo("カウント結果", f"{len(data)}文字です")


# ウィンドウ作成
root = tk.Tk()
root.title("メモ帳")
root.geometry("400x300")
tk.Button(root, text="文字数をカウントする", command=show_text).pack()


# テキストエリア
text = tk.Text(
    root,
    font=("Meiryo", 8)  # フォント名, サイズ
)
text.pack(expand=True, fill="both")

# 実行
root.mainloop()
