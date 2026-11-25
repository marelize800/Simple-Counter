import streamlit as st
from lib.db_handler import create_db, display_data,update
import time

st.session_state.price = 5

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
	</style>
	''', unsafe_allow_html=True)

create_db()
data = display_data()

st.title('The Coffee Club')
st.text('Every Cup Counts')
st.divider()

c1,c2 = st.columns(2)
with c1.container(border=True):
	st.subheader('Current balance')
	money = sum(row[2] for row in data)*5
	st.metric('Rand', f'R {money+220}.00')

with c2.container(border=True):
	st.subheader('Cups Served')
	total_cups = sum(row[2] for row in data)
	st.metric('Cups', f'{total_cups}')

with st.container(border=True):
	st.subheader('Savings Goal')
	goal = 1900
	c1,c2 = st.columns(2,vertical_alignment='center')
	current = sum(row[2] for row in data)*5+220
	cur = int((current/goal)*100)
	c1.subheader(f'R {current} / R {goal}')
	c2.metric('Goal %',value=cur)

st.header('Customers')
with st.container(border=True, key='customer_card_1'):
	c1,c2 = st.columns([0.6,0.4],vertical_alignment='center')
	with c1:
		st.header(data[0][1])
		st.text(f'{data[0][2]} coffees served')
	with c2:
		if st.button(f'+ Coffee {data[0][1]}'):
			name = data[0][1]
			qty = data[0][2]+1
			update(name,qty)
			st.balloons()
			time.sleep(2)
			st.rerun()


with st.container(border=True, key='customer_card_2'):
	c1,c2 = st.columns([0.6,0.4],vertical_alignment='center')
	with c1:
		st.header(data[1][1])
		st.text(f'{data[1][2]} coffees served')
	with c2:
		if st.button(f'+ Coffee {data[1][1]}'):
			name = data[1][1]
			qty = data[1][2]+1
			update(name,qty)
			st.balloons()
			time.sleep(2)
			st.rerun()

with st.container(border=True, key='customer_card_3'):
	c1,c2 = st.columns([0.6,0.4],vertical_alignment='center')
	with c1:
		st.header(data[2][1])
		st.text(f'{data[2][2]} coffees served')
	with c2:
		if st.button(f'+ Coffee {data[2][1]}'):
			name = data[2][1]
			qty = data[2][2]+1
			update(name,qty)
			st.balloons()
			time.sleep(2)
			st.rerun()
