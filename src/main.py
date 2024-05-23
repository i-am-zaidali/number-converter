import streamlit as st

st.title("Number Base Converter")

st.write("### Convert between binary, octal, decimal, and hexadecimal numbers")

col1, col2 = st.columns(2)

changed = st.session_state.get("changed", 0)


def on_change(base_key, **kwargs):
    state = kwargs.get(f"{base_key}-convert-input", None)
    if state is None:
        st.error(f"No state found for {base_key}")
    btn = {"binary": 2, "octal": 8, "decimal": 10, "hex": 16}
    base = btn.get(base_key, 2)
    try:
        changed = int(state, base)
        st.session_state.update({"changed": changed})
    except ValueError:
        st.error(f"Invalid input ({state}) for base {base_key}")


binary = col1.text_input(
    "Binary input",
    key="binary-convert-input",
    placeholder=bin(changed).replace("0b", ""),
    on_change=on_change,
    kwargs=st.session_state,
    args=("binary",),
)
octal = col1.text_input(
    "Octal input",
    key="octal-convert-input",
    placeholder=oct(changed).replace("0o", ""),
    on_change=on_change,
    kwargs=st.session_state,
    args=("octal",),
)
dec = col2.text_input(
    "Decimal input",
    key="decimal-convert-input",
    placeholder=str(changed),
    on_change=on_change,
    kwargs=st.session_state,
    args=("decimal",),
)
hexa = col2.text_input(
    "Hexadecimal input",
    key="hex-convert-input",
    placeholder=hex(changed).replace("0x", ""),
    on_change=on_change,
    kwargs=st.session_state,
    args=("hex",),
)
