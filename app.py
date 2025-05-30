import streamlit as st

# Function to choose evenly spaced items
def choose_evenly_spaced(lst, count):
    if count < 1:
        return []
    if count == 1:
        return [lst[0]]
    if count > len(lst):
        raise ValueError("Cannot choose more items than are in the list.")
    
    step = (len(lst) - 1) / (count - 1)
    indices = [round(i * step) for i in range(count)]
    return [lst[i] for i in indices]

# Fixed list of numbers
numbers = [
    4, 5, 6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
    43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56
]

# Streamlit UI
st.title("Skydio X2D Frequency Distributor")
st.write("Evenly spaces apart frequencies the maximum distance from one another in order to prevent overlapping channels.")

# Dropdown for item count selection
options = list(range(1, len(numbers) + 1))
count = st.selectbox("Number of channels needed", options, index=4)

# Button to generate selection
if st.button("Generate Spaced Frequencies"):
    try:
        result = choose_evenly_spaced(numbers, count)

        # Generate HTML table
        html = "<table style='width:100%; border-collapse: collapse;'>"
        html += "<tr><th style='text-align: left; padding: 4px;'>Vehicle</th><th style='text-align: left; padding: 4px;'>Frequency</th></tr>"
        for i, value in enumerate(result, start=1):
            html += f"<tr><td style='padding: 4px;'>{i}</td><td style='padding: 4px;'>{value}</td></tr>"
        html += "</table>"

        st.markdown(html, unsafe_allow_html=True)

    except ValueError as e:
        st.error(str(e))
