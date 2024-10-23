import hashlib
import time

# 挖礦目標：生成的hash值必須以多少個零開頭
DIFFICULTY = 2
TARGET_PREFIX = '0' * DIFFICULTY

def mine(block_data):
    nonce = 0
    start_time = time.time()
    while True:
        # 將區塊資料和 nonce 合併起來並進行hash運算
        data_to_hash = f"{block_data}{nonce}".encode()
        hash_result = hashlib.sha256(data_to_hash).hexdigest()
        
        # 如果找到符合條件的hash值，則挖礦成功
        if hash_result.startswith(TARGET_PREFIX):
            end_time = time.time()
            print(f"成功找到符合條件的hash值: {hash_result}")
            print(f"Nonce: {nonce}")
            print(f"執行時間: {end_time - start_time:.5f} 秒")
            break
        
        # 否則繼續嘗試下一個 nonce
        nonce += 1

if __name__ == "__main__":
    block_data = input("請輸入你的區塊資料:")
    print("開始挖礦...")
    mine(block_data)
