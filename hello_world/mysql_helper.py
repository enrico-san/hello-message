from multiprocessing import connection
import pymysql.cursors

# TODO as this is a quick and dirty mysql call, params are in the code. They must come from the environment
HOST ='172.17.0.3'
USER = 'root'
DB = 'acube'

def get_connection():
  connection = pymysql.connect(host=HOST,
                              user=USER,
                              database=DB,
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
  return connection

def update(customerId, messageType, amount):
  """
  Inserts a new row in the database if customer_id + type_id does not exist
  Otherwise increments the count field by one and add the amount to the existing amout
  """
  connection = get_connection()
  with connection:
      with connection.cursor() as cursor:
          # Create a new record
          sql = """
          INSERT INTO stats 
            (customer_id, type_id, count, amount) 
          VALUES
            (%(customerId)s, %(messageType)s, 1, %(amount)s)
          ON DUPLICATE KEY UPDATE
            count = count + 1,
            amount = amount + %(amount)s
          """
          cursor.execute(sql, {"customerId": customerId, "messageType": messageType, "amount": amount})

      connection.commit()

if __name__ == "__main__":
  print(update(1, 'a', '1.23'))