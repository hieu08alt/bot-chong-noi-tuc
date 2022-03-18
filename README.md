# Bot Chống Nói Tục

**Setup Bot:**
- Setup ban đầu:
1. Tạo tài khoản Discord và tạo bot *(search google)*
2. Tải Python: "https://www.python.org/downloads/" (nên xài Python 3.7)
3. Tải Discordpy: vô Command Prompt gõ `pip install discord.py`
4. ~~Tải ide để code :/~~

- Setup Bot:
1. Mở file `config.json`
2. Bỏ Token của Bot vào trong key `"TOKEN"`
3. Ghi tên Author bot vào key `"author"`
4. Bỏ thời gian vào key `"mute_time"` *(đơn vị: second)*
5. Bỏ ID của Channel cần thông báo Mute vào key `"id_channel_send"`
6. Trong Server Discord, tạo role `Muted` và hãy tắt quyền nói, nhắn tin, reaction,... *(những gì bạn muốn khi user bị mute)*

Demo
```json
{
  "TOKEN": "JIasdoisadpojsandjasio",
  "author": "hieudeptrai#8265",
  "mute_time": 900,
  "id_channel_send": 930811651014418472
}
```

**Lưu ý**
- Chạy file `main.py` để có bot hoạt động. vô Command Prompt ghi `python3 main.py` *(Lưu ý phải chuyển đến thư mục chứa file main rồi mới bắt đầu thực hiện lệnh)*
- Có thể thay đổi hoặc thêm những từ **NÓI TỤC** bằng những từ khác. Nhưng bạn phải đảm bảo là mỗi từ một dòng, cấm ghi 2 hoặc nhiều từ ở lên ghi 1 dòng.
- File `bad_word.txt` là file chứa từ nói tục. Khi phát hiện từ nói tục thì Bot lật tức mute
- Cách kiểm tra Bot đã hoạt động hay chưa: sau khi console in dòng chữ `Bot dang chay {tên bot}` thì bạn hãy vô một kênh bất kì nào đó (như spam bot) và gõ `!ping` Nếu bot nhắn lại thì bot đã chạy rồi!
- Nếu bạn muốn bot chạy 24/7 thì bạn cần một nơi để host. Thì cái đấy bạn từ tìm hiểu nhé!

**Chỉnh Sửa**
- 18/3/2022:
1. Tối ưu code
2. Fix lỗi Bot warn nhầm, từ đó từ 2 file `bad_word.txt` và `bad_word1.txt` thành 1 file thống nhất `bad_word.txt`. 