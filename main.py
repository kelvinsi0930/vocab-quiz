import random

# 建立單字資料庫（你可以自己加更多）
vocab = {
    "apple": "蘋果",
    "book": "書",
    "dog": "狗",
    "house": "房子",
    "computer": "電腦",
    "school": "學校"
}

# 隨機出題 5 題
questions = random.sample(list(vocab.keys()), 5)

score = 0

print("🔤 歡迎使用英文單字測驗工具！請輸入中文意思：\n")

for word in questions:
    answer = input(f"{word} 的中文意思是？ ")
    if answer == vocab[word]:
        print("✅ 正確！\n")
        score += 1
    else:
        print(f"❌ 錯了，正確答案是：{vocab[word]}\n")

print(f"🎉 測驗結束，你總共答對了 {score} / 5 題")
