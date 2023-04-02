class FacebookUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password      

    def login(self):
        if (self.username == 'abcdef' and self.password == '123456'):
            print("Login successful")
        else:
            print("Login failure")


class FacebookUserVIP(FacebookUser):
    def __init__(self, username, password, likeNums):
        super().__init__(username, password)
        self.likeNums = likeNums
    
    def likePost(self, nguoiMinhCanLike): 
        nguoiMinhCanLike.likeNums += 1
        
        
ronaldo = FacebookUserVIP("ronaldo", "123456", 1000)
john = FacebookUserVIP("john", "123456789", 2)




# class Xe:
#     	- name
# 	- brand
# 	- price
# 	- maxSpeed

# 	+ In ra dòng thông tin xe:
# 		"Chào bạn, xe này có tên là name, nhãn hiệu brand, có giá là price"

# class Xe Máy
# 	+ In giá trị xe:
# 		return price / maxSpeed (số thập phân)


# class Ô tô:
# 	+ Đăng kiểm ()
# 		Nếu max_speed > 30 => An toàn
# 		nếu không in ra không an toàn