# -------------------------------
# CHƯƠNG TRÌNH DUYỆT DFS TƯƠNG TÁC
# Khai báo lớp đồ thị
class Graph:
    def __init__(self):
        self.graph = {}  # Dạng danh sách kề (Adjacency List)

    # Hàm thêm cạnh (vô hướng)
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Hàm duyệt DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# PHẦN CHÍNH CỦA CHƯƠNG TRÌNH
if __name__ == "__main__":
    g = Graph()

    print("Nhập các cạnh của đồ thị ")
    print("(VD: A B) và (gõ done khi kết thúc)")
    while True:
        edge = input("Nhập cạnh: ").strip()
        if edge.lower() == 'done':
            break
        try:
            u, v = edge.split()
            g.add_edge(u, v)
        except ValueError:
            print(" Vui lòng nhập đúng định dạng: A B")

    print("\nDanh sách kề của đồ thị:")
    for key, value in g.graph.items():
        print(f"{key}: {value}")

    start_node = input("\nNhập đỉnh bắt đầu DFS: ").strip()

    print("\nThứ tự duyệt DFS:")
    g.dfs(start_node)
    print("\n--- Kết thúc chương trình ---")
