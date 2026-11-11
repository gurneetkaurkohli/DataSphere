import textwrap
import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIGURATION AND CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* ==========================================
   GLOBAL FONT
========================================== */

html, body, [class*="st-"], [class*="css-"],
h1, h2, h3, h4, h5, h6, p, label {
    font-family: "Times New Roman", Times, serif !important;
}
/* FIX STREAMLIT MATERIAL ICONS */

[data-testid="stIconMaterial"],
.material-icons,
.material-symbols-rounded,
span[data-testid="stIconMaterial"] {
    font-family: "Material Symbols Rounded" !important;
    font-weight: normal !important;
    font-style: normal !important;
    font-size: 20px !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    -webkit-font-feature-settings: "liga";
    -webkit-font-smoothing: antialiased;
}


/* ==========================================
   MAIN WEBSITE BACKGROUND
========================================== */

.stApp {
    background-color: #FBF7F4 !important;
    color: #3B2F2A !important;
}

[data-testid="stMain"] {
    background-color: #FBF7F4 !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* ==========================================
   MAIN HEADINGS
========================================== */

h1, h2, h3, h4, h5, h6 {
    color: #3B2F2A !important;
    font-weight: 700;
}


/* ==========================================
   PREMIUM SIDEBAR
========================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #3B2F2A 0%,
        #291C0E 100%
    ) !important;
}

[data-testid="stSidebar"] * {
    font-family: "Times New Roman", Times, serif !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #FBF7F4 !important;
}


/* ==========================================
   SIDEBAR BRAND
========================================== */

.sidebar-brand {
    padding: 12px 5px 22px 5px;
}

.sidebar-brand h1 {
    color: #FBF7F4 !important;
    font-size: 30px !important;
    margin-bottom: 5px !important;
}

.sidebar-brand h1 span {
    color: #B98F88 !important;
}

.sidebar-brand p {
    color: #D8C4AC !important;
    font-size: 11px !important;
    letter-spacing: 1px;
}


/* ==========================================
   SIDEBAR SEARCH
========================================== */

[data-testid="stSidebar"] input {
    background: #FBF7F4 !important;
    color: #3B2F2A !important;
    border: 1px solid #D8C4AC !important;
    border-radius: 10px !important;
}


/* ==========================================
   MENU HEADING
========================================== */

.sidebar-section-title {
    color: #D8C4AC;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-top: 22px;
    margin-bottom: 14px;
}


/* ==========================================
   NAVIGATION BUTTONS
========================================== */

[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 11px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    padding: 10px 14px !important;
    margin-bottom: 7px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}


/* INACTIVE BUTTONS */

[data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
    background: rgba(232,216,206,0.10) !important;
    color: #FBF7F4 !important;
    border: 1px solid rgba(232,216,206,0.18) !important;
}


/* HOVER EFFECT */

[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
    background: #7A6258 !important;
    border-color: #B98F88 !important;
    color: #FFFFFF !important;
}


/* ACTIVE BUTTON */

[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background: #B98F88 !important;
    color: #FFFFFF !important;
    border: 1px solid #D8C4AC !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}


/* BUTTON ICONS */

[data-testid="stSidebar"] div.stButton button span {
    color: #FBF7F4 !important;
}


/* ==========================================
   WORKSPACE CARD
========================================== */

.workspace-card {
    background: rgba(232,216,206,0.12);
    border: 1px solid rgba(232,216,206,0.20);
    border-radius: 12px;
    padding: 15px;
    margin-top: 12px;
}

.workspace-card .workspace-label {
    color: #D8C4AC !important;
    font-size: 10px;
    letter-spacing: 1.5px;
}

.workspace-card h3 {
    color: #FBF7F4 !important;
    font-size: 17px;
    margin: 5px 0;
}

.workspace-card p {
    color: #D8C4AC !important;
    font-size: 12px;
}


/* ==========================================
   SIDEBAR FOOTER
========================================== */

.sidebar-footer {
    text-align: center;
    color: #B98F88;
    font-size: 10px;
    letter-spacing: 1px;
    padding: 22px 0 5px 0;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(232,216,206,0.25) !important;
}


/* ==========================================
   MAIN BUTTONS
========================================== */


   .stButton > button {
    background-color: #7A6258 !important;
    color: #FBF7F4 !important;
    border: 1px solid #7A6258 !important;
    border-radius: 10px !important;
    padding: 12px 16px !important;
    font-family: "Times New Roman", Times, serif !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    background-color: #3B2F2A !important;
    color: #FBF7F4 !important;
    border-color: #3B2F2A !important;
}

/* ==========================================
   METRIC CARDS
========================================== */

[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 1px solid #E8D8CE !important;
    border-radius: 14px !important;
    padding: 18px !important;
    box-shadow: 0 3px 12px rgba(59,47,42,0.05);
}

[data-testid="stMetricLabel"] {
    color: #7A6258 !important;
}

[data-testid="stMetricValue"] {
    color: #3B2F2A !important;
}


/* ==========================================
   INPUT FIELDS
========================================== */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background: #FFFFFF !important;
    color: #3B2F2A !important;
    border: 1px solid #D8C4AC !important;
    border-radius: 9px !important;
}


/* ==========================================
   SELECT BOX
========================================== */

.stSelectbox div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border-color: #D8C4AC !important;
    border-radius: 9px !important;
}


/* ==========================================
   DATA TABLES
========================================== */

[data-testid="stDataFrame"] {
    border: 1px solid #E8D8CE !important;
    border-radius: 12px !important;
}


/* ==========================================
   DIVIDERS
========================================== */

hr {
    border-color: #E8D8CE !important;
}


/* ==========================================
   ALERT BOXES
========================================== */

[data-testid="stAlert"] {
    background: #F3E8E2 !important;
    border: 1px solid #D8C4AC !important;
    color: #3B2F2A !important;
}
/* ==========================================
   CREAM & COCOA COLOUR OVERRIDES
========================================== */

/* Main background */
.stApp,
[data-testid="stMain"] {
    background-color: #FBF7F4 !important;
}

/* Main headings */
h1, h2, h3, h4, h5, h6 {
    color: #3B2F2A !important;
}

/* Links and blue accents */
a {
    color: #7A6258 !important;
}

/* Progress bars */
.stProgress > div > div > div > div {
    background-color: #B98F88 !important;
}

/* Tabs */
[data-baseweb="tab-highlight"] {
    background-color: #B98F88 !important;
}

/* Selected navigation */
[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background-color: #B98F88 !important;
    border-color: #D8C4AC !important;
}

/* General cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    border-color: #E8D8CE !important;
}

/* Main buttons */
.stButton > button {
    background-color: #7A6258 !important;
    color: #FFFFFF !important;
}

/* Button hover */
.stButton > button:hover {
    background-color: #3B2F2A !important;
}
/* HOME PAGE HERO BANNER */
.home-hero {
    background: linear-gradient(135deg, #7A6258, #3B2F2A);
    padding: 45px;
    border-radius: 18px;
    margin-bottom: 30px;
    color: #FBF7F4 !important;
}

.stApp .home-hero h1 {
    color: #FBF7F4 !important;
}

.home-hero .hero-subtitle {
    color: #FBF7F4 !important;
}

.home-hero .hero-description {
    color: #E8D8CE !important;
}
/* ==========================================
   HOME PAGE - REMOVE BLUE ACCENTS
========================================== */

/* Getting Started card */
.getting-started-card {
    border-left: 6px solid #7A6258 !important;
    background: #FFFFFF !important;
    border-radius: 16px !important;
}

/* Main content text */
[data-testid="stMain"] p {
    color: #7A6258 !important;
}

/* Main content links */
[data-testid="stMain"] a {
    color: #7A6258 !important;
}

/* Home page cards */
[data-testid="stMain"] [data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #E8D8CE !important;
}

/* Step labels */
.step-label {
    color: #B98F88 !important;
}

/* Card descriptions */
.step-description {
    color: #7A6258 !important;
}

/* Remove blue borders */
[data-testid="stMain"] .stAlert {
    border-color: #D8C4AC !important;
}

/* Section headings */
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3 {
    color: #3B2F2A !important;
}

/* FIX DASHBOARD TEMPLATE BUTTON TEXT */

[data-testid="stMain"] div[data-testid="stButton"] button {
    background-color: #7A6258 !important;
    color: #FBF7F4 !important;
    border: 1px solid #7A6258 !important;
    border-radius: 10px !important;
    min-height: 48px !important;
    font-family: "Times New Roman", Times, serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    opacity: 1 !important;
}

/* Make sure nested button text is visible */
[data-testid="stMain"] div[data-testid="stButton"] button p,
[data-testid="stMain"] div[data-testid="stButton"] button span {
    color: #FBF7F4 !important;
    opacity: 1 !important;
}

/* Button hover */
[data-testid="stMain"] div[data-testid="stButton"] button:hover {
    background-color: #3B2F2A !important;
    border-color: #3B2F2A !important;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# INITIALIZE SESSION STATE
# ==========================================

if "data" not in st.session_state:
    st.session_state.data = None

if "original_data" not in st.session_state:
    st.session_state.original_data = None

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


# ==========================================
# PREMIUM SIDEBAR NAVIGATION
# ==========================================

# APP LOGO

st.sidebar.markdown("""
<div class="sidebar-brand">
    <h1>Data<span>Sphere</span></h1>
    <p>ANALYTICS & BUSINESS INTELLIGENCE</p>
</div>
""", unsafe_allow_html=True)


# SEARCH BAR

search_page = st.sidebar.text_input(
    "Search",
    placeholder="Search pages...",
    key="sidebar_search"
)


# NAVIGATION PAGES AND ICONS

pages = [
    ("Home", ":material/home:"),
    ("Upload Dataset", ":material/upload_file:"),
    ("Data Overview", ":material/analytics:"),
    ("Data Cleaning", ":material/cleaning_services:"),
    ("Data Filtering", ":material/filter_alt:"),
    ("Analytics Dashboard", ":material/dashboard:"),
    ("Dashboard Templates", ":material/dashboard_customize:"),
    ("Auto Dashboard", ":material/auto_awesome:"),
    ("Power BI Reports", ":material/monitoring:"),
    ("Insights", ":material/lightbulb:"),
    ("Download Reports", ":material/download:"),
    ("About", ":material/info:")
]


# SEARCH FILTER

if search_page:
    visible_pages = [
        item for item in pages
        if search_page.lower() in item[0].lower()
    ]
else:
    visible_pages = pages


# MENU HEADING

st.sidebar.markdown("""
<div class="sidebar-section-title">
    MAIN MENU
</div>
""", unsafe_allow_html=True)


# NAVIGATION BUTTONS

for page_name, page_icon in visible_pages:

    is_active = (
        st.session_state.current_page == page_name
    )

    if st.sidebar.button(
        page_name,
        key=f"nav_{page_name}",
        icon=page_icon,
        type="primary" if is_active else "secondary",
        use_container_width=True
    ):
        st.session_state.current_page = page_name
        st.rerun()


# GET CURRENT PAGE

page = st.session_state.current_page


# DIVIDER

st.sidebar.markdown("---")


# WORKSPACE CARD

st.sidebar.markdown("""
<div class="workspace-card">
    <p class="workspace-label">YOUR WORKSPACE</p>
    <h3>Universal BI Platform</h3>
    <p>Smart Data Analytics</p>
</div>
""", unsafe_allow_html=True)


# FOOTER

st.sidebar.markdown("""
<div class="sidebar-footer">
    POWERED BY STREAMLIT
</div>
""", unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.markdown("""
<div class="home-hero">
<h1 style="color:#FBF7F4 !important; font-size:38px; margin-bottom:15px;">
Universal Data Analytics Platform
</h1>
<p class="hero-subtitle" style="font-size:20px;">
Transform raw data into meaningful insights.
</p>
<p class="hero-description" style="font-size:16px;">
Upload, clean, analyze, and visualize your datasets
using one integrated analytics platform.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("## Platform Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
<div style="background:white;padding:28px;border-radius:16px;
border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(23,37,84,0.06);
min-height:190px;">
<p style="font-size:13px;color:#B98F88;font-weight:bold;">STEP 01</p>
<h3 style="color:#172554;">Upload Dataset</h3>
<p style="color:#64748B;font-size:16px;">
Import CSV and Excel files and begin exploring your data.
</p>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div style="background:white;padding:28px;border-radius:16px;
border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(23,37,84,0.06);
min-height:190px;">
<p style="font-size:13px;color:#B98F88;font-weight:bold;">STEP 02</p>
<h3 style="color:#172554;">Clean & Prepare</h3>
<p style="color:#64748B;font-size:16px;">
Handle missing values, remove duplicates, and prepare your dataset.
</p>
</div>
""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<div style="background:white;padding:28px;border-radius:16px;
border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(23,37,84,0.06);
min-height:190px;">
<p style="font-size:13px;color:#B98F88;font-weight:bold;">STEP 03</p>
<h3 style="color:#172554;">Analyze & Visualize</h3>
<p style="color:#64748B;font-size:16px;">
Discover patterns using interactive charts and statistical insights.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div style="background:white;padding:32px;border-radius:16px;
border:1px solid #E8D8CE;border-left:5px solid #7A6258;
box-shadow:0 6px 20px rgba(23,37,84,0.04);">
<h2 style="color:#3B2F2A;">Getting Started</h2>
<p style="color:#7A6258;font-size:16px;line-height:1.8;">
Begin by selecting <b>Upload Dataset</b> from the sidebar.
Upload a CSV or Excel file to explore your data, perform cleaning
operations, create visualizations, and download your results.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div style="background:white;padding:30px;border-radius:16px;
border:1px solid #E2E8F0;box-shadow:0 6px 20px rgba(23,37,84,0.04);">
<h2 style="color:#172554;">Supported Dataset Formats</h2>
<p style="color:#64748B;font-size:16px;line-height:1.8;">
CSV files (.csv) and Excel files (.xlsx)
</p>
<p style="color:#64748B;font-size:15px;">
Upload your dataset to begin your analysis workflow.
</p>
</div>
""", unsafe_allow_html=True)
    
# Upload Dataset page
elif page == "Upload Dataset":

    st.markdown("""
    <div style="margin-bottom:25px;">
        <h1 style="color:#172554;font-size:36px;">
            Upload Your Dataset
        </h1>
        <p style="color:#64748B;font-size:17px;">
            Import your data and begin exploring, cleaning, and analyzing it.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="background:white;padding:30px;border-radius:16px;border:1px solid #E2E8F0;box-shadow:0 5px 18px rgba(23,37,84,0.05);">
<h2 style="color:#172554;">Upload Data</h2>
<p style="color:#64748B;font-size:16px;">Select a dataset from your computer to get started.</p>
<p style="color:#64748B;font-size:14px;">Supported formats: CSV (.csv) and Excel (.xlsx)</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a dataset",
        type=["csv", "xlsx"],
        help="Upload a CSV or Excel file."
    )

    if uploaded_file is not None:

        try:

            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.session_state.data = df.copy()
            st.session_state.original_data = df.copy()

            st.success("Dataset uploaded successfully!")

            st.markdown("### File Information")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Rows", df.shape[0])

            with col2:
                st.metric("Total Columns", df.shape[1])

            with col3:
                st.metric(
                    "Missing Values",
                    int(df.isnull().sum().sum())
                )

            st.markdown("### Dataset Preview")

            st.dataframe(
                df.head(10),
                use_container_width=True
            )

            st.markdown("### Dataset Details")

            st.write("**File Name:**", uploaded_file.name)

            st.write(
                "**File Size:**",
                f"{uploaded_file.size / 1024:.2f} KB"
            )

            st.markdown(
                """
                <div style="
                    background-color: #F3E8E0;
                    color: #3B2F2A;
                    padding: 18px 22px;
                    border: 1px solid #D8C4AC;
                    border-left: 5px solid #B98F88;
                    border-radius: 10px;
                    font-size: 16px;
                    margin-top: 15px;
                ">
                    Your dataset is ready. Navigate to Data Overview
                    or Analytics Dashboard to continue.
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:

            st.error(f"Error reading file: {e}")
    # Data Filtering Page
elif page == "Data Filtering":

    st.title("Interactive Data Filtering")
    st.write(
        "Filter your dataset using categorical values "
        "or numerical ranges."
    )

    if st.session_state.data is not None:

        df = st.session_state.data

        st.subheader("Filter Your Dataset")

        selected_column = st.selectbox(
            "Select a column to filter",
            df.columns.tolist()
        )

        # Check whether the selected column is numerical
        if pd.api.types.is_numeric_dtype(df[selected_column]):

            st.write("This is a numerical column.")

            min_value = float(df[selected_column].min())
            max_value = float(df[selected_column].max())

            range_values = st.slider(
                "Select numerical range",
                min_value=min_value,
                max_value=max_value,
                value=(min_value, max_value)
            )

            if st.button("Apply Numerical Filter"):

                filtered_df = df[
                    (df[selected_column] >= range_values[0]) &
                    (df[selected_column] <= range_values[1])
                ]

                st.session_state.data = filtered_df.copy()

                st.success("Numerical filter applied successfully!")

                st.subheader("Filtered Dataset")

                st.dataframe(
                    filtered_df,
                    use_container_width=True
                )

                st.metric(
                    "Filtered Rows",
                    filtered_df.shape[0]
                )

                st.download_button(
                    "Download Filtered Dataset",
                    filtered_df.to_csv(index=False),
                    "filtered_dataset.csv",
                    "text/csv"
                )

        else:

            st.write("This is a categorical column.")

            unique_values = (
                df[selected_column]
                .dropna()
                .unique()
                .tolist()
            )

            selected_values = st.multiselect(
                "Select values to keep",
                unique_values,
                default=unique_values
            )

            if st.button("Apply Categorical Filter"):

                filtered_df = df[
                    df[selected_column].isin(selected_values)
                ]

                st.session_state.data = filtered_df.copy()

                st.success("Categorical filter applied successfully!")

                st.subheader("Filtered Dataset")

                st.dataframe(
                    filtered_df,
                    use_container_width=True
                )

                st.metric(
                    "Filtered Rows",
                    filtered_df.shape[0]
                )

                st.download_button(
                    "Download Filtered Dataset",
                    filtered_df.to_csv(index=False),
                    "filtered_dataset.csv",
                    "text/csv"
                )

        if st.button("Reset Dataset"):

            st.session_state.data = (
                st.session_state.original_data.copy()
            )

            st.success("Dataset reset successfully!")
            st.rerun()

    else:

        st.warning(
            "Please upload a dataset first from the Upload Dataset page."
        )
# Data Overview
elif page == "Data Overview":

    st.title("Dataset Overview")

    if st.session_state.data is not None:

        df = st.session_state.data

        # Dataset metrics
        total_rows = df.shape[0]
        total_columns = df.shape[1]
        missing_values = int(df.isnull().sum().sum())
        duplicate_rows = int(df.duplicated().sum())

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        categorical_columns = df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

          # Metric cards
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""<div style="background:white;padding:20px;border-radius:12px;
                border:1px solid #E2E8F0;text-align:center;">
                <div style="font-size:28px; color:#7A6258;">▦</div>
                <p>Total Rows</p><h2>{total_rows}</h2></div>""",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""<div style="background:white;padding:20px;border-radius:12px;
                border:1px solid #E2E8F0;text-align:center;">
                <div style="font-size:28px; color:#7A6258;">!</div>
                <p>Total Columns</p><h2>{total_columns}</h2></div>""",
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""<div style="background:white;padding:20px;border-radius:12px;
                border:1px solid #E2E8F0;text-align:center;">
                <div style="font-size:28px; color:#7A6258;">⧉</div>
                <p>Missing Values</p><h2>{missing_values}</h2></div>""",
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                f"""<div style="background:white;padding:20px;border-radius:12px;
                border:1px solid #E2E8F0;text-align:center;">
                <div style="font-size:28px; color:#7A6258;">≋</div>
                <p>Duplicate Rows</p><h2>{duplicate_rows}</h2></div>""",
                unsafe_allow_html=True
            )
        # Column information
        st.subheader("Column Information")

        column_info = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Non-Null Values": df.notnull().sum().values,
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            column_info,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Column Name": st.column_config.TextColumn(
                    "Column Name",
                    help="Name of the dataset column"
                ),
                "Data Type": st.column_config.TextColumn(
                    "Data Type"
                ),
                "Non-Null Values": st.column_config.NumberColumn(
                    "Non-Null Values"
                ),
                "Missing Values": st.column_config.NumberColumn(
                    "Missing Values"
                ),
                "Unique Values": st.column_config.NumberColumn(
                    "Unique Values"
                )
            }
        )

        # Dataset types
        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Numerical Columns")

            st.write(numerical_columns)

            st.metric(
                "Numerical Column Count",
                len(numerical_columns)
            )

        with col2:

            st.subheader("Categorical Columns")

            st.write(categorical_columns)

            st.metric(
                "Categorical Column Count",
                len(categorical_columns)
            )

        st.divider()

        # Missing values analysis
        st.subheader("Missing Values Analysis")

        missing_data = df.isnull().sum()

        missing_data = missing_data[
            missing_data > 0
        ].sort_values(ascending=False)

        if len(missing_data) > 0:

            missing_df = missing_data.reset_index()

            missing_df.columns = [
                "Column",
                "Missing Values"
            ]

            st.dataframe(
                missing_df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.success("No missing values detected!")

        st.divider()

        # Statistical summary
        st.subheader("Statistical Summary")

        summary_df = df.describe(include="all").T

        summary_styled = summary_df.style.format(precision=2, thousands=',', na_rep='?').set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", "#E8D8CE"),
                    ("color", "#3B2F2A"),
                    ("font-weight", "bold"),
                    ("border", "1px solid #D8C4AC"),
                    ("padding", "10px")
                ]
            },
            {
                "selector": "td",
                "props": [
                    ("background-color", "#FBF7F4"),
                    ("color", "#3B2F2A"),
                    ("border", "1px solid #E8D8CE"),
                    ("padding", "9px")
                ]
            }
        ])

        st.dataframe(
            summary_styled,
            use_container_width=True
        )

        st.divider()

        # Dataset preview
        st.subheader("Complete Dataset Preview")

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning(
            "Please upload a dataset from the Upload Dataset page first."
        )

# Other pages
# Data Cleaning
elif page == "Data Cleaning":

    st.title("Data Cleaning & Preprocessing")

    if st.session_state.data is not None:

        df = st.session_state.data

        st.subheader("Current Dataset")

        st.dataframe(df, use_container_width=True)

        st.divider()

        # Remove duplicates
        st.subheader("Remove Duplicate Rows")

        duplicate_count = int(df.duplicated().sum())

        st.write(f"Duplicate rows detected: {duplicate_count}")

        if st.button("Remove Duplicates"):

            st.session_state.data = df.drop_duplicates().reset_index(drop=True)

            st.success("Duplicate rows removed successfully!")

            st.rerun()

        st.divider()

        # Handle missing values
        st.subheader("Handle Missing Values")

        missing_count = int(df.isnull().sum().sum())

        st.write(f"Missing values detected: {missing_count}")

        missing_option = st.selectbox(
            "Choose how to handle missing values",
            [
                "Select an option",
                "Remove rows with missing values",
                "Fill numerical values with mean",
                "Fill numerical values with median",
                "Fill missing values with zero"
            ]
        )

        if st.button("Apply Missing Value Treatment"):

            cleaned_df = df.copy()

            if missing_option == "Remove rows with missing values":

                cleaned_df = cleaned_df.dropna()

            elif missing_option == "Fill numerical values with mean":

                numerical_cols = cleaned_df.select_dtypes(
                    include="number"
                ).columns

                cleaned_df[numerical_cols] = cleaned_df[
                    numerical_cols
                ].fillna(cleaned_df[numerical_cols].mean())

            elif missing_option == "Fill numerical values with median":

                numerical_cols = cleaned_df.select_dtypes(
                    include="number"
                ).columns

                cleaned_df[numerical_cols] = cleaned_df[
                    numerical_cols
                ].fillna(cleaned_df[numerical_cols].median())

            elif missing_option == "Fill missing values with zero":

                cleaned_df = cleaned_df.fillna(0)

            else:

                st.warning("Please select a treatment option.")

                st.stop()

            st.session_state.data = cleaned_df.reset_index(drop=True)

            st.success("Missing value treatment applied!")

            st.rerun()

        st.divider()

        # Remove columns
        st.subheader("Remove Unwanted Columns")

        columns_to_remove = st.multiselect(
            "Select columns to remove",
            df.columns.tolist()
        )

        if st.button("Remove Selected Columns"):

            if columns_to_remove:

                st.session_state.data = df.drop(
                    columns=columns_to_remove
                )

                st.success("Selected columns removed!")

                st.rerun()

            else:

                st.warning("Please select at least one column.")

        st.divider()

        # Rename columns
        st.subheader("Rename Columns")

        column_to_rename = st.selectbox(
            "Select column",
            df.columns.tolist(),
            key="rename_column"
        )

        new_column_name = st.text_input(
            "Enter new column name"
        )

        if st.button("Rename Column"):

            if new_column_name.strip():

                if new_column_name in df.columns and new_column_name != column_to_rename:

                    st.error("A column with that name already exists.")

                else:

                    st.session_state.data = df.rename(
                        columns={
                            column_to_rename: new_column_name.strip()
                        }
                    )

                    st.success("Column renamed successfully!")

                    st.rerun()

            else:

                st.warning("Please enter a valid column name.")

        st.divider()

        # Reset dataset
        st.subheader("Reset Dataset")

        if st.button("Reset to Original Dataset"):

            if st.session_state.original_data is not None:

                st.session_state.data = (
                    st.session_state.original_data.copy()
                )

                st.success("Dataset restored to original version!")

                st.rerun()

    else:

        st.warning("Please upload a dataset first.")

# Analytics Dashboard
elif page == "Analytics Dashboard":

    import plotly.express as px

    st.title("Interactive Analytics Dashboard")

    if st.session_state.data is not None:

        df = st.session_state.data
                # Dashboard KPI Cards
        total_records = df.shape[0]
        total_columns = df.shape[1]
        missing_values = df.isnull().sum().sum()
        duplicate_rows = df.duplicated().sum()

        st.subheader("Dataset Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="Total Records",
                value=f"{total_records:,}"
            )

        with col2:
            st.metric(
                label="Total Columns",
                value=total_columns
            )

        with col3:
            st.metric(
                label="Missing Values",
                value=f"{missing_values:,}"
            )

        with col4:
            st.metric(
                label="Duplicate Rows",
                value=f"{duplicate_rows:,}"
            )

        st.divider()

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        categorical_columns = df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        all_columns = df.columns.tolist()

        chart_type = st.selectbox(
            "Select Chart Type",
            [
                "Bar Chart",
                "Line Chart",
                "Pie Chart",
                "Scatter Plot",
                "Histogram",
                "Box Plot"
            ]
        )

        chart_title = st.text_input(
            "Chart Title",
            value="My Analytics Chart"
        )

        fig = None

        if chart_type == "Bar Chart":

            x_column = st.selectbox(
                "Category / X-axis",
                all_columns
            )

            if numerical_columns:

                y_column = st.selectbox(
                    "Numerical / Y-axis",
                    numerical_columns
                )

                aggregation = st.selectbox(
                    "Aggregation",
                    ["Sum", "Average", "Count", "Maximum", "Minimum"]
                )

                if st.button("Generate Chart"):

                    if aggregation == "Sum":
                        chart_data = df.groupby(x_column)[y_column].sum()

                    elif aggregation == "Average":
                        chart_data = df.groupby(x_column)[y_column].mean()

                    elif aggregation == "Count":
                        chart_data = df.groupby(x_column)[y_column].count()

                    elif aggregation == "Maximum":
                        chart_data = df.groupby(x_column)[y_column].max()

                    else:
                        chart_data = df.groupby(x_column)[y_column].min()

                    chart_data = chart_data.reset_index()

                    fig = px.bar(
                        chart_data,
                        x=x_column,
                        y=y_column,
                        title=chart_title
                    )

            else:

                st.warning(
                    "This dataset has no numerical columns for a bar chart."
                )

        elif chart_type == "Line Chart":

            if numerical_columns:

                x_column = st.selectbox(
                    "X-axis",
                    all_columns
                )

                y_column = st.selectbox(
                    "Y-axis",
                    numerical_columns
                )

                if st.button("Generate Chart"):

                    fig = px.line(
                    df,
                    x=x_column,
                    y=y_column,
                    title=chart_title,
                    color_discrete_sequence=["#7A6258"]
                )

            else:

                st.warning(
                    "A line chart requires a numerical column."
                )

        elif chart_type == "Pie Chart":

            category_column = st.selectbox(
                "Select Category",
                all_columns
            )

            if st.button("Generate Chart"):

                pie_data = df[
                    category_column
                ].value_counts().reset_index()

                pie_data.columns = [
                    category_column,
                    "Count"
                ]

                fig = px.pie(
                    pie_data,
                    names=category_column,
                    values="Count",
                    title=chart_title
                )

        elif chart_type == "Scatter Plot":

            if len(numerical_columns) >= 2:

                x_column = st.selectbox(
                    "X-axis",
                    numerical_columns
                )

                y_column = st.selectbox(
                    "Y-axis",
                    numerical_columns,
                    index=1
                )

                if st.button("Generate Chart"):

                    fig = px.scatter(
                        df,
                        x=x_column,
                        y=y_column,
                        title=chart_title
                    )

            else:

                st.warning(
                    "Scatter plots require at least two numerical columns."
                )

        elif chart_type == "Histogram":

            if numerical_columns:

                selected_column = st.selectbox(
                    "Select Numerical Column",
                    numerical_columns
                )

                if st.button("Generate Chart"):

                    fig = px.histogram(
                        df,
                        x=selected_column,
                        title=chart_title
                    )

            else:

                st.warning(
                    "Histograms require a numerical column."
                )

        elif chart_type == "Box Plot":

            if numerical_columns:

                y_column = st.selectbox(
                    "Select Numerical Column",
                    numerical_columns
                )

                x_column = st.selectbox(
                    "Group By (Optional)",
                    ["None"] + categorical_columns
                )

                if st.button("Generate Chart"):

                    if x_column == "None":

                        fig = px.box(
                            df,
                            y=y_column,
                            title=chart_title
                        )

                    else:

                        fig = px.box(
                            df,
                            x=x_column,
                            y=y_column,
                            title=chart_title
                        )

            else:

                st.warning(
                    "Box plots require a numerical column."
                )

        if fig is not None:
            chart_palette = [
                "#7A6258",
                "#B98F88",
                "#D8C4AC",
                "#A78D78",
                "#3B2F2A"
            ]

            for trace_index, trace in enumerate(fig.data):
                if trace.type == "pie":
                    trace.marker.colors = chart_palette
                elif hasattr(trace, "marker"):
                    trace.marker.color = chart_palette[trace_index % len(chart_palette)]

            fig.update_layout(
                template="plotly_white",
                colorway=[
                    "#7A6258",
                    "#B98F88",
                    "#D8C4AC",
                    "#A78D78",
                    "#3B2F2A"
                ],
                font=dict(
                    family="Times New Roman",
                    size=14,
                    color="#3B2F2A"
                ),
                title_font=dict(
                    family="Times New Roman",
                    size=22,
                    color="#3B2F2A"
                ),
                paper_bgcolor="#FBF7F4",
                plot_bgcolor="#FBF7F4",
                xaxis=dict(gridcolor="#E8D8CE", zerolinecolor="#D8C4AC"),
                yaxis=dict(gridcolor="#E8D8CE", zerolinecolor="#D8C4AC"),
                margin=dict(l=25, r=25, t=65, b=25)
            )
 
            st.plotly_chart(
                fig,
                use_container_width=True
            )

    else:

     st.warning(
            "Please upload a dataset before creating visualizations."
        )
# Dashboard Templates Gallery
elif page == "Dashboard Templates":

    st.title("Explore Dashboard Templates")

    st.write(
        "Choose a professional dashboard design. "
        "Your uploaded dataset will be used to generate the dashboard."
    )

    templates = {
        "Modern Executive": {
            "description": "A clean business dashboard with KPI cards and performance charts.",
            "theme": "Light",
            "icon": "EXECUTIVE"
        },
        "Sales Analytics": {
            "description": "Analyse sales, products, categories and revenue trends.",
            "theme": "Light",
            "icon": "SALES"
        },
        "Financial Analytics": {
            "description": "Explore income, expenses, profit and financial performance.",
            "theme": "Light",
            "icon": "FINANCE"
        },
        "HR Analytics": {
            "description": "Understand employees, departments and workforce statistics.",
            "theme": "Light",
            "icon": "HR"
        },
        "Marketing Analytics": {
            "description": "Analyse campaigns, customer data and marketing performance.",
            "theme": "Light",
            "icon": "MARKETING"
        },
        "General BI Dashboard": {
            "description": "A universal layout for exploring any type of dataset.",
            "theme": "Light",
            "icon": "GENERAL BI"
        },
        "Dark Analytics": {
            "description": "A modern dark dashboard with elegant visualizations.",
            "theme": "Dark",
            "icon": "DARK MODE"
        }
    }

    st.subheader("Available Designs")

    template_names = list(templates.keys())

    for start in range(0, len(template_names), 3):
        cols = st.columns(3)

        for index, col in enumerate(cols):
            position = start + index

            if position < len(template_names):
                name = template_names[position]
                details = templates[name]

                with col:
                    card_html = textwrap.dedent(f"""
                    <div style="
                        background-color: #E8D8CE;
                        padding: 24px;
                        border-radius: 16px;
                        border: 1px solid #D8C4AC;
                        min-height: 190px;
                        margin-bottom: 12px;
                        box-shadow: 0 5px 15px rgba(59,47,42,0.08);
                    ">
                        <h3 style="color:#3B2F2A; font-size:23px;">
                            {details['icon']}
                        </h3>
                        <p style="color:#7A6258; font-size:16px; line-height:1.6;">
                            {details['description']}
                        </p>
                        <small style="color:#7A6258; font-size:13px;">
                            {details['theme']} Theme
                        </small>
                    </div>
                    """)

                    st.markdown(card_html, unsafe_allow_html=True)

                    if st.button(
                        f"Select {name}",
                        key=f"template_{position}",
                        use_container_width=True
                    ):
                        st.session_state.selected_template = name
                        st.rerun()

    st.divider()

    if "selected_template" in st.session_state:
        st.success(
            f"Selected Template: {st.session_state.selected_template}"
        )
        st.info(
            "Your template selection is saved. "
            "Open Auto Dashboard to view your dashboard."
        )
    else:
        st.info("Select a dashboard template to continue.")


elif page == "Auto Dashboard":

    st.title("Universal BI Dashboard")
    selected_template = st.session_state.get(
    "selected_template",
    "General BI Dashboard"
)

    st.info(f"Active Dashboard Template: {selected_template}")

    st.write(
        "Automatically analyse your uploaded dataset "
        "and generate a comprehensive business intelligence overview."
    )

    if st.session_state.data is not None:

        df = st.session_state.data.copy()

        # Dataset Overview
        st.subheader("Dataset Overview")

        total_records = df.shape[0]
        total_columns = df.shape[1]
        missing_values = int(df.isnull().sum().sum())
        duplicate_rows = int(df.duplicated().sum())

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Records", f"{total_records:,}")

        with col2:
            st.metric("Total Columns", total_columns)

        with col3:
            st.metric("Missing Values", f"{missing_values:,}")

        with col4:
            st.metric("Duplicate Rows", f"{duplicate_rows:,}")

        st.divider()

        # Identify Column Types
        st.subheader("Automatic Dataset Understanding")

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        categorical_columns = df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        date_columns = []

        for column in categorical_columns:

            parsed_dates = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            valid_ratio = parsed_dates.notna().mean()

            if valid_ratio >= 0.80 and df[column].notna().any():
                date_columns.append(column)

        categorical_columns = [
            column for column in categorical_columns
            if column not in date_columns
        ]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Numerical Columns",
                len(numerical_columns)
            )

        with col2:
            st.metric(
                "Categorical Columns",
                len(categorical_columns)
            )

        with col3:
            st.metric(
                "Date Columns",
                len(date_columns)
            )

        # Display identified columns
        with st.expander("View Detected Column Categories"):

            st.write("Numerical Columns")
            st.write(numerical_columns or "None detected")

            st.write("Categorical Columns")
            st.write(categorical_columns or "None detected")

            st.write("Date Columns")
            st.write(date_columns or "None detected")

        st.divider()

        # Dataset Structure
        st.subheader("Dataset Structure")

        structure = pd.DataFrame({
            "Column Name": df.columns.astype(str),
            "Data Type": df.dtypes.astype(str).values,
            "Missing Values": df.isnull().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            structure,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        # Dataset Preview
        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(10),
            use_container_width=True
        )

        # =====================================
        # AUTOMATIC BI DASHBOARD GENERATOR
        # =====================================

        import plotly.express as px

        st.divider()

        st.header("Interactive Business Intelligence Dashboard")

        st.write(
            f"Selected Design: {selected_template}"
        )

        # Dashboard Theme

        dashboard_colors = {
    "Modern Executive": "#7A6258",
    "Sales Analytics": "#B98F88",
    "Financial Analytics": "#3B2F2A",
    "HR Analytics": "#A78D78",
    "Marketing Analytics": "#B98F88",
    "General BI Dashboard": "#7A6258",
    "Dark Analytics": "#3B2F2A"
}
        accent_color = dashboard_colors.get(
    selected_template,
    "#7A6258"
)
        # 1. KPI CARDS

        st.subheader("Key Performance Indicators")

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        with kpi1:
            st.metric("Total Records", f"{len(df):,}")

        with kpi2:
            st.metric("Total Columns", df.shape[1])

        with kpi3:
            st.metric(
                "Missing Values",
                int(df.isnull().sum().sum())
            )

        with kpi4:
            st.metric(
                "Duplicate Rows",
                int(df.duplicated().sum())
            )

        st.divider()

        # 2. NUMERICAL KPI CARDS

        st.subheader("Numerical Performance")

        if numerical_columns:

            metric_columns = st.columns(
                min(len(numerical_columns), 4)
            )

            for index, column in enumerate(numerical_columns[:4]):

                with metric_columns[index]:

                    total = df[column].sum()

                    st.metric(
                        label=f"Total {column}",
                        value=f"{total:,.2f}"
                    )

        # 3. AUTOMATIC BAR CHART

        st.divider()

        st.subheader("Category Performance")

        chart_col1, chart_col2 = st.columns(2)

        if categorical_columns and numerical_columns:

            with chart_col1:

                category = categorical_columns[0]
                numeric = numerical_columns[0]

                bar_data = (
                    df.groupby(category, dropna=False)[numeric]
                    .sum()
                    .reset_index()
                    .sort_values(numeric, ascending=False)
                    .head(10)
                )

                fig = px.bar(
                    bar_data,
                    x=category,
                    y=numeric,
                    title=f"{numeric} by {category}",
                    color_discrete_sequence=[accent_color]
                )

                fig.update_layout(
                    template="plotly_white",
                    font=dict(
                        family="Times New Roman",
                        size=14
                    )
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        elif numerical_columns:

            with chart_col1:

                fig = px.histogram(
                    df,
                    x=numerical_columns[0],
                    title="Numerical Distribution",
                    color_discrete_sequence=[accent_color]
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        # 4. AUTOMATIC PIE CHART

        if categorical_columns:

            with chart_col2:

                category = categorical_columns[
                    min(1, len(categorical_columns) - 1)
                ]

                pie_data = (
                    df[category]
                    .fillna("Missing")
                    .astype(str)
                    .value_counts()
                    .head(10)
                    .reset_index()
                )

                pie_data.columns = [category, "Count"]

                fig = px.pie(
                    pie_data,
                    names=category,
                    values="Count",
                    title=f"Distribution by {category}",
                    color_discrete_sequence=[
                        "#B98F88",
                        "#7A6258",
                        "#D8C4AC",
                        "#3B2F2A",
                        "#A78D78"
                    ]
                )

                fig.update_layout(
                    template="plotly_white"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        elif len(numerical_columns) >= 2:

            with chart_col2:

                fig = px.scatter(
                    df,
                    x=numerical_columns[0],
                    y=numerical_columns[1],
                    title="Numerical Relationship"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        # 5. NUMERICAL DISTRIBUTION

        if numerical_columns:

            st.divider()

            st.subheader("Numerical Data Analysis")

            selected_numeric = st.selectbox(
                "Choose a numerical column",
                numerical_columns,
                key="bi_numeric_column"
            )

            fig = px.histogram(
                df,
                x=selected_numeric,
                title=f"Distribution of {selected_numeric}",
                color_discrete_sequence=[accent_color]
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # 6. SCATTER PLOT

        if len(numerical_columns) >= 2:

            st.divider()

            st.subheader("Relationship Analysis")

            scatter_col1, scatter_col2 = st.columns(2)

            with scatter_col1:

                x_axis = st.selectbox(
                    "Select X-axis",
                    numerical_columns,
                    key="bi_scatter_x"
                )

            with scatter_col2:

                y_axis = st.selectbox(
                    "Select Y-axis",
                    numerical_columns,
                    index=1,
                    key="bi_scatter_y"
                )

            fig = px.scatter(
                df,
                x=x_axis,
                y=y_axis,
                title=f"{x_axis} vs {y_axis}",
                color_discrete_sequence=[accent_color]
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # 7. CORRELATION HEATMAP

        if len(numerical_columns) >= 2:

            st.divider()

            st.subheader("Correlation Analysis")

            correlation = df[numerical_columns].corr()

            fig = px.imshow(
                correlation,
                text_auto=True,
                title="Numerical Correlation Heatmap",
                color_continuous_scale=["#FBF7F4", "#E8D8CE", "#B98F88", "#7A6258", "#3B2F2A"]
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # 8. DATA SUMMARY

        st.divider()

        st.subheader("Statistical Summary")

        if numerical_columns:

            st.dataframe(
                df[numerical_columns].describe().T,
                use_container_width=True
            )

        st.success(
            "Your automatic BI dashboard has been generated successfully!"
        )
        
    else:

        st.warning(
            "Please upload a dataset first from the Upload Dataset page."
        )     
# Automated Insights
elif page == "Insights":

    st.title("Automated Data Insights")

    if st.session_state.data is not None:

        df = st.session_state.data

        st.write(
            "Explore automatically generated statistical "
            "observations about your dataset."
        )

        # Dataset quality
        st.subheader("Dataset Quality")

        total_missing = int(df.isnull().sum().sum())
        total_duplicates = int(df.duplicated().sum())

        col1, col2 = st.columns(2)

        col1.metric("Missing Values", total_missing)
        col2.metric("Duplicate Rows", total_duplicates)

        if total_missing == 0:
            st.success("No missing values detected.")

        else:
            st.warning(
                f"Your dataset contains {total_missing} missing values."
            )

        if total_duplicates == 0:
            st.success("No duplicate rows detected.")

        else:
            st.warning(
                f"Your dataset contains {total_duplicates} duplicate rows."
            )

        st.divider()

        # Numerical insights
        st.subheader("Numerical Insights")

        numerical_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        if numerical_columns:

            selected_column = st.selectbox(
                "Select a numerical column",
                numerical_columns
            )

            series = df[selected_column].dropna()

            if not series.empty:

                # DataSphere Numerical Insights Styling
                st.markdown("""
                    <style>
                    [data-testid="stMetricValue"] {
                        font-size: clamp(1.2rem, 2vw, 1.7rem) !important;
                        white-space: nowrap !important;
                        overflow: visible !important;
                        text-overflow: clip !important;
                    }

                    [data-testid="stMetric"] {
                        background: #FFFFFF;
                        border: 1px solid #E8D8CE;
                        border-radius: 16px;
                        padding: 18px 14px;
                        box-shadow: 0 4px 14px rgba(59, 47, 42, 0.06);
                    }
                    </style>
                """, unsafe_allow_html=True)

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "Average",
                    f"{series.mean():,.2f}"
                )

                col2.metric(
                    "Median",
                    f"{series.median():,.2f}"
                )

                col3.metric(
                    "Minimum",
                    f"{series.min():,.2f}"
                )

                col4.metric(
                    "Maximum",
                    f"{series.max():,.2f}"
                )

                st.markdown(f"""
                    <div style="
                        background:#F3E8E0;
                        border:1px solid #D8C4AC;
                        border-left:5px solid #B98F88;
                        border-radius:9px;
                        padding:15px 20px;
                        margin-top:18px;
                        color:#3B2F2A;
                        font-family:'Times New Roman',serif;
                        font-size:17px;">
                        The highest value in <b>{selected_column}</b>
                        is <b>{series.max():,.2f}</b>.
                    </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                    <div style="
                        background:#F3E8E0;
                        border:1px solid #D8C4AC;
                        border-left:5px solid #B98F88;
                        border-radius:9px;
                        padding:15px 20px;
                        margin-top:14px;
                        color:#3B2F2A;
                        font-family:'Times New Roman',serif;
                        font-size:17px;">
                        The lowest value in <b>{selected_column}</b>
                        is <b>{series.min():,.2f}</b>.
                    </div>
                """, unsafe_allow_html=True)

        else:

            st.info(
                "No numerical columns are available for analysis."
            )

        st.divider()

        # Categorical insights
        st.subheader("Categorical Insights")

        categorical_columns = df.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        if categorical_columns:

            selected_category = st.selectbox(
                "Select a categorical column",
                categorical_columns
            )

            category_counts = df[
                selected_category
            ].value_counts(dropna=False)

            if not category_counts.empty:

                st.write(
                    "Most frequent category:",
                    category_counts.index[0]
                )

                st.write(
                    "Frequency:",
                    category_counts.iloc[0]
                )

                # DataSphere Categorical Insights Chart
                category_chart_data = (
                    category_counts
                    .rename_axis(selected_category)
                    .reset_index(name="Count")
                )

                fig = px.bar(
                    category_chart_data,
                    x=selected_category,
                    y="Count",
                    title=f"Distribution by {selected_category}",
                    color_discrete_sequence=[
                        "#7A6258",
                        "#B98F88",
                        "#D8C4AC",
                        "#3B2F2A",
                        "#A78D78"
                    ],
                    text="Count"
                )

                fig.update_traces(
                    textposition="outside",
                    marker_line_color="#FBF7F4",
                    marker_line_width=1
                )

                fig.update_layout(
                    font_family="Times New Roman",
                    font_color="#3B2F2A",
                    paper_bgcolor="#FBF7F4",
                    plot_bgcolor="#FBF7F4",
                    title_font_color="#3B2F2A",
                    xaxis_title=selected_category,
                    yaxis_title="Count",
                    showlegend=False
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        else:

            st.info(
                "No categorical columns are available."
            )

        st.divider()

        # Correlation analysis
        st.subheader("Correlation Analysis")

        if len(numerical_columns) >= 2:

            correlation = df[
                numerical_columns
            ].corr()

            st.markdown("#### Correlation Heatmap")

            fig = px.imshow(
                correlation,
                text_auto=".3f",
                aspect="auto",
                color_continuous_scale=[
                    "#FBF7F4",
                    "#E8D8CE",
                    "#B98F88",
                    "#7A6258",
                    "#3B2F2A"
                ],
                zmin=-1,
                zmax=1,
                title="Numerical Variable Correlations"
            )

            fig.update_layout(
                font_family="Times New Roman",
                font_color="#3B2F2A",
                paper_bgcolor="#FBF7F4",
                plot_bgcolor="#FBF7F4",
                title_font_color="#3B2F2A",
                coloraxis_colorbar_title="Correlation",
                margin=dict(l=50, r=50, t=60, b=50)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            with st.expander("View Correlation Values"):
                st.dataframe(
                    correlation.style.format("{:.2f}"),
                    use_container_width=True
                )

        else:

            st.info(
                "At least two numerical columns are required "
                "for correlation analysis."
            )

    else:

        st.warning(
            "Please upload a dataset before generating insights."
        )

# Download Reports
elif page == "Download Reports":

    import io

    st.title("Download Data & Reports")

    if st.session_state.data is not None:

        df = st.session_state.data

        st.write(
            "Download your processed dataset and statistical reports."
        )

        st.subheader("Current Dataset")

        st.write(f"Rows: {df.shape[0]}")
        st.write(f"Columns: {df.shape[1]}")

        st.divider()

        # Download CSV
        st.subheader("Download Dataset as CSV")

        csv_data = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="DataSphere_Cleaned_Dataset.csv",
            mime="text/csv"
        )

        st.divider()

        # Download Excel
        st.subheader("Download Dataset as Excel")

        excel_buffer = io.BytesIO()

        with pd.ExcelWriter(
            excel_buffer,
            engine="openpyxl"
        ) as writer:

            df.to_excel(
                writer,
                index=False,
                sheet_name="Cleaned Data"
            )

            from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
            from datetime import datetime

            worksheet = writer.sheets["Cleaned Data"]

            # Add DataSphere branding above the dataset
            worksheet.insert_rows(1, 3)

            worksheet.merge_cells(
                start_row=1,
                start_column=1,
                end_row=1,
                end_column=max(len(df.columns), 1)
            )

            title_cell = worksheet.cell(row=1, column=1)
            title_cell.value = "DATASPHERE | DATA ANALYTICS PLATFORM"
            title_cell.font = Font(
                name="Times New Roman",
                size=18,
                bold=True,
                color="FBF7F4"
            )
            title_cell.fill = PatternFill(
                "solid",
                fgColor="3B2F2A"
            )
            title_cell.alignment = Alignment(
                horizontal="center",
                vertical="center"
            )

            worksheet.row_dimensions[1].height = 35

            worksheet.merge_cells(
                start_row=2,
                start_column=1,
                end_row=2,
                end_column=max(len(df.columns), 1)
            )

            subtitle_cell = worksheet.cell(row=2, column=1)
            subtitle_cell.value = (
                f"Generated on: {datetime.now().strftime('%d %B %Y, %I:%M %p')}"
            )
            subtitle_cell.font = Font(
                name="Times New Roman",
                size=11,
                italic=True,
                color="7A6258"
            )
            subtitle_cell.alignment = Alignment(horizontal="center")

            # Style dataset column headers
            header_fill = PatternFill("solid", fgColor="3B2F2A")
            header_font = Font(
                name="Times New Roman",
                bold=True,
                color="FFFFFF",
                size=11
            )

            for cell in worksheet[4]:
                cell.fill = header_fill
                cell.font = header_font
                cell.alignment = Alignment(
                    horizontal="center",
                    vertical="center",
                    wrap_text=True
                )

            worksheet.row_dimensions[4].height = 25

            # Style dataset rows
            cream_fill = PatternFill("solid", fgColor="FBF7F4")
            blush_fill = PatternFill("solid", fgColor="F3E8E0")
            thin_border = Border(
                bottom=Side(style="thin", color="D8C4AC")
            )

            for row in worksheet.iter_rows(
                min_row=5,
                max_row=worksheet.max_row
            ):
                for cell in row:
                    cell.font = Font(
                        name="Times New Roman",
                        size=10,
                        color="3B2F2A"
                    )
                    cell.fill = cream_fill if cell.row % 2 else blush_fill
                    cell.border = thin_border
                    cell.alignment = Alignment(vertical="center")

            # Adjust column widths
            from openpyxl.utils import get_column_letter

            for column_index in range(1, len(df.columns) + 1):
                column_letter = get_column_letter(column_index)

                max_length = max(
                    (
                        len(str(worksheet.cell(row=row_index, column=column_index).value))
                        if worksheet.cell(row=row_index, column=column_index).value is not None
                        else 0
                    )
                    for row_index in range(4, worksheet.max_row + 1)
                )

                worksheet.column_dimensions[column_letter].width = min(
                    max(max_length + 4, 14),
                    35
                )

            # Enable filters and freeze dataset headers
            last_column = get_column_letter(len(df.columns))
            worksheet.auto_filter.ref = f"A4:{last_column}{worksheet.max_row}"
            worksheet.freeze_panes = "A5"


        excel_data = excel_buffer.getvalue()

        st.download_button(
            label="Download Excel",
            data=excel_data,
            file_name="DataSphere_Cleaned_Dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.divider()

        # Statistical summary
        st.subheader("Download Statistical Summary")

        summary = df.describe(include="all").T

        summary_csv = summary.to_csv(index_label="Column").encode("utf-8")

        st.download_button(
            label="Download Statistical Summary",
            data=summary_csv,
            file_name="DataSphere_Statistical_Summary.csv",
            mime="text/csv"
        )

        st.divider()

        # Text report
        st.subheader("Download Analysis Report")

        report = f"""
DATASPHERE | DATA ANALYTICS REPORT
Universal Data Analytics Platform
Generated on: {pd.Timestamp.now().strftime("%d %B %Y, %I:%M %p")}

Dataset Overview
----------------
Total Rows: {df.shape[0]}
Total Columns: {df.shape[1]}
Missing Values: {int(df.isnull().sum().sum())}
Duplicate Rows: {int(df.duplicated().sum())}

Numerical Columns
----------------
{df.select_dtypes(include="number").columns.tolist()}

Categorical Columns
------------------
{df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()}

Statistical Summary
-------------------
{df.describe(include="all").to_string()}
"""

        st.download_button(
            label="Download Analysis Report",
            data=report,
            file_name="DataSphere_Analysis_Report.txt",
            mime="text/plain"
        )
        st.divider()

        # PDF Analytics Report
        st.subheader("Download Professional PDF Report")

        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            Table,
            TableStyle,
            KeepTogether
        )
        from datetime import datetime

        if st.button("Generate PDF Report"):

            pdf_buffer = io.BytesIO()

            pdf = SimpleDocTemplate(
                pdf_buffer,
                pagesize=A4,
                rightMargin=40,
                leftMargin=40,
                topMargin=40,
                bottomMargin=40
            )

            # Register Times New Roman fonts
            pdfmetrics.registerFont(TTFont(
                "TimesNewRoman",
                r"C:\Windows\Fonts\times.ttf"
            ))
            pdfmetrics.registerFont(TTFont(
                "TimesNewRoman-Bold",
                r"C:\Windows\Fonts\timesbd.ttf"
            ))
            pdfmetrics.registerFont(TTFont(
                "TimesNewRoman-Italic",
                r"C:\Windows\Fonts\timesi.ttf"
            ))

            styles = getSampleStyleSheet()

            # DataSphere PDF Theme
            styles["Title"].textColor = colors.HexColor("#3B2F2A")
            styles["Title"].fontName = "TimesNewRoman-Bold"
            styles["Title"].fontSize = 23
            styles["Title"].leading = 28

            styles["Heading2"].textColor = colors.HexColor("#7A6258")
            styles["Heading2"].fontName = "TimesNewRoman-Bold"
            styles["Heading2"].fontSize = 14

            styles["Normal"].fontName = "TimesNewRoman"
            styles["Normal"].textColor = colors.HexColor("#3B2F2A")

            story = []

            # Report Title
            story.append(
                Paragraph(
                    "DATASPHERE | DATA ANALYTICS REPORT",
                    styles["Title"]
                )
            )

            story.append(Spacer(1, 15))

            story.append(
                Paragraph(
                    f"Generated on: {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
                    styles["Normal"]
                )
            )

            story.append(Spacer(1, 20))

            # Dataset Overview
            story.append(
                Paragraph("1. Dataset Overview", styles["Heading2"])
            )

            overview_data = [
                ["Metric", "Value"],
                ["Total Records", str(df.shape[0])],
                ["Total Columns", str(df.shape[1])],
                ["Missing Values", str(int(df.isnull().sum().sum()))],
                ["Duplicate Rows", str(int(df.duplicated().sum()))]
            ]

            overview_table = Table(
                overview_data,
                colWidths=[220, 220]
            )

            overview_table.setStyle(
                TableStyle([
                        ("FONTNAME", (0, 0), (-1, -1), "TimesNewRoman"),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#3B2F2A")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("FONTNAME", (0, 0), (-1, 0), "TimesNewRoman-Bold"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D8C4AC")),
                    ("PADDING", (0, 0), (-1, -1), 8),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#FBF7F4"))
                ])
            )

            story.append(overview_table)
            story.append(Spacer(1, 20))

            # Column Information
            story.append(
                Paragraph("2. Column Information", styles["Heading2"])
            )

            numerical_cols = df.select_dtypes(
                include="number"
            ).columns.tolist()

            categorical_cols = df.select_dtypes(
                include=["object", "category", "bool"]
            ).columns.tolist()

            story.append(
                Paragraph(
                    f"Numerical Columns: {', '.join(map(str, numerical_cols)) or 'None'}",
                    styles["Normal"]
                )
            )

            story.append(Spacer(1, 8))

            story.append(
                Paragraph(
                    f"Categorical Columns: {', '.join(map(str, categorical_cols)) or 'None'}",
                    styles["Normal"]
                )
            )

            story.append(Spacer(1, 20))

            # Numerical Statistics
            story.append(
                Paragraph("3. Numerical Statistical Summary", styles["Heading2"])
            )

            if numerical_cols:

                stats = df[numerical_cols].describe().round(2)

                stats_data = [
                    ["Column", "Statistic", "Value"]
                ]

                for column in numerical_cols:
                    for statistic in stats.index:
                        stats_data.append([
                            str(column),
                            str(statistic),
                            str(stats.loc[statistic, column])
                        ])

                stats_table = Table(
                    stats_data,
                    colWidths=[180, 140, 100],
                    repeatRows=1
                )

                stats_table.setStyle(
                    TableStyle([
                        ("FONTNAME", (0, 0), (-1, -1), "TimesNewRoman"),
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#3B2F2A")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("FONTNAME", (0, 0), (-1, 0), "TimesNewRoman-Bold"),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D8C4AC")),
                        ("PADDING", (0, 0), (-1, -1), 6),
                        ("FONTSIZE", (0, 0), (-1, -1), 8),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#FBF7F4"))
                    ])
                )

                story.append(stats_table)

            else:

                story.append(
                    Paragraph(
                        "No numerical columns are available.",
                        styles["Normal"]
                    )
                )

            story.append(Spacer(1, 20))

            # Categorical Summary
            story.append(
                Paragraph("4. Categorical Data Summary", styles["Heading2"])
            )

            if categorical_cols:

                for column in categorical_cols:

                    category_heading = Paragraph(
                        f"<b>{str(column)}</b>",
                        styles["Normal"]
                    )

                    frequencies = df[column].value_counts(
                        dropna=False
                    ).head(10)

                    frequency_data = [["Category", "Count"]]

                    for value, count in frequencies.items():
                        frequency_data.append([
                            str(value)[:60],
                            str(count)
                        ])

                    frequency_table = Table(
                        frequency_data,
                        colWidths=[300, 120]
                    )

                    frequency_table.setStyle(
                        TableStyle([
                        ("FONTNAME", (0, 0), (-1, -1), "TimesNewRoman"),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#3B2F2A")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("FONTNAME", (0, 0), (-1, 0), "TimesNewRoman-Bold"),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D8C4AC")),
                            ("PADDING", (0, 0), (-1, -1), 6),
                            ("FONTSIZE", (0, 0), (-1, -1), 8)
                        ])
                    )

                    story.append(
                        KeepTogether([
                            category_heading,
                            Spacer(1, 6),
                            frequency_table,
                            Spacer(1, 12)
                        ])
                    )

            else:

                story.append(
                    Paragraph(
                        "No categorical columns are available.",
                        styles["Normal"]
                    )
                )

            # DataSphere Header and Footer
            def add_page_branding(canvas, document):
                canvas.saveState()

                page_width, page_height = A4

                canvas.setFont("TimesNewRoman-Bold", 9)
                canvas.setFillColor(colors.HexColor("#7A6258"))
                canvas.drawString(40, page_height - 25, "DATASPHERE")

                canvas.setStrokeColor(colors.HexColor("#D8C4AC"))
                canvas.setLineWidth(0.7)
                canvas.line(40, page_height - 32, page_width - 40, page_height - 32)

                canvas.setFont("TimesNewRoman", 8)
                canvas.setFillColor(colors.HexColor("#7A6258"))
                canvas.drawString(40, 22, "DataSphere | Universal Data Analytics Platform")
                canvas.drawRightString(
                    page_width - 40,
                    22,
                    f"Page {document.page}"
                )

                canvas.restoreState()

            # Build PDF
            pdf.build(
                story,
                onFirstPage=add_page_branding,
                onLaterPages=add_page_branding
            )

            pdf_buffer.seek(0)

            st.success("PDF report generated successfully!")

            st.download_button(
                label="Download PDF Report",
                data=pdf_buffer.getvalue(),
                file_name="DataSphere_Analytics_Report.pdf",
                mime="application/pdf"
            )
    else:

        st.warning(
            "Please upload a dataset before downloading reports."
        )

    


elif page == "Power BI Reports":

    st.markdown(
        """
<div style="background:linear-gradient(135deg,#7A6258,#3B2F2A);padding:38px 42px;border-radius:18px;margin-bottom:30px;color:#FBF7F4;">
<div style="color:#E8D8CE;font-size:13px;letter-spacing:3px;margin-bottom:12px;">DATA ANALYTICS &amp; BUSINESS INTELLIGENCE</div>
<div style="color:#FBF7F4;font-size:36px;font-weight:bold;line-height:1.2;margin-bottom:12px;">Power BI Reports</div>
<div style="color:#F1E4DC;font-size:17px;line-height:1.6;">Build interactive business dashboards and bring your insights together in DataSphere.</div>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("## Create Your Dashboard")

    st.write(
        "Use Microsoft Power BI to import your dataset, "
        "design visualisations and create interactive reports."
    )

    with st.container(border=True):

        st.markdown("### Microsoft Power BI")

        st.write(
            "Open Power BI Service in your browser and sign in "
            "with an account that has the required access."
        )

        st.link_button(
            "Open Microsoft Power BI",
            "https://app.powerbi.com/",
            use_container_width=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## How It Works")

    st.markdown("""
<div style="display:flex;gap:18px;flex-wrap:wrap;margin-top:20px;margin-bottom:30px;">

<div style="flex:1;min-width:190px;background:#FFFFFF;border:1px solid #E8D8CE;border-radius:16px;padding:25px;box-shadow:0 5px 18px rgba(59,47,42,0.07);">
<div style="color:#B98F88;font-size:14px;font-weight:bold;letter-spacing:2px;">STEP 01</div>
<h3 style="color:#3B2F2A;margin-top:18px;">Create</h3>
<p style="color:#7A6258;line-height:1.7;">Open Power BI and upload your CSV or Excel dataset.</p>
</div>

<div style="flex:1;min-width:190px;background:#FFFFFF;border:1px solid #E8D8CE;border-radius:16px;padding:25px;box-shadow:0 5px 18px rgba(59,47,42,0.07);">
<div style="color:#B98F88;font-size:14px;font-weight:bold;letter-spacing:2px;">STEP 02</div>
<h3 style="color:#3B2F2A;margin-top:18px;">Design</h3>
<p style="color:#7A6258;line-height:1.7;">Create charts, tables, cards and interactive visualisations.</p>
</div>

<div style="flex:1;min-width:190px;background:#FFFFFF;border:1px solid #E8D8CE;border-radius:16px;padding:25px;box-shadow:0 5px 18px rgba(59,47,42,0.07);">
<div style="color:#B98F88;font-size:14px;font-weight:bold;letter-spacing:2px;">STEP 03</div>
<h3 style="color:#3B2F2A;margin-top:18px;">Publish</h3>
<p style="color:#7A6258;line-height:1.7;">Save your report and add its secure embed URL to DataSphere.</p>
</div>

</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## Your Published Dashboard")

    st.write(
        "Bring your Power BI reports into DataSphere "
        "and access your business insights in one place."
    )

    with st.container(border=True):

        st.markdown("### Connect Your Power BI Report")

        st.write(
            "Paste the embed URL of your saved Power BI report below."
        )

        powerbi_url = st.text_input(
            "Power BI Report Embed URL",
            placeholder="Paste your Power BI embed URL here...",
            key="powerbi_report_url"
        )

        if powerbi_url:

            if powerbi_url.startswith("https://app.powerbi.com/"):

                st.success("Report URL accepted.")

                st.components.v1.iframe(
                    powerbi_url,
                    height=650,
                    scrolling=True
                )

            else:
                st.warning(
                    "Please enter a valid Power BI report URL."
                )

        else:
            st.markdown("""
<div style="background:#F5EAE4;border:1px dashed #B98F88;border-radius:14px;padding:45px 20px;text-align:center;margin-top:15px;">
<div style="font-size:28px;color:#7A6258;font-weight:bold;">Dashboard Preview</div>
<p style="color:#7A6258;font-size:15px;margin-top:12px;">Your published Power BI report will appear here.</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Important Information")

    st.write(
        "Use secure embedding for private reports. "
        "Users must have the appropriate Power BI permissions "
        "and licensing to view embedded reports."
    )

elif page == "About":

    st.title("About the Project")

    st.write(
        "This project is a universal data analytics "
        "and business intelligence platform."
    )

