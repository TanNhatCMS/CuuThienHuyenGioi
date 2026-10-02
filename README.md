# Cửu Thiên Huyền Giới (Nine Heavens: Will of the sword) — bản clone local

Clone game web từ trang itch.io: https://bienvh.itch.io/9t (tác giả bienvh).

Game Godot 4 export HTML5, chơi trên trình duyệt, text tiếng Việt.

## File

| File | Kích thước | Vai trò |
|---|---|---|
| index.html | 5.5 KB | Trang loader |
| index.js | 280 KB | Godot engine loader |
| index.wasm | 39.5 MB | Engine (WASM) |
| index.pck | 24.3 MB | Dữ liệu game |
| index.png, index.icon.png, index.apple-touch-icon.png | ~30 KB | Splash + icon |

Nguồn gốc: `https://html-classic.itch.zone/html/19507117/` (iframe URL lấy từ nút
"Run game" trên trang itch.io). Đã bỏ script tracking `static.itch.io/htmlgame.js`
khỏi index.html.

## Chạy local

```bash
python serve.py
# mở http://127.0.0.1:8123/
```

`serve.py` thêm header COOP/COEP (Cross-Origin-Opener-Policy / Cross-Origin-Embedder-Policy)
mà Godot web export cần khi bật cross-origin isolation.

Game lưu save trong localStorage/IndexedDB của browser theo origin — giữ nguyên domain
khi host (ví dụ qua FlyEnv, root trỏ về thư mục này) để save không bị mất.

## Host qua FlyEnv

Tạo site mới (ví dụ `9t.test`) với root `P:\9T`, bật thêm header COOP/COEP ở cấu hình
web server nếu engine báo thiếu SharedArrayBuffer.
