import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_items_crud():
    # Действие 1: создание товара
    new_item = {"name": "Laptop", "price": 228.1}
    response_create = client.post("/items", json=new_item)
    assert response_create.status_code == 200, "Ожидался статус 200 при создании"
    created = response_create.json()
    assert "id" in created, "Ответ должен содержать поле id"
    item_id = created["id"]
    assert created["name"] == new_item["name"], "Имя товара не совпадает"
    assert created["price"] == new_item["price"], "Цена товара не совпадает"

    # Действие 2: получение созданного товара
    response_get = client.get(f"/items/{item_id}")
    assert response_get.status_code == 200, "Ожидался статус 200 при получении"
    fetched = response_get.json()
    assert fetched["id"] == item_id, "ID в ответе не совпадает"
    assert fetched["name"] == new_item["name"], "Имя товара не совпадает при получении"
    assert fetched["price"] == new_item["price"], "Цена товара не совпадает при получении"

    # Действие 3: удаление товара
    response_delete = client.delete(f"/items/{item_id}")
    assert response_delete.status_code == 204, "Ожидался статус 204 при удалении"

    # Проверка, что товар действительно удалён
    response_get_after = client.get(f"/items/{item_id}")
    assert response_get_after.status_code == 404, "После удаления товар должен возвращать 404"

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #

    # ДОПОЛНИТЕЛЬНО (раскомментить код ниже): намеренно поставим цену меньше 0.01 (на это стоит валидатор в классе ItemIn)
    # new_item = {"name": "Laptop", "price": 0.0001}
    # response_create = client.post("/items", json=new_item)
    # assert response_create.status_code == 200, "Ожидался статус 200 при создании"
    # created = response_create.json()
    # assert "id" in created, "Ответ должен содержать поле id"
    # item_id = created["id"]
    # assert created["name"] == new_item["name"], "Имя товара не совпадает"
    # assert created["price"] == new_item["price"], "Цена товара не совпадает"


if __name__ == "__main__":
    pytest.main()
