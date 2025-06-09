import tkinter as tk
from tkinter import messagebox
import time
import threading

class FocusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TabFocus Trainer (Python 버전)")
        self.root.geometry("300x200")
        self.root.configure(bg="#f0f0f0")

        # A: 집중 시간 변수
        self.focus_seconds = 0

        # B: 포커스 상태
        self.has_focus = True

        # C: UI 구성
        self.label_title = tk.Label(root, text="🧠 집중력 트레이너", font=("Arial", 14), bg="#f0f0f0")
        self.label_title.pack(pady=10)

        self.label_time = tk.Label(root, text="집중 시간: 0초", font=("Arial", 12), fg="green", bg="#f0f0f0")
        self.label_time.pack(pady=5)

        self.label_status = tk.Label(root, text="상태: 집중 중 🟢", font=("Arial", 11), bg="#f0f0f0")
        self.label_status.pack(pady=5)

        # D: 포커스 이벤트 바인딩
        root.bind("<FocusIn>", self.on_focus_in)
        root.bind("<FocusOut>", self.on_focus_out)

        # E: 타이머 시작
        self.running = True
        threading.Thread(target=self.update_timer, daemon=True).start()

    def on_focus_out(self, event):
        if self.has_focus:
            self.has_focus = False
            self.label_status.config(text="상태: 이탈 중 🔴", fg="red")
            messagebox.showwarning("집중력 알림", "⚠️ 창에서 벗어났어요! 집중하세요!")

    def on_focus_in(self, event):
        if not self.has_focus:
            self.has_focus = True
            self.label_status.config(text="상태: 집중 중 🟢", fg="green")

    def update_timer(self):
        while self.running:
            if self.has_focus:
                self.focus_seconds += 1
                self.label_time.config(text=f"집중 시간: {self.focus_seconds}초")
            time.sleep(1)

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = FocusApp(root)
    root.mainloop()
