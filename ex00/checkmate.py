def checkmate(board):
    try:
        # แปลงกระดานเป็น List ของแถวแต่ละแถว
        rows = board.strip().split("\n")
        board_size = len(rows)  # ขนาดของกระดาน
        king_pos = None  # ตำแหน่งของ King

        # ค้นหาตำแหน่งของ King บนกระดาน
        # i = row
        # j = column
        for i in range(board_size):
            for j in range(len(rows[i])):
                if rows[i][j] == "K":
                    king_pos = (i, j)  # บันทึกตำแหน่งของ King
                    break
            if king_pos:
                break

        # ฟังก์ชันตรวจสอบการโจมตีโดย Rook หรือ Queen ในแนวตรง
        def is_threat_by_rook_or_queen(x, y, dx, dy):
            while 0 <= x < board_size and 0 <= y < len(rows[x]):
                x, y = x + dx, y + dy  # เดินไปในทิศทาง dx และ dy
                if not (0 <= x < board_size and 0 <= y < len(rows[x])):
                    break  # ออกจากลูปถ้าหลุดออกนอกกระดาน
                piece = rows[x][y]
                if piece != ".":  # ถ้าพบตัวหมาก
                    return piece in "RQ"  # ตรวจสอบว่าเป็น Rook หรือ Queen
            return False

        # ฟังก์ชันตรวจสอบการโจมตีโดย Bishop หรือ Queen ในแนวทแยง
        def is_threat_by_bishop_or_queen(x, y, dx, dy):
            while 0 <= x < board_size and 0 <= y < len(rows[x]):
                x, y = x + dx, y + dy  # เดินไปในทิศทาง dx และ dy
                if not (0 <= x < board_size and 0 <= y < len(rows[x])):
                    break  # ออกจากลูปถ้าหลุดออกนอกกระดาน
                piece = rows[x][y]
                if piece != ".":  # ถ้าพบตัวหมาก
                    return piece in "BQ"  # ตรวจสอบว่าเป็น Bishop หรือ Queen
            return False

        # ฟังก์ชันตรวจสอบการโจมตีโดย Pawn
        def is_threat_by_pawn(x, y):
            # Pawn สามารถโจมตีเฉียงไปข้างหน้า (บนกระดานแนวตรงคือ x+1)
            return any(
                0 <= nx < board_size and 0 <= ny < len(rows[nx]) and rows[nx][ny] == "P"
                for nx, ny in [(x + 1, y - 1), (x + 1, y + 1)]  # แนวเฉียงซ้ายและขวา
            )

        # ตรวจสอบว่ามีตัวหมากใดโจมตี King ได้หรือไม่
        x, y = king_pos
        if (
            is_threat_by_pawn(x, y) or  # ตรวจสอบการโจมตีจาก Pawn
            any(is_threat_by_rook_or_queen(x, y, dx, dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]) or  # Rook/Queen
            any(is_threat_by_bishop_or_queen(x, y, dx, dy) for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)])  # Bishop/Queen
        ):
            print("Success")  # King ถูกโจมตี
        else:
            print("Fail")  # King ไม่ถูกโจมตี

    except Exception as e:
        # แสดงข้อความ Error หากมีปัญหา
        print("Error:", str(e))