import streamlit as st

st.title("GCD and LCM Calculator")

st.write("Enter your integers below.")

first = st.number_input("First Integer", step=1, format="%d")
second = st.number_input("Second Integer", step=1, format="%d")

choice = st.radio(
    "Do you have a third integer to input?",
    ["No", "Yes"]
)

third = None

if choice == "Yes":
    third = st.number_input("Third Integer", step=1, format="%d")


# ==========================================
# EXTENDED EUCLIDEAN ALGORITHM
# ==========================================

def extended_gcd(a, b):

    original_a = a
    original_b = b

    steps = []

    old_r = a
    r = b

    old_x = 1
    x = 0

    old_y = 0
    y = 1

    while r != 0:

        quotient = old_r // r

        remainder = old_r - quotient * r

        steps.append({
            "a": old_r,
            "b": r,
            "q": quotient,
            "r": remainder,
            "x": old_x,
            "y": old_y
        })

        old_r, r = r, remainder

        old_x, x = x, old_x - quotient * x

        old_y, y = y, old_y - quotient * y

    steps.append({
        "a": old_r,
        "b": 0,
        "q": "-",
        "r": 0,
        "x": old_x,
        "y": old_y
    })

    return old_r, old_x, old_y, steps


# ==========================================
# LCM
# ==========================================

def lcm(a, b):

    gcd_value, x, y, steps = extended_gcd(a, b)

    product = a * b
    result = product // gcd_value

    return gcd_value, product, result


# ==========================================
# CALCULATE BUTTON
# ==========================================

if st.button("Calculate GCD and LCM"):

    if first == 0 or second == 0 or (choice == "Yes" and third == 0):

        st.error("Please enter integers other than 0.")

    else:

        # ==========================================
        # GCD COMPUTATION
        # ==========================================

        st.header("GCD Computation")

        gcd_first_second, x1, y1, steps = extended_gcd(first, second)

        st.write(
            f"**Extended Euclidean Algorithm for GCD({first}, {second})**"
        )

        for step in steps:

            if step["q"] != "-":

                st.write(
                    f"{step['a']} = {step['b']}({step['q']}) + {step['r']}"
                )

                st.write(
                    f"x = {step['x']}, y = {step['y']}"
                )

        st.write("---")

        st.write(
            f"**GCD({first}, {second}) = {gcd_first_second}**"
        )

        st.write(
            f"**x = {x1}, y = {y1}**"
        )

        st.write(
            f"**Verification:** "
            f"({first})({x1}) + ({second})({y1}) = {gcd_first_second}"
        )

        if choice == "Yes":

            final_gcd, x2, y2, steps = extended_gcd(
                gcd_first_second,
                third
            )

            st.write("---")

            st.write(
                f"**Extended Euclidean Algorithm for "
                f"GCD({gcd_first_second}, {third})**"
            )

            for step in steps:

                if step["q"] != "-":

                    st.write(
                        f"{step['a']} = {step['b']}({step['q']}) + {step['r']}"
                    )

                    st.write(
                        f"x = {step['x']}, y = {step['y']}"
                    )

            st.write("---")

            st.write(
                f"**GCD({gcd_first_second}, {third}) = {final_gcd}**"
            )

            st.write(
                f"**x = {x2}, y = {y2}**"
            )

            st.write(
                f"**Verification:** "
                f"({gcd_first_second})({x2}) + "
                f"({third})({y2}) = {final_gcd}"
            )

        else:

            final_gcd = gcd_first_second

        st.success(f"Final GCD = {final_gcd}")


        # ==========================================
        # LCM COMPUTATION
        # ==========================================

        st.header("LCM Computation")

        gcd_value, product, first_lcm = lcm(first, second)

        st.write(
            f"**LCM({first}, {second})**"
        )

        st.write(
            f"= ({first} × {second}) ÷ GCD({first}, {second})"
        )

        st.write(
            f"= ({first} × {second}) ÷ {gcd_value}"
        )

        st.write(
            f"= {product} ÷ {gcd_value}"
        )

        st.write(
            f"= **{first_lcm}**"
        )

        if choice == "Yes":

            gcd_value_2, product_2, final_lcm = lcm(
                first_lcm,
                third
            )

            st.write("---")

            st.write(
                f"**LCM({first_lcm}, {third})**"
            )

            st.write(
                f"= ({first_lcm} × {third}) ÷ "
                f"GCD({first_lcm}, {third})"
            )

            st.write(
                f"= ({first_lcm} × {third}) ÷ {gcd_value_2}"
            )

            st.write(
                f"= {product_2} ÷ {gcd_value_2}"
            )

            st.write(
                f"= **{final_lcm}**"
            )

        else:

            final_lcm = first_lcm

        st.success(f"Final LCM = {final_lcm}")