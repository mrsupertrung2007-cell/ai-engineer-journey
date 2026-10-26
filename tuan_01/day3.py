import json
lich_su_chat = {
    "nguoi_dung" : "Bạn tên gì?",
    "AI" : "Tôi là trợ lý ảo." 
}
du_lieu_json = json.dumps(lich_su_chat, indent=4,ensure_ascii=False)
print(du_lieu_json)