from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        
        data = request.json.get('data', [])

        
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        alphabet_string = ""

        
        for item in data:
            if item.isalpha(): 
                alphabets.append(item.upper()) 
                alphabet_string += item
            elif item.isnumeric(): 
                num = int(item)
                total_sum += num 
                if num % 2 == 0:
                    even_numbers.append(str(num)) # Add to even numbers list
                else:
                    odd_numbers.append(str(num)) # Add to odd numbers list
            else:
                special_characters.append(item) # Add everything else to special characters

        # Create the special reversed string with alternating caps
        reversed_str = alphabet_string[::-1]
        concat_string = ""
        for i, char in enumerate(reversed_str):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()

        # Build the final JSON response with your details
        response = {
            "is_success": True, # Set operation status to true
            "user_id": "aman_singh_15022004", # Format: full_name_ddmmyyyy
            "email": "aman.singh2004@chitkara.edu.in", # Your email ID
            "roll_number": "2010991234", # Your roll number
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum), # The sum must be returned as a string
            "concat_string": concat_string
        }
        # Return the response with a 200 OK status code
        return jsonify(response), 200

    except Exception as e:
        # If any error occurs, return a failure response
        return jsonify({"is_success": False, "error": str(e)}), 500

# This makes the server run when you execute the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

