# main_module.py
import os

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            row_dict = {header[i]: values[i] for i in range(len(header))}
            data.append(row_dict)
    return data

def calculate_indicators(data):
    sma_values = []
    rsi_values = []
    for i in range(len(data)):
        if i >= 4:
            close_prices = [float(data[j]['Close']) for j in range(i-4, i+1)]
            sma = sum(close_prices) / 5
            sma_values.append(sma)
        if i >= 13:
            gains = losses = 0
            for j in range(i-13, i):
                price_diff = float(data[j+1]['Close']) - float(data[j]['Close'])
                if price_diff > 0:
                    gains += price_diff
                else:
                    losses += abs(price_diff)
            avg_gain = gains / 14
            avg_loss = losses / 14
            if avg_gain == 0 and avg_loss == 0:
                rsi = 50
            else:
                if avg_loss != 0 and avg_loss > 1e-10:
                    rs = avg_gain / avg_loss
                    rsi = 100 - (100 / (1 + rs))
                else:
                    rsi = 100
            rsi_values.append(rsi)
    return sma_values, rsi_values

def write_to_file(file_path, values, header):
    with open(file_path, 'w') as file:
        file.write(','.join(header) + '\n')
        for value in values:
            file.write(str(value) + '\n')

def main():
    # Get the absolute path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # File paths (using relative paths)
    input_file_path = 'orcl.csv'  # Updated file path
    sma_file_path = os.path.join(script_dir, 'orcl-sma.csv')
    rsi_file_path = os.path.join(script_dir, 'orcl-rsi.csv')

    # Print script directory and file paths for debugging
    print(f"Script directory: {script_dir}")
    print(f"Input file path: {input_file_path}")

    # Check if the 'orcl.csv' file exists
    if not os.path.exists(input_file_path):
        print(f"Error: 'orcl.csv' file not found in the specified directory.")
        return

    # Load data from the CSV file
    historical_data = load_data(input_file_path)

    # Calculate indicators
    sma_values, rsi_values = calculate_indicators(historical_data)

    # Write SMA values to file
    write_to_file(sma_file_path, sma_values, ['SMA'])

    # Write RSI values to file
    write_to_file(rsi_file_path, rsi_values, ['RSI'])

    print("Done!... YOU NAILED IT LINA!")

if __name__ == "__main__":
    main()

