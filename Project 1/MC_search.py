import pandas as pd 
import streamlit as st

# Apply Minecraft-like theme to Streamlit
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');  /* Minecraft-like font */
    
    /* Apply font to entire page */
    html, body, [class*="css"] {
        font-family: 'VT323', monospace;
    }

    /* Apply font to the title */
    .stTitle {
        font-family: 'Press Start 2P', cursive;  /* Different font for title */
        color: #f4d03f;  /* Minecraft-like color (golden yellow) */
        text-align: center; /* Optional: Center-align the title */
    }

    /* Apply font to all titles in the sidebar and main content */
    .stSubheader, .stHeader, .stSidebar .sidebar-content, .css-1d391kg {
        font-family: 'VT323', monospace;
    }

    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
        color: white;
    }

    /* Streamlit buttons and text inputs */
    .stButton>button {
        background-color: #3a3a3a;
        color: white;
        border-radius: 5px;  /* Keep button rounded (you can change this if you want square buttons) */
        font-family: 'VT323', monospace;
    }
    .stTextInput>div>div>input {
        background-color: #2d2d2d;
        color: white;
        border: 2px solid #4CAF50;
    }

    /* Titles and Subheaders */
    .stSubheader {
        font-family: 'VT323', monospace;
        color: #ffffff;  /* White color for subheaders */
    }
    
    /* Category radio button labels */
    .stRadio>div>label {
        font-family: 'VT323', monospace;
        color: #ffffff;
    }

    /* Make radio buttons square instead of circular */
    .stRadio > div > div > label > div {
        border-radius: 0 !important;  /* Make square buttons */
    }

    .stRadio > div > div > div[aria-checked="true"] {
        background-color: #3a3a3a !important;
        border-radius: 0 !important;  /* Square active button */
    }

    /* Sidebar title */
    .sidebar .sidebar-header {
        font-family: 'VT323', monospace;
        color: #f4d03f;
    }

    </style>
""", unsafe_allow_html=True)

# Load the multi-indexed DataFrame from a CSV
df = pd.read_csv("mc_items.csv", header=[0, 1])  # Adjust headers for multi-index columns if needed

# If the DataFrame has a multi-index on the columns, reset or flatten it
if isinstance(df.columns, pd.MultiIndex):
    df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]

# # Display columns to verify correct loading
# st.write("DataFrame Columns:", df.columns.tolist())

# Define the function to generate keywords
def generate_keywords(row):
    keywords = set()
    
    # Adjust for potential multi-index access
    item_name_column = 'Item Properties_Item Name'
    item_name = row[item_name_column].lower() if item_name_column in row else ""
    
    keywords.update(item_name.split())

    if "diamond" in item_name:
        keywords.update(["blue", "shiny", "precious"])
    elif "emerald" in item_name:
        keywords.update(["green", "gem", "precious"])
    elif "gold" in item_name:
        keywords.update(["yellow", "golden"])
    elif "iron" in item_name:
        keywords.update(["gray", "iron"])
    elif "grass" in item_name:
        keywords.update(["green", "natural", "plant"])
    elif "stone" in item_name:
        keywords.update(["gray", "rock", "solid"])
    elif "glass" in item_name:
        keywords.update(["transparent", "clear"])
    elif "wood" in item_name:
        keywords.update(["brown", "wooden"])
    elif "coal" in item_name:
        keywords.update(["black", "dark", "coal"])
    elif "bedrock" in item_name:
        keywords.update(["gray", "dark", "bedrock", "rock"])
    elif "redstone" in item_name:
        keywords.update(["red", "redstone"])
    elif "dirt" in item_name:
        keywords.update(["brown", "dirt", "block"])
    elif "sand" in item_name:
        keywords.update(["beige", "yellow", "sand", "block"])
    elif "crafting table" in item_name:
        keywords.update(["brown", "crafting", "craft", "table", "wooden", "block"])

    return ", ".join(keywords)

# Apply the function
df['Keywords'] = df.apply(generate_keywords, axis=1)

# Save updated dataset
df.to_csv("mc_items_keywords.csv", index=False)

# Sidebar category selection (unchanged)
st.sidebar.title("Select Category")
category = st.sidebar.radio(
    "Options",
    ["Items", "Paintings", "Entities", "Enchantments", "Structures"]
)

# Display selected category in main panel
st.title(f"Minecraft {category} Search System")

if category == "Items":
    data = pd.read_csv("mc_items_keywords.csv")
else:
    st.write(f"""Category "{category}" coming soon.""")
    data = None

# Search bar for keywords (unchanged)
keywords = st.text_input("Enter keywords (e.g., 'blue, block')").lower()

# Perform the search if keywords are entered
if keywords and data is not None:
    keyword_list = [kw.strip() for kw in keywords.split(",")]

    # Ensure Keywords column is treated as a string
    data['Keywords'] = data['Keywords'].fillna("").astype(str)

    # Filter rows based on keyword presence
    results = data[data['Keywords'].apply(lambda x: all(kw in x for kw in keyword_list))]

    # Display results
    if not results.empty:
        st.write(f"Matching {category}:")
        st.dataframe(results)
    else:
        st.write("No matching results found.")