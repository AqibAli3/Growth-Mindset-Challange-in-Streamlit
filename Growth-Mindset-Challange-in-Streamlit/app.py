import streamlit as st
import pandas as pd
import os

def load_css(css_file):
    css_path = os.path.join(os.path.dirname(__file__), css_file)
    print(f"Loading CSS from: {css_path}")
    try:
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        print(f"File not found: {css_path}")

load_css('styles.css')


# Initialize task list
@st.cache_data(ttl=60)
def get_data():
    try:
        return pd.read_csv('data/tasks.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Task', 'Status'])

df = get_data()

# Save DataFrame to CSV
def save_data(dataframe):
    # Create the directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    dataframe.to_csv('data/tasks.csv', index=False)
    print(f"Data saved to data/tasks.csv")

# Title and description
st.title('Task Management Application')
st.write('Organize and manage your daily tasks efficiently.')

# Add new task
st.header('Add a New Task')
new_task = st.text_input('Task:')
if st.button('Add Task'):
    if new_task:
        new_row = pd.DataFrame({'Task': [new_task], 'Status': ['Incomplete']})
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        st.success('Task added successfully!')

# Display tasks
st.header('Your Tasks')
st.write(df)

# Update task status
st.header('Update Task Status')
task_to_update = st.selectbox('Select Task', df['Task'])
new_status = st.selectbox('New Status', ['Incomplete', 'Complete'])
if st.button('Update Status'):
    df.loc[df['Task'] == task_to_update, 'Status'] = new_status
    save_data(df)
    st.success('Task status updated successfully!')

# Delete a task
st.header('Delete a Task')
task_to_delete = st.selectbox('Select Task to Delete', df['Task'])
if st.button('Delete Task'):
    df = df[df['Task'] != task_to_delete]
    save_data(df)
    st.success('Task deleted successfully!')
