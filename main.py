import streamlit as st

if "numero" not in st.session_state:
    st.session_state["numero"] = 0


def main():
    st.subheader(f"Contador: {st.session_state.numero}")

    boton = st.button("Aumentar valor")

    if boton:
        st.session_state.numero += 1
        st.rerun()
    
    print(st.session_state.numero)

if __name__ == "__main__":
    main()