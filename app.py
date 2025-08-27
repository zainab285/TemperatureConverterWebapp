from flask import Flask, render_template, request

app = Flask(__name__)

def convert_temperature(temp, from_scale, to_scale):
    # Convert input temperature to Celsius first
    if from_scale == 'C':
        celsius = temp
    elif from_scale == 'F':
        celsius = (temp - 32) * 5 / 9
    elif from_scale == 'K':
        celsius = temp - 273.15
    else:
        return None

    # Convert Celsius to target scale
    if to_scale == 'C':
        return celsius
    elif to_scale == 'F':
        return (celsius * 9 / 5) + 32
    elif to_scale == 'K':
        return celsius + 273.15
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def temperature_converter():
    result = ''
    if request.method == 'POST':
        temp = request.form.get('temperature')
        from_scale = request.form.get('from_scale')
        to_scale = request.form.get('to_scale')

        if temp:
            try:
                temp = float(temp)
                if from_scale == to_scale:
                    result = f"No conversion needed. Both scales are {from_scale}."
                else:
                    converted = convert_temperature(temp, from_scale, to_scale)
                    if converted is None:
                        result = "Invalid scale selected."
                    else:
                        result = f"{temp}°{from_scale} is {converted:.2f}°{to_scale}"
            except ValueError:
                result = "Please enter a valid number."
        else:
            result = "Please enter a temperature."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


