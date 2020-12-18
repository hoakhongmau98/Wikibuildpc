Trang web này đang trong thời gian phát triển.
-
* missing site components:
    * Gpu - Vga
    * Hdd - Ssd 
    * Psu 
    * Colling 
    
* > build/product.py 
  > * count price 
  > * show list product selected.
  

<h3>Data được claw từ trang hanoicomputer.com</h3>
> /static/Categories
* Gồm 12 thể loại: với cây thư mục.
* > /Categories/Category_classify -- file csv chứa các mục phân loại sản phẩm.
* > /Categories/Element -- file csv định dạng các sản phẩm dựa trên phân loại định sẵn.
* > /Categories/img -- chứa ảnh của các sản phẩm
* > /Categories/Error -- file csv định dạng các sản phẩm không có hình ảnh.
* > /Categories/Product -- file csv lưu Code, Name, price, infor của từng sản phẩm.
* > /Categories/Text - File text chứa thông tin của từng phân loại. 