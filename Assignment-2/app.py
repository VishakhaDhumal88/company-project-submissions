# app.py
from flask import Flask, request, jsonify
from models import db, Transaction

def numbers_to_key(numbers):
    """Helper: creates a hashable & order-insensitive key for number lists."""
    return ','.join(map(str, sorted(numbers)))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sumapi.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/api/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json(force=True)
    if not data or "numbers" not in data:
        return jsonify({"error": "Missing 'numbers' field."}), 400
    numbers = data.get("numbers")
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"error": "Field 'numbers' must be a list of numbers."}), 400
    key = numbers_to_key(numbers)
    trx = Transaction.query.filter_by(numbers=key).first()
    if trx:
        # Return cached result
        return jsonify({
            "numbers": numbers,
            "sum": trx.result,
            "cached": True
        }), 200
    # Compute sum and save transaction
    result = sum(numbers)
    trx = Transaction(numbers=key, result=result)
    db.session.add(trx)
    db.session.commit()
    return jsonify({
        "numbers": numbers,
        "sum": result,
        "cached": False
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
