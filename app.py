import streamlit as st

result = 0
lengthUnits = ['meters', 'kilometers', 'miles', 'feet', 'inches', 'yards', 'centimeters', 'millimeters']
tempUnits = ['Celsius', 'Fahrenheit', 'Kelvin']
volumeUnits = ['liters', 'milliliters', 'gallons', 'fluid ounces', 'cups', 'cubic meters', 'cubic centimeters']
weightUnits = ['kilograms', 'grams', 'pounds', 'ounces', 'tons', 'milligrams']
digitalStorageUnits = ['bytes', 'kilobytes (KB)', 'megabytes (MB)', 'gigabytes (GB)', 'terabytes (TB)', 'petabytes (PT)']

def convert_length(val, fromVal, toVal):
    meter_conversion = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254,
        'yards': 0.9144,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    meters = val * meter_conversion[fromVal]
    result = meters / meter_conversion[toVal]
    return result

def convert_temp(val, fromVal, toVal):
    if fromVal == 'Celsius':
        kelvin = val + 273.15
    elif fromVal == 'Fahrenheit':
        kelvin = (val - 32) * 5/9 + 273.15
    else:
        kelvin = val
    
    if toVal == 'Celsius':
        return kelvin - 273.15
    elif toVal == 'Fahrenheit':
        return (kelvin - 273.15) * 9/5 + 32
    else:
        return kelvin

def convert_vol(val, fromVal, toVal):
    liter_conversion = {
        'liters': 1,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'fluid ounces': 0.0295735,
        'cups': 0.236588,
        'cubic meters': 1000,
        'cubic centimeters': 0.001
    }
    liters = val * liter_conversion[fromVal]
    result = liters / liter_conversion[toVal]
    return result

def convert_weight(val, fromVal, toVal):
    kg_conversion = {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'tons': 1000,
        'milligrams': 0.000001
    }
    kg = val * kg_conversion[fromVal]
    result = kg / kg_conversion[toVal]
    return result

def convert_digital_storage(val, fromVal, toVal):
    byte_conversion = {
        'bytes': 1,
        'kilobytes (KB)':1024,
        'megabytes (MB)':1048576,
        'gigabytes (GB)':1073741824,
        'terabytes (TB)':1099511627776,
        'petabytes (PT)':1125899906842624
    }
    bytes = val * byte_conversion[fromVal]
    result = bytes / byte_conversion[toVal]
    return result

st.set_page_config(page_title="Unit Converter", layout="wide")

st.title("🔢 Unit Converter App 🚀")

conversion = st.selectbox('🔄 Select a conversion', ['📏 Length', '🌡 Temperature', '🛢 Volume', '⚖ Weight', 'Digital Storage'])
value = st.number_input("✏ Enter value to convert")

if conversion == '📏 Length':
    fromVal = st.selectbox('📍 From:', lengthUnits)
    toVal = st.selectbox('🎯 To:', lengthUnits)
    if st.button("🔄 Convert"):
        result = convert_length(value, fromVal, toVal)
        st.success(f"✅ {value} {fromVal} = {result:.6f} {toVal}")

elif conversion == '🌡 Temperature':
    fromVal = st.selectbox('📍 From:', tempUnits)
    toVal = st.selectbox('🎯 To:', tempUnits)
    if st.button("🔄 Convert"):
        result = convert_temp(value, fromVal, toVal)
        st.success(f"✅ {value} {fromVal} = {result:.2f} {toVal}")

elif conversion == '🛢 Volume':
    fromVal = st.selectbox('📍 From:', volumeUnits)
    toVal = st.selectbox('🎯 To:', volumeUnits)
    if st.button("🔄 Convert"):
        result = convert_vol(value, fromVal, toVal)
        st.success(f"✅ {value} {fromVal} = {result:.6f} {toVal}")

elif conversion == '⚖ Weight':
    fromVal = st.selectbox('📍 From:', weightUnits)
    toVal = st.selectbox('🎯 To:', weightUnits)
    if st.button("🔄 Convert"):
        result = convert_weight(value, fromVal, toVal)
        st.success(f"✅ {value} {fromVal} = {result:.6f} {toVal}")

elif conversion == 'Digital Storage':
    fromVal = st.selectbox('📍 From:', digitalStorageUnits)
    toVal = st.selectbox('🎯 To:', digitalStorageUnits)
    if st.button("🔄 Convert"):
        result = convert_digital_storage(value, fromVal, toVal)
        st.success(f"✅ {value} {fromVal} = {result:.6f} {toVal}")

else:
    st.warning("⚠ Invalid selection, please choose a valid option.")
