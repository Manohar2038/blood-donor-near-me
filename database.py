import mysql.connector
from config import DB_CONFIG


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_donors(needed_bg):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT d.*, u.name
        FROM donors d
        JOIN users u ON d.user_id = u.id
        JOIN blood_compatibility bc
        ON d.blood_group = bc.donor_blood_group
        WHERE bc.recipient_blood_group = %s
        AND d.is_available = TRUE
        AND (
            d.last_donation_date IS NULL
            OR d.last_donation_date <=
            DATE_SUB(CURDATE(), INTERVAL 90 DAY)
        )
    """

    cursor.execute(query, (needed_bg,))
    donors = cursor.fetchall()

    cursor.close()
    conn.close()

    return donors


def get_total_donors():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM donors"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_total_requests():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM blood_requests"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

def get_donors_by_blood_group():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT
            blood_group,
            COUNT(*) AS total
        FROM donors
        GROUP BY blood_group
        ORDER BY blood_group
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_donors_by_blood_group():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT
            blood_group,
            COUNT(*) AS total
        FROM donors
        GROUP BY blood_group
        ORDER BY blood_group
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result