import streamlit as st
import pandas as pd



# Load custom CSS
def load_css(style_file):
    css_file = os.path.join(style_file)
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
load_css('styles.css')

# Page title
st.title('Growth Mindset Challange in Streamlit')


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
    dataframe.to_csv('data/tasks.csv', index=False)

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
