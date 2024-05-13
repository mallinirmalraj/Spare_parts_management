import sqlite3
conn = sqlite3.connect('spare_part_maintenance.db')
machine_option = 'NPM'
cursor = conn.cursor()
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


# Function to establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('spare_part_maintenance.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
# Route to delete data from the database
@app.route('/delete_data', methods=['POST'])
def delete_data():
    data = request.get_json()  # Assuming you're sending JSON data with the IDs to delete
    ids_to_delete = data.get('ids')  # Assuming the JSON data has a key 'ids' containing a list of IDs to delete

    if not ids_to_delete:
        return jsonify({'message': 'No IDs provided for deletion'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Loop through the IDs and delete corresponding rows from the database
        for id in ids_to_delete:
            cursor.execute("DELETE FROM your_table WHERE id=?", (id,))

        conn.commit()
        return jsonify({'message': 'Data deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)

