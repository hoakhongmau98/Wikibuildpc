import json


data = {}

data['product'] = []
data['product'].append({
    'Name': 'Cpu - Center Processing Unit',
    'Content': 'Gồm 2 nhà phân phối lớn là Intel và AMD. Bộ não quan trọng của toàn bộ hệ thống',
    'Link_direct': '/Cpu'
})
data['product'].append({
    'Name': 'Main - Motheroard',
    'Content': 'Tấm nền của các linh kiện, kết nối và đảm bảo tính hoạt động',
    'Link_direct': '/Main'
})
data['product'].append({
    'Name': 'Ram - Random Access Memmory',
    'Content': 'Bộ nhớ lưu trữ ngắn hạn, phục vụ làm bộ nhớ đệm gaio tiếp dữ liệu tức thời',
    'Link_direct': '/Ram'
})
data['product'].append({
    'Name': 'Gpu - Graphic Processing Unit',
    'Content': 'Thay mặt CPU xử lý các tác vụ đồ họa nặng nề, các tính toán phức tạp',
    'Link_direct': '/Vga'
})
data['product'].append({
    'Name': 'Case',
    'Content': 'Vỏ máy, nơi sắp xếp các linh kiện trong một khối nhất định, đảm bảo không gian kết nối.',
    'Link_direct': '/Case'
})
data['product'].append({
    'Name': 'Ssd - Solid Stage Drive',
    'Content': 'Bộ nhớ lưu trữ dữ liệu tốc độ cao, giá thành cao nhwung hiệu quả mang lại vượt HDD.',
    'Link_direct': '/Ssd'
})
data['product'].append({
    'Name': 'Hdd - Hard Disk Drive',
    'Content': 'Bộ nhớ dung lượng cao, lưu trữ dữ liệu ổn định lâu dài, tuy tốc độ thấp nhưng có nhiều công nghệ trợ'
               ' giúp phát triển cho các sever.',
    'Link_direct': '/Hdd'
})
data['product'].append({
    'Name': 'Psu - Power Suply Unit',
    'Content': 'Bộ phận cung cấp năng lượng ổn định cho các thiết bị cấu thành nên PC và các thiết bị ngoại vi.',
    'Link_direct': '/Psu'
})
data['product'].append({
    'Name': 'Fan',
    'Content': 'Bao gồm các hệ hống, bộ phận đảm nhiệm vai trò giải quyết vấn đề nhiệt lượng tỏa ra khi vận hành.',
    'Link_direct': '/Fan'
})
data['product'].append({
    'Name': 'Mouse',
    'Content': 'Chuột máy tính, hỗ trợ điều khiển, trải nhiệm và gia tăng độ chính xác cho game thủ. Với những công'
               ' nghệ riêng biệt đáp ứng cho một bộ phận game thủ có yêu cầu độ chính xác cao.',
    'Link_direct': '/Mouse'
})
data['product'].append({
    'Name': 'Monitor',
    'Content': 'Màn hình hiển thị hình ảnh, các lựa chọn dành cho dân chuyên nghiệp và những người sử dụng phổ thông,'
               ' phù hợp với từng yêu cầu về chất lượng hiển thị đáp ứng.',
    'Link_direct': '/Monitor'
})
data['product'].append({
    'Name': 'Keyboard',
    'Content': 'Là bộ phận nhập liệu từ người dùng. Gồm có bàn phím cơ và bàn phím cao su, tích hợp nhiều công nghệ hỗ'
               ' trợ như: blutut, wifi, ... ',
    'Link_direct': '/Keyboard'
})
with open('index.txt', 'w') as outfile:
    json.dump(data, outfile)

# import json
#
# with open('index.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['product']:
#         print('Name: ' + p['Name'])
#         print('Website: ' + p['Content'])
#         print('')
