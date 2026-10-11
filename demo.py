from matcher import match_product

catalog = {"caderno azul": [{"id": "sample-a", "price": 12.0, "category": "papelaria"}],
           "caneta preta": [{"id": "sample-b", "price": 3.0, "category": "papelaria"}]}
for name, price in [("caderno azu", 12.0), ("caneta preta", 9.0)]:
    print(name, "=>", match_product(name, price, catalog))
print("Sugestões apenas: nenhuma integração ou alteração foi executada.")
