from django.shortcuts import render
from .models import MasterData,CustomerReport,BillingsBacklog,PortalUtility
import xlrd
import csv

# Create your views here.
def create_master():
	import pdb;pdb.set_trace()
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
			except:
				import pdb;pdb.set_trace()
				# print e

def save_customer():
	import pdb;pdb.set_trace()
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
	return render(request,'index.html',{'e_end':electric_end_points,'g_end':gas_end_points,'w_end':water_end_points,'sa_essential_orders':sa_essential,'sa_enhanced_orders':sa_enhanced,'other_sa':other_sa})


def second_view(request):
	master_data = MasterData.objects.all()
	return render(request,'overview.html',{'master_data':master_data})


def show_gas_meter(request):
	show_gas_list = []
	master_data = MasterData.objects.all()
	gas_customers = PortalUtility.objects.filter(gas='Y')
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
	water_customers = PortalUtility.objects.filter(water='Y')
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
	electric_customers = PortalUtility.objects.filter(electric='Y')
	for customer in electric_customers:
		obj = master_data.filter(customer_id=customer.customer_id)
		try:
			customer_report = CustomerReport.objects.get(customer_id=customer.customer_id)
		except:
			customer_report = None
		if obj:
			show_electric_list.append(obj[0])
	return render(request,'overview_electric.html',{'master_data':show_electric_list})

def save_billingblockhold():
	book = xlrd.open_workbook('media/' + 'BillingsBacklogOnhold.xlsx')
	sheet = book.sheet_by_index(0)
	for i in range(sheet.nrows):
		col = sheet.row_values(i)
	# for i in range(sheet.nrows):
		if col[0] != '' and col[0]!='order_status':
			try:
				print 'Good'
				node = BillingsBacklog()
				node.order_status = col[0]
				node.salesperson = col[1]
				node.date_entered = col[2]
				node.cust_name_bill_to = col[3]
				node.customer_name = col[4]
				node.item_number = col[5]
				node.item_description = col[6]
				node.order_number = col[7]
				node.order_line_number = col[8]
				node.total_sales = col[9]
				node.quantity = col[10]
				node.unit_sales_price = col[11]
				node.project_code = col[12]
				node.date_invoiced = col[13]    
				node.ship_to_number = col[14]
				node.early_ship = col[15]
				node.promotion_region = col[16]
				node.product_code = col[17]
				node.entered_by = col[18]
				node.item_class = col[19]
				node.date_committed = col[20]
				node.customer_no_bill_to = col[21]
				node.date_requested = col[22]
				node.date_customer_request = col[23]
				node.customer_po = col[24]
				node.warehouse = col[25]
				node.facility = col[26]
				node.item_type = col[27]
				node.ship_to_state = col[28]
				node.invoice_number = col[29]
				node.manufacturing_group = col[30]
				node.hold_reason = col[31]
				node.po_number = col[32]
				node.save()
			except Exception as e:
				import pdb;pdb.set_trace()
				# print e
def customer_overview(request,pk):
	# try:
	# 	cust_id = MasterData.objects.get(id=pk).customer_id
	# except:
	# 	cust_id = None
	# 	return HttpResponse('No Customer')	
	return render(request,'customeroverview.html')