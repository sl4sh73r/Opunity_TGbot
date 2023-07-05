import sqlite3


class BotDB:

    def __init__(self):
        """Инициализирует соединение с БД"""
        self.conn = sqlite3.connect('database/OpunityBD.db')
        self.cursor = self.conn.cursor()
        self.conn.set_trace_callback(print)

    def add_user(self, user_id):
        """Добавляет пользователя в БД"""
        self.cursor.execute(
            '''
            INSERT INTO user (`user_id`, `state`)
            VALUES (?, ?);
            ''',
            (user_id, 1))
        return self.conn.commit()
    
    def add_order(self, user_id):
        """Добавляет заказ в БД"""
        self.cursor.execute(
            '''
            INSERT INTO orders (`user_id`)
            VALUES (?);
            ''',
            (user_id, )
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def add_seller(self, seller_id):
        """Добавляет исполнителя в БД"""
        self.cursor.execute(
            '''
            INSERT INTO seller (`seller_id`)
            VALUES (?);
            ''',
            (seller_id, )
        )
        return self.conn.commit()

    def save_orders_info(self, id, params: dict):
        query = f'''
                UPDATE orders
                SET description = "{params.get('description')}",
                    quantity = "{params.get('quantity')}",
                    length = "{params.get('length')}",
                    width = "{params.get('width')}",
                    height = "{params.get('height')}",
                    material = "{params.get('material')}",
                    color = "{params.get('color')}",
                    post_processing = "{params.get('post_processing')}",
                    sample = "{params.get('image_id')}"
                WHERE id = {id};
                '''
        self.cursor.execute(query)
        self.conn.commit()

    def save_seller_info(self, seller_id, params: dict):
        query = f'''
                UPDATE seller
                SET employment_type = "{params.get('employment_type')}",
                    person_info = "{params.get('person_info')}",
                    inn = "{params.get('inn')}",
                    payment_details = "{params.get('payment_details')}",
                    logo = "{params.get('logo')}",
                    experience = "{params.get('experience')}",
                    portfolio_link = "{params.get('portfolio_link')}",
                    guarantees = "{params.get('guarantees')}",
                    confidentiality = "{params.get('confidentiality')}"
                WHERE seller_id = {seller_id};
                '''
        self.cursor.execute(query)
        self.conn.commit()

    def user_exists(self, user_id):
        """Проверяет, есть ли пользователь в БД"""
        query = self.cursor.execute(
            '''
            SELECT id FROM user 
            WHERE user_id = ?;
            ''',
            (user_id, )
        )
        return query.fetchone() is not None
    
    def check_seller_exists(self, seller_id):
        query = self.cursor.execute(
            f'''
            SELECT seller_id FROM seller
            WHERE seller_id = ?;
            ''',
            (seller_id, )
        )
        
        return query.fetchone() is not None

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()


"""
def save_description(self, id, description):
        self.cursor.execute(
            f'''
            UPDATE orders
            SET description = "{description}"
            WHERE id = {id};
            '''
        )
        return self.conn.commit()

    def save_quantity(self, id, quantity):
        self.cursor.execute(
            f'''
            UPDATE orders
            SET quntity = {quantity}
            WHERE id = {id};
            '''
        )
        return self.conn.commit()
"""