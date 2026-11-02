
import streamlit as st

from database import (
    get_total_donors,
    get_total_requests,
    get_donors_by_blood_group
)


# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="Blood Donor Near Me",
    page_icon="🩸",
    layout="wide"
)


# ---------------------------------
# APPLICATION HEADER
# ---------------------------------

st.title("🩸 Blood Donor Near Me")

st.write(
    "Find nearby blood donors and help save lives."
)

st.divider()


# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.selectbox(
    "Select Page",
    [
        "Home",
        "Register as Donor",
        "Request Blood",
        "View Matches",
        "Admin Analytics"
    ]
)


# ---------------------------------
# HOME PAGE
# ---------------------------------

if menu == "Home":

    st.header("Welcome!")

    st.write(
        "Blood Donor Near Me helps patients "
        "find compatible blood donors nearby."
    )

    st.subheader("Project Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🩸 Blood Group Compatibility")

        st.info("📍 Nearby Donor Search")

    with col2:
        st.info("⚡ Priority-Based Matching")

        st.info("📊 Admin Analytics")


# ---------------------------------
# REGISTER AS DONOR
# ---------------------------------

elif menu == "Register as Donor":

    st.header("🩸 Donor Registration")

    st.write(
        "Register yourself as a blood donor."
    )

    with st.form("donor_registration_form"):

        name = st.text_input("Full Name")

        email = st.text_input("Email")

        phone = st.text_input("Phone Number")

        blood_group = st.selectbox(
            "Blood Group",
            [
                "A+", "A-", "B+", "B-",
                "AB+", "AB-", "O+", "O-"
            ]
        )

        city = st.text_input("City")

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=18
        )

        weight = st.number_input(
            "Weight (KG)",
            min_value=1.0,
            max_value=300.0,
            value=50.0
        )

        submitted = st.form_submit_button(
            "Register as Donor"
        )

        if submitted:

            if not name or not email or not phone or not city:

                st.error("Please fill in all required fields.")

            else:

                st.success(
                    "Registration form validated. "
                    "Database registration will be connected next."
                )


# ---------------------------------
# REQUEST BLOOD
# ---------------------------------

elif menu == "Request Blood":

    st.header("🏥 Request Blood")

    with st.form("blood_request_form"):

        requester_name = st.text_input(
            "Patient / Requester Name"
        )

        blood_group = st.selectbox(
            "Required Blood Group",
            [
                "A+", "A-", "B+", "B-",
                "AB+", "AB-", "O+", "O-"
            ]
        )

        units = st.number_input(
            "Units Required",
            min_value=1,
            max_value=20,
            value=1
        )

        urgency = st.selectbox(
            "Urgency",
            [
                "Critical",
                "High",
                "Medium"
            ]
        )

        hospital = st.text_input(
            "Hospital Name"
        )

        submitted = st.form_submit_button(
            "Find Blood Donors"
        )

        if submitted:

            if not requester_name or not hospital:

                st.error("Please fill in all required fields.")

            else:

                st.success(
                    "Blood request validated. "
                    "Donor matching integration will be added next."
                )


# ---------------------------------
# VIEW MATCHES
# ---------------------------------

elif menu == "View Matches":

    st.header("🔍 Donor Matches")

    st.info(
        "Ranked donor results will appear here "
        "after connecting the matching engine."
    )


# ---------------------------------
# ADMIN ANALYTICS
# ---------------------------------

elif menu == "Admin Analytics":

    st.header("📊 Admin Analytics")

    st.write(
        "Overview of blood donors and blood requests."
    )

    try:

        # Fetch statistics from MySQL

        total_donors = get_total_donors()

        total_requests = get_total_requests()

        blood_group_data = get_donors_by_blood_group()


        # Display total counts

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                label="Total Donors",
                value=total_donors
            )

        with col2:

            st.metric(
                label="Total Blood Requests",
                value=total_requests
            )


        st.divider()


        # Blood group statistics

        st.subheader("🩸 Donors by Blood Group")

        if blood_group_data:

            chart_data = {
                row["blood_group"]: row["total"]
                for row in blood_group_data
            }

            st.bar_chart(chart_data)

            st.subheader("Detailed Statistics")

            st.table(blood_group_data)

        else:

            st.info(
                "No donor records found in the database."
            )


        # Refresh button

        if st.button("🔄 Refresh Analytics"):

            st.rerun()


    except Exception as e:

        st.error(
            f"Unable to load analytics: {e}"
        )


# ---------------------------------
# FOOTER
# ---------------------------------

st.divider()

st.caption(
    "Blood Donor Near Me | Python + MySQL + DSA"
)
