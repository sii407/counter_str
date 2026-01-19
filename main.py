import tkinter as tk
from tkinter import messagebox
global data
def save():
  data = text.get("1.0", "end-1c")
  # memo = data

def show_text():
  data = text.get("1.0", "end-1c")
  messagebox.showinfo("カウント結果", f"{len(data)}文字です")

def make_window():
  sub = tk.Toplevel(root)
  sub.title("メモ2")
  sub.geometry("400x300")
  sub.focus_set()
  sub_text = tk.Text(sub)
  sub_text.pack(expand=True, fill="both")
  sub_text.insert(tk.END, data)


# ウィンドウ作成
root = tk.Tk()
root.title("メモ1")
root.geometry("400x300")
tk.Button(root, text="文字数をカウントする", command=show_text).pack()
tk.Button(root, text="保存", command=save).pack()
tk.Button(root, text="新しいメモを作成", command=make_window).pack()


# テキストエリア
text = tk.Text(
    root,
    font=("Meiryo", 8)  # フォント名, サイズ
)
text.pack(expand=True, fill="both")

# 実行
root.mainloop()
