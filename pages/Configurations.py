import streamlit as st
from lib.db_handler import add_user

st.title('Nothing to see here')
# st.text('Configure pricing,quantities and more')
# st.divider()

st.html('''
	<style>
	.stApp{
	background-color: pink;
	color: #111
	}
	.stButton Button{
	background-color: purple;
	color: #fff
	}

	.stFormSubmitButton Button{
	background-color:purple
	}

	.stMetric Label {
	color: #111;
	}
	.stMarkdownEllipsis {
	color: #111;
	}
	.stSidebar{
	background-color: pink
	}
	.stMarkdownContainer{
	color: #111
	}
	</style>
	''')


# st.subheader('Add user')
# with st.expander('User Info'):
# 	with st.form('add_user',border=False):
# 		name = st.text_input('User Name:')
# 		qty = st.number_input('How Many Cups: ')
# 		if st.form_submit_button('Add User'):
# 			add_user(name,qty)
# 			st.balloons()