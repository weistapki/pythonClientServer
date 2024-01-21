import matplotlib.pyplot as plt
import networkx as nx

# Створюємо граф
G = nx.DiGraph()

# Додаємо вузли
G.add_node("Client")
G.add_node("Encrypt Client Data")
G.add_node("Send Encrypted Data to Server")
G.add_node("Server")
G.add_node("Receive Encrypted Data")
G.add_node("Decrypt Server Data")
G.add_node("Write to File (received.txt)")
G.add_node("Decrypt and Write to File (decrypted_received.txt)")

# Додаємо ребра (зв'язки між вузлами)
G.add_edge("Client", "Encrypt Client Data")
G.add_edge("Encrypt Client Data", "Send Encrypted Data to Server")
G.add_edge("Send Encrypted Data to Server", "Server")
G.add_edge("Server", "Receive Encrypted Data")
G.add_edge("Receive Encrypted Data", "Decrypt Server Data")
G.add_edge("Decrypt Server Data", "Write to File (received.txt)")
G.add_edge("Write to File (received.txt)", "Decrypt and Write to File (decrypted_received.txt)")

# Виводимо граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color="skyblue", font_size=8, edge_color="gray", node_shape='o')
plt.show()