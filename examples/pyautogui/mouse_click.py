import pyautogui
import time

TOTAL_CLICKS = 900_000

# 給使用者 5 秒時間把滑鼠移到正確位置
print("5 seconds to prepare...")
time.sleep(5)

for i in range(TOTAL_CLICKS):
    pyautogui.click()

print("Done. Program exiting.")