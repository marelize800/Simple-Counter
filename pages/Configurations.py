import streamlit as st
from lib.db_handler import add_user

st.title('Nothing to see here')
# st.text('Configure pricing,quantities and more')
# st.divider()
st.markdown('''
	<style>
	.stApp{
	background-color: #211812;
	color: #e6bb83
	}
	.stButton Button{
	background-color: #503b2c;
	color: #111
	}
	.stMetric Label {
	color: #111;
	}
	.stMarkdownEllipsis {
	color: #e6bb83;
	}
	.stSidebar{
	background-color: #211812;
	color: #e6bb83
	}
	.st-key-money{
	color: blue
	}
	hr{
	border-color: #e6bb83 !important
	}
	.stContainer{
	background-color: red;
	}

	div[role="slider"]{
	background-color: blue !important;
	}
	</style>''',unsafe_allow_html=True)


# st.subheader('Add user')
# with st.expander('User Info'):
# 	with st.form('add_user',border=False):
# 		name = st.text_input('User Name:')
# 		qty = st.number_input('How Many Cups: ')
# 		if st.form_submit_button('Add User'):
# 			add_user(name,qty)
# 			st.balloons()
