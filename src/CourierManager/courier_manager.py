class CourierManager:
    base: [Courier]
    
    # функция которая по заказу определяет курьера, который будет доставлять этот заказ, или определяет
    # что такого нет. От заказа нужно: откуда, куда, как долго можно ехать(в часах), вес(кг), объем(литры).
    # коды ошибок 
    # 0 - все хорошо
    # 1 - не успеем доехать
    # 2 - слишком тяжёлый заказ
    # 3 - слишком объемный заказ
    # 4 - нет свободных курьеров
    def choose_courier(order: Order) -> (Courier, int):
        
        # проверяем что есть активные курьеры
        found_active_cour = False
        for cour in base:
            if cour.active:
                found_active_cour = True
                break            
        if not found_active_cour:
            return (0, 4)
        
        if order.weight > 7.0 or order.volume > 5.0:
            # считаем, что для большего веса или объема нужна машина
            
            # проверяем что успеем доехать
            if dist(order.start, order.end) / TranSpeedEnum[CAR] > order.time_limit:
                return (0, 1)
            
            for cour in base:
                if cour.transport == CAR and cour.active == True:
                    cour.take_order(order)
                    return (cour, 0)
                
            if order.weight > 7.0:
                return (0, 2)
            else:
                return (0, 3)
        
        # вес меньше 7, объем меньше 5
        # проверяем что есть курьеры, которые смогут доставить за требуемое время
        for cour in base:
            if cour.active and dist(order.start, order.end) / TranSpeedEnum[cour.transport] <= ordr.time_limit:
                return (cour, 0)
        
        # иначе говорим, что не успеваем доехать
        return (cour, 1)
    
    # добавление нового курьеры в базу
    def add_courier(name: str,
                 phone_number: str,
                 age: int,
                 living_address: Adderss,
                 area: DistrictEnum,
                 transport: TransportEnum,
                 salary: int,
                 registration_time: int) -> void:
        cour = Courier(name, phone_number, living_address, area, transport, salary, registration_time)
        base.append(cour)