import mysql.connector

def get_user_ids(manager_id):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'pii'
    }
    
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        query = """
        SELECT ed.id 
        FROM encryptdecrypt ed 
        JOIN manager m ON m.manager_id = ed.manager_id  
        WHERE m.manager_id = %s
        """
        cursor.execute(query, (manager_id,))
        user_ids = cursor.fetchall()
        
        return user_ids  # Return the user IDs list instead of printing them
    
    except mysql.connector.Error as err:
        print("Error:", err)
        return []
    
    finally:
        cursor.close()
        connection.close()

def good(manager_id):
    return get_user_ids(manager_id)  # Ensure this returns the list
