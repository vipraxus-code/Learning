const input1 = document.getElementById("input1");
const input2 = document.getElementById("input2");
const select1 = document.getElementById("select1");
const select2 = document.getElementById("select2");
const conversions = {
    "celsius_fahrenheit": (val) => val * 9/5 + 32,
    "celsius_kelvin": (val) => val + 273.15,
    "fahrenheit_celsius": (val) => (val - 32) * 5/9,
    "fahrenheit_kelvin": (val) => (val - 32) * 5/9 + 273.15,
    "kelvin_celsius": (val) => val - 273.15,
    "kelvin_fahrenheit": (val) => (val - 273.15) * 9/5 + 32
};

let lastActive = input1;

input1.onfocus = input1.oninput = () => {
    lastActive = input1;
    convert(input1, input2, select1, select2);
};

input2.onfocus = input2.oninput = () => {
    lastActive = input2;
    convert(input2, input1, select2, select1);
};

select1.onchange = select2.onchange = () => {
    if (lastActive === input1) {
        convert(input1, input2, select1, select2);
    } else {
        convert(input2, input1, select2, select1);
    }
};

function convert(from_input, to_input, from_select, to_select) {
    const rawVal = from_input.value.trim();
    if (rawVal === "" || isNaN(Number(rawVal))) {
        to_input.value = "";
        return;
    }
    if (from_select.value === to_select.value) {
        to_input.value = rawVal;
        return;
    }
    
    const key = `${from_select.value}_${to_select.value}`;
    if (conversions[key]) {
        to_input.value = parseFloat(conversions[key](Number(rawVal)).toFixed(4));
    }
}