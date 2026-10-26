def tao_tin_nhan_dich(cau_hoi):
    ngon_ngu = "tiếng Pháp"
    prompt = f"hay dich cau {cau_hoi} sang ngon ngu {ngon_ngu}"
    tin_nhan = {
        "role": "user",
        "content": prompt  # Vẫn quy tắc cũ: prompt là biến rồi nên không cần f"{prompt}"
    }
    return tin_nhan  # Đã kéo lùi ra ngoài cho bằng hàng với chữ tin_nhan

cac_cau_hoi = ["Xin chào", "Tạm biệt", "Cảm ơn"]

# Dùng biến 'cau' để lấy từng câu hỏi trong danh sách
for cau in cac_cau_hoi:
    # GỌI HÀM: Đưa 'cau' vào máy xay sinh tố 'tao_tin_nhan_dich', hứng kết quả vào biến 'ket_qua'
    ket_qua = tao_tin_nhan_dich(cau)
    print(ket_qua)

# Kết quả in ra sẽ là 3 Dictionary chứa 3 câu prompt dịch tiếng Pháp!