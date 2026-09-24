# Tạo pwHash + blob (danh sách ảnh/nhạc đã mã hoá) để dán vào CONFIG trong index.html
# Dùng: python make_lock.py   (sửa PW / ASSETS bên dưới nếu muốn đổi)
import hashlib, base64, json

PW = "0312"  # ngày sinh, viết liền
ASSETS = {
    "photos": ["./assets/imgs/3.jpg", "./assets/imgs/4.jpg", "./assets/imgs/2.jpg", "./assets/imgs/1.jpg"],
    "tracks": [
        ["./assets/mp3/thang_cuoi.mp3", "Thằng Cuội"],
        ["./assets/mp3/ruoc_den_thang_8.mp3", "Rước Đèn Tháng Tám"],
        ["./assets/mp3/cay_da_quan_doc.mp3", "Cây Đa Quán Dốc"],
    ],
}

def sha(s): return hashlib.sha256(s.encode()).digest()

def make(pw, assets):
    data = json.dumps(assets, ensure_ascii=False, separators=(",", ":")).encode()
    out = bytearray()
    for j in range((len(data) + 31) // 32):
        ks = sha(f"gk|{pw}|{j}")
        out += bytes(b ^ k for b, k in zip(data[j * 32:(j + 1) * 32], ks))
    return sha("gomii-v1|" + pw).hex(), base64.b64encode(bytes(out)).decode()

if __name__ == "__main__":
    h, blob = make(PW, ASSETS)
    print(f'pwHash: "{h}",\nblob: "{blob}",')
