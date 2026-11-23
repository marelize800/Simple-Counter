import streamlit as st
from lib.db_handler import create_db, display_data,update
import time

st.session_state.price = 5


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
	.stMetric Label {
	color: #111;
	}
	.stMarkdownEllipsis {
	color: #111;
	}
	.stSidebar{
	background-color: pink
	}
	.st-key-money{
	color: blue
	}
	</style>
	''')



create_db()
data = display_data()

if len(data) <= 1:
	totals = 0
else:
	totals = 600+(data[0][2]*st.session_state.price)+(data[1][2]*st.session_state.price)+(data[2][2]*st.session_state.price)

st.title('Coffee Sales tracker v1.0')
with st.container(key='money'):
	st.subheader(f'Current Money: R {totals}')
st.divider()

# if st.button("Manage Users"):
# 	st.switch_page('pages/Configurations.py')



if len(data) <= 1:
	st.info('No users to display')
else:
	c1,c2,c3 = st.columns(3)
	with c1.container(border=True):
		if st.button('Add a cup for Francois'):
			name = 'Francois'
			qty = data[0][2]+1
			st.info(qty)
			update(name,qty)
			st.balloons()
			time.sleep(2)
			st.rerun()
		st.subheader(data[0][1])
		st.metric(label='Cups',value=data[0][2])

	with c2.container(border=True):
		if st.button('Add a cup for Andre'):
			name = 'Andre'
			qty = data[1][2]+1
			st.info(qty)
			update(name,qty)
			st.balloons()
			time.sleep(2)
			st.rerun()
		st.subheader(data[1][1])
		st.metric(label='Cups',value=data[1][2])

	with c3.container(border=True):
		if st.button('Add a cup for Marelize'):
			name = 'Marelize'
			qty = data[2][2]+1
			st.info(qty)
			update(name,qty)
			st.balloons()
			time.sleep(2)
			st.rerun()
		st.subheader(data[2][1])
		st.metric(label='Cups',value=data[2][2])