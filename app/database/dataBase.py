import sqlite3 as sql
class DataBase:
    
    def __init__(self):
        self.DBName = "messages"
        self.conn = sql.connect(self.DBName + '.sqlite')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Messages (
            id INTEGER PRIMARY KEY,
            message_id INTEGER NOT NULL,
            time TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            content TEXT,
            deleted BOOLEAN
            )
        ''')

        self.conn.commit()
        self.conn.close()
    
    def newMessage(self, message):
        self.conn = sql.connect(self.DBName + '.sqlite')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''INSERT INTO Messages (message_id, time, user_id, content, deleted) VALUES (?,?,?,?,?)''', 
                            (message["id"],
                                message["date"], 
                                message["user_id"], 
                                message["text"], 
                                False))
        self.conn.commit()
        self.conn.close()
    
    def deleteMessage(self, user_id, message_ids):
        self.conn = sql.connect(self.DBName + '.sqlite')
        self.cursor = self.conn.cursor()
        up = list()
        for message_id in message_ids:
            up.append(self.cursor.execute('''UPDATE Messages SET deleted = ? WHERE user_id = ? AND message_id = ?''', 
                                (True, user_id, message_id)))
        self.conn.commit()
        self.conn.close()
        return up
                
    def selectMessages(self, user_id, message_id):
        self.conn = sql.connect(self.DBName + '.sqlite')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT content FROM Messages WHERE user_id = ? AND message_id = ?''', (user_id, message_id))
        message = self.cursor.fetchall()
        self.conn.close()
        return message
                