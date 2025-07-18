def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
        print("After kitchen update:", chai_type)

    kitchen()
    print("Final chai_type in update_order:", chai_type)

update_order()
