from django.shortcuts import render
from .models import MasterData,CustomerReport,BillingsBacklog,PortalUtility
import xlrd
import csv
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
import xlsxwriter
import StringIO
from operator import itemgetter
from datetime import date
# Create your views here.
def create_master():
	# import pdb;pdb.set_trace()
	book = xlrd.open_workbook('media/' + 'SA Build Master Sheet.xlsx')
	# res = len(book.sheet_names())
	# print res
	# for rs in range(res):
	sheet = book.sheet_by_index(0)
	for i in range(sheet.nrows):
	    col = sheet.row_values(i)
	# for i in range(sheet.nrows):
	    if col[0] != '' and col[0]!='Utility':
			try:
				# import pdb;pdb.set_trace()
				print 'Good'
				node = MasterData()
				node.utility = col[0]
				node.customer_id = col[1]
				node.status_for_reporting = col[2]
				node.integrator = col[3]
				node.build_product = col[4]
				node.ps_engagement = col[5]
				node.transformer = col[6]
				node.energy_insight = col[7]
				node.voltage_insight = col[8]
				node.unbilled_energy = col[9]
				node.oms = col[10]
				node.sma = col[11]
				node.additional_notes = col[12]
				node.rni_new_or_migration = col[13]    
				node.time_zone = col[14]
				node.w_end_points = col[15]
				node.e_end_points = col[16]
				node.g_end_points = col[17]
				node.jira_ticket = col[18]
				node.region = col[19]
				try:
					node.project_code = int(float(col[20]))
				except:
					node.project_code = col[20]
				node.sensus_order = col[21]
				node.salesforce_case = col[22]
				node.order_date = col[23]
				node.sa_handed_to_integrator = col[24]
				node.sent_for_invoicing_on = col[25]
				node.annual_fee_trigger_date = col[26]
				node.one_time_setup_fee = col[27]
				node.year1_annual_fee = col[28]
				node.year2_annual_fee = col[29]
				node.year3_annual_fee = col[30]
				node.year4_annual_fee = col[31]
				node.year5_annual_fee = col[32]
				node.total_end_points = col[33]
				node.var = col[34]
				node.point_of_contact = col[35]
				node.point_of_contact_emails = col[36]
				node.salesperson = col[37]
				node.name_of_billing_vendor = col[38]
				node.training_fee = col[39]
				node.training_complete = col[40]
				node.time_order_to_hand_over = col[41]
				node.time_handover_to_invoice = col[42]
				node.time_order_to_invoice = col[43]
				node.time_since_order = col[44]
				node.column29 = col[45]
				node.column30 = col[46]
				node.column31 = col[47]
				node.column40 = col[48]
				node.timezone = col[49]
				node.poc_email = col[50]
				node.billing_vendor = col[51]
				node.sa_handed_over_to_integrator_date = col[52]
				node.column32 = col[53]
				node.column37 = col[54]
				node.column38 = col[55]
				node.column39 = col[56]
				node.portal_only = col[57]
				node.migration_type = col[58]
				node.save()
			except Exception,e:
				import pdb;pdb.set_trace()
				# print e

def save_customer():
	# import pdb;pdb.set_trace()
	rows = []
	with open('media/Customers_Report.csv', 'r') as csvfile: 
	# creating a csv reader object 
		csvreader = csv.reader(csvfile) 
		  
		# extracting field names through first row 
		fields = csvreader.next() 

		# extracting each data row one by one 
		for row in csvreader: 
		    rows.append(row) 
	for row in rows:
		if row[0] != '' and row[0] != 'Customer_ID':
			node = CustomerReport()
			node.customer_id = row[0]
			node.customer_name = row[1]
			node.commodity = row[2]
			node.first_read_date = row[3]
			node.first_read_device = row[4]
			node.active_meters_count = row[5]
			node.inactive_meters_count = row[6]
			node.orphaned_meters_count = row[7]
			node.save()


def save_utility():
	rows = []
	with open('media/customer_portal_utility_statistics_report.csv', 'r') as csvfile: 
	# creating a csv reader object 
		csvreader = csv.reader(csvfile) 
		  
		# extracting field names through first row 
		fields = csvreader.next() 

		# extracting each data row one by one 
		for row in csvreader: 
		    rows.append(row) 
	for row in rows:
		if row[0] != '' and row[0] != 'Customer_ID':
			node = PortalUtility()
			node.customer_id = row[0]
			node.customer_name = row[1]
			node.portal_users_count = row[2]
			node.water = row[3]
			node.gas = row[4]
			node.electric = row[5]
			node.alerts = row[6]
			node.bill = row[7]
			node.dashboard_menu = row[8]
			node.goal = row[9]
			node.goals = row[10]
			node.goal_menu = row[11]
			node.google_maps = row[12]
			node.mactivity = row[13]
			node.meters = row[14]
			node.meters_menu = row[15]
			node.notifications = row[16]
			node.outages = row[17]
			node.outages_menu = row[18]
			node.outdoors = row[19]
			node.peers = row[20]
			node.recipients = row[21]
			node.recipients_menu = row[22]
			node.terms = row[23]
			node.treshold = row[24]
			node.tresholds = row[25]
			node.treshhold_menu = row[26]
			node.units = row[27]
			node.units_menu = row[28]
			node.usage = row[29]
			node.usage_detail = row[30]
			node.usage_forecast_menu = row[31]
			node.user = row[32]
			node.user_menu = row[33]
			node.usg_disclaimer = row[34]
			node.other_groups = row[35]
			node.save()	
def return_data(request):
	customer_data = CustomerReport.objects.all()
	master_sheet_data = MasterData.objects.all()
	portal_data = PortalUtility.objects.all()
	for data in customer_data:
		filter_master = master_sheet_data.filter(customer_id = data.customer_id)
		filter_portal_data = portal_data.filter(customer_id =data.customer_id)
		

def dashboard(request):
	customer = CustomerReport.objects.all()
	master_data = MasterData.objects.all()
	end_point_data = {}
	water_end_points = 0
	for data in master_data:
		try:
			water_end_points += int(data.w_end_points)
		except:
			if '<' in data.w_end_points:
				water_end_points+= int(data.w_end_points.replace('<',''))
			else:
				if data.w_end_points != '':
					water_end_points+= int(float(data.w_end_points))
				

	gas_end_points = 0
	for data in master_data:
		try:
			gas_end_points += int(data.g_end_points)
		except:
			if '<' in data.g_end_points:
				gas_end_points+= int(data.g_end_points.replace('>',''))
			else:
				if data.g_end_points != '':
					gas_end_points+= int(float(data.g_end_points))
	electric_end_points = 0
	for data in master_data:
		try:
			electric_end_points+= int(data.e_end_points)
		except:
			if '<' in data.e_end_points:
				electic_end_points+= int(data.e_end_points.replace('>',''))
			else:
				if data.e_end_points != '':
					electric_end_points+= int(float(data.e_end_points.replace(',','')))
	# import pdb;pdb.set_trace()
	sa_enhanced_orders = master_data.filter(build_product='SA Enhanced').count()
	sa_essential_orders = master_data.filter(build_product='SA Essential').count()
	total = master_data.count()
	sa_enhanced = (float(sa_enhanced_orders)/float(total))*100
	sa_essential = (float(sa_essential_orders)/float(total))*100
	other_sa = 100.0- (sa_essential + sa_enhanced)
	show_portal_list = []
	master_customers = BillingsBacklog.objects.filter(item_description__icontains='PORTAL')
	for customer in master_customers:
		obj = master_data.filter(project_code=customer.project_code)
		# try:
		# 	customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		# 	customer_report = None
		if obj:
			if obj[0] not in show_portal_list:
				show_portal_list.append(obj[0])
	sa_orders =  master_data.count() - len(show_portal_list)
	portal_orders = len(show_portal_list)
	total_orders = master_data.count()
	sa_o = (float(sa_orders)/float(total_orders))*100
	sa_p = (float(portal_orders)/float(total_orders))*100
	# other_sa = 100.0- (sa_enhanced + sa_essential)
	return render(request,'index.html',{'e_end':electric_end_points,'g_end':gas_end_points,'w_end':water_end_points,'sa_essential_orders':sa_essential,'sa_enhanced_orders':sa_enhanced,'other_sa':other_sa,'sa_o':sa_o,'sa_p':sa_p})


def second_view(request):
	master_data = MasterData.objects.all()
	return render(request,'overview.html',{'master_data':master_data})


def show_gas_meter(request):
	show_gas_list = []
	master_data = MasterData.objects.all()
	gas_customers = PortalUtility.objects.filter(gas='Y',water='N',electric='N')
	for customer in gas_customers:
		obj = master_data.filter(customer_id=customer.customer_id)
		try:
			customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		except:
			customer_report = None
		if obj:
			show_gas_list.append(obj[0])
	return render(request,'overview_gas.html',{'master_data':show_gas_list})

def show_water_meter(request):
	# import pdb;pdb.set_trace()
	show_water_list = []
	master_data = MasterData.objects.all()
	water_customers = PortalUtility.objects.filter(electric='N',water='Y',gas='N')
	for customer in water_customers:
		obj = master_data.filter(customer_id=customer.customer_id)
		try:
			customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		except:
			customer_report = None
		if obj:
			show_water_list.append(obj[0])
	return render(request,'overview_water.html',{'master_data':show_water_list})


def show_electric_meter(request):
	show_electric_list = []
	master_data = MasterData.objects.all()
	electric_customers = PortalUtility.objects.filter(electric='Y',water='N',gas='N')
	for customer in electric_customers:
		obj = master_data.filter(customer_id=customer.customer_id)
		try:
			customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		except:
			customer_report = None
		if obj:
			show_electric_list.append(obj[0])
	return render(request,'overview_electric.html',{'master_data':show_electric_list})
def show_combo_meter(request):
	show_combo_list = []
	master_data = MasterData.objects.all()
	master_customers = PortalUtility.objects.all().exclude(electric='Y',water='N',gas='N').exclude(electric='N',water='Y',gas='N').exclude(gas='Y',water='N',electric='N')
	for customer in master_customers:
		obj = master_data.filter(customer_id=customer.customer_id)
		try:
			customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		except:
			customer_report = None
		if obj:
			show_combo_list.append(obj[0])
	return render(request,'overview_combo.html',{'master_data':show_combo_list})
def show_portal_customers(request):
	show_portal_list = []
	master_data = MasterData.objects.all()
	# master_customers = PortalUtility.objects.filter(electric='Y',water='Y',gas='Y')
	master_customers = BillingsBacklog.objects.filter(item_description__icontains='PORTAL')
	for customer in master_customers:
		obj = master_data.filter(project_code=customer.project_code)
		# try:
		# 	customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		# 	customer_report = None
		if obj:
			if obj[0] not in show_portal_list:
				show_portal_list.append(obj[0])
	return render(request,'overview_portal.html',{'master_data':show_portal_list})

def show_addons(request):
	show_addon_list = []
	master_data = MasterData.objects.all()
	# master_customers = PortalUtility.objects.filter(electric='Y',water='Y',gas='Y')
	master_customers = BillingsBacklog.objects.filter(item_description__icontains='VOLTG INSIGHT') | BillingsBacklog.objects.filter(item_description__icontains='OUTAGE MANGMNT SYSTEM') | BillingsBacklog.objects.filter(item_description__icontains='UNBILLED ENERGY') |BillingsBacklog.objects.filter(item_description__icontains='TRNSFRMR UTILIZ')
	for customer in master_customers:
		obj = master_data.filter(project_code=customer.project_code)
		# try:
		# 	customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		# 	customer_report = None
		if obj:
			if obj[0] not in show_addon_list:
				show_addon_list.append(obj[0])
	return render(request,'overview_addon.html',{'master_data':show_addon_list})
def show_invoice_next_month(request):
	show_invoice_list = []
	master_data = MasterData.objects.all()
	# master_customers = PortalUtility.objects.filter(electric='Y',water='Y',gas='Y')
	master_customers = BillingsBacklog.objects.all()
	for customer in master_data:
		dates = []
		objs = master_customers.filter(project_code=customer.project_code)
		for obj in objs:
			try:
				if obj.date_invoiced != '':
					obj.date_invoiced = from_excel_ordinal(int(float(obj.date_invoiced)))
					dates.append(obj.date_invoiced)
			except:
				pass
		if dates != []:
			# import pdb;pdb.set_trace()
			if len(dates) > 1:
				sorted_date = sorted(dates)
				startDate = sorted_date[-1]
				endDate = date(startDate.year + 1, startDate.month, startDate.day)
				# replace year only
				endDate = startDate.replace(startDate.year + 1)
				today_date = datetime.now().date()
				if today_date.month == 12:
					one_month_date = date(today_date.year, 1, today_date.day)
				else:
					one_month_date = date(today_date.year, today_date.month + 1, today_date.day)
				if one_month_date.month == endDate.month and one_month_date.year==endDate.year:
				# if one_month_date > endDate:
					# import pdb;pdb.set_trace()
					show_invoice_list.append(customer)
			else:
				startDate = dates[0]
				endDate = date(startDate.year + 1, startDate.month, startDate.day)
				# replace year only
				endDate = startDate.replace(startDate.year + 1)
				today_date = datetime.now().date()
				if today_date.month == 12:
					one_month_date = date(today_date.year, 1, today_date.day)
				else:
					one_month_date = date(today_date.year, today_date.month + 1, today_date.day)
				if one_month_date.month == endDate.month and one_month_date.year == endDate.year:
				# if one_month_date > endDate:
					# import pdb;pdb.set_trace()
					show_invoice_list.append(customer)
		# try:
		# 	customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		# 	customer_report = None
		# if obj:
		# 	if obj[0] not in show_portal_list:
		# 		show_portal_list.append(obj[0])
	return render(request,'overview_next_month.html',{'master_data':show_invoice_list})

def show_notinvoiced(request):
	show_addon_list = []
	master_data = MasterData.objects.all()
	# master_customers = PortalUtility.objects.filter(electric='Y',water='Y',gas='Y')
	master_customers = BillingsBacklog.objects.filter(order_status__icontains='Backlog - Current',invoice_number='')
	for customer in master_customers:
		obj = master_data.filter(project_code=customer.project_code)
		# try:
		# 	customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		# 	customer_report = None
		if obj:
			if obj[0] not in show_addon_list:
				show_addon_list.append(obj[0])
	return render(request,'overview_notinvoiced.html',{'master_data':show_addon_list})

def from_excel_ordinal(ordinal, _epoch0=datetime(1899, 12, 31)):
    if ordinal > 59:
        ordinal -= 1  # Excel leap year bug, 1900 is not a leap year!
    return (_epoch0 + timedelta(days=ordinal)).replace(microsecond=0).date()

def save_billingblockhold():
	book = xlrd.open_workbook('media/' + 'BillingsBacklogOnhold.xlsx')
	sheet = book.sheet_by_index(0)
	for i in range(sheet.nrows):
		col = sheet.row_values(i)
	# for i in range(sheet.nrows):
		if col[0] != '' and col[0]!='Name' and col[0]!='Datetime' and col[0]!='Filters' and col[0]!='Records' and col[0] != 'Order Status' :
			try:
				print 'Good'
				node = BillingsBacklog()
				node.order_status = col[0]
				node.salesperson = col[33]
				node.date_entered = col[32]
				node.cust_name_bill_to = col[3]
				node.customer_number_bill_to = col[2]
				node.ship_to_number = col[4]
				node.customer_name_ship_to = col[5]
				node.customer_name = col[6]
				node.item_number = col[7]
				node.item_description = col[8]
				node.order_number = col[9]
				node.order_line_number = col[10]
				node.total_sales = col[13]
				node.quantity = col[15]
				node.unit_sales_price = col[16]
				node.project_code = col[20]
				node.date_invoiced = col[27]    
				node.early_ship = col[11]
				node.promotion_region = col[35]
				node.product_code = col[18]
				node.entered_by = col[34]
				node.item_class = col[19]
				node.date_committed = col[28]
				node.date_requested = col[29]
				node.date_customer_request = col[30]
				node.customer_po = col[36]
				node.warehouse = col[37]
				node.facility = col[38]
				node.item_type = col[39]
				node.ship_to_state = col[40]
				node.invoice_number = col[45]
				node.manufacturing_group = col[48]
				node.hold_reason = col[52]
				node.po_number = col[53]
				node.save()
			except Exception as e:
				import pdb;pdb.set_trace()
				# print e
def customer_overview(request,pk):
	try:
		portal_user_data = []
		gas_data = []
		water_data = []
		electric_data = []
		obj = MasterData.objects.get(id=pk)
		given_gas_points = obj.g_end_points
		if given_gas_points == '':
			given_gas_points = '0.0' 
		given_water_points = obj.w_end_points
		if given_water_points == '':
			given_water_points = '0.0'
		given_electric_points = obj.e_end_points
		if given_electric_points == '':
			given_electric_points = '0.0'
		cust_id = obj.customer_id
		utility = obj.utility 
		sa_type = obj.build_product
		project_code = obj.project_code
		meter_data = CustomerReport.objects.filter(customer_id=cust_id)
		actual_water_count = 0
		actual_electric_count = 0
		actual_gas_count = 0
		if meter_data:
			for mdata in meter_data:
				if mdata.commodity == 'WATER':
					actual_water_count = int(mdata.active_meters_count)
				elif mdata.commodity == 'ELECTRIC':
					actual_electric_count = int(mdata.active_meters_count)
				elif mdata.commodity == 'GAS':
					actual_gas_count = int(mdata.active_meters_count)
		gas_data.append(int(float(given_gas_points)))
		gas_data.append(actual_gas_count)
		water_data.append(int(float(given_water_points.replace('<',''))))
		water_data.append(actual_water_count)
		electric_data.append(int(float(given_electric_points)))
		electric_data.append(actual_electric_count)
		billing_obj = BillingsBacklog.objects.filter(project_code=project_code)
		if billing_obj:
			found_portal_users = 0
			for bobj in billing_obj:
				if 'CONSUMER PORTAL <1500 ANNL ANNUAL USE FEE 0-1500' in bobj.item_description:
					found_portal_users = 1500
			actual_portal_users=  PortalUtility.objects.filter(customer_id=cust_id)
			if actual_portal_users:
				actual_portal_users_count = int(actual_portal_users[0].portal_users_count)
			else:
				actual_portal_users_count = 0
			portal_user_data.append(found_portal_users)
			portal_user_data.append(actual_portal_users_count)
			# invoice_date =
			master_annual_fees = [] 
			# text_messages_data = 
			# ELE CONSUMER PORTAL <1500 ANNL ANNUAL USE FEE 0-1500
			get_unique_invoices = []
			get_unique_date_committed = []
			for bobj in billing_obj:
				if bobj.date_invoiced !='':
					if bobj.date_invoiced not in get_unique_invoices:
						get_unique_invoices.append(bobj.date_invoiced)
				else:
					if bobj.date_committed not in get_unique_date_committed:
						get_unique_date_committed.append(bobj.date_committed)
			# SENSUS ELE ANALYTCS ENH 5-10K  ENHANCED   ANNUAL FEE
			water_objs = billing_obj.filter(item_description__icontains = 'WTR ANALYTICS')
			electric_objs = billing_obj.filter(item_description__icontains = 'ELE ANALYTCS')
			gas_objects = billing_obj.filter(item_description__icontains = 'GAS ANALYTCS')
			other_objs =  [obj for obj in billing_obj if 'ANNL ANNUAL USE' in obj.item_description]
			for obj in other_objs:
				try:
					if obj.date_invoiced != '':
						obj.date_invoiced = from_excel_ordinal(int(float(obj.date_invoiced)))
				except:
					pass
			for obj in billing_obj:
				try:
					if obj.date_invoiced != '':
						obj.date_invoiced = from_excel_ordinal(int(float(obj.date_invoiced)))
				except:
					pass
				try:
					if obj.date_entered != '':
						obj.date_entered = from_excel_ordinal(int(float(obj.date_entered)))
				except:
					pass
			master_annual_data = []
			for inobj in get_unique_invoices:
				#Filter Water Object
				total_annual_fee = 0 
				wobj = water_objs.filter(date_invoiced=inobj)
				#Filter gas Object
				gobj = gas_objects.filter(date_invoiced=inobj)
				#Filter Electric object
				eobj = electric_objs.filter(date_invoiced=inobj)
				if wobj:
					for obj in wobj:
						total_annual_fee += int(float(obj.total_sales))
						order_no = obj.order_number
						order_line_number = obj.order_line_number
						invoice_number = obj.invoice_number
				if gobj:
					for obj in gobj:
						total_annual_fee += int(float(obj.total_sales))
						order_no = obj.order_number
						order_line_number = obj.order_line_number
						invoice_number = obj.invoice_number
				if eobj:
					for obj in eobj:
						total_annual_fee += int(float(obj.total_sales))
						order_no = obj.order_number
						order_line_number = obj.order_line_number
						invoice_number = obj.invoice_number	
				if total_annual_fee>0:
					master_annual_data.append([from_excel_ordinal(int(float(inobj))),total_annual_fee,invoice_number,order_no,int(order_line_number)])
			# if len(master_annual_data)>1:
				# import pdb;pdb.set_trace()
				# master_annual_data = sorted(master_annual_data,key=itemgetter(3),reverse=True)		
			for cobj in get_unique_date_committed:
				total_annual_fee = 0 
				wobj = water_objs.filter(date_committed=cobj)
				#Filter gas Object
				gobj = gas_objects.filter(date_committed=cobj)
				#Filter Electric object
				eobj = electric_objs.filter(date_committed=cobj)
				if wobj:
					for wwo in wobj:
						total_annual_fee = float(wwo.total_sales)
						order_no = wwo.order_number
						order_line_number = wwo.order_line_number
						invoice_number = wwo.invoice_number
						if total_annual_fee>0:
							master_annual_data.append(['',total_annual_fee,invoice_number,order_no,int(order_line_number)])
			
				if gobj:
					for ggo in gobj:
						total_annual_fee = float(ggo.total_sales)
						order_no = ggo.order_number
						order_line_number = ggo.order_line_number
						invoice_number = ggo.invoice_number
						if total_annual_fee>0:
							master_annual_data.append(['',total_annual_fee,invoice_number,order_no,int(order_line_number)])
			
				if eobj:
					for eeo in eobj:
						total_annual_fee = float(eeo.total_sales)
						order_no = eeo.order_number
						order_line_number = eeo.order_line_number
						invoice_number = eeo.invoice_number
						if total_annual_fee>0:
							master_annual_data.append(['',total_annual_fee,invoice_number,order_no,int(order_line_number)])
				# if total_annual_fee>0:
					# master_annual_data.append(['',total_annual_fee,invoice_number,order_no,order_line_number])
			if len(master_annual_data)>1:
				# import pdb;pdb.set_trace()
				master_annual_data = sorted(master_annual_data,key=itemgetter(4),reverse=False)
			# msg_data = ''
			# setup_data = ''
			# addon_data = ''
			# for obj in billing_obj: 
			# 	if 'TEXT MESSAGES' in obj.item_description:
			# 		msg_data+= '$ '+obj.total_sales + ', '
			# for obj in billing_obj:
			# 	if 'SYSTEM SETUP' in obj.item_description:
			# 		setup_data+= '$'+obj.total_sales+ ', ' 
			# for obj in billing_obj:
			# 	if 'SENSUS CUSTOM DEVELOP SERVICES' in obj.item_description:
			# 		addon_data+= '$'+obj.total_sales+ ', '
			# if msg_data == '':
			# 	msg_data = '$0'
			# if setup_data == '':
			# 	setup_data = '$0'
			# if addon_data == '':
			# 	addon_data = '$0'
			msg_data = []
			setup_data = []
			addon_data = []
			for obj in billing_obj:
				if 'TEXT MESSAGES' in obj.item_description:
					try:
						msg_data.append([from_excel_ordinal(int(float(obj.date_invoiced))),obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
					except:
						msg_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
			# TEXT MESSAGES 
			# SYSTEM SETUP
			for obj in billing_obj:
				if 'SYSTEM SETUP' in obj.item_description:
					try:
						setup_data.append([obj.date_invoiced,obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
					except:
						setup_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
			# SENSUS CUSTOM DEVELOP SERVICES
			for obj in billing_obj:
				if 'VOLTG INSIGHT' in obj.item_description:
					try:
						addon_data.append([from_excel_ordinal(int(float(obj.date_invoiced))),obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])		
					except:
						addon_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
				if 'OUTAGE MANGMNT SYSTEM' in obj.item_description:
					try:
						addon_data.append([from_excel_ordinal(int(float(obj.date_invoiced))),obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])		
					except:
						addon_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])			
		
				if 'UNBILLED ENERGY' in obj.item_description:
					try:
						addon_data.append([from_excel_ordinal(int(float(obj.date_invoiced))),obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])		
					except:
						addon_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
				if 'TRNSFRMR UTILIZ' in obj.item_description:
					try:
						addon_data.append([from_excel_ordinal(int(float(obj.date_invoiced))),obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])		
					except:
						addon_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])
				# if '' in obj.item_description:
				# 	try:
				# 		addon_data.append([from_excel_ordinal(int(float(obj.date_invoiced))),obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])		
				# 	except:
				# 		addon_data.append(['',obj.total_sales,obj.invoice_number,obj.order_number,obj.order_line_number])								

		else:
			cust_id = ''
			sa_type = ''
			master_annual_data = []
			error = True
			other_objs = []
			msg_data = []
			addon_data = []
			setup_data = []
			billing_obj = None
			electric_data = []
			gas_data = []
			water_data = []
			portal_user_data = []						
			return render(request,'customeroverview.html',{'cust_id':cust_id,'master_annual_data':master_annual_data,'other_objs':other_objs,'utility':utility,'sa_type':sa_type,'portal_user_data':portal_user_data,'gas_data':gas_data,'water_data':water_data,'electric_data':electric_data,'billing_obj':billing_obj,'setup_data':setup_data,'addon_data':addon_data,'msg_data':msg_data,'error':error,'project_code':project_code})


	except Exception,e:
		# import pdb;pdb.set_trace()
		cust_id = ''
		sa_type = ''
		master_annual_data = []

	return render(request,'customeroverview.html',{'cust_id':cust_id,'master_annual_data':master_annual_data,'other_objs':other_objs,'utility':utility,'sa_type':sa_type,'portal_user_data':portal_user_data,'gas_data':gas_data,'water_data':water_data,'electric_data':electric_data,'billing_obj':billing_obj,'setup_data':setup_data,'addon_data':addon_data,'msg_data':msg_data,'project_code':project_code})



def delete_data():
	customer_data = CustomerReport.objects.all()
	master_sheet_data = MasterData.objects.all()
	portal_data = PortalUtility.objects.all()
	backhold_data = BillingsBacklog.objects.all()
	for data in customer_data:
		data.delete()
	for data in master_sheet_data:
		data.delete()
	for data in portal_data:
		data.delete()
	for data in backhold_data:
		data.delete()

		
def to_be_invoiced():
	import datetime
	d1 = datetime.date.today()
	from dateutil.relativedelta import relativedelta
	d2 = d1 + relativedelta(months=1)
	next_month = d2.month()
	from dateutil import parse


@csrf_exempt
def download_customer_report(request):
	data = request.POST
	project_code = json.loads(data['project_code'])
	from django.utils import timezone
	time_audit = timezone.now()
	time_stamp = time_audit.strftime("%Y_%m_%d")
	file_name = 'customer_report_'+time_stamp+'.xlsx'
	response = HttpResponse(content_type='application/openxmlformats-officedocument.spreadsheetml.sheet')
	response['Content-Disposition'] = 'attachment; filename='+file_name
	output = StringIO.StringIO()
	wb = xlsxwriter.Workbook(output)
	nodes = BillingsBacklog.objects.filter(project_code=project_code)
	p_data = list(nodes.values_list('item_number','item_description','order_number','order_line_number','date_entered','total_sales','date_invoiced','invoice_number','salesperson','cust_name_bill_to','customer_name'))
	ws = wb.add_worksheet(str(project_code))
	ws.insert_image('A1', 'media/sensus_xylem_logo.png')
	columns = ['Item Number','Item Description','Order Number','Order Line Number','Date Entered','Total Sales','Date Invoiced','Invoice Number','Sales Person','Customer Bill To','Customer Ship TO']
	#Writing columns
	ws.set_column('A:A', 10)
	ws.set_column('B:B', 50)
	ws.set_column('C:C', 20)
	ws.set_column('D:D', 10)
	ws.set_column('E:E', 10)
	ws.set_column('F:F', 20)
	cell_format = wb.add_format({'bold': True, 'font_color': 'white','bg_color':'#27367f'})
	for idx,col in enumerate(columns):
	    ws.write(3, idx, col,cell_format)

	#Writing rows data
	for rowidx,result in enumerate(p_data,start=3):
		# import pdb;pdb.set_trace()
	    for idx, val in enumerate(result):
	    	try:
	            if idx == 6:
	                try:
	                    val = timezone.localtime(val).strftime('%a %b %d %H:%M%p %Y')
	                except:
	                    pass
	            ws.write(rowidx+1, idx, val.__str__())
	        except:
	            ws.write(rowidx+1, idx, val.__repr__())
		# import pdb;pdb.set_trace()
	wb.close()
	response.write(output.getvalue())
	return response