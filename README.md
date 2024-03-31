## I. Sinh mê cung
- Sử dụng thuật toán Kruskal ngẫu nhiên để tạo mê cung
- Lý do chọn kruskal:
  + Thuật toán kruskal được ứng dụng để tìm cây khung nhỏ nhât
  + Cây khung là 1 đồ thị liên thông, không có chu trình và có (và duy nhất) đường đi giữa 2 điểm bất kỳ. Nên ta luôn tạo được mê cung có lời giải     
- Thuật toán:  
  + Coi mỗi ô là 1 điểm trên đồ thị
  + Khởi tạo 1 đồ thị $T = \emptyset$.
  + Khi $|T| < n^2$ (với $n \times n$ là kích thước mê cung) lặp lại các bước:
      - Chọn ngẫu nhiên 1 cạnh e bất kỳ $e \notin T$.
      - Nếu $T + e$ không tạo thành1 chu trình thì $T = T + e$
  + Khi $|T| = n*2$ thì ta thu được T là cây khung
  + Với mỗi cạnh trong $T$ ta sẽ xóa bức tường ngăn 2 đỉnh của cạnh đó

## II. Giải mê cung  
### II.1. Thuật toán A*  
#### 1.1 Giới thiệu
- Thuật toán A* là thuật toán tìm đường đi từ 1 nút khởi tạo ban đầu đến nút đich.
- Thuật toán sử dụng 1 hàm ước lượng heuristic để đánh giá đường đi tốt nhất có thể đi.
#### 1.2 Thuật toán
- Giả sử trạng thái ban đầu là $n_0$, trạng thái hiện tại là $n$.
- Ta có hàm đánh giá $f(n) = g(n) + h(n)$. Trong đó:
  + $g(n)$ là chi phí từ trạng thái $n_0$ đến trạng thái $n$
  + $h(n)$ là hàm heuristic ước lượng chi phí từ $n$ đến đích
  + $f(n)$ là chi phí ước lượng từ $n_0$ đích.

### II.2 Ứng dụng A* trong bài toán tìm đường đi trong mê cung
B1. Đặt $OPEN = {n_0}$ và $CLOSE = \emptyset $. Khi đó $f(n_0) = g(n_0) = h(n_0) = 0$  
B2. Lặp lại các bước sau đến khi gặp điều kiện dừng:
  - Nếu $OPEN$ rỗng: bài toán vô nghiệm => thoát khỏi vòng lặp
  - Ngược lại:
    + Chọn $n_i$ trong tập $OPEN$ sao cho $f(n_i)$ nhỏ nhất.
    + Lấy $n_i$ ra khỏi $OPEN$ và thên vào tập $CLOSE$
    + Nếu $n_i$ là đích $\Rightarrow$ Thoát.
    + Ngược lại. Tạo danh sách các trạng thái tiếp theo của $n_i$ (hay các điểm lân cận $n_i$)
    + Với mỗi trạng thái $n_k$ thuộc danh sách trên ta thực hiện các bước:
      - Tính $g(n_k) = g(n_i) + cost(n_i,n_k)$. Với $cost(n_i,n_k)$ là chi phí đi từ $n_i$ tới $n_k$ ta coi bằng 1
      - $h(n_k)$ (Trong bài toán này tôi sử dụng $h(n_k)$ = vị trí tại đích - vị trí tại $n_k$)
      - $f(n_k) = g(n_k) + h(n_k)$
      - Nếu $n_k$ chưa xuất hiện trong $OPEN$ và $CLOSE$ thì ta thêm $n_k$ vào $OPEN$      
      
