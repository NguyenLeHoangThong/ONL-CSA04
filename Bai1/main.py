class ConMeo:
    # hàm constructor => hàm này tự động chạy khi gọi class ra, ví dụ gọi ConMeo() là nó tự động chạy
    def __init__(self, nameInput, ageInput):
        self.name = nameInput
        self.age = ageInput

    
    # # self dùng để truy cập vào attribute/method của đối tượng (instance) được tạo ra => self chính là cái instance đấy
    # def named(self, inputName):
    #     self.name = inputName

conMeoHoang = ConMeo("Jerry", 10) # Tạo instance với constructor

conMeoNha = ConMeo("Alice", 5) # Tạo instance với constructor

print("Meo hoang: ", conMeoHoang.name)
print("Meo nha: ", conMeoNha.name)
